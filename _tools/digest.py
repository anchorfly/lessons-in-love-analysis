# -*- coding: utf-8 -*-
"""Ren'Py -> readable digest: label headers with source line numbers,
dialogue/narration, menu options, jumps/calls/flags. Lust labels truncated."""
import io, os, re

SRC = r"C:\Users\anke\Desktop\LIL\分析\游戏文本"
OUT = r"C:\Users\anke\Desktop\LIL\分析\.digest"
os.makedirs(OUT, exist_ok=True)

skip_pat = re.compile(
    r'^\s*(scene |show |hide |play |stop |queue |window |with |pause |nvl |'
    r'\$ renpy|transform |image |define |default |init |style |screen |text |'
    r'add |vbox|hbox|frame|button|key |mousearea|bar |use |has |pass$|return$|'
    r'old |new |voice |camera|zorder|parallel|block|choice |from )'
)
label_pat = re.compile(r'^label\s+([A-Za-z0-9_]+)')
dial_pat = re.compile(r'^(\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s+"(.*)"\s*$')
nar_pat = re.compile(r'^\s*"(.*)"\s*:?\s*$')
ctl_pat = re.compile(r'^\s*(jump\s+\S+|call\s+\S+|if\s+.*|elif\s+.*|else\s*:|menu\s*:|menu\s+\S+|\$\s+\S+.*)$')
opt_pat = re.compile(r'^\s*"(.+?)":\s*$')

def digest_file(path):
    lines = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
    out = []
    cur = None
    cur_lines = []          # buffered digest lines of current label
    is_lust = False
    def flush():
        nonlocal cur_lines
        if cur is None:
            out.extend(cur_lines); cur_lines = []
            return
        if is_lust and len(cur_lines) > 30:
            head, tail = cur_lines[:20], cur_lines[-8:]
            out.extend(head)
            out.append("...[lust label truncated, %d lines omitted]..." % (len(cur_lines)-28))
            out.extend(tail)
        else:
            out.extend(cur_lines)
        cur_lines = []
    for i, ln in enumerate(lines, 1):
        m = label_pat.match(ln)
        if m:
            flush()
            cur = m.group(1)
            is_lust = ('lust' in cur) or ('nude' in cur) or ('sex' in cur)
            out.append("")
            out.append("===== [%d] %s =====" % (i, cur))
            continue
        if skip_pat.match(ln):
            continue
        if dial_pat.match(ln):
            cur_lines.append("[%d]%s" % (i, ln.rstrip()))
        elif opt_pat.match(ln) or ctl_pat.match(ln):
            cur_lines.append("[%d]%s" % (i, ln.rstrip()))
        elif nar_pat.match(ln):
            cur_lines.append("[%d]%s" % (i, ln.rstrip()))
        # else: noise
    flush()
    return out

for fn in sorted(os.listdir(SRC)):
    if not fn.endswith('.rpy'):
        continue
    res = digest_file(os.path.join(SRC, fn))
    dst = os.path.join(OUT, fn.replace('.rpy', '.txt'))
    io.open(dst, 'w', encoding='utf-8').write('\n'.join(res))
    print("%-28s %6d -> %6d lines" % (fn, sum(1 for _ in io.open(os.path.join(SRC,fn), encoding='utf-8', errors='replace')), len(res)))
