import re, json

blob = open(r"C:\Users\anke\Desktop\LIL\分析\guide.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'<script id="release" type="application/json">(.*?)</script>', blob, re.S)
REL = json.loads(m.group(1))
print("RELEASE.version =", REL.get("version"))
print("RELEASE keys =", list(REL.keys()))
its = REL.get("items", [])
print("版本更新事件数:", len(its))
print()
for k, it in enumerate(its):
    # 兼容不同字段名
    lab = it.get("label") or it.get("id") or it.get("key")
    title = it.get("title") or it.get("name") or ""
    print("  [%02d] label=%-24s title=%s" % (k+1, lab, title))
