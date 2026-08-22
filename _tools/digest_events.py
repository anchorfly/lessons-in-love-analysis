#!/usr/bin/env python3
"""digest_events.py — Ren'Py .rpy -> readable digest.

Keeps: label headers (with source line numbers), dialogue/narration lines,
jump/call targets, menu option texts. Strips code noise (python $ blocks,
scene/show/play/audio, style/screen declarations...).
Explicit/lust-ish labels are truncated: keep head 20 + tail 8 lines.

Output line format:
  ===== [SRC_LINE] LABEL <name> =====
  [SRC_LINE] spk: text        (speaker line)
  [SRC_LINE] N: text          (unframed narration)
  [SRC_LINE] >> jump <label>  (control flow)
  [SRC_LINE] *OPT: text       (menu option)

Usage: digest_events.py <src.rpy> <out.txt>
"""
import re
import sys

CODE_KW = {
    'scene', 'show', 'hide', 'play', 'stop', 'queue', 'with', 'pause',
    'window', 'image', 'transform', 'label', 'return', 'if', 'elif',
    'else', 'while', 'for', 'pass', 'screen', 'define', 'default',
    'init', 'python', 'menu', 'renpy', 'style', 'frame', 'vbox',
    'hbox', 'text', 'textbutton', 'button', 'add', 'at', 'music',
    'sound', 'voice', 'camera', 'jump', 'call', '$',
}
TRUNCATE_LABEL = re.compile(r'(lust|sex|nude|inappropriate|bonusanim|anim)', re.I)
HEAD_KEEP, TAIL_KEEP = 20, 8


def extract_text(line, start):
    """Extract quoted text starting after position `start` (speaker end)."""
    m = re.search(r'"((?:[^"\\]|\\.)*)"', line[start:])
    return m.group(1) if m else ''


def digest(src_path, out_path):
    with open(src_path, encoding='utf-8') as f:
        lines = f.readlines()
    out = []
    i = 0
    n = len(lines)
    label_re = re.compile(r'^label\s+(\w+)')
    while i < n:
        m = label_re.match(lines[i])
        if not m:
            i += 1
            continue
        label = m.group(1)
        src_no = i + 1
        body = []
        j = i + 1
        in_menu = False
        while j < n and not label_re.match(lines[j]):
            raw = lines[j]
            stripped = raw.strip()
            j += 1
            if not stripped:
                continue
            first = stripped.split(None, 1)[0]
            # menu option: "text":  (indented quote ending with colon)
            mo = re.match(r'^"([^"]*)"\s*:', stripped)
            if mo:
                body.append(f"[{j-1}] *OPT: {mo.group(1)}")
                in_menu = True
                continue
            # jump / call
            if first in ('jump', 'call'):
                tgt = stripped.split(None, 1)[1].split()[0] if len(stripped.split(None, 1)) > 1 else ''
                body.append(f"[{j-1}] >> {first} {tgt}")
                continue
            if first in CODE_KW:
                continue
            # dialogue: word "text"
            md = re.match(r'^(\w+)\s+"', stripped)
            if md:
                spk = md.group(1)
                text = extract_text(stripped, md.end(1))
                body.append(f"[{j-1}] {spk}: {text}")
                continue
            # bare narration: "text"
            if stripped.startswith('"'):
                text = extract_text(stripped, 0)
                body.append(f"[{j-1}] N: {text}")
                continue
        # truncate explicit labels
        if TRUNCATE_LABEL.search(label) and len(body) > HEAD_KEEP + TAIL_KEEP + 4:
            cut = len(body) - HEAD_KEEP - TAIL_KEEP
            body = body[:HEAD_KEEP] + [f"[TRIMMED {cut} lines of explicit content]"] + body[-TAIL_KEEP:]
        out.append(f"===== [{src_no}] LABEL {label} =====")
        out.extend(body)
        i = j
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(f"digest written: {out_path}  ({len(out)} lines)")


if __name__ == '__main__':
    digest(sys.argv[1], sys.argv[2])
