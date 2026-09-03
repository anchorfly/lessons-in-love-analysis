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

# 检查延伸分支 beachseven4f1/f2 是否存在
extra = {}
for f in glob.glob(os.path.join(BASE,"*.rpy")):
    txt = open(f, encoding="utf-8", errors="ignore").read()
    for lab in ("beachseven4f1","beachseven4f2"):
        if re.search(rf'^[ \t]*label\s+{lab}\s*:', txt, re.M):
            extra[lab] = os.path.basename(f)

out = []
def log(s=""): out.append(s)

def first_meaningful(lines, start, end):
    """从 start 行起，返回首个有意义(对话/语句/flag)的短摘要，abstract 敏感内容。"""
    for k in range(start, min(end, len(lines))):
        ls = lines[k].strip()
        if not ls or ls.startswith("#"): continue
        # flag 设置
        fm = re.match(r'\s*\$([A-Za-z0-9_]+)\s*=\s*(.+)', ls)
        if fm:
            return f"[$ 设 {fm.group(1)} = {fm.group(2)[:30]}]"
        # jump/call
        jm = re.match(r'\s*(jump|call)\s+([A-Za-z0-9_]+)', ls)
        if jm:
            return f"[→ {jm.group(1)} {jm.group(2)}]"
        # 对话
        dm = re.match(r'\s*[A-Za-z_]\w*\s+"([^"]*)"', ls)
        if dm:
            t = dm.group(1)
            return "「"+t[:45]+("…" if len(t)>45 else "")+"」"
        if re.match(r'\s*scene|image|play |show ', ls):
            return "[场景/演出]"
    return "[（无后续语句）]"

for lab in labels:
    fn, blk = blocks[lab]
    lines = blk.split("\n")
    log(f"\n{'='*64}\n### {lab}  [{fn}]\n{'='*64}")
    # if/elif/else 详情
    for i, l in enumerate(lines):
        m = re.match(r'^(\s*)(if|elif|else)(\b|\s*:)(.*)$', l)
        if not m: continue
        indent = len(m.group(1)); kw = m.group(2); cond = m.group(4).strip().rstrip(":")
        # 找该分支块（同级缩进结束）
        j = i+1
        while j < len(lines):
            if lines[j].strip()=="" : j+=1; continue
            if len(lines[j]) - len(lines[j].lstrip()) <= indent:
                break
            j += 1
        detail = first_meaningful(lines, i+1, j)
        if kw == "else":
            log(f"  └ else:  {detail}")
        else:
            log(f"  ├ if {cond[:70]}:  {detail}")
    # menu
    for i, l in enumerate(lines):
        if re.match(r'\s*menu\s*(?:\([^)]*\))?\s*:', l):
            log(f"  [MENU] 行{i+1}")
            j = i+1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].startswith("\t")):
                ls = lines[j].strip()
                om = re.match(r'^"([^"]*)"\s*:', ls)
                if om:
                    tgt=""
                    k=j+1
                    while k<len(lines) and (lines[k].startswith(" ")) and lines[k].strip():
                        km=re.search(r'\b(jump|call)\s+([A-Za-z0-9_]+)', lines[k])
                        if km: tgt=f" → {km.group(1)} {km.group(2)}"; break
                        if re.match(r'"', lines[k].strip()): tgt=" (对话)"; break
                        k+=1
                    log(f"      • {om.group(1)[:50]}{tgt}")
                j+=1

log("\n"+"="*64)
log("### 延伸分支（beachseven4intro 的 menu 目标）")
log("="*64)
for lab in ("beachseven4f1","beachseven4f2"):
    if lab in extra:
        # 提取块大小
        f = glob.glob(os.path.join(BASE, extra[lab]))
        txt = open(f[0], encoding="utf-8", errors="ignore").read()
        m = re.search(rf'^[ \t]*label\s+{lab}\s*:', txt, re.M)
        st=m.start(); nx=re.search(r'\n[ \t]*label\s+[A-Za-z0-9_]+\s*:', txt[st+1:])
        en=st+1+nx.start()+1 if nx else len(txt)
        log(f"  {lab} [{extra[lab]}] {len(txt[st:en])} 字符")
    else:
        log(f"  {lab}: 未找到（可能不在本版本）")

open(r"C:\Users\anke\Desktop\LIL\分析\_beachseven_detail.txt","w",encoding="utf-8").write("\n".join(out))
print("写入 _beachseven_detail.txt，", len(out), "行")
