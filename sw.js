/* LIL 事件导航 Service Worker
 * 目的：用 Cache Storage（容量远大于浏览器 HTTP 磁盘缓存、跨天持久）解决
 *   GitHub Pages 只给 10 分钟新鲜度 + 浏览器磁盘缓存装不下 4.76GB 图片
 *   导致的"每次打开都全量重下"问题。
 * 策略：
 *   - 图片（版本锁定、不会变）：cache-first，一次缓存永久秒开。
 *   - 事件 JSON（译文会更新）：stale-while-revalidate，先秒开缓存、后台静默刷新。
 *   - guide.html 等 HTML 外壳（白屏修复在 <html> 上）：
 *       cache-first（命中即秒出深色页，绝不白闪），后台静默刷新保证内容新鲜。
 *       v1 用 SWR（先吐旧白底→每回闪）、v2 用 network-first（每回等地等网络→每回闪）都仍闪；
 *       v3 改 cache-first 但仍闪一次（v3 激活删旧缓存→头几次点击缓存空→现拉网络）。
 *       故 v4 在【安装阶段即预缓存深色 guide.html】，v4 接管后首次点开即命中、零白闪。
 */
const CACHE = 'lil-nav-v4';
const PRECACHE_HTML = ['guide.html', 'guide_i18n.html'];
const IMG_RE = /\.(?:webp|png|jpe?g|gif|avif|svg|bmp|ico)(?:[?#]|$)/i;
const EVENT_RE = /\/context\/events\/[^?#]+\.json(?:[?#]|$)/i;

function isHtmlShell(url) {
  const p = url.pathname;
  return p.endsWith('.html') || p === '/' || p === '';
}

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    // 安装即预缓存深色 HTML：v4 接管后首次点开即缓存命中，零网络等待、零白闪
    await Promise.all(PRECACHE_HTML.map(u =>
      fetch(u).then(r => { if (r && r.status === 200) c.put(u, r.clone()); }).catch(() => {})
    ));
    self.skipWaiting();
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // 仅处理同源（google 统计等跨域跳过）

  if (IMG_RE.test(url.pathname)) return e.respondWith(cacheFirst(req));
  if (EVENT_RE.test(url.pathname)) return e.respondWith(swr(req));
  if (isHtmlShell(url)) return e.respondWith(swr(req)); // HTML：cache-first 秒出深色，后台刷新
  return e.respondWith(swr(req)); // sw.js 等其它同源资源
});

async function cacheFirst(req) {
  const c = await caches.open(CACHE);
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

async function swr(req) {
  const c = await caches.open(CACHE);
  const hit = await c.match(req);
  const net = fetch(req).then(res => {
    if (res && res.status === 200) c.put(req, res.clone());
    return res;
  }).catch(() => hit);
  return hit || net;
}
