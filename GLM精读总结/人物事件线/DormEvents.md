# DormEvents 事件线全析（DormEvents.rpy，源 31082 行）

> 分析基准：`_tmp_match/events/_digest_Dorm.txt`（自研 digest 管线抽取，保留 label 头[带源行号]＋台词＋旁白）。
> 引文格式：`[源行XXXX]` 指向 DormEvents.rpy 原文行号。成人向内容一律抽象表述。
> 文件定位：**宿舍共享系统（Dorm Wars）** 中枢——并非单一角色路线，而是所有角色的宿舍养成/群像交汇处。主线重头戏压在文件**最尾部**五个 label（roomwithclocks → restofthenewthing → lettert → ticktock → trinity1），是全作神话体系（God / USER 系统 / 世界改写 / 元叙事）信息密度最高的一段。

---

## 一、结构总览

- **路由层**：`dorms[1]` / `firstdorm[17]` / `dormweekend[105]` / `dormmonday~friday[124/159/194/259/300]` / `doorknock[336]`——按星期与敲门选择分发到各角色宿舍。
- **角色养成链**（每个角色一套）：`*firsthall`（初次走廊相遇）→ `*hall`（日常走廊）→ `*dorm`（首次进房）→ `*dormN`（N=5/10/15… 好感阶梯）→ `*dormgen`（通用）→ 大量 `*replay` / `*anim` / `[LUST-TRIMMED]` 动画回放桩。
  涉及角色：Yumi、Maya、Miki、Futaba、Rin、Chika、Makoto、Ayane、Ami、Sana（及其 firsthall/hall 双版本）。
- **尾部元叙事簇**（主线核心，源 29117–31082）：
  - `roomwithclocks[29117]` → `restofthenewthing[30288]` → `lettert[30432]` → `ticktock[30516]` → `trinity1[30646]`。

---

## 二、主线重头戏：尾部元叙事簇（逐 label 精读）

### 1. roomwithclocks[29117] —— "有钟的房间"
- 叙述者（Sensei 第一人称）醒在"有钟的房间"，钟无指针却以不同节奏 tick；被绑在腐木椅上，白蚁啃噬手臂、自身木质化——**"感谢巨大的白色卵囊 / 感谢白蚁女王"**，并出现"termite queen 图像 + 卵"的 UI 插入。
- **"six"（女孩）** 以日文循环呼唤：`ようこそ！元気ですか？幸せですか？ムラムラしてるの？怖いの？教えて。学びたい。`（欢迎！你还好吗？幸福吗？发情了吗？害怕吗？告诉我。我想学。）源29779–29782、30207–30211。反复说 **"The whole WORLD belongs to you"**（源29815）、"Doesn't this view remind you that GOD is real?"（源29817）、"Welcome to the edge end of the world"（源29810）。
- **"te"（Teacher）角色**登场（源29935）：自述"提前打卡来给你上关于 how to do sex to girls 的课"，讽刺性提到"that fucking whore with the ponytail and the watermelon fetish"（指 Maki，西瓜癖女孩），并宣称"recreational incest dates back to the very beginning of sex itself"（源29958）。当 `[redacted]` 内容出现时"Class is cancelled"（源29969）。→ 明显的**对游戏本体与家长/平台审查的元讽刺**。
- **"sev"（Seven?）角色**登场（源29988）：请 Sensei"牺牲一两年寿命回答一个问题"；称"you've been here for [totaldays] days…managed to avoid losing yourself entirely…avoid violently raping anyone"（源30003–30005）；对"viewers/观众"说话 "He thinks it's a game"（源29999）——**把 Sensei 框定为被观看的真人秀角色**，与 Ami 线的"玩家层"完全贯通。
- **USER2 系统事件**（源30052–30077）：`USER2 WOULD LIKE TO OPEN CONVERSATION WITH YOU` → `USER2 HAS OPENED A CONVERSATION` → `USER2 IS TYPING...` → `GREETINGS` → `USER2 HAS DISCONNECTED DUE TO ISSUES WITH "NETWORK"` → `ROUTINE MAINTENANCE HAS BEGUN` → `TIME REMAINING: 2`。**与 Ami 线 `USER1 HAS SUCCESSFULLY LOGGED IN` 同构**——存在多用户（至少 USER1/USER2）管理员系统；"ROUTINE MAINTENANCE / 倒计时 2" = **重置（reset）的运维隐喻**。
- 乱码文本段（源30092–30100）："wake up in a room with clocks / I want to go home / I see myself / I don't like it / it reminds me / let me forget / make it stop"——**世界故障/角色自我认知崩解**的视觉化。
- 结尾反复 "I WANT TO PET THE CAT" / "PET THE CAT"（源30151–30206）——**白猫**首次作为执念意象出现（见 trinity1 呼应）。

### 2. restofthenewthing[30288] —— "蛋 / 圣餐"意象
- 手握"温热的蛋"，内部有东西在动；叙述者说 "Body of Christ. Amen."（源30341–30346）——**基督教圣餐（身体/血）的戏仿**；蛋的填充"restore what I lost of my teeth. I am whole once more."（源30357–30358）。
- `q` 角色出现说 "Smile! It's all there is to do here."（源30373–30391）"Congratulations! You learned! Go learn more! Become stronger! Smile always!"（源30386–30398）；结尾 `Teenagers are exhausting.`（源30402）。随后跳转到各星期推进 label（`advancetotues` 等）。

### 3. lettert[30432] —— 字母 T 与 six 再临
- Sensei 迷路，远处聚光灯照着**巨大字母 T**，叙述者称"T 是我最不喜欢的字母"。six 从字母 T 后现身（源30465 "You've been born twice and yet question the snow?"），邀 Sensei 走近"taste me"；Sensei 拒绝后"miss out on some story content…the world becomes a safer place…nudity is bad"（源30499）——**对内容分级的又一次元自嘲**。

### 4. ticktock[30516] —— 开发者女孩 "am i okay" 与 GOD 宣传
- 回到"世界上最喜欢的房间"，six 在旁。关键句（源30535、30537）：
  `Her name is 61 6d 20 69 20 6f 6b 61 79 and she refuses to have sexual intercourse with me on her best friend's bed.`
  `Her name is 61 6d 20 69 20 6f 6b 61 79 and she's really tired of having to revise so many important scenes in this stupid game to comply with community guidelines.`
  - **十六进制解码**：`61 6d 20 69 20 6f 6b 61 79` = `a m (space) i (space) o k a y` = **"am i okay"**（我是 okay 吗）。
  - 该女孩"不是像你和我这样的人"，"is an emissary of GOD God gOD goD GOd HOPE"（源30546）；"tired of revising scenes to comply with community guidelines" + "trapped down here at the bottom of everything"（源30567 "I'm sorry you're trapped down here"）——**她是被困在"一切底部的开发者/编辑化身**，负责按社区准则修订场景。Sensei 称她 `[amimaster]`（源30570）与 `[ayanemaster]`（源30603）——玩家-master 变量的混用。
- six 反问 "Doesn't confuse you at all? Seeing me as a 0 instead who I normally am?"（源30579）——暗示 six 平时"非 0"形态。
- 结尾叙述者突兀宣示（源30625–30627）：`Everything you believe in is fake! The only living real thing is Kumon-mi! All that happens here is gospel! Throw yourself into the wishing well a new, happier life! Praise be!`——**Kumon-mi 本位宣传 voice**（与 Ami 线"只有 Kumon-mi 真实"母题一致）。

### 5. trinity1[30646] —— 神话核心（[uncle]/[niece]、Ami 改写世界、Maya "God is dead"）
- **乱伦框架开场**：Sensei 想看"[niece]"在做什么 → "AMI! COME OUT OF YOUR ROOM!"；叙述者："Ami's [uncle]"、"Sensei™, your friendly neighborhood teacher and Ami's [uncle]"（源30643、30671）。Ami 换衣时"tracing her fingers along her developing chest and wondering if I am going to touch her tonight"（源30670）——此 dream-layer 中 Sensei=Ami 的叔叔。
- **Ami 的独白（源30805–30879）**——主线关键：
  - "I've done everything I can to make you recognize me, and yet you still only see me as a [niece]."（源30801）
  - "I don't care that we're related. I want to be with you forever."（源30803）
  - "Why are you so insistent on breaking me?"（源30807）
  - "I can see everything…About everyone. And honestly—It's really scary."（源30817–30820）
  - **"I'd even rewrite the world. But, sadly...that's not something I have the power to do. That's something only God can do. And since you don't believe in God, it looks like I can never get the world I truly want, doesn't it?"**（源30860–30867）——**坐实：Ami 渴望改写世界但无力，唯有 God（=Maya 造世者）能；直接印证"Maya=世界制造者 / Ami 是求助者"主线论**。
  - 她溶解为"一滩东西"（源30886），众人围观。
- **Maya 双相现身**：
  - 溶解段中 Maya 与 Ami 狂笑（`sssssss` / `kkkkkkk`，源30754–30755），Maya 对 Ami 说 "Why don't you suck his cock then, you fucking whore?"（源30768）——戏谑、操控、非人感。
  - 随后**现实层 Maya**（源30901–31077）：凌晨 3 点，雪，雪白猫，三盏聚光灯间的树，废弃**[school]**建筑。Maya 借"stations of the cross"阐释**三神/一神**隐喻（源31014–31021），并明示 "Three gods is far too many. Two gods is also too many. And so is one. I wish they'd all just go away."（源31022–31025）。
  - **Maya 结语（源31042–31045）**：`"God is dead. So we'll never have to worry about three all at once. But, if for some strange reason, one day we do—I hope that you will choose the least callous of them."`
  - **系统覆写（源31053–31065）**：`//ERROR //GOD IS NOT DEAD //GOD IS ALIVE AND WELL //HE RISES //SLEEPS AMONG US //RAPES THE ONES WE LOVE //CONSENSUALLY HUGS THE ONES WE LOVE //WE MUST WATCH AS OUR DREAMS ARE DESECRATED //PRAISE BE` → `Your affection with God has increased to [god_love]! It will change nothing!`——**"God 已死"被更高层系统否决，"GOD IS ALIVE"且以"rape / consensual hug"的并置揭示 God 的矛盾本质；god_love 是真实存在的数值变量**。文件在此以省略号收束。

---

## 三、各角色宿舍链概要（含抽样引文）

> 以下基于 label 结构＋抽样 intro；详细逐事件未全量线性精读（文件 16653 行，以养成/回放为主，主线集中于尾部）。

- **Maya 链**（mayafirsthall[353] / mayahall[412] / mayadormgen[12919] / mayadorm5–35[13373/13616/13851/14304/14504/15126/15365]）：走廊即显"Maya 没有家人在 Kumon-mi"（源2125 "Maya doesn't have any family in Kumon-mi, so she'd probably be forced to come stay with us"）；与 Ami 的 karaoke 约定（源2093、2101 "Maya just hangs out on the bench and eats the whole time"）。Maya 在宿舍线中始终是"外来者/观察者"定位，与尾部 trinity1 的造世者身份呼应。
- **Ami 链**（amifirsthall[930] / amihall[1008] / amidormgen[12888] / amidorm5–40[13083/13373?/14705/14921/15126?/15641]、amifingerreplay / amihjreplay[LUST-TRIMMED] / amimissionaryanim）：走廊 intro 中 Ami 称 Maya 同去 karaoke（源2093）；与 Sensei 的"[uncle]/[niece]"张力在 trinity1 集中爆发。Ami 在宿舍线频繁以"depressing"自嘲（源2052、2315），并多次表达对"改写世界"的无力（见 trinity1）。
- **Chika 链**（chikafirsthall[662] / chikahall[730] / chikadorm[1116] / chikadorm5–20[1176/1361/1633/2326]、chikadormgen[1144]、chikafingerreplay / chikahjreplay[LUST-TRIMMED]）：占有欲强（与 Ayane 线 Chika 提三人行呼应）；"memory will suffice"（源2770）。
- **Chinami 链**（chikadorm 区含 chinami 段）：源3650 "Chinami has had enough of this world."（源3649 "that's just how the world works, Chinami"）— 存在"受够了这个世界"的元感叹。
- **Yumi 链**（yumifirsthall[309] / yumihall[342] / yumidorm[1130] / yumidorm5–35[1842/1984/2136/2499/2655/2815/3038]）：Yumi 多次"memory sucks / 记不住"（源2229、4653、2229）；"walked all over town…legs are fuckin' dead"（源4286）——底层打工养妹设定；与 Ayane 线"Yumi 二次觉醒"形成交叉。
- **Miki 链**（mikufirsthall[428] / mikuhall[486] / mikudorm[6867] / mikudorm5–40[7117/7264/7430/8699/8925]、mikudormfingeranim / endofmikudormfreak[8888]）：典型养成。
- **Makoto 链**（makotofirsthall[747] / makotohall[813] / makotodorm[6844] / makotodorm5–25[6926/8120/8339]、makotohjreplay[LUST-TRIMMED] / makotofingerreplay / makotobjreplay / makotomissreplay）：与 Ayane 线"Makoto 加入 Rooftop Apocalypse Squad"呼应。
- **Ayane 链**（ayanefirsthall[827] / ayanehall[917] / ayanedorm[3257] / ayanedorm5–35[3631/3798/3963/5062/5446/6119]、ayanedormgen[4076]、ayanemissreplay / ayanebjreplay[LUST-TRIMMED] / ayanecowgirlrep）：源7365 "You came to see me! In my room! Alone! Without Ami or Maya or anybody! It finally happened!"——Ayane 渴望独处；源8034 "Maya comes from outside of Kumon-mi and I'm with her basically every day"——再次确认 Maya 的外来属性。
- **Sana 链**（sanafirsthall[1023] / sanahall[1098] / sanadorm[3272] / sanadorm5–50[3285/3424/3832/4649/4873/5628/5872/6401/6613]、sanadormgen[4088]）：源7872 "It's much better than this world…and that's why I spend so much time here"——Sana 指向"另一个更好的世界"（与 Ayane 线"世界共享"讨论呼应）；"edge of the world" 话题（源6986/7014/7187）。
- **Rin 链**（rinfirsthall[577] / rinhall[648] / rindorm[9123] / rindorm6to9[9470] / rindorm10–50[9779/9916/10091/10780/10949/12389/12595]、rindorm50special[12595]）：典型养成；beachfive15 清单提及"Rin and Otoha broke up"（跨 Ayane 线）。
- **Futaba 链**（futabadorm[9136] / futabafirstvisit[9159] / futabadorm6to9[9485] / futabadorm10–45[9502/9598/10365/11183/11357/11956/12174]、futabahjreplay[LUST-TRIMMED] / futababjreplay / futababoobjobreplay / futabafingerreplay）：典型养成。

---

## 四、与主线咬合点（编号清单）

1. **USER 系统确证**：`USER2` 事件（源30052–30077）与 Ami 线 `USER1` 同构，证明存在多用户/管理员层；`ROUTINE MAINTENANCE / TIME REMAINING: 2` = 重置的运维隐喻。
2. **"被困底部的开发者女孩"**：ticktock 中 hex 名 "am i okay"（源30535）的女孩，"tired of revising scenes to comply with community guidelines""trapped down here"——**元作者/编辑化身**，标识"游戏内部还有更底层的制作者"。
3. **God 神话体系**：trinity1 中 Maya "God is dead" 被系统覆写为 "GOD IS ALIVE AND WELL…RAPES THE ONES WE LOVE / CONSENSUALLY HUGS THE ONES WE LOVE"，并引入真实数值 `god_love`（源31048、31073）——God 是矛盾实体（侵犯/拥抱并置），且可被"崇拜"。
4. **Ami 改写世界愿望**：trinity1 源30860–30867——Ami 想重写世界但只有 God（Maya）能；坐实"Maya=造世者 / Ami=无力求助者"主线论。
5. **"只有 Kumon-mi 真实" 宣传 voice**：ticktock 源30625–30627 与 Ami 线母题一致——Kumon-mi 本位世界观。
6. **六/six 角色**：贯穿 roomwithclocks / lettert / ticktock，日文"教えて。学びたい"循环，称世界属于 Sensei、GOD 真实——疑似造世者（Maya/Sekai）的某一面向或信使。
7. **白猫意象**：roomwithclocks "PET THE CAT" 执念（源30151–30206）与 trinity1 雪白猫（源30996、31036）呼应——可能是 six/某角色的化身或伏笔。
8. **"sev" 真人秀框架**：把 Sensei 称为被观众观看的秀（源29999 "He thinks it's a game"）——与 Ayane 线玩家喊话（undeservedfuture7）共同构成"元叙事玩家层"。
9. **三神/一神隐喻**：trinity1 源31014–31025 Maya 借"stations of the cross"阐释——可能映射 Sensei / Maya / 某第三实体（或 USER1/USER2/USER3）的三元神结构。
10. **Sana 的"另一个更好的世界"**：源7872 与 Ayane 线"world where everyone shares"呼应——指向主世界外的维度。
11. **Maya 外来属性反复确认**：源2125（无家人在 Kumon-mi）、源8034（来自 Kumon-mi 之外、每天和 Ayane 在一起）——与"Maya 造世、非本世界原生"一致。
12. **跨线角色网**：Chika 三人行（Ayane 线）、Makoto 加入 Rooftop Apocalypse Squad（Ayane 线 beachfive15）、Rin&Otoha 分手（beachfive15）、Yumi 打工养妹（与 Ayane 线觉醒交叉）——宿舍线是群像交汇中枢。

---

## 五、未解伏笔

1. **"six" 的真实身份**：日文循环呼唤、hex 名"am i okay"的开发者女孩、trinity1 的六/six——三者是否为同一实体？six 是否即 Sekai / Maya 的某一面？
2. **God 的"三个"是谁**：Maya 说"三神太多、二神太多、一神也太多"，系统却称"GOD IS ALIVE"——三个 God 对应哪三个实体（Sensei? Maya? USER? Sekai?）？
3. **USER1 / USER2 / USER3 的关系**：USER1 在 Ami 线登录，USER2 在此断开，USER3(pareidolia) 在旁白分析文档中提及——三者层级与权限？
4. **"ROUTINE MAINTENANCE / TIME REMAINING: 2"**：倒计时 2 指什么单位？距离下一次重置还有 2 天？还是 2 次？
5. **白猫**：roomwithclocks 与 trinity1 的雪白猫是否同一角色？与"dark figure strokes her hair / purring"（源30112–30113）的暗影人物关系？
6. **"am i okay" 女孩的被困**：她为何"trapped down here at the bottom of everything"？是否即被囚的 Maya（呼应 Ayane 线 GIRL MAKER 旁白）？
7. **[uncle]/[niece] 框架**：trinity1 中 Sensei=Ami 叔叔——这是 dream-layer 设定、还是某重置轮的过去关系？与 Ami 现实线（非亲属）矛盾如何解释？
8. **"stations of the cross" 三元映射**：Maya 阐释的三神/一神，是否对应后续章节（如 SECOND beach update / Jamaica 提及，源30744）要揭开的实体？
9. **废弃 [school] 建筑**：trinity1 源31006 "abandoned[school] building" 与 Kumon-mi 学校关系？是"底层"还是"原型世界"？
10. **god_love 变量**：是否真影响后续（如某结局需要 god_love）？"It will change nothing!"（源31074）是反讽还是实情？

---

## 六、Label 总表（按组，含源行号）

**路由/星期**
| Label | 源行 |
|-------|------|
| dorms | 1 |
| firstdorm | 17 |
| dormweekend | 105 |
| dormmonday | 124 |
| dormtuesday | 159 |
| dormwednesday | 194 |
| dormthursday | 259 |
| dormfriday | 300 |
| doorknock | 336 |

**角色养成链（firsthall→hall→dorm→dormN）**
| 角色 | firsthall | hall | dorm | dorm5 | dorm10 | dorm15 | dorm20 | dorm25 | dorm30 | dorm35 | dorm40 | dorm45 | dorm50 |
|------|-----------|------|------|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Maya | 353 | 412 | 12919(gen) | 13373 | 13616 | 13851 | 14304 | 14504 | 15126 | 15365 | — | — | — |
| Ami | 930 | 1008 | 12888(gen) | 13083 | 13373? | 14121 | 14705 | 14921 | 15126? | 15641 | — | — | — |
| Chika | 662 | 730 | 1116 | 1176 | 1361 | 1633 | 2326 | — | — | — | — | — | — |
| Chinami | (chikadorm 区) | — | — | — | — | — | — | — | — | — | — | — | — |
| Yumi | 309 | 342 | 1130 | 1842 | 1984 | 2136 | 2499 | 2655 | 2815 | 3038 | — | — | — |
| Miki | 428 | 486 | 6867 | 7117 | 7264 | 7430 | — | — | 8699 | 8925 | — | — | — |
| Makoto | 747 | 813 | 6844 | 6926 | 8120 | 8339 | — | — | — | — | — | — | — |
| Ayane | 827 | 917 | 3257 | 3631 | 3798 | 3963 | 5062 | 5446 | 6119 | — | — | — | — |
| Sana | 1023 | 1098 | 3272 | 3285 | 3424 | 3832 | 4649 | 4873 | 5628 | 5872 | 6401 | 6613 | — |
| Rin | 577 | 648 | 9123 | 9470(6to9) | 9779 | 9916 | 10091 | 10780 | 10949 | 12389 | 12595 | — | — |
| Futaba | 9159(firstvisit) | — | 9136 | 9485(6to9) | 9502 | 9598 | 10365 | 11183 | 11357 | 11956 | 12174 | — | — |

（注：多数角色含 `*dormgen` / `*replay` / `[LUST-TRIMMED]` 动画回放桩，未全列。）

**尾部元叙事簇（主线核心）**
| Label | 源行 | 性质 |
|-------|------|------|
| roomwithclocks | 29117 | 元（six / te / sev / USER2 / 白蚁女王） |
| restofthenewthing | 30288 | 元（蛋/圣餐意象） |
| lettert | 30432 | 元（字母 T / six 再临） |
| ticktock | 30516 | 元（hex 名 "am i okay" / 开发者女孩 / GOD 宣传） |
| trinity1 | 30646 | **神话核心**（[uncle]/[niece] / Ami 改写世界 / Maya "God is dead" + 系统覆写 / god_love） |

---

## 小结

DormEvents 是**群像交汇中枢＋元叙事爆发点**。其 16653 行 digest 中，前 ~29000 行是各角色宿舍养成/回放（主线价值以"Maya 外来属性""Sana 另世界""Yumi 打工"等交叉点为主）；真正的主线炸药在尾部五个 label：roomwithclocks 建立"有钟房间/六/USER2 维护倒计时"框架，ticktock 揭示"被困底部的开发者女孩（hex 名 am i okay）"与 Kumon-mi 本位宣传，trinity1 则以 Ami"想改写世界但只有 God 能"与 Maya"God is dead"+ 系统覆写"GOD IS ALIVE"将**造世者神话、多用户管理员系统、玩家观看层**三者收束。这与 Ami 线（USER1 / hex 密码 / "只有 Kumon-mi 真实"）、Ayane 线（Maya 造世 / Himawari 管理员 / "Maya Makinami does not exist"）完全咬合，应据此在《人物事件线全梳理》中确立"God/Maya=造世者、USER=管理员、Kumon-mi=真实层"的三层世界观。
