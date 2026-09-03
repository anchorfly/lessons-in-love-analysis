import re, glob, os

BASE = r"C:\Users\anke\Desktop\LIL\分析\游戏文本"
labels = ["beachseven1","beachseven2","beachseven3","beachsevenio1","beachsevenami1",
          "beachsevenchika1","beachseventouka1","beachsevenwakana1","beachsevenwakana2",
          "beachsevenkarin1","beachsevenchika2","beachsevenrin1","beachsevenimani1",
          "beachseven4intro","beachseven5"]

blocks = {}
for f in glob.glob(os.path.join(BASE,"*.rpy")):
    txt = open(f, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r'^[ \t]*label\s+([A-Za-z0-9_]+)\s*:', txt, re.M):
        lab = m.group(1)
        if lab not in labels: continue
        st = m.start()
        nx = re.search(r'\n[ \t]*label\s+[A-Za-z0-9_]+\s*:', txt[st+1:])
        en = st+1+nx.start()+1 if nx else len(txt)
        blocks[lab] = (os.path.basename(f), txt[st:en])

out = []
def log(s=""): out.append(s)

for lab in labels:
    fn, blk = blocks[lab]
    log(f"\n{'='*70}\n### {lab}  [{fn}]\n{'='*70}")
    lines = blk.split("\n")

    # 1) menu 块
    menu_count = 0
    for i, l in enumerate(lines):
        if re.match(r'\s*menu\s*(?:\([^)]*\))?\s*:', l):
            menu_count += 1
            log(f"\n  [MENU #{menu_count}] 行{i+1}")
            # 收集选项："文本": 或 "文本" 然后缩进块
            j = i+1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].startswith("\t")):
                ls = lines[j].strip()
                if re.match(r'^"[^"]*"\s*:', ls) or re.match(r'^"[^"]*"\s*$', ls):
                    # 选项是这一行；找其跳转
                    tgt = ""
                    k = j+1
                    while k < len(lines) and (lines[k].startswith(" ") or lines[k].startswith("\t")) and lines[k].strip():
                        km = re.search(r'\b(jump|call)\s+([A-Za-z0-9_]+)', lines[k])
                        if km: tgt = f" -> {km.group(1)} {km.group(2)}"; break
                        if re.match(r'"', lines[k].strip()): tgt = " (对话)"; break
                        k += 1
                    opt = re.match(r'^"([^"]*)"', ls).group(1)
                    log(f"      • {opt[:60]}{tgt}")
                j += 1
    if menu_count == 0:
        log("  (无玩家选项 menu)")

    # 2) if/elif/else 条件分支（去重计数）
    conds = {}
    for i, l in enumerate(lines):
        m = re.match(r'\s*(if|elif|else)\b\s*(.*?):\s*$', l)
        if m:
            kw, cond = m.group(1), m.group(2).strip()
            key = (kw, cond)
            conds.setdefault(key, 0)
            conds[key] += 1
    log(f"\n  条件分支 (if/elif/else) 共 {sum(conds.values())} 处，去重 {len(conds)} 类:")
    for (kw, cond), n in conds.items():
        disp = cond if cond else "—(无条件的else)—"
        log(f"      {kw:5s} {disp[:90]}  ×{n}" if n==1 else f"      {kw:5s} {disp[:90]}  ×{n}")

open(r"C:\Users\anke\Desktop\LIL\分析\_beachseven_branch.txt","w",encoding="utf-8").write("\n".join(out))
print("已写入 _beachseven_branch.txt，总行数:", len(out))
