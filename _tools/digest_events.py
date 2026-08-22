#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
digest_events.py - 将 Ren'Py 事件脚本压缩为"可读摘要"：
- 保留 label 头（带源行号）
- 保留对话/旁白（剥离引号，旁白记为 N:）
- 保留 jump/call 跳转
- 保留 menu 选项（*OPT:）
- 剥离所有代码噪音（if/show/scene/play/$python/注释/空行等）
- lust 类 label 截断为头 20 行 + 尾 8 行，压缩露骨中段

用法: python digest_events.py <src.rpy> [out.txt]
"""
import sys, re, os

CODE_KW = {
    'if','elif','else','while','for','with','return','show','scene','play',
    'hide','call','jump','menu','label','window','transform','pass','python',
    'init','default','image','camera','pause','queue','stop','voice','nvl',
    'centered','while','camera','animate','onlayer','zorder','at','behind',
}
LUST_KW = [
    'lust','sex','reverse','thigh','blow','anal','fing','virg','creampie',
    'handjob','paizuri','titjob','footjob','nipple','pussy','cum','dick',
    'penis','masturb','naked','nude','showersex','bathsex','hand','blowjob',
    'foot','tit','boob','ass','cock','oral','ride','strip','lewd','horny',
    'fuck','bj','hj','hands','aftercare','nuru','spank','ride',
]
HEAD, TAIL = 20, 8

def extract_text(line, start):
    """从 start 之后提取引号内的文本（剥离首尾引号，丢弃末尾属性）。"""
    q1 = line.find('"', start)
    if q1 == -1:
        return line[start:].strip()
    q2 = line.rfind('"')
    if q2 <= q1:
        return line[q1+1:].strip()
    return line[q1+1:q2]

def main():
    if len(sys.argv) < 2:
        print("usage: digest_events.py <src.rpy> [out.txt]")
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else src[:-4] + "_digest.txt"
    with open(src, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    outbuf = []
    cur_label = None
    label_lines = []
    in_menu = False

    def flush(labelname, ln_lines):
        is_lust = any(k in (labelname or '').lower() for k in LUST_KW)
        if is_lust and len(ln_lines) > (HEAD + TAIL + 4):
            for x in ln_lines[:HEAD]:
                outbuf.append(x)
            outbuf.append(f"[TRIMMED {len(ln_lines)-HEAD-TAIL} lines of explicit content]")
            for x in ln_lines[-TAIL:]:
                outbuf.append(x)
        else:
            for x in ln_lines:
                outbuf.append(x)

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip('\n')
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('#'):
            continue
        if stripped.startswith('$'):
            continue
        # label
        m = re.match(r'^label\s+(\w+)\s*:', stripped)
        if m:
            if cur_label is not None:
                flush(cur_label, label_lines)
            cur_label = m.group(1)
            label_lines = []
            outbuf.append(f"\n===== [{i}] LABEL {cur_label} =====")
            in_menu = False
            continue
        # jump / call
        mj = re.match(r'^(?:jump|call)\s+(\w+)', stripped)
        if mj:
            label_lines.append(f"[{i}] >> {mj.group(0)}")
            continue
        # menu start
        if re.match(r'^menu\s*:', stripped):
            in_menu = True
            continue
        # menu option:  "text":
        if in_menu:
            mo = re.match(r'^"([^"]*)"\s*:', stripped)
            if mo:
                label_lines.append(f"[{i}] *OPT: {mo.group(1)}")
                continue
            # 退出菜单：出现非引号开头的行且非跳转则结束菜单
            if not stripped.startswith('"'):
                in_menu = False
                # 不 continue，继续走下方解析
            else:
                continue
        # 跳过已知代码关键字开头的行
        first = stripped.split(None, 1)[0] if stripped else ''
        if first in CODE_KW:
            continue
        # 对话（带 speaker）： WORD "text"
        md = re.match(r'^(\w+)\s+"', stripped)
        if md:
            spk = md.group(1)
            text = extract_text(stripped, md.end(1))
            label_lines.append(f"[{i}] {spk}: {text}")
            continue
        # 旁白（裸引号）： "text"
        mn = re.match(r'^"', stripped)
        if mn:
            text = extract_text(stripped, 0)
            label_lines.append(f"[{i}] N: {text}")
            continue
        # 其它代码行：跳过
    if cur_label is not None:
        flush(cur_label, label_lines)

    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(outbuf) + '\n')
    print(f"digest written: {out}  ({len(outbuf)} lines)")

if __name__ == '__main__':
    main()
