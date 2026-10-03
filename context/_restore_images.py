# -*- coding: utf-8 -*-
"""
场景图片补全脚本：
原 guide.html 的 content 里，图片是 <img class="scene-img" src="..."> 穿插在文字行之间，
events/*.json 生成时把图片全丢了。本脚本把图片按原始顺序挂回 JSON。

锚点策略：
  遍历原 content 行序列，对每张图片记录「它前面最近的那句对话/旁白文本」作为锚点；
  在 JSON 里找到该锚点文本的那行，把图片插到它后面（同锚点多图则按序）。
  图片在 JSON 中表示为 {"img": "src", "alt": "...", "cap": "说明"}。
"""
import re, json, html, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GUIDE = r"C:\Users\anke\Desktop\LIL\分析\guide.html"
EVENTS = r"C:\Users\anke\Desktop\LIL\分析\context\events"
DRY_RUN = False   # 已验证95.2%插回率，正式写文件

def norm(t):
    return " ".join(html.unescape(t or "").split()).strip()

print("读取原 guide.html ...")
s = open(GUIDE, encoding="utf-8").read()
m = re.search(r'<script id="data" type="application/json">(.*?)</script>', s, re.S)
cats = json.loads(m.group(1).replace("<\\/", "</"))
label2content = {}
for c in cats:
    for it in c.get("items", []):
        lab = it.get("label")
        if lab and "content" in it and lab not in label2content:
            label2content[lab] = it["content"]
print(f"  含 content 的事件: {len(label2content)}")


def build_img_map(content_html):
    """返回 {锚点文本(norm): [ {img,alt,cap}, ... ]}，以及无锚点的图片列表"""
    # 把 content 切成 token 序列：按出现的标签顺序
    tokens = []
    for tm in re.finditer(
            r'<div class="(l|c|opt)"[^>]*>(.*?)</div>'
            r'|<img[^>]*class="scene-img"[^>]*>'
            r'|<div class="scene-cap"[^>]*>(.*?)</div>', content_html, re.S):
        g = tm.group(0)
        if g.startswith('<img'):
            src = re.search(r'src="([^"]+)"', g)
            alt = re.search(r'alt="([^"]*)"', g)
            tokens.append(("img", {"src": src.group(1) if src else "",
                                   "alt": html.unescape(alt.group(1)) if alt else ""}))
        elif 'scene-cap' in g:
            cap = html.unescape(re.sub(r"<[^>]+>", "", tm.group(3) or "")).strip()
            tokens.append(("cap", cap))
        else:
            cls = tm.group(1); body = tm.group(2)
            dlg = re.search(r'<span class="d"[^>]*>(.*?)</span>', body)
            if dlg:
                txt = html.unescape(re.sub(r"<[^>]+>", "", dlg.group(1)))
            else:
                txt = html.unescape(re.sub(r"<[^>]+>", "", body)).replace("\xa0", " ").strip()
            txt = norm(txt)
            if not txt:
                continue
            tokens.append(("txt", txt))
    # 给每张图找前序最近文本作为锚点
    imap = {}
    last_txt = None
    orphan = []
    for kind, val in tokens:
        if kind == "txt":
            last_txt = val
        elif kind == "cap":
            continue
        elif kind == "img":
            if last_txt is None:
                orphan.append(val)
            else:
                imap.setdefault(last_txt, []).append(val)
    return imap, orphan


print("\n=== 单事件验证 (amifirsthall) ===")
imap, orphan = build_img_map(label2content["amifirsthall"])
print(f"  锚点图片映射条目: {len(imap)}, 无锚点(开头图): {len(orphan)}")
tot_img = sum(len(v) for v in imap.values()) + len(orphan)
print(f"  图片总数: {tot_img}")

evj = json.load(open(EVENTS + "\\amifirsthall.json", encoding="utf-8"))
hit = sum(1 for l in evj["lines"] if norm(l.get("en", "")) in imap)
print(f"  JSON 中能命中锚点的行: {hit}/{len(evj['lines'])}")

# ---------- 全量写回 ----------
print("\n\n========== 全量补图 ==========")
files = sorted(glob.glob(EVENTS + "\\*.json"))
st = {"files": 0, "img_total": 0, "img_hit": 0, "orphan": 0, "no_content": 0}
seen_imgs = set()
for fp in files:
    evj = json.load(open(fp, encoding="utf-8"))
    lab = evj.get("label", "")
    if lab not in label2content:
        st["no_content"] += 1
        continue
    imap, orphan = build_img_map(label2content[lab])
    n = sum(len(v) for v in imap.values()) + len(orphan)
    if n == 0:
        continue
    st["img_total"] += n
    newlines = []
    inserted = 0
    for l in evj["lines"]:
        newlines.append(l)
        key = norm(l.get("en", ""))
        if key in imap and imap[key]:
            for im in imap.pop(key):
                newlines.append({"img": im["src"], "alt": im["alt"]})
                inserted += 1
                st["img_hit"] += 1
                seen_imgs.add(im["src"])
    # 无锚点的图（理论上应为空，若有则放最前面）
    for im in orphan:
        newlines.insert(0, {"img": im["src"], "alt": im["alt"]})
        st["orphan"] += 1
    if inserted or orphan:
        evj["lines"] = newlines
        if not DRY_RUN:
            # 保留缩进可读格式（避免压缩单行毁掉 git diff）
            json.dump(evj, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        st["files"] += 1

print(f"处理文件: {st['files']} / {len(files)}")
print(f"图片总数: {st['img_total']}  插回: {st['img_hit']}  无锚点置顶: {st['orphan']}")
print(f"guide 无 content 的事件: {st['no_content']}")
print(f"去重后图片资源数: {len(seen_imgs)}")
