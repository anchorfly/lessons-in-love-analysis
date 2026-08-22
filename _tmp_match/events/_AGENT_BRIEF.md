# 升级任务通用指令（Agent Brief）

你正在把一份「浅版」角色事件分析 markdown，升级为**逐事件精读**，用于《Sensei / Lessons in Love / Dreams of an Aki》（Sekai 项目）的学术式源文分析。

## 工作目录（绝对路径）
`C:\Users\anke\Desktop\LIL\分析\_tmp_match\events`

## 你拥有的材料
- 每个角色有一份预提取的「digest」文本：剥离了 Ren'Py 代码噪音，保留
  (a) 标签头 `===== [NNNN] LABEL =====`（NNNN = 该 label 在原始 .rpy 的源行号）；
  (b) 带说话人前缀的台词行；
  (c) 旁白行。
- 已存在的浅版 md（3–6KB 的交叉点浓缩版）。你必须在原地**覆盖重写**为深读版。

## 黄金模板（先读这两个，照其结构/深度/引用风格复刻）
- `Maya.md`（六部分结构，约 22KB —— 你的目标深度）
- `Ami.md`（约 30KB）
重点学习：如何按时间线把 label 分组、如何引用英文原文并附简短中译、如何给每条引文打源行号 `[NNNN]`、如何抽象处理成人内容。

## digest 中的说话人前缀
`N:`=旁白 · `s:`=Sensei · `m:`=Maya · `a:`=Ami · `ay:`=Ayane · `se:`=Sekai · `ni:`=Niki · `wil:`=Wilford · `mak:`=Makoto · `y:`=Yumi · `u:`=Uta · `no:`=Nodoka · `k:`=Kaori · `q:`=神秘瓜贩
其他角色通常为名字缩写（如 `rin:`/`kir:`/`har:`/`mik:`/`io:`/`sar:`/`tsu:`/`nor:`/`yas:`/`tou:`/`ot:`/`mol:`/`yuk:`/`tsb:`/`wak:`/`osa:`/`nao:`/`rik:`/`kao:`）。结合上下文推断——digest 通常保留说话人可见身份。

## 内容政策（强制）
- digest 中成人/性描写已被系统抽象为 token：`hugnant`、`[rape]`、`[teenage]`、`[high_school]`、`[[redacted]]`、`[[TEMPLATE9]]`、`[[PARANOID]]` 等。**不得展开、描述或改写性内容**。对亲密/性场景只引用其**结构性/母题性**功能，并标注源 token + 行号。重点放在人物关系、世界观/元叙事母题、剧情推进。
- 用精确中文写作。每条引文打源行号 `[NNNN]`，对齐 Maya.md 风格。

## 流程（每个角色）
1. 在角色的 digest 上 Grep `^===== \[`，取得权威 label 总表（含源行号）。
2. 分块 Read digest（limit ~600；若提示「Output too large」则缩小 limit 并用 offset 顺序接力）。**不得跳过任何 label**，覆盖全部行。
3. 每个 label 提取：发生了什么、关键台词（英文原文 + 简短中译）、人物发展、以及任何世界观/元叙事相关性（循环/重置/Sekai/USER3/ground zero/锚点如神社/宿舍时钟/屋顶）。
4. 识别与主线咬合点：提及 Maya/Ami/Sekai/USER3、重置循环、「固定锚点」地点、「ground zero」、及其他具名角色的出现。

## 输出（覆盖写原 `<角色>.md`），六部分
一、角色基本盘（身份；表面性格；隐藏/深层状态；关键变量 love/lust；人物关系）
二、love 线逐事件脉络（按时间线分组 label；逐条叙述事件 + 关键引文带 `[NNNN]`；这是主体，要详尽）
三、亲密线概貌（仅抽象：结构性/母题性；标注 token + 行号；不得展开性内容）
四、与主线咬合点（核心 meta 证据，5–10 条，带 `[NNNN]` 引用）
五、未解伏笔（开放问题 / 未解线索）
六、label 总表（全部 label 带源行号 `[NNNN]`）

## 目标厚度
对标 Maya.md（建议 ≥18KB）。详尽是这次任务的核心。

完成后汇报：写了哪些文件、每个角色多少 label、digest 有无异常。
