# Chika 事件线精读摘要（ChikaEvents.rpy，v0.55，约 11360 行 / 50 个 label）

> 注：任务书标注 49 个 label，实测 `^label` 共 **50** 个，见文末总表。

## 一、角色基本盘

- **姓名**：Chika Chosokabe（長宗我部千花），金发 gyaru，主角 Sensei 的学生兼恋人。
- **家庭**：母亲已故（由她独自抚养妹妹 **Chinami**，第三人称自称"Chinami"），父亲早年抛弃家庭；后与 **Yumi** 合租公寓，Yumi 搬走后 Rin 常来。Chinami 称 Sensei 为"Papa"。
- **性格弧线**：忠诚专一的痴情 gyaru → 得知 Sensei 多线恋爱后精神崩坏（"Rabies"→"cannibalism"隐喻），逐渐 yandere 化，同时被迫重构自己的爱情观并发展对 Rin 的感情。
- **数值体系**：`chika_love` / `chika_lust` 双轨；关键节点有巨额跳变（spring4 结尾 `chika_love += 1000`，christmalloween2 结尾 `+= 100`），配合 `chikadorm45`、`chikaspring1~8`、`chikachristmalloween1~2` 等完成旗标。
- **职业**：maid cafe 员工（与 Uta 同店），工资用于养 Chinami 与付房租（月村庄"Tsukioka"名下、女性专用公寓，管理者 Touka）。

## 二、Love 线逐事件脉络

### 路由层
- `mall` (L1)：总入口 hub，按 `chika_love >= 5/10/15/20/40/45` 与章节旗标分发至 `firsttimemall`/`mall2to4`/`mall5/10/15/20/40/45` 等；`chikamaid`(L25)/`chikainvite`(L34) 为邀请类入口，`chikablock` 时拒绝。
- `callchikamorning`(L136)/`callchikaafternoon`(L207)/`callchikanight`(L256)：电话联系 hub；`chikanightgen2`(L217) 夜间日常。

### 早期约会（love 5→20）
- `firsttimemall` (L324)：首次商场约会，确立关系基础。
- `mall5` (L562)、`mall10` (L808)、`mall15` (L1240)、`mall20` (L1600)：商场系列升级，穿插 Chinami 扮狗（"Woof!"）撞见 Ami/Maya 的喜剧桥段（`whyissheadog14` 等 scene，约 L1500–1550）。
- `chikainvite1` (L1921)、`chikainvite2` (L2303)：邀请上门事件；`chikainviteaff`(L2471)、`chikainvitelicking`、`chikainvitehandjob`(L2492) 为分支亲密事件（归入 lust 轨）。

### 温泉初夜（love 25 段）
- `day272` (L2513)：日期事件铺垫。
- `chikaonsen1` (L2612) → `onsenbegin` (L2687) → `chikaonsen2` (L3124) → `chikaonsen3` (L3596) → `chikaonsen4` (L3657)：love 线温泉初夜。关键台词：
  - `"Nuh-uh-uh. Not yet, [chikamaster]."` / 「还不行哦，[chikamaster]。」
  - `"I just need a few minutes to mentally prepare myself."` / 「我只需要几分钟做一下心理准备。」
  - Chika 以"第一次"郑重交付，情感浓度极高，是关系正式化的锚点。

### 关系深化与同居提议（love 40→45）
- `chikaspecial40` (L4339)、`mall40` (L4695) + `mall40p2` (L4920)：love 40 特别事件与商场后续。
- `chikalunch` 系列（约 L4500–4540，位于 mall40 段内）：Chika 提出毕业后与 Chinami 同住——`"Do you think there's any chance that maybe Chinami and I could move in with you?"`（「你觉得有没有可能……我和 Chinami 搬来和你一起住？」），牵出 Yumi 去向悬念。
- `chikadate45` (L5345) + `restofchinamibr` (L5433)：love 45 约会。
- `mall45` (L6151)、`chikaspecial45` (L6566)：love 45 特别事件。
- `chikadorm45` (L6939)：公寓事件，愤怒性爱收束；旁白伏笔——
  - `"But soon, it will end with another beside us."` / 「但很快，它将以另一个在我们身旁的人告终。」
  - `"What worm-covered secrets will we pull from out the earth?"` / 「我们会从土里挖出怎样爬满蠕虫的秘密？」
  - 结尾 `$ chikadorm45 = True`，love/lust 各 +1。

### Spring 系列（第四章日常，崩坏与重构）
- `chikaspring1` (L7542)：Chika 怒斥 Ami——`"You creepy, clingy, incestuous bitch!"`（「你这个令人毛骨悚然、死缠烂打的乱伦贱人！」），Yumi 劝阻。
- `chikaspring2` (L7944)、`chikaspring3` (L8358)：Yumi 矛盾激化段（Chika 迁怒 Yumi，"想杀她"级别的争吵）。
- `chikaspring4` (L8701)：Sensei 向 Chika 摊牌自己多线恋爱。Chika 强行"消化"：`"There is no longer a need to worry about Chika Chosokabe! All is good here in the life I've always wanted."`（「再也不用担心长宗我部千花了！我一直想要的人生里一切都好。」）——明显的自我欺骗；Sensei 暗示她像得了狂犬病（`"You know rabies is pretty much 100%% fatal..."`），系统提示 `Chika has contracted [RABIES]! Her sanity has decreased by 10!`，`chika_love += 1000`。独白：`"I just have a 'different idea of what love is.'"`（「我只是对爱有'不一样的理解'。」）
- `chikaspring5` (L9161)：与 Rin 共浴。Rin 质疑 Chika 与她发生关系是否只为报复/拉拢——`"But are you 'smarter' because you want to be? Or because you have to be?"`（「你的'变聪明'是因为你想，还是因为你不得不？」）；Chika 承认早就知道 Sensei 出轨而 Rin 隐瞒，宣称 `"I won't lose Sensei... I'm winning. He loves me most of all."`（「我不会失去 Sensei……我在赢。他最爱的是我。」）并暴露自己长期对 Rin 有意：`"Do you really think I have been flirting and trying to dress you up in cute outfits for so long just because we're really good friends?"`。结尾 Chinami 乱入喜剧缓冲；提及 Futaba 父母失联伏笔。
- `chikaspring6` (L9487)：maid cafe 探班。Chika 对客人展现 yandere 服务风格（`"Never fucking joke with me like that again. Got it? Good. Die, you fucking pigs."`）；随后与 Sensei 深谈，核心台词：
  - `"Hurting with you beats hurting alone."` / 「和你一起痛，好过独自痛。」
  - `"I have given you everything. Not just my body and my heart, but my family."` / 「我给了你一切——不只是身体和心，还有我的家人。」
  - `"I need you... to need me."` / 「我需要你……需要我。」
  - `"Leave the changing to me, Sensei... I'm young. I still can."` / 「改变的事交给我吧，Sensei……我还年轻，我还做得到。」
  - 结尾假设性问题："如果五年、十年后才遇到我，你会要我的电话号码吗？"
- `chikaspring7` (L9930)：**超现实梦境段**。回家发现 Chinami 机械式复读欢迎语，神秘角色 "six"（`The one who really needs to wake up is you!`）出现，十六进制密文，"hypercube" 超立方体序列——Chika 被吸入立方体，进入 "Spacy's Summer Blast Savings event"（集体纵欲的商场幻境），被无面怪物 "q" 与幻境 Chinami 围攻，最终自我说服 `"This is Heaven."`。醒来后独白：`"Everyone is right. I am going insane."`、`"Why would God... give me a gift?"`。本段是全文件最重的 meta/恐怖演出，与主线"红商场"意象直接咬合。
- `chikaspring8` (L10315)：Chika 电话召唤 Sensei "have all of the sex"；Chinami 与 Touka 被支开；maid 制服性爱场景，Sensei 以 `"I love you"` 打断她的自动导航式发狂；分支：若 `tsukasaspring5` 条件满足则 jump 至 Tsukasa 线，否则标记 `tsukasaspring5miss` 等一串 miss 旗标（本事件挤占其他角色事件的时间成本）。

### Christmalloween（圣诞万圣节派对，收束段）
- `chikachristmalloween1` (L10690)：Chika 穿 Jirai Kei 盛装赴会，把 Rin 引开欲"再尝一口"（`"Rabies had turned to cannibalism."`），却撞见 Yumi。向 Yumi 坦白对 Rin 的感情：`"I may have cheated on him. With a girl. Who I am now pretty sure I have a major crush on."`。Yumi 顺口说出 **母亲患癌**——`"The only thing really worth writin' home about is my mom getting cancer anyway."`。Chika 意识到自己自我沉溺到没问过 Yumi 的近况，崩溃独白：`"What's happened to me?... Is this really who I am now?..."`，在厕所自残式痛哭。
- `chikachristmalloween2` (L11013)：**对 Rin 正式告白**。核心台词：
  - `"You are way more than just a friend to me! ... I think I'm in love with you and if I didn't admit that tonight, I'd probably just die."` / 「你对我来说远不止朋友！……我想我爱上你了，今晚不说出来我大概会死。」
  - 但随即宣布 `"I don't think we should hang out anymore."`（「我觉得我们不该再往来了。」）——以自我牺牲保护 Chinami、病中的 Yumi 妈妈和摇摇欲坠的师生关系：`"Sometimes, you need to sacrifice something you love if it means protecting everything else."`
  - Rin 挽留：`"Smother me. Smother me if that will keep you from leaving. I love you, Chika."`；Chika 仍离开：`"But on the bright side... I'll still see you in school!"`。`chika_love += 100`，jump 至 `nodokachristmalloween1`。

## 三、Lust 线概貌（抽象表述）

- lust 轨事件以直白性爱场景为主，常带旁观者视角：如 `poorgirldoggystyle` 系列（约 L6000–6060）以女教师 tb 偷窥+内心挣扎独白（`"I mustn't. Chika is like a daughter to me."`）呈现。
- `chikalust15`(L4214)/`chikalust25`(L5649) 及对应 skip label（L4171/L5602）为 lust 门槛节点；`chikainvite` 分支（licking/handjob/missionary L4318）为早期 lust 内容。
- 后期 lust 与 love 轨高度纠缠：spring8 的 maid 性爱同时是情感急救（Sensei 用告白打断她的失控），结尾按旗标分流并产生跨角色 miss 连锁。
- lust 轨的功能性：为 love 轨的崩坏提供"身体先行、心理滞后"的注脚——Chika 用性确认占有权，旁观角色（tb、Uta、客人）的反应则外化她已偏离常态。

## 四、与主线咬合点

1. **多线恋爱核心矛盾**：Sensei 的 forced polyamory 是 Chika 崩坏的直接原因；spring4 摊牌与 spring6 谈判是全游戏"诚实vs幻想"主题在 Chika 线的落点。
2. **红商场/Spacy's 意象**：spring7 的 hypercube 梦境与"Summer Blast Savings event"直接复用主线的 Great [REDACTED] Mall 世界观，暗示 Chika 的疯狂与 mall 的超自然存在同源。
3. **角色网络**：Yumi（前室友、母亲患癌）、Rin（告白对象、同时追求 Sensei）、Ami（被骂"incestuous"）、Uta（maid cafe 同事，"almost kissed Ami"梗）、Touka（公寓房东阶层）、Futaba（父母失联）、Sana（被提及点破 Chika 疯狂）、Tsukasa（spring8 分支 jump）。
4. **时间调度**：事件结尾统一 `jump endofsatch4` / `endofweekdaych4`，spring8 的 miss 旗标链（tsukasa/chinami/tsubasa）体现第四章"一天只能选一个女孩"的排他设计。
5. **maid cafe**：Chika 的职场与 Uta/Osako 线共享场景，`chikathemaid` 段（spring6）展示其 yandere 服务风格已成都市传说级存在。

## 五、未解伏笔

1. **"another beside us"**（chikadorm45 结尾）：暗示未来将有第三人加入（结合 spring7 的 Chinami 恐怖化描写与 `chinamicthree` 三人行旗标，指向不明）。
2. **"worm of Giles Corey"**（spring7 旁白）与 hypercube 密文：Chika 的"礼物/疯狂"来源未解释，`"Why would God... give me a gift?"` 直接抛出。
3. **Yumi 母亲的癌症**（christmalloween1）：刚揭晓，后续走向未定；Yumi 与 Noriko 的接近亦未收束。
4. **Futaba 父母失联**（spring5 提及，christmalloween2 中"回来但被项目封锁通信"的解释存疑）。
5. **Chika 对 Rin 的告白悬置**：告白+绝交的双重操作后两人关系如何发展（`"I hope that you're exactly the same."`）留待后续版本。
6. **"五年十年后要电话号码"** 的假设性对话：Chika 对"非师生关系下的可能性"的执念，疑似长期伏笔。
7. **Tsukioka 家的房租为何便宜**（spring5：`"it's gotta be the fucking bubble wrap"`）：公寓背景未解。
8. **Uta "almost kissed Ami"**：一句被掐断的八卦，未展开。

## 六、Label 总表（50 个）

| # | Label | 行号 | 类别 | 简述 |
|---|-------|------|------|------|
| 1 | mall | 1 | 路由 | love 值分发总入口 |
| 2 | chikamaid | 25 | 路由 | maid cafe 邀请入口 |
| 3 | chikainvite | 34 | 路由 | 上门邀请入口（含 chikablock） |
| 4 | mallgen2 | 49 | 日常 | 商场通用日常 |
| 5 | chikainvitegen | 78 | 日常 | 邀请通用日常 |
| 6 | callchikamorning | 136 | 路由 | 早晨电话 |
| 7 | callchikaafternoon | 207 | 路由 | 午后电话 |
| 8 | chikanightgen2 | 217 | 日常 | 夜间通用 |
| 9 | callchikanight | 256 | 路由 | 夜间电话 |
| 10 | firsttimemall | 324 | love | 首次商场约会 |
| 11 | mall2to4 | 536 | love | 商场 love 2–4 |
| 12 | mall5 | 562 | love | 商场 love 5 |
| 13 | mall10 | 808 | love | 商场 love 10（含 Chinami 扮狗喜剧） |
| 14 | mall15 | 1240 | love | 商场 love 15 |
| 15 | mall20 | 1600 | love | 商场 love 20 |
| 16 | chikainvite1 | 1921 | love | 邀请事件 1 |
| 17 | chikainvite2 | 2303 | love | 邀请事件 2 |
| 18 | chikainviteaff | 2426 | 分支 | 邀请·好感分支 |
| 19 | chikainvitelicking | 2471 | lust | 邀请·舔舐分支 |
| 20 | chikainvitehandjob | 2492 | lust | 邀请·手交分支 |
| 21 | day272 | 2513 | love | 第 272 日事件（温泉前置） |
| 22 | chikaonsen1 | 2612 | love | 温泉 1 |
| 23 | onsenbegin | 2687 | love | 温泉初夜本体 |
| 24 | chikaonsen2 | 3124 | love | 温泉 2 |
| 25 | chikaonsen3 | 3596 | love | 温泉 3 |
| 26 | chikaonsen4 | 3657 | love | 温泉 4 |
| 27 | chikalust15skip | 4171 | lust | lust 15 跳过版 |
| 28 | chikalust15 | 4214 | lust | lust 15 事件 |
| 29 | chikainvitemissionary | 4318 | lust | 邀请·传教士分支 |
| 30 | chikaspecial40 | 4339 | love | love 40 特别事件（含 chikalunch 同居提议） |
| 31 | mall40 | 4695 | love | 商场 love 40 |
| 32 | mall40p2 | 4920 | love | 商场 love 40 后篇 |
| 33 | chikadate45 | 5345 | love | love 45 约会 |
| 34 | restofchinamibr | 5433 | love | Chinami 相关后续 |
| 35 | chikalust25skip | 5602 | lust | lust 25 跳过版 |
| 36 | chikalust25 | 5649 | lust | lust 25 事件（含 poorgirldoggystyle 段） |
| 37 | mall45 | 6151 | love | 商场 love 45 |
| 38 | chikaspecial45 | 6566 | love | love 45 特别事件 |
| 39 | chikadorm45 | 6939 | love | 公寓事件（伏笔"another beside us"） |
| 40 | chikaspring1 | 7542 | spring | 怒斥 Ami |
| 41 | chikaspring2 | 7944 | spring | 与 Yumi 矛盾（上） |
| 42 | chikaspring3 | 8358 | spring | 与 Yumi 矛盾（下） |
| 43 | chikaspring4 | 8701 | spring | 摊牌·[RABIES]（love+1000） |
| 44 | chikaspring5 | 9161 | spring | 与 Rin 共浴对峙 |
| 45 | chikaspring6 | 9487 | spring | maid cafe 探班·谈判 |
| 46 | chikaspring7 | 9930 | spring | hypercube 梦境·Spacy's 幻境 |
| 47 | chikaspring8 | 10315 | spring | maid 制服性爱（跨线分支） |
| 48 | chikachristmalloween1 | 10690 | 节日 | 派对·与 Yumi 谈心·母癌揭晓 |
| 49 | chikachristmalloween2 | 11013 | 节日 | 对 Rin 告白+绝交（love+100） |
| 50 | （jump 出口） | 11361 | — | `jump nodokachristmalloween1`（文件止） |

> 注：`chikalunch`/`poorgirldoggystyle`/`firstonsen` 等为事件段内的 scene/子段落名，非独立 label；`chikathemaid*`、`chikamaidsex*`、`chikaconfesses*` 等为 scene 名序列。
