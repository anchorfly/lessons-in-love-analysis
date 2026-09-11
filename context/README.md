# LIL guide.html 三语翻译 — 工作区说明（给翻译 agent）

## 这是什么

`guide.html` 是 Ren'Py 视觉小说《Lessons in Love》的事件导航页。现在要做**中文 / 英文 / 中英对照**三模式切换。你的任务是：把这里的中文词条翻译成**英文**，填进各 `zh-en` 对照表。

> 方向说明：站点的正文（对话）原始语言是**英文**，UI 界面文案原始语言是**中文**。
> 所以——**UI 文案是「中→英」**（已有中文，补英文）；**对话正文是「英→中」**（已有英文，补中文）。两边方向相反，别搞混。

## 目录结构

```
context/
├── README.md            ← 本说明
├── ui/zh-en.json        ← UI 界面文案（中→英）。量小，先做这个。
├── speakers/zh-en.json  ← 说话人名对照（中→英）。角色名多为英文名，按需补充。
├── cats/zh-en.json      ← 分类名（中→英）
├── versions/zh-en.json  ← 版本号相关文案（中→英）
└── events/              ← 每个事件一个 {label}.json，正文逐句对照（英→中）
```

## 文件格式（严格 JSON，UTF-8，禁止注释）

### ui / speakers / cats / versions（中→英）

```json
{
  "中文词条": "English Translation",
  "游戏图片": "Game Image"
}
```

- **key = 中文原文（一个字都不能改）**，value = 你翻的英文。
- key 必须与现有词条**逐字符一致**（含标点、空格、全角符号），否则整合时对不上。
- 不需要翻译的（如纯版本号、已是英文的）可以留空字符串 `""` 或省略该 key，整合时回退显示原文。

### events/{label}.json（英→中，逐句对照）

每个事件一个文件，文件名 = 事件 label（如 `chikachristmalloween2.json`）：

```json
{
  "label": "chikachristmalloween2",
  "title_zh": "在学校见你",
  "lines": [
    { "en": "Chika: Hey, you made it.", "zh": "Chika：嘿，你来了。" },
    { "en": "...", "zh": "" }
  ]
}
```

- `lines[].en` = 英文原句（**必须与源文逐字符一致**，作为对齐锚点）。
- `lines[].zh` = 你翻的中文。`""` 表示待翻译。
- `title_zh` = 事件标题的中文译名。

## 翻译要求

0. **路径/文件名一律英文**：目录名、文件名用英文或事件 label 原名，禁止中文命名（中文路径在 URL 里会百分号编码，跨系统可能 404）。中文只进 JSON 的 value，不进路径。
1. **不改 key / en 原文**，只填 value / zh。这是铁律。
2. 保留原文的换行、语气、角色口癖（如 Chika 的活泼、Touka 的克制）。
3. 双关、梗、专有名词（如 Sekai、pareidolia、ELATION PROTOCOL）尽量直译并保持一致，拿不准就保留原词加注释。
4. 一次可以只翻一部分文件——**增量进行**，翻好哪些交哪些，整合端只认已填的条目。

## 交付

翻好的 JSON 直接放回原目录覆盖即可。整合脚本会读取并把译文注入 guide.html。
