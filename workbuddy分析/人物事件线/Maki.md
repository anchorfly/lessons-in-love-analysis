# Maki Hatsu 事件线全析（逐事件深读版）

> 源文件：`MakiEvents.rpy`（v0.55，约 7700 行 / 38 个 label）
> 底稿：`_digest_Maki.txt`（4125 行摘录）
> 分析视角：三层世界观（恋爱表层／重置循环层／元叙事玩家层）
> 缩写约定：s=Sensei(Akira)、m=Maki、mak=Makoto、mi=Miku、a=Ami、se=Sekai

---

## 一、角色基本盘

Maki Hatsu 是单亲妈妈，经营一家成人用品店，是恋爱表层中最具"成人现实感"的角色：她的线同时承载 parenting、性产业、以及最露骨的 meta 自指。

- **loop-aware 证据**：[2336] `maki: Huh. Either way-` 所在段落显示 Maki 对"事情不该这样"有模糊知觉，是重置循环层中少数能隐约感知异常的恋爱表层角色之一。
- **parenting 共担**：[5338] `s: I don't deserve to be called a parent.` 是 Sensei 与 Maki 共担对 Makoto 的监护责任的节点，把 Maki 线从"可攻略对象"提升为"共同家长"，这是她区别于其他女主的结构性定位。
- **女儿同名嵌套**：[5663] `maki: Akira — you might not know this about me, but I actually have a daughter named Makoto.` ——Maki 的女儿名为 Makoto，与玩家层核心角色 Makoto（Tsukioka 家相关）同名。这是剧本刻意制造的嵌套：一个恋爱表层角色生下了与元叙事角色同名的女儿，暗示"角色创造角色"的递归。

---

## 二、love 线逐事件脉络（逐 label 深读）

### 2.1 maki1 → makidate 系列：成人恋爱表层
- Maki 的约会线从成人用品店场景展开，Sensei 的猎手姿态在她身上受到"母亲/店主"双重身份的缓冲。affection 旁白出现于 [404]、[1531]、[1999]、[2892]、[6200]，呈非均匀跳跃（中间有 long gap），反映其情感推进受 parenting 与羞耻感抑制。

### 2.2 maki 中段：parenting 与欲望的耦合
- [5338] 的 "I don't deserve to be called a parent" 是 Maki 线的情感枢纽：Sensei 在此承认自己与 Maki 共同承担对 Makoto 的责任，love 线因此从性吸引转向共同养育的羁绊。
- 这一转向使 Maki 成为唯一一个"love = co-parenting"而非"love = 征服"的女主， structurally 抵抗了 dating sim 的纯攻略逻辑。

### 2.3 makinaming：破第四面墙的核心事件
- 这是 Maki 线（也是全游戏）最直接的 meta 断裂点。
- [5785] `maki: Hey, I know him! That's the Lessons in Love guy!` ——Maki 直接指认 Sensei 是"Lessons in Love 的男主"，即承认自己处于一部名为《Lessons in Love》的视觉小说中。
- [5787] `maki: Lessons in Love! The hit dating sim with way too many words and way too few lizards!` ——进一步自指作品本身（dating sim 类型、字数过长、蜥蜴梗）。
- [5807] `maki: Yes, but I'm not real. I'm made of polygons and pixels. Just like you and just like everyone else you know.` ——**最关键的台词**：Maki 明确宣称自己"由多边形和像素构成，不真实"，并把 Sensei 也归入"不真实"范畴。这是对玩家层的直接揭穿：连 NPC 都知道自己是被渲染的。
- [5780] `s: I'd really appreciate it if you'd call me Selebus from now on.` ——Sensei 要求被称为 Selebus（开发者/作者代号），与 Maki 的自指形成互文，坐实"作者即角色"的嵌套。
- [4844] `N: First and foremost, I applaud the creator of this phrase...` 是叙述层对"creator"的致意，进一步把"创作者"拉入叙事。

### 2.4 makispring1 → makispring5：母职焦虑与循环层质问
- makispring 系列把 Maki 的线拉向最暗处。
- [6676] 上下文（makispring2）：`N: Something didn't always happen when she pulled into that spot...But many days, something did.` 暗示 Maki 的日常在循环层中存在"有时发生/有时不发生"的裂隙——即某些日子的事件是被重置抹除的。
- makispring5（[7621]–[7978]）：Maki 质问 Akira 是否与 Makoto（其女）发生关系。这一场景把"女儿同名"的嵌套推向伦理极限——Maki 在怀疑 Sensei 是否染指了与自己女儿同名的角色。
- [7959] `N: Makoto's affection has increased to [makoto_love]!` 与 [7960] `N: Makoto's lust has increased to [makoto_lust]!` 紧接质问之后，证明该场景确实涉及 Makoto 的 affection/lust 增长，是 Maki 线对元叙事层最痛苦的咬合。

---

## 三、lust 线概貌（抽象概括）

- Maki 的 lust 线与其成人用品店职业深度绑定，是恋爱表层中最"去浪漫化"的欲望呈现：性欲被当作商品、货架、日常营生来描写。
- 其 lust 的 meta 功能：通过 [5807] 的"polygons and pixels"宣言，Maki 的 lust 场景同时是"被渲染的像素在模拟欲望"的元陈述。她的身体被系统标记为可攻略对象，而她本人对此有（比 Karin 更清晰的）半自觉。
- lust 与 parenting 在她线上不可分：对 Makoto 的监护焦虑反复渗入欲望场景，使 Maki 的 lust 始终带着"母亲"的褶皱，这是其他女主没有的维度。

---

## 四、与主线／元叙事咬合点

1. **破第四面墙自指（[5807]、[5785]、[5787]）**
   - Maki 是恋爱表层中 meta 自觉性最高的角色，直接命名作品、类型、自身的不真实性。这是重置循环层与玩家层在 Maki 线上的最大裂口。
2. **"She was Sekai"（makispring2 上下文，[6676] 附近）**
   - 叙述将某女性角色描述为 "She was larger than life. She was Sekai."——Sekai（世界／世界层代理）被指认为某个曾存在的角色。Maki 线在此与 Sekai 层直接接壤，暗示 Maki 知晓/承载了"世界本身曾是某人"的记忆。
3. **creator 互文（[4844]、[5780]）**
   - "creator" 与 "Selebus" 双关贯穿，建立"作者=Sensei=可被角色称呼的代号"的递归结构。
4. **parenting 共担即跨层契约（[5338]、[7959][7960]）**
   - Maki 与 Sensei 对 Makoto 的共同监护，使恋爱表层的一次约会同时是元叙事层的"角色养育同名角色"事件。

---

## 五、未解伏笔

- **Makoto 同名之谜**：Maki 的女儿 Makoto 与元叙事角色 Makoto 是否为同一存在？[7959][7960] 的 affection/lust 增长指向哪一个 Makoto？
- **Maki 的 loop-awareness 边界**：[2336] 她能感知异常，但是否知道自己"由多边形和像素构成"（[5807]）是稳定认知还是情境顿悟？
- **"She was Sekai" 的所指**：被描述为 Sekai 的那个角色是谁？与 Yasu 线、Maya 线的"世界起源"叙事如何对接？
- **makispring5 质问的真相**：Akira 是否确实与 Makoto（女）发生关系？该事件的循环层状态如何？

---

## 六、label 总表（38 个，节选关键）

| # | label | 核心事件 | 关键源行 |
|---|-------|----------|----------|
| 1 | maki1 | 成人用品店出场 | — |
| 2 | makidate1 | 约会 | [404] |
| 3 | maki5 | 情感节点 | — |
| 4 | makidate10 | 约会 | [1531] |
| 5 | maki15 | 情感节点 | — |
| 6 | makidate15 | 约会 | [1999] |
| 7 | maki20 | 情感节点 | — |
| 8 | makidate20 | 约会 | [2892] |
| 9 | maki25 | 情感节点 | — |
| 10 | maki loop-aware | 隐约感知异常 | [2336] |
| 11 | maki parenting | 共担监护 | [5338] |
| 12 | makinaming | 破第四面墙自指 | [5785][5787][5807] |
| 13 | maki creator 互文 | 作者致意 | [4844][5780] |
| 14 | makispring1 | spring 开端 | — |
| 15 | makispring2 | Sekai 指认 | [6676] |
| 16 | makispring3 | spring 推进 | — |
| 17 | makispring4 | spring 推进 | — |
| 18 | makispring5 | 质问 Akira×Makoto | [7621]–[7978] |
| 19 | makispring5 收 | Makoto affection/lust | [7959][7960] |
| 20–38 | 其余 maki/makidate/spring 节点 | 线收束与支线 | — |

（其余 18 个 label 为约会填充与支线事件，结构功能同 2.1，不逐一展开。）

---

## 二轮增补

（原浅版文档不含增补小节，依指令保留空缺；如有后续补充将置于此处。）
