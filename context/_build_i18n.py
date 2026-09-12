# -*- coding: utf-8 -*-
"""
guide.html 三语化改造（骨架 + 按需加载）
读 guide.html（内嵌 content 的 58MB 版）→ 输出 guide_i18n.html：
  - data 块里每个事件剥离 content（正文已在 context/events/{label}.json）
  - 注入三模式切换（中/英/对照）+ 逐句对照渲染器（按需 fetch events/{label}.json）
  - 默认中文，localStorage 记选择，中文样式跟随英文
不推 GitHub（三语调试期）。
"""
import re, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SRC = r"C:\Users\anke\Desktop\LIL\分析\guide.html"
OUT = r"C:\Users\anke\Desktop\LIL\分析\guide_i18n.html"
EVENTS_BASE = "context/events"   # fetch 路径前缀（相对 guide.html 所在目录）

print("读取 guide.html ...")
with open(SRC, encoding="utf-8") as f:
    s = f.read()
print(f"  原始大小: {len(s):,} 字符")

# ---------- 1. 定位并解析 data 块 ----------
m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', s, re.S)
assert m, "找不到 data 块"
data_text = m.group(2)
# 还原 </ 转义
data_text_clean = data_text.replace("<\\/", "</")
cats = json.loads(data_text_clean)
print(f"  data 块解析: {len(cats)} 个分类")

# ---------- 2. 剥离 content，统计 ----------
total_events = 0
stripped_bytes = 0
have_content = 0
for c in cats:
    for it in c.get("items", []):
        total_events += 1
        if "content" in it:
            stripped_bytes += len(it["content"])
            have_content += 1
            it["hasContent"] = True   # 标记：正文在 events/{label}.json
            del it["content"]          # 剥离
print(f"  事件总数: {total_events}, 剥离 content: {have_content}, 释放 {stripped_bytes:,} 字符")

# ---------- 3. 重新序列化 data（瘦身） ----------
new_data = json.dumps(cats, ensure_ascii=False).replace("</", "<\\/")
print(f"  新 data 块: {len(new_data):,} 字符 (原 {len(data_text):,})")
s = s[:m.start(2)] + new_data + s[m.end(2):]
print(f"  替换后总大小: {len(s):,} 字符")

# ---------- 4. 注入三语 CSS ----------
LANG_CSS = """
  /* ===== 三语切换按钮 ===== */
  .langsw{display:flex;border:1px solid var(--line);border-radius:8px;overflow:hidden;flex:0 0 auto}
  .langsw button{background:transparent;border:0;color:var(--muted);padding:6px 12px;cursor:pointer;font-size:13px}
  .langsw button.on{background:var(--accent);color:#fff}
  /* ===== 三语显隐（DOM 同原版：对话行 .l>.s+.d，旁白行 .c；中文行是镜像 .zh-l）=====
     字体/颜色/加粗完全沿用原版 .content 规则，此处只管显隐 */
  [data-lang="zh"] .content .en-l{display:none}     /* 中文：只显中文行 */
  [data-lang="en"] .content .zh-l{display:none}     /* 英文：只显英文行 */
  [data-lang="bi"] .content .zh-l{margin-bottom:6px} /* 对照：中文行在英文行之下，加间距 */
  /* 未翻译行（no-zh）：中文/对照模式下回退显示英文行 */
  [data-lang="zh"] .content .en-l.no-zh{display:block}
  [data-lang="zh"] .content .l.en-l.no-zh{display:flex}
  [data-lang="bi"] .content .zh-l.no-zh{display:none}
  .content .loading{color:var(--muted);font-style:italic}
"""

# 在 </style> 前插入
si = s.find("</style>")
assert si > 0, "找不到 </style>"
s = s[:si] + LANG_CSS + s[si:]
print("  注入三语 CSS")

# ---------- 5. 注入三语切换按钮到 header ----------
# 找 header 的 .top 容器，在 zoom 控件附近加语言切换
LANG_BTN = '<div class="langsw" role="group" aria-label="language"><button data-l="zh" onclick="setLang(\'zh\')">中文</button><button data-l="en" onclick="setLang(\'en\')">English</button><button data-l="bi" onclick="setLang(\'bi\')">对照</button></div>'
# 插在 zoom div 之前（header .top 内）
zm = re.search(r'(<div class="zoom")', s)
if zm:
    s = s[:zm.start(1)] + LANG_BTN + s[zm.start(1):]
    print("  注入语言切换按钮")
else:
    print("  ⚠ 未找到 zoom 控件，按钮未注入")

# ---------- 6. 注入三语 JS（setLang + 渲染器 + 改造 openEvent） ----------
LANG_JS = """
<script>
/* ===== 三语框架 ===== */
const EVENTS_BASE = "__EVENTS_BASE__";
let LANG = localStorage.getItem("lil_lang") || "zh";
const _evCache = {};   // label -> Promise<json>

function setLang(l){
  LANG = l;
  document.body.dataset.lang = l;
  localStorage.setItem("lil_lang", l);
  document.querySelectorAll(".langsw button").forEach(b=>b.classList.toggle("on", b.dataset.l===l));
}
function _esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

/* 拉取某事件的对照 JSON（带缓存） */
function fetchEvent(label){
  if(_evCache[label]) return _evCache[label];
  _evCache[label] = fetch(EVENTS_BASE + "/" + encodeURIComponent(label) + ".json")
    .then(r => { if(!r.ok) throw new Error("HTTP "+r.status); return r.json(); })
    .catch(e => ({label:label, title_zh:"", lines:[], _err:String(e)}));
  return _evCache[label];
}

/* 把 lines 渲染成与原版一致的 DOM 结构：
   对话行(有spk): .l > .s[颜色] + .d   （同原版）
   旁白行(无spk): .c                  （同原版）
   中文行 = 英文行的镜像，保证视觉 100% 一致 */
/* 渲染完整克隆的行序列（100% 还原原版 DOM 结构）：
   图片行 {img} / 对话行 {spk,en,zh} / 旁白代码行 {en,zh} / 空行 {en:""}
   中文行 = 英文行镜像（图片除外，图片中英共用） */
function renderLines(lines){
  let h = "";
  for(const L of lines){
    // 图片行：中英共用，不参与切换
    if(L.img){
      h += '<img class="scene-img" loading="lazy" src="'+_esc(L.img)+'" alt="'+_esc(L.alt||"")+'">';
      continue;
    }
    const en = L.en || "";
    const zh = L.zh || "";
    // 空行：原版是 <div class="c">&nbsp;</div>
    if(!en && !zh){
      h += '<div class="c">&nbsp;</div>';
      continue;
    }
    const hasZh = zh.trim().length > 0;
    const nozh = hasZh ? "" : " no-zh";
    // scene-cap 场景说明行（不参与三语切换，中英共用——英文是 scene 指令）
    if(L.cap){
      h += '<div class="scene-cap">'+_esc(en)+'</div>';
      continue;
    }
    if(L.spk){
      // 对话行：原版 .l > .s[颜色] + .d
      const col = L.spkColor || "";
      const spkHtml = '<span class="s"'+(col?' style="color:'+col+'"':'')+'>'+_esc(L.spk)+'</span>';
      h += '<div class="l en-l'+nozh+'">'+spkHtml+'<span class="d">'+_esc(en)+'</span></div>';
      h += '<div class="l zh-l'+nozh+'">'+spkHtml+'<span class="d">'+_esc(zh)+'</span></div>';
    } else if(L.opt){
      // 选项行：原版 .opt
      h += '<div class="opt en-l'+nozh+'">'+_esc(en)+'</div>';
      h += '<div class="opt zh-l'+nozh+'">'+_esc(zh)+'</div>';
    } else if(!hasZh && /^(label\s|scene\s|jump\s|call\s|show\s|play\s|stop\s|if\s|\$|menu|pause|return|with\s|hide\s)/.test(en.trim())){
      // 代码/指令行（无中文翻译价值）：中英共用，只显示一次
      h += '<div class="c">'+_esc(en)+'</div>';
    } else {
      // 旁白叙述行：原版 .c，中英对照
      h += '<div class="c en-l'+nozh+'">'+_esc(en)+'</div>';
      h += '<div class="c zh-l'+nozh+'">'+_esc(zh)+'</div>';
    }
  }
  return h || '<span class="loading">（无正文数据）</span>';
}

/* 包装 openEvent：正文改为按需 fetch 渲染 */
const _openEvent_orig = openEvent;
openEvent = function(i, idx, rel){
  const c = DATA[i], it = c.items[idx];
  if(it && it.hasContent){
    // 先渲染骨架（不含正文）
    const savedContent = it.content;   // 已无 content，只是占位
    it.content = '<span class="loading">加载中…</span>';
    _openEvent_orig(i, idx, rel);
    it.content = savedContent;
    // 再 fetch 填充
    const contentBox = document.querySelector(".content");
    fetchEvent(it.label).then(d => {
      if(contentBox){
        contentBox.innerHTML = renderLines(d.lines || []);
        // 标题副行：对照/中文模式下显示中文标题
        if(d.title_zh){
          const meta = document.querySelector(".meta");
          if(meta && !meta.querySelector(".ttl-zh")){
            const lang = document.body.dataset.lang;
            if(lang !== "en"){
              meta.insertAdjacentHTML("beforeend", ' &nbsp;<span class="ttl-zh" style="color:var(--muted)">'+_esc(d.title_zh)+'</span>');
            }
          }
        }
      }
    });
  } else {
    _openEvent_orig(i, idx, rel);
  }
};

/* 初始化语言 */
(function(){
  document.body.dataset.lang = LANG;
  document.querySelectorAll(".langsw button").forEach(b=>b.classList.toggle("on", b.dataset.l===LANG));
})();
</script>
"""
LANG_JS = LANG_JS.replace("__EVENTS_BASE__", EVENTS_BASE)

# 在 </body> 前注入
bi = s.rfind("</body>")
assert bi > 0, "找不到 </body>"
s = s[:bi] + LANG_JS + s[bi:]
print("  注入三语 JS")

# ---------- 7. 写输出 ----------
with open(OUT, "w", encoding="utf-8") as f:
    f.write(s)
print(f"\\n输出: {OUT}")
print(f"  最终大小: {len(s):,} 字符")
