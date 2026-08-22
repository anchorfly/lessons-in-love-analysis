# Kaori Suzume 事件线梳理（KaoriEvents.rpy，v0.55，约 6900 行 / 28 label）

> 基于 `_digest_Kaori.txt`（4134 行）精读。Kaori 线是本作 **meta 密度最高的"普通角色"路线之一**——USER2、timeloop、ghost、Sekai、voices、creator 全部在此交汇。所有结论标注源行号。

---

## 一、角色基本盘

- **身份**：同班同学，设定为"宅在家里打游戏的公主型少女"（自称 Princess Kaori），常居家中、由 Sensei 上门探访（kaoriinvite 系列）。
- **表面性格**：傲娇、以"公主"自居、沉迷电玩；与 Uta（女仆咖啡厅）有互动（kaoridate15p2 等）。
- **深层状态**：她的路线 progressively 揭示她并非普通学生——kaorispring3 直接把她与 "Ami 和 Maya 同款异色瞳的小女孩"、"被附身的幽灵"、"Sekai 的声音"挂钩，是主线 Mythos 的关键拼图。
- **关键变量**：kaori_love / kaori_lust；bonus 分支。

## 二、love 线逐事件脉络

- **kaoriinvite1–2**（[6847]/[7254]）：上门约会的收尾节点。
- **kaoridate1 → kaoridate40**（[318]–[3829]）：随 love 值递进的居家/外出约会（含 kaoridate15p2/p3 的 Uta 交叉）。
- **kaorispecial35 / kaorispecial40**（[3018]/[3434]）：特殊事件。
- **kaoricamp1–2**（[4384]/[4687]）：露营修复线。
- **halloweenkaori1–2**（[4985]/[5372]）：万圣节。
- **kaorispring1–3**（[5706]/[6104]/[6412]）：第四章弹簧事件，**spring3 是 meta 核心**（见第四节）。

## 三、lust 线概貌（抽象概括）

lust 节点主要挂在 kaoriinvite 菜单与 date 系列内。meta 含量集中在 spring3 的旁白崩坏与 connor 登场，而非露骨段本身。

## 四、与主线咬合点（本角色最核心部分）

1. **USER2 离线**（[2641]）：kaorispecial40 结尾，系统文本 `//////////////////////////USER2 HAS GONE OFFLINE`——与 Ami 线 USER1（amidate50p4 [5170] `USER1 HAS SUCCESSFULLY LOGGED IN`）、DormEvents 的 USER2 事件同构，是"玩家/观测者登出"的元叙事信号。
2. **"Ami 与 Maya 同款眼睛的小女孩"**（[3841]）：旁白 "we just randomly discovered a little girl with eyes matching Ami and Maya for no reason whatsoever"——指向一个兼具 Ami 与 Maya 特征的"复制体/孩子"，与 Ami 线 amidate50p4 的"Maya 不存在论"、Ayane 未来线的 Himawari 形成呼应。
3. **幽灵附身 + Sekai 的眼睛**（kaorispring3 [5072]起）：旁白 "it's not enough for my life to be riddled with timeloops. I have to deal with ghosts too. And you...have been possessed by the one that haunts me."（[5072]）；[5139] "Sekai's eyes...Me not hearing you for years before you showed up."
4. **voices 母题**（[5197]–[5201]）：附身 Kaori 的声线说出 "So many voices, all fighting for control over a prospect! ...she could hear all of them! She was being pulled in so many directions!"——直接回响 Ami 亡母被"voices/poems"吞噬的设定（amispring3 [10456]），并点明"神要靠信徒存在"（[5203] "In order for a god to live, that god must have people who believe in them"）。
5. **connor 开发者登场**（[5792]–[5803]）："This is Connor. He's in charge of maintaining continuity in the world"——一个 meta 开发者角色，训斥玩家 "you've decided to play the game like a fucking LOSER and avoid boning certain cartoons because their cartoon age is lower...a route the creator despises"（[5797]），并提及 **Selebus**（creator）"straight up forgets you exist sometimes"（[5800]）。这是"作者/连贯性维护者"层级的直球现身。
6. **Maya 关联**：早期 "Oh no. She's turning into Maya."（[436]）、"Maya level speed"（[1004]）；[3876] "And I'm closer to Maya than ever before." 暗示 Kaori 路线最终与 Maya 本体趋同。

## 五、未解伏笔

- USER2 是谁？与 USER1（Ami 线）、USER3/pareidolia（旁白分析文档）如何对应？
- "Ami 和 Maya 同款眼睛的小女孩"是何人？是否即某角色的童年/复制体？
- connor 所说的"creator 厌恶的路线"暗示存在"正确/错误"玩法——这与 Ami 线 amispring5 的"你没按游戏规则玩"如何互文？
- Kaori 是否被某"神"（god_love 体系）附身？其"ghost"身份未明。

## 六、label 总表（28 个）

callkaorimorning[1] · callkaoriafternoon[17] · callkaorinight[61] · kaoriinvite[97] · kaoriinvitegen[103] · kaoriinviteaff[149] · kaorinoongen2[193] · kaorimorninggen2[229] · kaorigenmorning[258] · kaorigenafternoon[288] · kaoridate1[318] · kaoridate5[647] · kaoridate10[943] · kaoridate15[1233] · kaoridate15p2[1592] · kaoridate15p3[1942] · kaoridate20[2277] · kaoridate25[2652] · kaorispecial35[3018] · kaorispecial40[3434] · kaoridate40[3829] · kaoricamp1[4384] · kaoricamp2[4687] · halloweenkaori1[4985] · halloweenkaori2[5372] · kaorispring1[5706] · kaorispring2[6104] · kaorispring3[6412] · kaoriinvite1[6847] · kaoriinvite2[7254]
