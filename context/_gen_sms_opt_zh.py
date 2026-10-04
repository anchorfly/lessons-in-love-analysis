# -*- coding: utf-8 -*-
"""生成短信选项的中文映射，并注入 guide.html。

背景：短信选项（menu 选项）只存在于 sms.content 骨架里、且只有英文；
events/{label}.json 的 lines 里没有对应条目。译文散落在 context/_gap_zh/*.json
与 context/_mt_zh.json 里（EN→ZH 映射）。

用法：python context/_gen_sms_opt_zh.py
注入位置：guide.html 里 <script id="data">…</script> 之后，包在
  /* SMS_OPT_ZH_START */ … /* SMS_OPT_ZH_END */ 之间（幂等，可重复运行）。
"""
import io, sys, os, re, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r'C:/Users/anke/Desktop/LIL/分析'
G = os.path.join(ROOT, 'guide.html')

t = open(G, encoding='utf-8').read()

# 1) 抽短信选项
m = re.search(r'<script id="data"[^>]*>(.*?)</script>', t, re.S)
if not m:
    print('找不到 <script id="data">'); sys.exit(1)
DATA = json.loads(m.group(1).replace('<\\/', '</'))
opts = []
for c in DATA:
    for x in (c.get('sms') or []):
        for mm in re.finditer(r'<div class="opt"[^>]*>([\s\S]*?)</div>', x.get('content', '')):
            s = re.sub(r'<[^>]*>', '', mm.group(1)).replace('&nbsp;', ' ').strip()
            if s and s not in opts:
                opts.append(s)

# 2) 合并译文源
emap = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'context', '_gap_zh', '*.json'))):
    try:
        d = json.load(open(f, encoding='utf-8'))
        if isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, str) and k not in emap:
                    emap[k] = v
    except Exception:
        pass
for f in (os.path.join(ROOT, 'context', '_mt_zh.json'),):
    if os.path.exists(f):
        try:
            d = json.load(open(f, encoding='utf-8'))
            if isinstance(d, dict):
                for k, v in d.items():
                    if isinstance(v, str) and k not in emap:
                        emap[k] = v
        except Exception:
            pass

# 3) 只保留能匹配上的
mapped = {s: emap[s] for s in opts if s in emap}
print('短信选项 %d 个，匹配到译文 %d 个' % (len(opts), len(mapped)))

# 4) 注入
body = json.dumps(mapped, ensure_ascii=False, separators=(',', ':'))
block = ('/* SMS_OPT_ZH_START */\n<script>var SMS_OPT_ZH = %s;</script>\n/* SMS_OPT_ZH_END */' % body)

if '/* SMS_OPT_ZH_START */' in t:
    t = re.sub(r'/\* SMS_OPT_ZH_START \*/[\s\S]*?/\* SMS_OPT_ZH_END \*/', block, t, count=1)
else:
    anchor = '</script>'
    i = t.index('<script id="data"')
    j = t.index(anchor, i) + len(anchor)
    t = t[:j] + '\n' + block + t[j:]

tmp = G + '.tmp%d' % os.getpid()
open(tmp, 'w', encoding='utf-8').write(t)
os.replace(tmp, G)
print('已注入 guide.html（%d 条，约 %d 字节）' % (len(mapped), len(body)))
