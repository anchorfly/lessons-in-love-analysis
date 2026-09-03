import re, glob, os

BASE = r"C:\Users\anke\Desktop\LIL\分析\游戏文本"
labels = ["beachseven1","beachseven2","beachseven3","beachsevenio1","beachsevenami1",
          "beachsevenchika1","beachseventouka1","beachsevenwakana1","beachsevenwakana2",
          "beachsevenkarin1","beachsevenchika2","beachsevenrin1","beachsevenimani1",
          "beachseven4intro","beachseven5"]

# 收集块
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

print("找到块:", len(blocks), "/ 15\n")
for lab in labels:
    fn, blk = blocks.get(lab, ("? 未找到",""))
    if not blk:
        print(f"[缺失] {lab}"); continue
    menus = len(re.findall(r'\bmenu\s*:', blk))
    branch_kw = len(re.findall(r'\b(if|elif|else)\b', blk))
    jumps = re.findall(r'\b(jump|call)\s+([A-Za-z0-9_]+)', blk)
    sub = re.findall(r'^[ \t]*label\s+([A-Za-z0-9_]+)\s*:', blk, re.M)
    sub = [s for s in sub if s != lab]
    bonus = len(re.findall(r'\b(bonus)\b', blk, re.I))
    print(f"{lab:18s} [{fn:22s}] {len(blk):>7}字符 | menu={menus} if/else={branch_kw} jump/call={len(jumps)} 子label={len(sub)} bonus={bonus}")
    if sub:
        print(f"    子label: {sub}")
