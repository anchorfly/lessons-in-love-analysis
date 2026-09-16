/* LIL 事件导航 Service Worker
 * 目的：用 Cache Storage（容量远大于浏览器 HTTP 磁盘缓存、跨天持久）解决
 *   GitHub Pages 只给 10 分钟新鲜度 + 浏览器磁盘缓存装不下 4.76GB 图片
 *   导致的"每次打开都全量重下"问题。
 * 策略（图片 / 译文 JSON / HTML 三张独立缓存，互不牵连）：
 *   - 图片（版本锁定、不会变）：cache-first，一次缓存永久秒开。独立缓存 lil-img-vX，永不 bump。
 *   - 事件 JSON（译文会更新）：cache-first，命中即秒读、无后台重取噪点。
 *       独立缓存 lil-evt-vX，名字稳定、不再靠 bump。译文刷新由 guide.html 开机拉
 *       `context/events/evtver.json` 全量版本清单，与本地 lastSeen 比对，只 delete
 *       哈希对不上的那几条缓存条目（精准+有界，不涨不漏）；没改的事件永久秒出。
 *   - guide.html 等 HTML 外壳（白屏修复在 <html> 上）：
 *       v25 起改为「网络优先 + 1.2s 超时兜底缓存」（原来 swr = 先吐旧版，
 *       导致改完必须刷新两次才生效，逼得让人去 Unregister —— 绝不允许）。
 *       现在正常刷新一次就是新内容；断网/极慢时自动落回缓存。独立缓存 lil-doc-vX。
 *       v1 用 SWR（先吐旧白底→每回闪）、v2 用 network-first（每回等地等网络→每回闪）都仍闪；
 *       v3 改 cache-first 但仍闪一次（v3 激活删旧缓存→头几次点击缓存空→现拉网络）。
 *       故 v4 在【安装阶段即预缓存深色 guide.html】，v4 接管后首次点开即命中、零白闪。
 *   - v5：guide.html 补 `color-scheme:dark`（浏览器起手就用深色画布，治跨页跳转白闪）；
 *       并 bump 缓存版本以重新预缓存「带 color-scheme 的新版 HTML」。
 *   - v6：事件 JSON 由 swr（每次打开后台发刷新请求、Network 面板现 200/304 噪点）改回 cache-first，
 *       与图片一致——命中即秒读、无后台重取；译文更新靠 bump 缓存版本触发刷新。
 *   - v7：把原先「图片+JSON+HTML 共用一个 lil-nav-vX」拆成三张独立缓存
 *       （lil-img / lil-evt / lil-doc）。刷新译文只 bump lil-evt，
 *       再也不会顺手清空 4.76GB 图片缓存、逼用户重下图片。
 *   - v8：弃用 bump（整库删除 = 粗粒度、且旧策略会连图片一起清）。改用「开机全量版本
 *       清单比对 + 条目级精准删除」：译文更新只重算 evtver.json，SW 缓存名保持不变，
 *       线上仅重拉改动的文件。图片缓存名 lil-img-vX 永不改、永不失效。
 *   - v9（事件缓存兜底）：v8 的 evtver 精准失效在个别客户端未生效（译文已更新、
 *       线上 JSON 已是新内容，用户仍看到旧译文），故把 CACHE_EVT v6→v7 整表重建一次。
 *       ⚠️ 铁律：CACHE_EVT 改名时，必须同步改 guide.html 与 guide_i18n.html 里
 *       硬编码的 caches.open('lil-evt-vN')，否则精准失效会指向一张死缓存、永久失效。
 */
const CACHE_IMG = 'lil-img-v1';   // 图片：版本锁死，永不 bump、永不失效
const CACHE_EVT = 'lil-evt-v7';   // 事件译文 JSON：v9 兜底 bump 到 v7；日常失效仍靠 evtver 精准删条目
const CACHE_DOC = 'lil-doc-v25';   // HTML 外壳等：网络优先(1.2s 超时回退缓存)。
                                  //       v25=HTML/其它资源改网络优先(1.2s超时回退缓存)，刷新一次即生效，不再需要手动清缓存
                                  //       v24=guide_i18n 转正为 guide.html（正式发布）
                                  //       v23=切语言保持正文阅读位置（锚点行）
                                  //       v22=上下事件导航标题随语言切换：补齐 prev/next 的 label
                                  //       v21=短信三级页也回顶部 + 与事件一致清空 curCat（返回列表回顶部）
                                  //       v20=预载完成自动重绘时豁免回顶部（_skipScrollTop），避免打断阅读
                                  //       v19=撤销误加的内嵌 Zalgo 字体（v15 是刻意移除）+ 正式页换页回顶部
                                  //       v18=ayanedorm20 英文改 bonus=True 真名 Still Young（bonus 规则：True=非和谐）
                                  //       v17=正式页 guide.html 同步换页回顶部修复（与 i18n 页同一份）
                                  //       v16=页面英文 title 统一改 avn 真名（22 条，中英对齐）
                                  //       v15=移除内嵌 Zalgo 字体，乱码行统一改为「原文 + 半角括号中文」
                                  //       v14=短信标题/面包屑随语言切换（_itemByLabel 补索引 c.sms；openSms meta 挂 data-lab）
                                  //       v13=历史版本事件/首页等换页后回到顶部（原来保留原滚动位置）
                                  //       v12=25 条专名：知名/历史人物译出、造语按理解译、编号不动
                                  //       v11=i18n 页内嵌标题刷新（Number Girl->编号女孩）
                                  //       v10=中文标题全量内嵌（ZH_TITLES_BUILTIN），events json 移除 title_zh
                                  //       v9=字体改为 data URI 内嵌(22KB base64)+独立字体族 LilZalgoCJK，彻底消除路径依赖
                                  //       v8=自托管 Noto Sans SC 子集修中文 Zalgo(16KB,含 CJK+U+0300-036F 全组合符),国内离线可用
                                  //       v7=CJK+组合符字形兜底：.content 加 LilCjk @font-face(unicode-range)，修中文 Zalgo 显示缺字形方框
                                  //       v6=事件缓存 lil-evt-v6→v7（+两个页面同步硬编码缓存名），修 roomwithclocks 中文译文不刷新
                                  // ⚠️ 铁律：每改一次 guide.html / guide_i18n.html 就必须 +1（v3→v4→…），
                                  // 否则浏览器一直吃 SW 缓存的旧 HTML，用户必须手动清缓存才能看到改动。
                                  // 历史：v3=_syncEvtCache 缓存失效+undefined/滚动修复；
                                  //       v4=「错过时显示」红字中文三态切换（missTxt/missHtml/missOf + ZH_MISSED）
                                  //          + 正文过滤 rpy `label xxx:` 声明行（stripLeadingCode）。
const PRECACHE_HTML = ['guide.html', 'guide_i18n.html'];
const IMG_RE = /\.(?:webp|png|jpe?g|gif|avif|svg|bmp|ico)(?:[?#]|$)/i;
const EVENT_RE = /\/context\/events\/[^?#]+\.json(?:[?#]|$)/i;
const MANIFEST_RE = /\/context\/events\/evtver\.json(?:\?[^#]*)?$/i; // 版本清单：绕过 SW 缓存，页面用 no-store 直连最新

function isHtmlShell(url) {
  const p = url.pathname;
  return p.endsWith('.html') || p === '/' || p === '';
}

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE_DOC);
    // 安装即预缓存深色 HTML：v4 接管后首次点开即缓存命中，零网络等待、零白闪。
    // 已缓存则跳过，避免重复预缓存 1.3MB 的 guide.html。
    await Promise.all(PRECACHE_HTML.map(async (u) => {
      if (await c.match(u)) return;
      try {
        const r = await fetch(u);
        if (r && r.status === 200) await c.put(u, r.clone());
      } catch (_) {}
    }));
    self.skipWaiting();
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    // 只保留当前三张缓存；其余（含旧版 lil-nav-vX、旧带数字版本缓存）一律删除。
    // v8 起缓存名稳定、不再 bump；译文失效靠 guide.html 开机精准删条目，不在此清。
    const KEEP = new Set([CACHE_IMG, CACHE_EVT, CACHE_DOC]);
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => !KEEP.has(k)).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // 仅处理同源（google 统计等跨域跳过）

  // 版本清单绕过 SW：不进任何缓存，由页面用 no-store 直连拿最新（保证开机比对永远新鲜）
  if (MANIFEST_RE.test(url.pathname)) return;

  if (IMG_RE.test(url.pathname))   return e.respondWith(cacheFirst(req, CACHE_IMG));
  if (EVENT_RE.test(url.pathname)) return e.respondWith(cacheFirst(req, CACHE_EVT));
  // HTML 外壳 + sw.js + context/_missed_zh.json 等：网络优先（1.2s 超时回退缓存）。
  // 目的：普通用户「刷新一次」就能看到新内容，不需要任何开发者工具操作。
  return e.respondWith(netFirst(req, CACHE_DOC, 1200));
});

async function cacheFirst(req, name) {
  const c = await caches.open(name);
  const hit = await c.match(req);
  if (hit) return hit;
  try {
    const res = await fetch(req);
    if (res && res.status === 200) c.put(req, res.clone());
    return res;
  } catch (err) {
    return hit || new Response('', { status: 504 });
  }
}

async function swr(req, name) {
  const c = await caches.open(name);
  const hit = await c.match(req);
  const net = fetch(req).then(res => {
    if (res && res.status === 200) c.put(req, res.clone());
    return res;
  }).catch(() => hit);
  return hit || net;
}

/* 网络优先 + 超时回退缓存（v25）：
   先发网络请求，timeout 毫秒内回来就用网络的（= 最新内容），并顺手更新缓存；
   超时/失败则用缓存（离线可用）；既没网络又没缓存才 504。
   ⚠️ 这是「改完刷新一次就生效」的关键：旧版 swr 会先吐旧缓存，导致必须刷新两次。 */
async function netFirst(req, name, timeout) {
  const c = await caches.open(name);
  const net = fetch(req).then(res => {
    if (res && res.status === 200) c.put(req, res.clone());
    return res;
  }).catch(() => null);
  const hit = await c.match(req);
  const win = await Promise.race([
    net,
    new Promise(r => setTimeout(() => r(null), timeout || 1200))
  ]);
  if (win) { if (win.status === 200 || !hit) return win; }   // 网络成功（或没缓存可用）→ 用网络
  if (hit) return hit;                                        // 网络慢/非 200 → 回退缓存
  const late = await net;                                     // 没缓存：继续等网络
  return late || new Response('', { status: 504 });
}
