# Karin Kizuna 事件线梳理（KarinEvents.rpy，v0.55，约 5800 行 / 26 label）

> 基于 `_digest_Karin.txt`（3169 行）精读。Karin 线的 meta 价值集中在 **第四章 spring4/spring5**：Maya 作为"游戏主角"的元形象直接在 Karin 面前显像，并伴随 [[PARANOID]] 状态效果。所有结论标注源行号。

---

## 一、角色基本盘

- **身份**：空手道社成员（与 Kirin 同社），运动型少女，主要场景是足球场/道场（soccerfieldkarin / karinsoccer 系列）。
- **表面性格**：自信、好胜、对 Sensei 直球；与 Kirin 有"互相较劲又互相照顾"的关系（karinspring 系列常同框）。
- **深层状态**：她的路线在第四章被一股"脑中 new voices"（[4573]）侵入，并目击 Maya 以"游戏主角"姿态显像——暗示 Karin 的视角被主线 Mythos 接管。
- **关键变量**：karin_love / karin_lust；bonus 分支。

## 二、love 线逐事件脉络

- **karindate1 → karindate30**（[249]–[3316]）：随 love 值递进的约会（含 karinsoccer15 [1720] / karinsoccer20 [2117] 的社团交叉）。
- **karinspring1–7**（[3735]–[5660]）：第四章弹簧事件，**spring4/spring5 是 meta 重头戏**（见第四节）。
- 早期 routing：soccerfieldkarin[92]、karinsoccergen[164] 等。

## 三、lust 线概貌（抽象概括）

lust 节点挂在 date 系列与 invite 菜单内。meta 含量集中在 spring4 的"Maya 显像 + 状态效果"，而非露骨段本身。

## 四、与主线咬合点

1. **Maya 作为"游戏主角"显像**（karinspring4 [4174]–[4179]）：Karin 线中，Maya 以三种元形象直接对 Sensei 说话——
   - "Hi, I'm Maya — the main heroine of Lessons in Love. I do the time thing."（[4174]）
   - "Hi, I'm Maya — the main heroine of Lessons in Love. You killed me. You killed me, Akira. Millions of years of memories, stripped away by a one night stand. Way to go. What a way to end things."（[4179]）
   - "Hi, I'm Maya — the main heroine. I like watermelons."（[4192]）
   这是 Maya 的"meta 自述"第一次在**非 Maya 自身路线**里出现，且直指"时间操控者"与"被 Akira 毁灭"的神话核心。
2. **[[PARANOID]] 状态效果**（[4379]）：事件结尾系统文本 "Akira has gained the status effect [[PARANOID]!"——与 Ami 线 amispring1 的 [[DEPRESSED]]、[[BEDRIDDEN]] 同属"系统状态效果"体系，证明主线事件会向 Sensei 写入心理状态。
3. **脑中 new voices**（[4573]）：旁白 "I'm not sure such a thing would stop me. But...I still have no clue what the new voices in my head even want"——承接 Ami 亡母的 "voices" 母题，暗示 Karin 也被某种更高存在"接入"。
4. **Ami 的 meta 宣言**（[5969]）：ami 在 karinspring7 附近说 "There's not really anything I wouldn't do to make sure my story goes on at this point."——Ami 以"确保自己的故事继续"为动机，点明角色对自身叙事的执念。
5. **Maya 行走异常**（[2671]）：ka "Maya hasn't been walking the same ever since."——Karin 注意到 Maya 的异常，侧面印证 Maya 的"被囚/非人"状态。

## 五、未解伏笔

- Maya 在 Karin 线显像时说的"你杀了我，Akira"指什么事件？是否与"被囚的 Maya"设定相关？
- "new voices" 与 Ami 亡母的 voices、Karin 自身路线有何承接关系？
- [[PARANOID]] 状态是否影响后续章节？

## 六、label 总表（26 个）

callkarinmorning[1] · karinpool[16] · callkarinafternoon[20] · callkarinnight[51] · soccerfieldkarin[92] · karinsoccergen2[102] · karinnoongen2[133] · karinsoccergen[164] · karingenafternoon[192] · karingennight[222] · karindate1[249] · karindate5[585] · karindate10[954] · karindate15[1364] · karinsoccer15[1720] · karinsoccer20[2117] · karindate20[2537] · karindate25[2920] · karindate30[3316] · karinspring1[3735] · karinspring2[3989] · karinspring3[4399] · karinspring4[4718] · karinspring5[5012] · karinspring6[5296] · karinspring7[5660]
