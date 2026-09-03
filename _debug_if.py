import re, glob, os

BASE = r"C:\Users\anke\Desktop\LIL\分析\游戏文本"
labels = ["beachseven1","beachseven5","beachsevenio1","beachsevenchika1"]
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

for lab in labels:
    fn, blk = blocks[lab]
    lines = blk.split("\n")
    print(f"\n{'#'*60}\n### {lab} [{fn}] 总行数={len(lines)}\n{'#'*60}")
    # 真实 if 语句行（行首 if/elif/else 后跟空格+内容+冒号，允许行尾注释）
    real = [(i+1, l) for i,l in enumerate(lines)
            if re.match(r'^\s*(if|elif|else)\b(\s+|\s*:)', l) and (':' in l)]
    print(f"真实分支语句(if/elif/else 行): {len(real)}")
    for ln, l in real[:40]:
        print(f"   L{ln}: {l.strip()[:100]}")
    # 含 'if' 但非分支（对话）示例
    dlg = [(i+1, l) for i,l in enumerate(lines)
           if re.search(r'\bif\b', l) and not re.match(r'^\s*(if|elif|else)\b(\s+|\s*:)', l)]
    if dlg:
        print(f"   ...(对话/其它含'if'的行: {len(dlg)} 处，例 L{dlg[0][0]}: {dlg[0][1].strip()[:80]})")
