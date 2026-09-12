# -*- coding: utf-8 -*-
"""
译文应用脚本：读补丁文件 _patch.json（{label: {en: zh}} 或 {label: {"__title__": "标题"}}），
把中文写进 context/events/{label}.json 对应行的 zh 字段。
只填空白的 zh，不覆盖已有译文。保留 indent=2 格式。
用法: python _apply_zh.py _patch.json
"""
import json, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

EVENTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events")

patch = json.load(open(sys.argv[1], encoding="utf-8"))
total = 0
for lab, mapping in patch.items():
    fp = os.path.join(EVENTS, lab + ".json")
    if not os.path.exists(fp):
        print(f"  ⚠ 文件不存在: {lab}")
        continue
    d = json.load(open(fp, encoding="utf-8"))
    title = mapping.pop("__title__", None)
    if title:
        d["title_zh"] = title
    n = 0
    for l in d["lines"]:
        en = (l.get("en") or "")
        if en in mapping and not (l.get("zh") or "").strip():
            l["zh"] = mapping[en]
            n += 1
    json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    done = sum(1 for l in d["lines"] if (l.get("zh") or "").strip())
    print(f"  {lab}: +{n} 行 → 本事件共 {done} 行已翻")
    total += n
print(f"合计写入 {total} 行")
