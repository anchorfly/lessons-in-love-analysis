# -*- coding: utf-8 -*-
"""
按用户思路重写 events/*.json：
1. 直接从 guide.html 的 content 完整克隆每一行（含图片、scene-cap、代码行），en 100% 还原原版
2. 说话人名（spk/spkColor）从 .s span 提取
3. 中文 zh 按 en 文本从旧 JSON 搬过来（保住已翻的 2.2 万行）
4. title_zh 也保住
行类型：
  - 对话行: {"spk","spkColor","en","zh"}
  - 旁白/代码行: {"en","zh"}
  - 图片行: {"img","alt","cap"}
  - 空行: {"en":""}
"""
import re, json, html, glob, sys, io
from collections import defaultdict, deque
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GUIDE = r"C:\Users\anke\Desktop\LIL\分析\guide.html"
EVENTS = r"C:\Users\anke\Desktop\LIL\分析\context\events"
DRY_RUN = False   # 试跑通过：图片100%、译文0丢失，正式写入

def norm(t):
    return " ".join(html.unescape(t or "").split()).strip()

print("读取 guide.html ...")
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


def content_to_lines(content_html):
    """把 content HTML 完整还原成行序列，每一行原样保留。"""
    out = []
    # content 里行以 \n 分隔（构建期 join("\n")）
    raw_lines = content_html.split("\n")
    for raw in raw_lines:
        raw = raw.strip()
        if not raw:
            continue
        # 空行占位 <div class="c">&nbsp;</div>
        if re.fullmatch(r'<div class="c">&nbsp;</div>', raw):
            out.append({"en": ""})
            continue
        # 图片
        im = re.match(r'<img[^>]*class="scene-img"[^>]*>', raw)
        if im:
            src = re.search(r'src="([^"]+)"', raw)
            alt = re.search(r'alt="([^"]*)"', raw)
            out.append({"img": src.group(1) if src else "",
                        "alt": html.unescape(alt.group(1)) if alt else ""})
            continue
        # scene-cap 场景说明（scene xxx）
        cm = re.match(r'<div class="scene-cap"[^>]*>(.*?)</div>', raw, re.S)
        if cm:
            txt = html.unescape(re.sub(r"<[^>]+>", "", cm.group(1))).strip()
            out.append({"en": txt, "cap": True})
            continue
        # 对话行 .l（.s 说话人 + .d 对话）
        lm = re.match(r'<div class="l">(.*?)</div>', raw, re.S)
        if lm:
            body = lm.group(1)
            sm = re.search(r'<span class="s"[^>]*?style="color:([^"]+)"[^>]*>(.*?)</span>', body)
            if not sm:
                sm = re.search(r'<span class="s"[^>]*>(.*?)</span>', body)
            dm = re.search(r'<span class="d"[^>]*>(.*?)</span>', body, re.S)
            spk = html.unescape(re.sub(r"<[^>]+>", "", sm.group(2))).strip() if sm else ""
            col = sm.group(1) if sm and 'style="color:' in (sm.group(0) or "") else ""
            en = html.unescape(re.sub(r"<[^>]+>", "", dm.group(1))) if dm else ""
            row = {"en": en}
            if spk:
                row["spk"] = spk
                if col:
                    row["spkColor"] = col
            out.append(row)
            continue
        # 旁白/代码行 .c（无说话人）或 .opt（选项）
        om = re.match(r'<div class="(c|opt)"[^>]*>(.*?)</div>', raw, re.S)
        if om:
            cls = om.group(1)
            txt = html.unescape(re.sub(r"<[^>]+>", "", om.group(2))).replace("\xa0", " ").strip()
            if not txt:
                out.append({"en": ""})
                continue
            row = {"en": txt}
            if cls == "opt":
                row["opt"] = True
            out.append(row)
            continue
        # 兜底：未知标签剥掉留纯文本
        txt = html.unescape(re.sub(r"<[^>]+>", "", raw)).replace("\xa0", " ").strip()
        if txt:
            out.append({"en": txt})
    return out


# ---------- 单事件验证 ----------
print("\n=== 单事件验证 amifirsthall ===")
lines = content_to_lines(label2content["amifirsthall"])
print(f"  克隆行数: {len(lines)}")
n_img = sum(1 for l in lines if "img" in l)
n_dlg = sum(1 for l in lines if l.get("spk"))
n_cap = sum(1 for l in lines if l.get("cap"))
print(f"  图片行 {n_img} / 对话行(带spk) {n_dlg} / 场景说明 {n_cap}")
for l in lines[:10]:
    if "img" in l:
        print(f"    [图] {l['img']}")
    elif l.get("spk"):
        print(f"    [话] {l['spk']}: {l['en'][:40]}")
    elif l.get("en"):
        print(f"    [文] {l['en'][:50]}")
    else:
        print(f"    [空]")


# ---------- 全量重建 ----------
print("\n\n========== 全量重建 events ==========")
files = sorted(glob.glob(EVENTS + "\\*.json"))
st = {"files": 0, "lines": 0, "imgs": 0, "zh_kept": 0, "zh_lost": 0, "no_content": 0, "title_kept": 0}
for fp in files:
    old = json.load(open(fp, encoding="utf-8"))
    lab = old.get("label", "")
    if lab not in label2content:
        st["no_content"] += 1
        continue
    # 旧译文映射：en文本 -> zh（队列防重复句错位）
    zh_map = defaultdict(deque)
    for l in old.get("lines", []):
        z = (l.get("zh") or "").strip()
        if z:
            zh_map[norm(l.get("en", ""))].append(z)
    old_title_zh = old.get("title_zh", "")

    # 从 content 完整克隆
    newlines = content_to_lines(label2content[lab])
    for l in newlines:
        if "img" in l or not l.get("en"):
            continue
        key = norm(l["en"])
        if key in zh_map and zh_map[key]:
            l["zh"] = zh_map[key].popleft()
            st["zh_kept"] += 1
        else:
            l["zh"] = ""
    # 旧有译文但没匹配上的（理论上不应发生）
    st["zh_lost"] += sum(len(q) for q in zh_map.values())

    newj = {"label": lab, "title_zh": old_title_zh, "lines": newlines}
    if old_title_zh:
        st["title_kept"] += 1
    st["lines"] += len(newlines)
    st["imgs"] += sum(1 for l in newlines if "img" in l)
    if not DRY_RUN:
        json.dump(newj, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    st["files"] += 1

print(f"重建文件: {st['files']} / {len(files)}（无 content: {st['no_content']}）")
print(f"总行数: {st['lines']}  图片行: {st['imgs']}")
print(f"中文译文保住: {st['zh_kept']}  丢失: {st['zh_lost']}  标题保住: {st['title_kept']}")
