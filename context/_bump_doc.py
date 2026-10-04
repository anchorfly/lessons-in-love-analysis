# -*- coding: utf-8 -*-
"""
一键 bump：把 sw.js 的 CACHE_DOC 版本号 +1（改过 guide.html / guide_i18n.html 后必跑）。

用法：
  python context/_bump_doc.py            # +1 并打印
  python context/_bump_doc.py "说明文字"  # +1，同时在注释里记一行本次改了什么

背景：HTML 外壳走 SW 的 swr 缓存（CACHE_DOC）。改了 HTML 不 bump，
浏览器就一直吃旧缓存，用户必须手动清缓存才能看到改动。
"""
import re, os, sys, time

ROOT = r'C:/Users/anke/Desktop/LIL/分析'.replace('\\', '/')
SW = os.path.join(ROOT, 'sw.js')

txt = open(SW, encoding='utf-8').read()
m = re.search(r"const CACHE_DOC = 'lil-doc-v(\d+)'", txt)
if not m:
    print('没找到 CACHE_DOC 常量，检查 sw.js'); sys.exit(1)

old, new = int(m.group(1)), int(m.group(1)) + 1
txt = txt.replace("lil-doc-v%d" % old, "lil-doc-v%d" % new)

note = sys.argv[1] if len(sys.argv) > 1 else ''
if note:
    # 在 CACHE_DOC 声明的注释块末尾追加一行记录
    anchor = "const CACHE_DOC = 'lil-doc-v%d';" % new
    i = txt.index(anchor)
    j = txt.index('\n', i)
    txt = txt[:j + 1] + "                                  //       v%d=%s\n" % (new, note) + txt[j + 1:]

tmp = SW + '.tmp%d' % os.getpid()
open(tmp, 'w', encoding='utf-8').write(txt)
for _ in range(5):
    try:
        os.replace(tmp, SW); break
    except Exception as e:
        print('重试', e); time.sleep(1)
else:
    print('写入失败'); sys.exit(1)

print('CACHE_DOC: lil-doc-v%d -> lil-doc-v%d  ✅' % (old, new))
print('（改完 HTML 记得跑这个；事件 json 是另一条链路，跑 _gen_evtver.py）')
