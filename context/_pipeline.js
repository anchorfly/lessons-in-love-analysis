// LIL 全量翻译流水线
// 用法:
//   node _pipeline.js gen "Ami Arakawa"   为某分类所有事件生成骨架(en 已填,zh 全空;已翻的跳过)
//   node _pipeline.js gen <label>         为单个事件生成骨架
//   node _pipeline.js inject <label>      读 events/_zh/<label>.json {title_zh, zh:[...]} 注入骨架并校验
//   node _pipeline.js verify <label>      校验某事件 en 与源文逐字符一致 + 统计空 zh
//   node _pipeline.js verify all          校验 events/ 下全部文件
//   node _pipeline.js stats               全局进度
//   node _pipeline.js pending "分类名"    列出该分类还未翻的 label
const fs = require('fs');
const path = require('path');
const DIR = __dirname;
const GUIDE = 'C:/Users/anke/Desktop/LIL/分析/guide.html';
const EV = path.join(DIR, 'events');
const ZH = path.join(EV, '_zh');

function loadData() {
  const html = fs.readFileSync(GUIDE, 'utf8');
  const bodyStart = html.indexOf('<body>');
  const dataStart = html.indexOf('<script id="data"', bodyStart);
  const dataTagEnd = html.indexOf('>', dataStart) + 1;
  const dataEnd = html.indexOf('</script>', dataStart);
  return JSON.parse(html.slice(dataTagEnd, dataEnd));
}

function textLines(content) {
  const out = [];
  const re = /<div class="(l|c|opt)"[^>]*>([\s\S]*?)<\/div>/g;
  let m;
  while ((m = re.exec(content)) !== null) {
    if (m[1] !== 'l') continue; // 只收 .l 对话行([c] 是脚本代码)
    const dm = m[2].match(/<span class="d"[^>]*>([\s\S]*?)<\/span>/);
    if (!dm) continue;
    let txt = dm[1].replace(/<[^>]*>/g, '')
      .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'");
    txt = txt.trim();
    if (txt) out.push(txt);
  }
  return out;
}

function allItems(DATA) {
  const items = [];
  for (const c of DATA) {
    for (const it of (c.items || [])) items.push({ cat: c.name, kind: 'event', label: it.label, title: it.title, content: it.content });
    for (const sm of (c.sms || [])) items.push({ cat: c.name, kind: 'sms', label: sm.label, title: '(短信) ' + (sm.title || ''), content: sm.content });
  }
  return items;
}

function isTranslated(f) {
  try {
    const j = JSON.parse(fs.readFileSync(f, 'utf8'));
    return j.lines && j.lines.length > 0 && j.lines.every(l => l.zh && l.zh.length > 0);
  } catch (e) { return false; }
}

function findItem(DATA, label) {
  return allItems(DATA).find(i => i.label === label);
}

const cmd = process.argv[2];
const arg = process.argv[3] || '';

if (cmd === 'gen') {
  const DATA = loadData();
  const items = allItems(DATA);
  let targets;
  if (arg === 'all') targets = items;
  else {
    const cat = items.filter(i => i.cat === arg);
    targets = cat.length ? cat : items.filter(i => i.label === arg);
  }
  if (!targets.length) { console.log('no target for:', arg); process.exit(1); }
  let gen = 0, skip = 0;
  for (const it of targets) {
    if (!it.label || !it.content) { console.log('SKIP (no label/content):', it.cat, it.title); continue; }
    const f = path.join(EV, it.label + '.json');
    if (fs.existsSync(f) && isTranslated(f)) { skip++; continue; }
    const lines = textLines(it.content).map(en => ({ en, zh: '' }));
    const j = { label: it.label, title_zh: '', lines };
    fs.writeFileSync(f, JSON.stringify(j, null, 1), 'utf8');
    gen++;
    console.log('gen', it.label, lines.length + ' 行');
  }
  console.log(`\ndone: generated=${gen} skipped(已翻)=${skip}`);
}

else if (cmd === 'inject') {
  const f = path.join(EV, arg + '.json');
  const zf = path.join(ZH, arg + '.json');
  const j = JSON.parse(fs.readFileSync(f, 'utf8'));
  const z = JSON.parse(fs.readFileSync(zf, 'utf8'));
  if (!Array.isArray(z.zh) || z.zh.length !== j.lines.length) {
    console.log(`FAIL: zh 数组长度 ${z.zh.length} != lines ${j.lines.length}`); process.exit(1);
  }
  if (z.title_zh) j.title_zh = z.title_zh;
  j.lines.forEach((l, i) => { l.zh = z.zh[i]; });
  fs.writeFileSync(f, JSON.stringify(j, null, 1), 'utf8');
  fs.unlinkSync(zf);
  console.log('inject ok:', arg, `(${j.lines.length} 行, title_zh="${j.title_zh}")`);
}

else if (cmd === 'verify') {
  const DATA = loadData();
  const labels = arg === 'all'
    ? fs.readdirSync(EV).filter(f => f.endsWith('.json')).map(f => f.slice(0, -5))
    : [arg];
  let bad = 0, empty = 0, ok = 0;
  for (const lb of labels) {
    const f = path.join(EV, lb + '.json');
    if (!fs.existsSync(f)) { console.log('MISSING', lb); continue; }
    const item = findItem(DATA, lb);
    const j = JSON.parse(fs.readFileSync(f, 'utf8'));
    const src = item ? textLines(item.content) : null;
    const zEmpty = j.lines.filter(l => !l.zh).length;
    if (!src) { console.log('NO-SRC', lb, `${j.lines.length} 行, 空 zh=${zEmpty}`); empty += zEmpty; continue; }
    let mismatch = 0;
    for (let i = 0; i < Math.min(src.length, j.lines.length); i++) {
      if (src[i] !== j.lines[i].en) mismatch++;
    }
    if (mismatch || src.length !== j.lines.length) {
      bad++;
      console.log(`MISMATCH ${lb}: src=${src.length} json=${j.lines.length} diff=${mismatch}`);
    } else { ok++; empty += zEmpty; }
  }
  console.log(`\nverify: ok=${ok} mismatch=${bad} 空zh总数=${empty}`);
}

else if (cmd === 'stats') {
  const DATA = loadData();
  const items = allItems(DATA);
  const labels = new Set(items.map(i => i.label).filter(Boolean));
  const dup = items.length - labels.size;
  const files = fs.existsSync(EV) ? fs.readdirSync(EV).filter(f => f.endsWith('.json')) : [];
  let done = 0, skeleton = 0, totalLines = 0, doneLines = 0;
  for (const f of files) {
    const j = JSON.parse(fs.readFileSync(path.join(EV, f), 'utf8'));
    totalLines += j.lines.length;
    if (j.lines.every(l => l.zh && l.zh.length)) { done++; doneLines += j.lines.length; }
    else skeleton++;
  }
  console.log(`事件总数(含短信): ${items.length}${dup ? ' [label重复 ' + dup + ' !]' : ''}`);
  console.log(`events/ 文件: ${files.length}  已翻: ${done}  骨架待翻: ${skeleton}  未生成: ${labels.size - files.length}`);
  console.log(`行数: 已翻 ${doneLines} / 骨架内 ${totalLines}`);
}

else if (cmd === 'pending') {
  const DATA = loadData();
  const items = allItems(DATA).filter(i => i.cat === arg);
  for (const it of items) {
    const f = path.join(EV, it.label + '.json');
    const done = fs.existsSync(f) && isTranslated(f);
    if (!done) console.log((fs.existsSync(f) ? 'SKELETON ' : 'NONE     ') + it.label);
  }
}

else { console.log('unknown cmd'); process.exit(1); }
