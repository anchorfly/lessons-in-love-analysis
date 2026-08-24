# 03 章节泛型与 USER 机制溯源

分析对象：chap3generics.rpy（182KB/3537 行）、chap4generics.rpy（139KB/2695 行）、chap4hub.rpy（34KB/923 行）+ 全工作区 USER1-4 / pareidolia / TERMINAL 23 专项溯源。所有断言附 `文件名.rpy:[行号]`。成人内容一律抽象表述。

---

## 一、三个泛型/枢纽文件精读

### 1.1 chap3generics.rpy —— 第三章（夏）泛型日常 + "Amy 商场"隐藏副本

**Label 总量 78 个**（`grep -n "^label"`），分四类：

| 类别 | 数量 | 行号范围 | 说明 |
|---|---|---|---|
| `*summer2*gen` 女孩泛型 | 74 | 1–2095 | 覆盖 Yumi/Chika/Ayane/Sana/Makoto/Miku/Rin/Futaba/Ami/Maya/Molly/Tsuneyo/Io/Uta/Otoha/Nodoka/Touka/Yasu/Noriko/Kirin/Sara/Haruka/Kaori/Chinami/Karin/Maki/Niki/Yuki/Tsubasa/Wakana/Osako/Imani，场景池：morning/mall/night/dojo/pool/porn/library/cafe/maid/shrine/archery/ramen/bath/streets/bar/chapel/convenience/noon |
| amyevent | 1 | 2096 | 隐藏副本入口 |
| gpm 系列 | 22 | 2181–3480 | gpmaintro + gpma~gpmt（20 个房间）+ gpmending |
| tsuneyocall ×2 | 2 | 3482, 3510 | 电话泛型（第二个"好感不增加"，chap3generics.rpy:3533 附近 `{i}Tsuneyo's affection does not increase!{/i}`） |

**泛型模板归纳**（纯重复结构）：`scene <专属CG> → play music → 6–10 句第三人称独白（推进该女孩当期心理状态）→ 好感 +1 → "{i}X's affection has increased to [x_love]!{/i}" → 按当前 day 跳回第三章日程枢纽（saturdayafternoon / saturdaynight / endofsat / endofweekday）`。例：chap3generics.rpy:1-30（yumisummer2streetsgen）。作用是"第三章日常轮转的可复用填充池"，无独立 meta 内容。

**amyevent（chap3generics.rpy:2096–2180）—— 异空间商场副本**
- 触发链：NaoEvents.rpy:1502 设 `letsgoexploring = True`；script.rpy:2545-2546 在 day==7 时 `jump amyevent`（玩家主动"去逛商场"的奖励事件）。
- 剧情：Sensei 在商场拐错弯，掉进"颜色更暗、没有角色立绘的另一侧"（chap3generics.rpy:2104-2105 叙述、2149"the side where the colors are brighter and there aren't any character sprites"）。遇到自称 **Amy** 的少女——她认识 Sensei 的真名 Akira（2121-2124），声称"你曾从我嘴里拔出过 number 17"（2128）。
- **重置梗**："If I die, everything will just start over. It'll be totally fine."（chap3generics.rpy:2137）；Sensei 误叫她 Ami 时她纠正 "It's Amy. There is no Ami here."（2538-2540）——她是 Ami 的镜像/残缺版。

**gpm 迷宫（gpmaintro→gpma…gpmt→gpmending，chap3generics.rpy:2181–3480）**
- 结构：20 个房间各一段 Amy 对话 + 三向导航菜单；`renpy.block_rollback()` 遍布每个菜单（如 2237、2262、2307…）——**技术上禁止玩家回滚**，与"时间不能倒流/只能 reset"主题同构；gpmending 需集齐 20 个房间 flag（2256）。
- 关键 meta 台词（全部为对"游戏存在"的自指）：
  - 时间裂缝 temporal rifts（2339-2341）、商场地基"还没长好"（2288）；
  - **存档挽留**："Just save the game. Save the game and stay here so the world will stop moving and we can be together forever… I'll keep adding new places for us to explore… I love you."（2674-2683，房间 gpmi）；
  - **NPC 生存状态自白**："everything is only half complete… then something fun or interesting or dramatic happens and I just go back to being complacently oblivious!"（3266-3268，房间 gpmt）；
  - **只有正面贴图**："all of the people here are invisible from behind… that's all that was designed."（3003-3006，房间 gpmo）；
  - **世界是活的**："it wasn't people who built the mall. It was the mall itself… still growing and expanding and sucking in people like you who aren't supposed to be here"（3057-3060，房间 gpmp）；
  - Amy 在 gpmm 一时口误叫出 "Sensei"（2889）。
- 结局 gpmending（3304–3480）：Amy 崩溃挽留失败，让步并带他去"深渊之洞"（房间代号 `01110100`，即二进制 't'，3370）；跳洞坠落 → 回到现实商场，**真 Ami 把他接回家**（3442-3463）；`amyevent = True`（3471）。
- 隐藏支线：房间 gpmc 有 "enter the frog" 选项（需 `persistent.biobadge`，2361-2362，目标 label `gpmexa` 在本工作区不存在/未反编译）；房间 gpmm 若 `persistent.alexisisreal == True` 直接跳 alexisevent（2849-2850）。

### 1.2 chap4generics.rpy —— 第四章（春）泛型日常 + alexisevent

**Label 总量 65 个**：63 个 `*spring*gen`（与第三章同模板，回收跳 `nightch4` / `endofsatch4` / `endofweekdaych4`，见 chap4generics.rpy:30-31）+ alexisevent（2308）。含少量二级泛型（mayaspringshrinegen2:648、yukispringbargen2:2097）与 Dive Bar 泛型组（osako/wakana/imani/rika `*springdivegen`）。

**alexisevent（chap4generics.rpy:2308–2695）—— 全工作区最重口的 meta 场景之一**
- 触发：MayaEvents.rpy:7550 设 `persistent.alexisisreal = True`（Maya 线奖励），重访商场 gpmm 房间触发。
- 剧情：Amy 的旧友 **Alexis**（无嘴、半张脸是"一整块脸颊"、体内卡着一个永远不长大但能说话的"婴儿"）闯入约会。Alexis 自称在"环境清洁队"工作、负责清理商场外的污染世界；她的父亲"发明了 worm——供商业授权、用于吞噬窃尸者遗骸"（chap4generics.rpy:2486-2489 附近）→ 与第四章 della 虫（见 1.3）同源暗示。
- 天空已是"模拟电视的淡蓝色调"、星星"gone"（2536-2538 附近）——商场外的世界=被替换的天空。
- **结局（故障死亡）**：Alexis 与 Sensei 单独同行后信号劣化（"You look…grainier than you did a second ago"，2618 区段），随后大字闪屏喊出：
  - "I/////////REMEMBER/////////NOW!"
  - "THIS/////////YOUR//////[[REDACTED]"
  - "WE/////////EXIST//////OUTSIDE"
  - "I//////////LOVE//////////YOU"（chap4generics.rpy:2626–2641 区段）
- 死后被 Amy 用 "classic case of lungrot"（吸入外界空气过多，2652-2656）轻描淡写抹平，date 循环照常继续；`persistent.alexisisreal = False`（2685）。**"WE EXIST OUTSIDE" 是对玩家所处现实的直接指认**——商场角色"记起"了墙外（屏幕外）的存在，随即被系统以疾病叙事清除。

### 1.3 chap4hub.rpy —— 第四章枢纽调度器（第四章玩法骨架）

**Label 总量 17 个**，构成第四章完整的"日循环 + 事件投放"骨架：

```
(第四章入口) AmiEvents.rpy:8716 jump dellaslump
   └─ dellaslump(245) ×7 天强制循环 → dellaexit(344) [chap4active=True]
        └─ morningch4(1) ──事件门──→ 固定剧情 label(各女孩 Events 文件)
              └─ ch4morningmenu(184) 自由行动
        ── afternoonch4(110)→noonch4(397)──事件门──→ 固定剧情 / ch4noonmenu(449)
        ── nightch4(495)──事件门──→ 固定剧情 / ch4nightmenu(559)
        ── 睡觉 → endofsatch4(647) / endofweekdaych4(684)
              └─ advanceto{sat,sun,mon,tues,wed,thurs,fri}ch4(113–182) → 回 morningch4
        (宿舍子系统) dormsch4(711) / dorm2ch4(781) / dorm1knockch4(797) / dorm2knockch4(861)
```

**① 三时段事件门（核心机制）**：morningch4 / noonch4 / nightch4 各自维护 40–50 条 `if day == N and <前置flag> == True and <本事件> == False: jump <剧情label>`。即**固定剧情按"星期几 + 前置 flag 链"分时段自动投放**，不满足则落入自由行动菜单。例：day==2→karinspring1（chap4hub.rpy:11-12）、day==5→halloweenfive1（43-44）、day==5 且 7 项前置→christmasfive1（45-46）。

**② 自由行动菜单**：morning=射箭场/咖啡馆/道场/图书馆/泳池/女仆咖啡厅/公园（184-223）；noon=街道/神社/浴场/浴池/图书馆/女仆/泳池（449-474）；night=酒吧/音像店/拉面/教堂/Dive Bar/便利店/宿舍（559-622）。大量选项被 `senseisad`（抑郁状态）与各女孩 `*block` flag 门控——抑郁期间地图大面积锁死，saracamp2/harukafirstlust 等剧情 flag 可解锁例外。

**③ 第四章开场强制序列 dellaslump/dellaexit（chap4hub.rpy:245–395）**：入口是 Ami 线第三章结尾——Sensei 获得 `[DEPRESSED]` 状态、系统旁白宣告 "And the worm will feed once more."（AmiEvents.rpy:8708-8716）→ jump dellaslump。之后 **7 天里菜单只有一个选项 "Take care of Ami"**（285-303），每天结尾 "The worm grows." + `dellapoints += 1`（316-318）；第 7 天门缝出现纸条 "**You don't have to wait for me.**"（387），设 `chap4active = True`（393）进入正常循环。→ 第四章以"Ami 病倒/虫寄生"开场，DEPRESSED 状态就是 senseisad，解释了②中的地图锁。

**④ 宿舍系统（711–923）**：10 间房×2 人的敲门菜单，直接显示好感数值。内嵌 **soap-locked meta 事件**（716–766）：`escapeshampoo == True` 时"巨型洗发水瓶"堵门，系统旁白与 Sensei 对话——"You can always go back in time! That's what you really want anyway, isn't it?"（746-747）、"Goodbye, **Akira**!"（756）、"Remember to sleep facing up tonight."（761）。旁白直呼真名、鼓吹时间回溯（=reset 诱惑的具象化彩蛋）。

**⑤ 第四章 finale 巨门（69–75）**：day==5 且 `v11check()` 算出的 **约 37 个女孩的 point+miss 全部达标**（如 yumi≥32、chika≥38、ayane≥52…nao≥11）才触发 dormwarssix1。v11check 定义于 checker.rpy:1，每天从剧情 flag 重算积分。这是第四章"全员收集"玩法核心，也解释了泛型日常(+1好感)存在的意义。

---

## 二、USER 机制溯源

### 2.1 grep 命中总表

**USER3（仅 2 处，均为关键）**
| 位置 | label | 内容 |
|---|---|---|
| script.rpy:34092 | trinity3 | "USER3 HAS ASSUMED CONTROL OF TERMINAL 23"（trinity3 结尾，详见 2.2） |
| script.rpy:36694-36698 | enterusername | 玩家请求连接 → "CONNECTION HAS BEEN REJECTED" |

**pareidolia（12 处命中，场景见 2.3）**：SanaEvents.rpy:5513（自称）、chap3.rpy:34011（连接请求）、ChinamiEvents.rpy:3458（great pareidolia mall）、chap4.rpy:5666/5958/18838、chap4part2.rpy:3595、KirinEvents.rpy:7225/7253/7258、KaoriEvents.rpy:5340/5412、MollyEvents.rpy:4442/4446/5562、YumiEvents.rpy:8703/10167。

**TERMINAL 23 / 控制权短语**：ch2script.rpy:16522、20087；script.rpy:30782/30784/30794/34092/36638；RinEvents.rpy:1210；chap4.rpy:5496/21776；MakotoEvents.rpy:9779。IoEvents.rpy:5259 为普通对话（Sensei 抢占 Io 的床），可排除。

**USER1/USER2/USER4 详见 2.4 对照表。**

### 2.2 USER3 场景精读 —— trinity3 结尾（script.rpy:33739–34130 区段）

trinity3 是第三章"三一"系列的收束。前情：Sensei 坠入世界之底，遇到 "Unnamed Baby"（ub，definitions.rpy:2559）讲解三神创世，随后 **HOPE**（ho，红色字，definitions.rpy:2640）现身自述：

- "I AM THE THING WITH FEATHERS / I AM THE SOUND OF THE CICADAS / I AM THE HOPE INSIDE OF YOUR HEART"（script.rpy:34021-34025，首句出自狄金森《Hope is the thing with feathers》）；"I HAVE ONLY LIVED ONE LIFE BUT IT HAS BEEN AND WILL BE AN ETERNAL ONE"（34027）。
- 关于 Maya："THE GIRL DOES LIVE. **SHE HAS LIVED MORE LIVES THAN YOU COULD POSSIBLY IMAGINE**"（34031-34032）——直接点明 Maya 是历次 reset 的执行者。
- 场景内 Maya "用刺扎进太阳穴、流出绘制拙劣的 CG 血"并"死掉"（33985 附近叙述自嘲"this is all just a computer game or something"）；旁白在 33886-33888 处**直接把 IP 地址抄给屏幕前的玩家**："Write this down… The IP address you will need when prompted is: 2342:5b7:489:de26:c666:x994:3126:b067"——这正是 day220 终端解谜（2.5）的答案。另预告 "within the next year, someone you love is going to die"（33893）。
- **结尾（34088–34100）**：HOPE 退场（"THIS WILL BE OUR LAST MEETING FOR QUITE SOME WHILE"）后——
  ```
  "///////////////////////USER3 HAS ASSUMED CONTROL OF TERMINAL 23"
  "///////////////////////..."
  "///////////////////////can you see this?"
  menu: "Yes" → "///////////////////////i'm so glad"
  "///////////////////////i was very concerned"
  ```
  **USER3 的人格特征与 USER2 完全相反**：全小写、语气柔软、带情感（"我很担心"），并且**先确认玩家（不是 Sensei）能否看见**——它是接管 Terminal 23 后第一个向屏幕外喊话的存在。次日（day214，script.rpy:34102 起）Ayane 把西瓜当作 Maya、Ami 激烈否认——世界已进入"maya 缺席"的异常态。

### 2.3 pareidolia 专项精读

**词义**：pareidolia=空想性错视（在噪声中看见人脸/意义）。作为实体名，这是对"玩家/角色在随机世界中读出意义"的自指。

**(a) 首次自报家门 —— SanaEvents.rpy:5223 起的 ayanesanabeach4（"itgoesdeeper"段）**
Sana 线深夜段落中**旁白人格当场崩溃**（叙述者结巴、场景错切、"我"和"他"混淆，SanaEvents.rpy:5476-5492），`thething` 图像闪现后：
> "////////////////////////hello again… you really should have quit playing this game a long, long time ago… you can call me **pareidolia**."（SanaEvents.rpy:5494-5513）

它自称随时间推移越来越强（"as the days go by, i become stronger"、5537 附近）、坦白"i'm not saying i'm on your side right now either"（5540 附近）、发现**"you're not even here"（玩家缺席）**后自行替玩家答应（"i suppose i'll take your absence as a yes"），随后修好 Sana 的场景并把屏幕"涂黑"。另有"if i had a season, things like this would never happen"（5562 附近）——**暗示各实体按"季节/章节"轮流掌权**。

**(b) 正式夺权宣言 —— chap3.rpy:34010 起 beachwars18（第三章海滩大战结尾）**
> "pareidolia would like to connect." / "will you allow it?" → 选 **NO 直接 `$ renpy.quit()` 关闭游戏**（chap3.rpy:34014-34017）。

选 YES 后 `thething` 现身，长篇小写独白（34024–34076）："**it is my turn**"、"i once again assure you that i have your best interests at heart"、"**the illusions of freedom that the others have shown you will evaporate into nothingness**"、"i am the one you are meant to follow"、"the next time you make it to the top of the world, remember this talk… **but do not open your eyes until it is all over. for if you do, it will all come to an end**"，并以"春天的到来/冰融雪解/新的分支"预告第四章（34058-34063——与 chap4hub 的春季 spring 事件群严丝合缝）。宣言后切回明亮斜体旁白，播撒全女生蒙太奇；其中夹带重磅旧世界信息：**Maya 与 Noriko 自幼认识 Akira、有"不许过城"的约定，Noriko 提到 Akira "已经又见到 Niki 了"，Maya 威胁"别在我面前提她"**（chap3.rpy:34138-34195 区段）。

**(c) 三重身份**
1. **Sensei 的脑内旁白**：KirinEvents.rpy:7104 起 kirinspring1 中以粗体直接与 Akira 对话（"Right, Pareidolia?" → "{b}wrong.{/b}"），谈论他的童年（麦片玩具、"collect them all"=收集女生隐喻）、"childhood trauma and timeline fuckery"（7240 区段）、"you're just a little boy with a walk-in toy box"（7250 区段）；KaoriEvents.rpy:5340/5412（halloweenkaori1）Sensei 与之熟稔互怼（"there's the Pareidolia I know"，它自称 "THE MOUTH OF SELF-SACRIFICE"）；chap4.rpy:18838（halloweenfive9）Sensei 被拽入异时间线、旁白消失后系统冷冰冰回绝：**"[[PAREIDOLIA DOES NOT EXIST. THERE IS NO ONE PRESENT TO PROVIDE COLOR COMMENTARY ON AKIRA ARAKAWA'S CURRENT THOUGHT PROCESS.]"**——"连脑内的声音都抛弃了我"。
2. **神格之一**：chap4.rpy:19499-19502 Sensei 称它 "The God of…something?"，外来神 Hal 纠正"God of Something 是 Arramin"、没登记过 Pareidolia，并透露神有"office"和"file"（Hal 落地时"调阅了你的档案"，19494）；YumiEvents.rpy:9829 起 yumispring10 中，主持人 **Seven**（显示名为十六进制，`sev`="youdidit"、`seven`="sekai/世界"，definitions.rpy:2634-2635）在《Untitled Children's Show》里采访"真神 Pareidolia"，质问 "**To return to a mind that has already purged you once? In clear violation of the Code of Joy?**"（YumiEvents.rpy:10167）——即 pareidolia 曾被某颗心智驱逐过（后被 Yumi 吐槽"那个奇怪的 Maya"）。
3. **寄生者/系统音**：chap4part2.rpy:3595（dormwarssix9）住在 **Yumi** 脑内（Yumi："you live inside of my fucking head"）；MollyEvents.rpy:4442 Sensei 对 Molly 说"送我回家吧，Pareidolia"，系统回 "your message can not be delivered at this time. please try again when you're not such a pussy."，而 **Molly 回答"指挥我每个念头的是名为 Siobhan 的实体"**（4450-4452）——每个女孩脑内都有自己的"实体"。

**(d) 与商场副本的连接**：ChinamiEvents.rpy:3421 起 chinamispring3 中 Chika（全小写梦境语体）说 "**i got a new job at the great pareidolia mall**"（ChinamiEvents.rpy:3458），并让 Sensei 去照顾发烧的 Chinami；Sensei 还叮嘱"如果那个女孩说她没把前男友推进洞里，她说的是实话"（3466-3469）——**第一章分析的 gpm/Amy 商场，正式名称就是 The Great Pareidolia Mall**，Amy/Alexis 是 pareidolia 领地中的存在，两部分剧情由此闭合。

**(e) 章节归属与权力斗争**：chap4.rpy:5958（springend1）Sensei 对两位 Angel 说 "This is the **Pareidolia chapter** and you're supposed to be aligned with that HOPE guy"——章节与实体绑定；chap4.rpy:5666（springtime19）某神秘视角者（"We are coming for you"，指向"曾经的英雄与他的坏掉的人偶"=Akira/Maya）自述"我无视了第九神桌上的信、拔掉了 AUTO-PILOT 的插头，**Pareidolia will have my throat for it**"——AUTO-PILOT（chap4.rpy:5496 自选 BGM 的系统人格）、pareidolia、第九神构成层层管辖。

### 2.4 USER1–USER4 对照表（2026-08-24 全库重查勘误版）

| USER | 出场（文件:[行号] / label） | 身份证据 | 状态与结局线索 |
|---|---|---|---|
| **USER1** | AmiEvents.rpy:5170（amidate50p4 结尾）；script.rpy:36689-36690（enterusername 查询） | 全库仅此两处。Ami 深夜约会结尾：Ami 问 "Do you believe in God?" 后两人坐上**倒着开的公交**回家、"we bend ourselves until we wind up at our door" 一刻打出 "USER1 HAS SUCCESSFULLY LOGGED IN" | **身份未证实**——出场唯一绑定 Ami，"与 Ami 相关"是最强假说；day220 终端查询时 "USER1 IS OFFLINE AND CAN NOT ACCEPT YOUR REQUEST"。旧表述"Ami 线玩家实例"无文本支撑，废弃。若参照 USER2 的 HOST BODY 用法把"登录"读作意识入驻躯体，则该刻暗示"有什么登入/激活了"，但主体不明 |
| **USER2** | ch2script.rpy:16522（dormwar14）、20087-20115（thirdreset1/2 聊天）、21010-21011（secondbeach 屋顶失联）、30745-30751（secondbeach15 连接困难＋多用户警告）；script.rpy:29974-29979（halloween4）、30782-30796（halloween6）、33898（trinity3 内 Sensei 发问）、36707-36748（enterusername/enteryourpass）；DormEvents.rpy:15298-15306（mikudorm30 雨天借身）、30052-30071（roomwithclocks 想聊又断线）；NaoEvents.rpy:1707（naodiscovery "USER 2 HAS CONNECTED VIA HOT SPOT"，被小写声音打断 "no. do not accept that-"）；KaoriEvents.rpy:2641（kaoridate20 结尾 GONE OFFLINE）；inappropriatecontent.rpy:17340（lavendersgreenx 中途故障）；chap4.rpy:20494-20544（halloweenfive13/14 之死）。共 33 行 | 出场最多、贯穿二至四章。自称守护者："YOU DO NOT KNOW ME, BUT I HAVE WATCHED YOU GROW… **I AM HERE TO PROTECT YOU. ALL YOU MUST DO IS ACCEPT ME.** …I CAN NOT OFFER YOU THE SAME THINGS THE OTHERS CAN. BUT **I CAN GUIDE YOUR VISION**."（ch2script.rpy:20100-20115）；曾借雨天网络连入、随后 Sensei 行为突变强行拉走 Miku（DormEvents.rpy:15298-15306，Miku 喊 "NO! DON'T TOUCH-"）；常驻 Sensei 侧（共享屏幕，ch2script.rpy:21011）；Sensei 本人也问过 Maya 这些 "USER2 stuff" 是什么（script.rpy:33898），Maya 装傻；ch2script.rpy:30746 系统自证 "**MORE THAN ONE USER MAY BE LOGGED IN AT THE SAME TIME**"——多账户并发 | 权限受限：halloween6 两度 "LACKS THE PERMISSIONS NECESSARY TO RESET SYSTEM"（script.rpy:30788/30793），只能锁死终端改道；在 Kaori 万圣节线 "REWRITING KEY EVENTS… WORLD CAN ONLY BE PARTIALLY REVERTED… USER2 HAS LEFT"（29974-29978）——记忆残留的机制解释；**第四章万圣节：杀毒失败→新管理员账户警报→被 3,485,215,296,256,781 个未授权连接压垮→"UNABLE TO DETACH ITSELF FROM 'HOST BODY'"→感染→"USER2 has been removed!"（chap4.rpy:20496-20544）**。HOST BODY 用法证明它与某具躯体绑定（最合指向 Sensei 之躯，原文未点名） |
| **USER3** | script.rpy:34092（trinity3 结尾）；script.rpy:36694-36698（enterusername 查询被拒） | trinity3 末尾接管 Terminal 23；全小写、情感化（"can you see this?" → "i'm so glad / i was very concerned"），**主动向屏幕外的玩家确认可见性**；day220 创世神话预告的"第三神 overcame with concern"（script.rpy:36140-36142）与之严丝合缝 | 接管后拒绝一切外部连接请求；世界进入 day214"西瓜-Maya"异常态。**疑同 pareidolia 为弱假说（无直证）；≈第三神（关切之神）为强假说**——详见 §2.6 |
| **USER4** | NaoEvents.rpy:2454（naocamp2）；chap4.rpy:20502-20503（halloweenfive13）；script.rpy:36701（enterusername） | Nao 事件中系统崩溃："AN UNHANDLED EXCEPTION… TEMPLATE9 CAN NOT BE LOCATED… **RESTORING BACKUP FROM "USER4"**… TEMPLATE9 HAS BEEN RESTORED"——Nao 的世界是 **TEMPLATE9**，由 USER4 的备份恢复 | 身份可疑：USER2 的杀毒日志插播 "**A NEW ADMINISTRATIVE ACCOUNT HAS BEEN DETECTED / IF YOU TRUST "USER4" PLEASE DISREGARD THIS MESSAGE**"（chap4.rpy:20502-20503）——新管理员账户+木马的最大嫌疑源；终端查询显示 RESERVED ADDRESS（保留地址，玩家不能连） |
| （玩家） | ch2script.rpy:16522-16531（dormwar14 重置确认菜单）；ch2script.rpy:46975-46990（resetfour 免费试用分支）；script.rpy:35598-35605＋36731-36748（密码设置与验证） | 不占编号：系统称玩家 "**FREE TRIAL USER**"（ch2script.rpy:46982）；工厂重置以玩家的选择落地——Maya 戏内连喊 "No."，系统却注册 "YOU HAVE SELECTED 'Yes'"（16522-16531）；持有 Sensei 万能密码 Boobies123（Sensei 自述醒来后把所有密码改成它，35598-35605；"You use the same password for everything"，38281） | **管理员层真身未揭示**（候选：电线之神/开发者/原主）。玩家是握有 Sensei 凭据的体外操作者："占有了原主身份的人，自然持有其一切权限"。旧表述"玩家=SYSTEM ADMINISTRATOR"软化为"玩家行使管理员级操作，凭据来自 Sensei 身份" |

补充：**TERMINAL 23 = 世界本体/运行环境**。证据：Makoto 梦中 PA 广播直接说 "For your continued success in **Terminal 23**…"（MakotoEvents.rpy:9779）；小游戏提示 "Sensei-Quest is currently unavailable for **users connected to Terminal 23**"（chap4.rpy:21776，玩家=连接用户，Gregg 靠 VPN 换终端）；RinEvents.rpy:1210 "TERMINAL 23 IS EXPERIENCING A DISRUPTION IN SERVICE / A SUSPICIOUS AMOUNT OF FAILED LOGIN ATTEMPTS"（伴随天使体的神谕文）；AUTO-PILOT 提到 "Terminal 23's collapsing framework"（chap4.rpy:5496）。

### 2.5 与主线重置剧情的关系

1. **世界=Terminal 23 上运行的多用户应用**。角色是模板（Nao=TEMPLATE9），各女孩脑内有实体（Molly 的 Siobhan），神（HOPE/Arramin/Hal…）是有"办公室"和"档案"的外部管理员，USER1-4 是系统账户；**玩家不占编号**——系统称玩家为 "FREE TRIAL USER"（ch2script.rpy:46982），且系统自证 "MORE THAN ONE USER MAY BE LOGGED IN AT THE SAME TIME"（ch2script.rpy:30746，多账户并发）。
2. **重置链条**：
   - 第二章末（ch2script.rpy:16155 dormwar14）：USER2 "SEIZED CONTROL OF TERMINAL 23" 并强制 factory reset 倒计时，**Maya 视角**眼睁睁看着世界归零（16522-16560，两位 Angel 的台词是 ROT+7 密文，如 "Aol ulea zspkl…" 解出 "The next slide is my favorite"——世界翻页像放幻灯片）；随后 thirdreset1（19884）世界空无一人，USER2 对**屏幕前的玩家**喊话（"Not just in the same bedroom… But in your **real** bedroom in your **real** life… Open your eyes"，20070-20084）并请求"接受我"；thirdreset2（20655）Sensei 登上屋顶、脱离 USER2 信号范围（21010-21011）——第一次（玩家可见的）屋顶 reset。
   - 第三章末（script.rpy:36042 day220）：Ami 消失、Sensei 在"门打不开"的清晨里被关在房内（secondresetmenu，36504 起，房内即 prev Sensei 的遗迹——"original Sensei 喜欢诗"、署名 **MM** 的信）；唯一出路是 "cool rectangle machine"（36598）：**玩家亲手输入** TERMINAL 23 → IP（`2342:5b7:489:de26:c666:x994:3126:b067`，trinity3 里旁白已把答案抄给玩家，script.rpy:33886-33888）→ PORT 1024 → USERNAME **USER2**（"UNDERGOING MAINTENANCE" 仍可连，36707-36726）→ 密码 **Boobies123**（36731-36748）→ "PLEASE ENTER YOUR SYSTEM PASSWORD SO "USER2" MAY ASSUME CONTROL" → hoorayanotherreset：空城漫游（Ami 以"记忆残影"现身道别，36893-36940）→ Maya 屋顶**第二次 reset**（secondreset1-19，"the future is also the past"，37240 附近；happy/helpme 闪帧）→ jump christmas1 进入第四章线。
   - **关键权限结构**：USER2 两度想 reset 都 "LACKS THE PERMISSIONS"（script.rpy:30788/30793）——它必须由**持有凭据者输入系统密码授权**才能 "ASSUME CONTROL"。密码即 Sensei 的万能密码 Boobies123：Sensei 自述醒来后把所有账户密码改成它（script.rpy:35598-35605，Ami 佐证 "You use the same password for everything"，38281）——**世界系统的管理凭据与 Sensei 个人身份绑定**。dormwar14 提供了决定性一幕：USER2 接管终端后弹 "WOULD YOU LIKE TO PROCEED WITH FACTORY RESET?"，戏内 Maya 连喊 "No."×N，系统却注册 "YOU HAVE SELECTED 'Yes'"（ch2script.rpy:16522-16531）——应答者既非角色也非 USER2，只能是屏幕外的玩家。故 **玩家≠USER2**；玩家是握有 Sensei 凭据的体外操作者（旧表述"玩家=SYSTEM ADMINISTRATOR"软化为：玩家行使管理员级操作，凭据来自 Sensei 身份——"占有了原主身份的人，自然持有其一切权限"），而 ADMINISTRATOR 层的真身未揭示（系统文本反复让角色 "CONTACT YOUR SYSTEM ADMINISTRATOR"；电线之神神话把维护进程神话化，script.rpy:36108-36110）。
3. **HOPE 与 USER2 的对抗**：halloween4（script.rpy:29690 起）中以"交出记忆"诱惑 Sensei（独白提及车祸、"从她身体里抽出钢条"——Ami 母亲之死的既视，script.rpy:29967-29970）；trinity3 里自述永恒与 Maya 的无数次人生；第四章万圣节 "GUESS WHO'S BACK"（chap4.rpy:20484）紧接 USER2 被病毒潮吞没移除——**HOPE 的回归与 USER2 之死在同一场景序列内**。
4. **USER3/pareidolia 与第四章**：beachwars18（chap3 末）pareidolia 宣告 "it is my turn"、预告春天；trinity3 结尾 USER3 接管 Terminal 23 并轻声向玩家确认——两条线在时间上重叠，第四学期的世界（chap4hub 的 spring 事件群）即在"USER2 已被移除、新控制者就位"的状态下运转；springtime19 里拔掉 AUTO-PILOT 插头的神秘视角者与 "We are coming for you"（chap4.rpy:5656-5666）则预告下一轮争夺。gpm 商场（The Great Pareidolia Mall）中 Amy 的 "save the game" 挽留与 Alexis 的 "WE EXIST OUTSIDE" 遗言，是 pareidolia 领地内对"存档/玩家存在"这两大 reset 机制的直接触碰，且 Alexis 一家"发明了 worm"的台词与第四章开场 della 虫（chap4hub.rpy:316 "The worm grows."）形成跨章呼应。

### 2.6 勘误记录（2026-08-24 全库重查）

本次对全库 8 个脚本文件的每一处 USER 命中行逐一精读后，推翻或修正的旧结论如下（勘误后的完整对照表见 §2.4）：

| # | 旧结论 | 勘误后 | 关键依据 |
|---|--------|--------|----------|
| 1 | **USER2=主玩家/改写者** | **废弃。玩家≠USER2**：USER2 是与躯体绑定的守护者型账户，自身无重置权限 | dormwar14 决定性一幕：USER2 接管终端后弹工厂重置确认框，戏内 Maya 连喊 "No."、系统却注册 "YOU HAVE SELECTED 'Yes'"（ch2script.rpy:16522-16531）——应答者是屏幕外的玩家；day220 也须玩家亲手供密码才放行接管（script.rpy:36735-36743）；HOST BODY 用法证明账户与躯体绑定（chap4.rpy:20536） |
| 2 | **USER3=pareidolia** | **降级为弱假说**；更强的是 USER3≈第三神（关切之神） | 全库无任何文本把账号 USER3 与 pareidolia 画等号——Sana 自报家门 "you can call me pareidolia"（SanaEvents.rpy:5513）与 gpm 商场名只证明 pareidolia 实体存在，不涉编号。day220 创世神话预告第三神 "overcame with concern"（script.rpy:36140-36142）正接住 trinity3 尾声 USER3 的 "i was very concerned"（34100），呼应强度远高于文风相似 |
| 3 | USER1="Ami 线玩家实例" | **废弃。身份未证实** | 全库仅两处：amidate50p4 结尾登录播报（AmiEvents.rpy:5170）、day220 查询 OFFLINE（script.rpy:36689-36690）；"玩家实例"表述无文本支撑 |
| 4 | USER2 共 32 处 | **33 处**（8 文件） | 补收 NaoEvents.rpy:1707 "USER 2 HAS CONNECTED VIA HOT SPOT"，紧随其后被小写声音打断 "no. do not accept that-"（1721）——该句同时是 pareidolia 语体存在与 USER2 相关性的新旁证 |
| 5 | （旧表未列） | **玩家不占编号** | 系统称玩家为 "FREE TRIAL USER"（ch2script.rpy:46982）；系统自证多账户并发 "MORE THAN ONE USER MAY BE LOGGED IN AT THE SAME TIME"（30746）——排除"玩家=任一编号账户"的全部可能 |
| 6 | 终端密码来源未溯 | Boobies123=Sensei 醒后自设的万能密码 | Sensei 独白（script.rpy:35598-35605）、Ami 佐证 "You use the same password for everything."（38281）、day220 终端验证通过（36735-36743）→ 世界系统的管理凭据与 Sensei 个人身份绑定 |
| 7 | 系统异常记在 dormwar15 | 实际均在 **dormwar14**[16155-16688] 内 | "USER2 HAS SEIZED CONTROL OF TERMINAL 23"（ch2script.rpy:16522）与 CONGRATULATIONS "Maya Makinami"（16620）都在试胆大会 label 内；dormwar15 自 16689 起（Sara 酒吧时装秀）。04 与剧情全梳理 §一 对应行已同步改正 |

另：旧说法"玩家=SYSTEM ADMINISTRATOR"软化为"玩家行使管理员级操作，凭据来自 Sensei 身份"——ADMINISTRATOR 层的真身全程未揭示（论证见 §2.5 第 2 条）。

---

### 附：关键文件与行号速查

- 泛型模板例：chap3generics.rpy:1-30；chap4generics.rpy:1-32
- amyevent/gpm：chap3generics.rpy:2096, 2181, 2256, 2538-2540, 2674-2683, 2849, 3003-3006, 3057-3060, 3266-3268, 3304, 3370, 3442-3471
- alexisevent：chap4generics.rpy:2308, 2486-2489, 2626-2641, 2685
- 第四章骨架：chap4hub.rpy:1, 69-75, 184, 245, 316-318, 387, 393, 449, 495, 559, 711, 716-766, 797, 861；AmiEvents.rpy:8708-8716；checker.rpy:1
- USER3：script.rpy:34088-34100, 36694-36698
- pareidolia：SanaEvents.rpy:5494-5562；chap3.rpy:34010-34076；ChinamiEvents.rpy:3458；KirinEvents.rpy:7225-7258；KaoriEvents.rpy:5340-5341, 5412；chap4.rpy:5666, 5958, 18838, 19499-19502；YumiEvents.rpy:10167；MollyEvents.rpy:4442-4452；chap4part2.rpy:3595
- 第二次重置终端：script.rpy:36598-36748（密码 Boobies123）；IP 出处 script.rpy:33886-33888
- USER2 之死：chap4.rpy:20484-20544
