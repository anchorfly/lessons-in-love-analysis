# -*- coding: utf-8 -*-
"""
说话人名补全脚本：
原 guide.html 的每个事件 content 里，每行 .l 的说话人名在 <span class="s" style="color:...">名字</span>，
对话在 <span class="d">: 内容</span>。events/*.json 生成时把说话人名丢了（只留 .d 的 ": 内容"）。
本脚本：从原 guide.html 抽出每个事件每行的 (spk名字, spk颜色)，按行对齐补进 events/*.json 的 spk/spkColor 字段。
只加字段，不动 en/zh/label/title_zh。
"""
import re, json, html, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

GUIDE = r"C:\Users\anke\Desktop\LIL\分析\guide.html"
EVENTS = r"C:\Users\anke\Desktop\LIL\分析\context\events"
DRY_RUN = False   # 已验证 0 未匹配，正式写文件

print("读取原 guide.html ...")
s = open(GUIDE, encoding="utf-8").read()

# 解析 data 块 -> {label: content_html}
m = re.search(r'<script id="data" type="application/json">(.*?)</script>', s, re.S)
cats = json.loads(m.group(1).replace("<\\/", "</"))
label2content = {}
for c in cats:
    for it in c.get("items", []):
        lab = it.get("label")
        if lab and "content" in it and lab not in label2content:
            label2content[lab] = it["content"]
print(f"  原 guide 含 content 的事件: {len(label2content)}")

def parse_lines(content_html):
    """从 content HTML 抽出每行的 (spk名, spk颜色, 对话纯文本)。
    .l 行 = 对话(带.s+.d)；.c 行 = 旁白/指令(无说话人)；.opt 选项。"""
    out = []
    # 逐 div 行抓
    for dm in re.finditer(r'<div class="(l|c|opt)"[^>]*>(.*?)</div>', content_html, re.S):
        cls, body = dm.group(1), dm.group(2)
        spk = re.search(r'<span class="s"[^>]*style="color:([^"]+)"[^>]*>(.*?)</span>', body)
        dlg = re.search(r'<span class="d"[^>]*>(.*?)</span>', body)
        if dlg:  # 对话行
            name = re.sub(r"<[^>]+>", "", spk.group(2)) if spk else ""
            color = spk.group(1) if spk else ""
            text = html.unescape(re.sub(r"<[^>]+>", "", dlg.group(1)))
            out.append(("dlg", html.unescape(name).strip(), color, text))
        else:      # 旁白/指令/选项行
            text = html.unescape(re.sub(r"<[^>]+>", "", body)).replace("\xa0", " ").strip()
            out.append(("narr", "", "", text))
    return out

# 先在一个事件上验证行数对齐
TEST = "amifirsthall"
evj = json.load(open(EVENTS + "\\" + TEST + ".json", encoding="utf-8"))
guide_lines = parse_lines(label2content[TEST])
print(f"\n=== 对齐验证: {TEST} ===")
print(f"  guide 行数: {len(guide_lines)}")
print(f"  json 行数: {len(evj['lines'])}")
print("  guide 前6行 (类型,名字,颜色,对话):")
for g in guide_lines[:6]:
    print("   ", g[0], repr(g[1]), g[2], repr(g[3][:30]))
print("  json 前6行 en:")
for l in evj["lines"][:6]:
    print("   ", repr(l["en"][:30]))


# ---------- 全量补全：按对话文本匹配 ----------
def norm(t):
    return " ".join((t or "").split()).strip()

print("\n\n========== 全量补全说话人名 ==========")
files = sorted(glob.glob(EVENTS + "\\*.json"))
stats = {"files": 0, "lines_total": 0, "dlg_matched": 0, "dlg_nomatch": 0, "no_content": 0}
sample_unmatched = []

for fp in files:
    evj = json.load(open(fp, encoding="utf-8"))
    lab = evj.get("label", "")
    if lab not in label2content:
        stats["no_content"] += 1
        continue
    # 建立 guide 该事件的「对话文本 -> (名字,颜色)」映射（同一文本可能多次出现，取队列）
    glines = parse_lines(label2content[lab])
    from collections import defaultdict, deque
    txt2spk = defaultdict(deque)
    for typ, name, color, text in glines:
        if typ == "dlg":
            txt2spk[norm(text)].append((name, color))
    # 给 json 每行补 spk
    changed = False
    for l in evj["lines"]:
        stats["lines_total"] += 1
        key = norm(l.get("en", ""))
        if key and key in txt2spk and txt2spk[key]:
            name, color = txt2spk[key].popleft()  # 按出现顺序消耗
            if name:
                l["spk"] = name
                if color:
                    l["spkColor"] = color
                stats["dlg_matched"] += 1
                changed = True
        elif key.startswith(":"):
            # 是对话行但没匹配到名字
            stats["dlg_nomatch"] += 1
            if len(sample_unmatched) < 10:
                sample_unmatched.append((lab, key[:40]))
    if changed:
        if not DRY_RUN:
            # 保留缩进可读格式（原文件是 indent=2 的逐行结构，压成单行会毁掉 git diff）
            json.dump(evj, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        stats["files"] += 1

print(f"处理文件: {stats['files']} 补了名字 / 总文件 {len(files)}")
print(f"总行数: {stats['lines_total']}")
print(f"对话行匹配到名字: {stats['dlg_matched']}")
print(f"对话行未匹配: {stats['dlg_nomatch']}")
print(f"guide 无 content 的事件: {stats['no_content']}")
if sample_unmatched:
    print("未匹配样例:")
    for lab, t in sample_unmatched:
        print(f"  {lab}: {t}")

