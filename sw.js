/* LIL 事件导航 Service Worker
 * 目的：用 Cache Storage（容量远大于浏览器 HTTP 磁盘缓存、跨天持久）解决
 *   GitHub Pages 只给 10 分钟新鲜度 + 浏览器磁盘缓存装不下 4.76GB 图片
 *   导致的"每次打开都全量重下"问题。
 * 策略：
 *   - 图片（版本锁定、不会变）：cache-first，一次缓存永久秒开。
 *   - 事件 JSON（译文会更新）：stale-while-revalidate，先秒开缓存、后台静默刷新。
 *   - guide.html 等 HTML 外壳（会随部署变化、且白屏修复在 <html> 上）：
 *       network-first + 强制绕过 HTTP 缓存，永远取线上最新版，绝不吐旧白底页。
 *       （仅作离线回退缓存，线上永远走网络新内容）
 */
const CACHE = 'lil-nav-v2';
const IMG_RE = /\.(?:webp|png|jpe?g|gif|avif|svg|bmp|ico)(?:[?#]|$)/i;
const EVENT_RE = /\/context\/events\/[^?#]+\.json(?:[?#]|$)/i;

function isHtmlShell(url) {
  const p = url.pathname;
  return p.endsWith('.html') || p === '/' || p === '';
}

self.addEventListener('install', () => self.skipWaiting());

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
  if (isHtmlShell(url)) return e.respondWith(networkFirst(req));
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

async function networkFirst(req) {
  const c = await caches.open(CACHE);
  try {
    // cache:'reload' 绕过 HTTP 磁盘缓存，永远从服务器取最新 HTML（白屏修复即生效）
    const res = await fetch(req, { cache: 'reload' });
    if (res && res.status === 200) c.put(req, res.clone()); // 仅作离线回退
    return res;
  } catch (err) {
    const hit = await c.match(req);
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
