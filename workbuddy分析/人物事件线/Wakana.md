# Wakana 事件线全析（逐事件深读版）

> 源文件：`WakanaEvents.rpy` ｜ digest：`_digest_Wakana.txt` ｜ 共 20 个 label
> 定位：成年角色、Osako 的"前任老师/伴侣"；全作中少数**敢当面拒绝 Sensei 且掌握其把柄话语权**的成年女性。元叙事价值在 **"Nothing is real!" 系统式宣告、"the three poems"（三首诗母题）、"I raped Molly or killed Maya"（迭代记忆）、"a million poems"、"the school year won't ever end"**——直接接入 voices/poems 核心母题与循环层。

## 一、角色基本盘
- 全名 **Wakana Watabe**（dormwarssix9 自报姓名，见增补第5条），成年角色，与 Osako 有师生+情欲过往：两人曾是恋人，紫色餐厅是二人初次约会地（`wakanadate25p3` [2222]）；Osako 线 [3006] "She was actually my teacher before Akira-sensei was"。
- 出身富裕家庭但坚持自食其力（[2280]-[2285] 不靠父母）；早产儿＋脊柱手术事故留下慢性背痛，曾练 kyudo（弓道）（背痛揭秘 [2057]-[2134]，`wakanadate25p2`）。生日 10 月 10 日（[3435]）。
- 文学素养极高：最爱诗人 Poe（[430]-[434]）、最爱的诗是 Byron "She Walks in Beauty"（[463]-[473]）；曾任教职，却感到"payoff"消失（教职意义感丧失 [393]-[397]）。
- 性格底色：长期求死倾向与自我厌弃。接电话口头禅（[226]）、挂断语 "I want to fucking die."（[71]）；"I was not designed for love"（[682]）；"I despise every fiber of every person's being"（[2017]）；有服药过量住院旧事（[2429]）。
- 关系网：Osako（前恋人/现仍纠缠）、Imani（Dare 吻戏联动 [2924]、退出"拉皮"风波 [2343]-[2374]）、Rika（nudes 自白、"Operation: Cathy Simms" 共谋 [4691]-[4873]）、Ami（诗歌与母亲话题 [4177]-[4178]）。

## 二、love 线逐事件脉络

### 前置电话/日常组

**`callwakanamorning`**［起始行 1］：jump 路由入口（按时间段分流至 morning/afternoon/night 三个版本）。早晨版为冷场电话：Sensei 打来后长时间无话（[24]-[31] 的沉默间隙），Wakana 接起即以丧气短句应对——确立"这通电话本身就是负担"的关系基调。

**`callwakanaafternoon`**［起始行 40］：下午电话，以 Wakana 的招牌挂断语收束：
> w: I want to fucking die.（[71]
不是修辞夸张，而是她日常化的告别方式；本句在 `callwakanamorning` 家族三连中被重复使用，构成角色签名。

**`callwakananight`**［起始行 80］：夜晚来电**无人接听**。三个时段电话分别给出"冷场／求死宣言／失联"三种回应，用最小成本完成角色状态速写：她随时可能滑出可联系范围。

**`wakananightgen`**［起始行 115］：咖啡店喝茶日常。Sensei 打断她的自贬："before you go wanting to fucking die"（[124]）——连关心都要借用她的求死梗。随后 Sensei 内心旁白给出对她的定评：
> N: her entire personality seems to be nothing more than a vicious cycle of varying levels of sadness（[147]
"不同程度的悲伤组成的恶性循环"——官方盖章的抑郁底色，也是后续所有事件的情感基准线。

**`wakanadive`**［起始行 171］：酒吧群像事件。潜水（dive＝下町小酒吧）场景中与众人同席，散场后与 Sensei 同乘出租车全程沉默。affection +3。沉默同行是她表达亲近的罕见方式：不需要语言维持的关系。

### date 链

**`wakanadate1`**［起始行 216］：办公室约会，Sensei 帮她判卷开场。要点：
- 接电话口头禅（[226]）——工作电话一来就切换成职业冷腔；
- 对同事/上级 Frost 的厌恶（[342]-[349]）；
- 教职"payoff"消失感（[393]-[397]）：曾经支撑她的职业意义正在蒸发；
- 文学口味自述：Poe（[430]-[434]）、Byron "She Walks in Beauty"（[463]-[473]）。
分析：date1 用"改卷+聊诗"建立智识型关系框架——两人的 intimacy 从一开始就建立在文本之上，这为 date15 的"诗歌大赛"和"三首诗"母题埋线。

**`wakanadate5`**［起始行 520］：做饭灾难约会（恰逢 Osako 结婚纪念日前后，时间点本身即是刺）。要点：
- John 让鸡念经文式闹剧（[591]-[594]）；
- 红色 Jell-O 粉事故（[852]-[861]）；
- 核心台词："I was not designed for love"（[682]）——把自己表述为出厂缺陷品；
- rope/Fortnite 舞玩笑（[896]/[898]）：在自贬里掺入网络梗，是她缓解羞耻的标准防御。
分析：本事件把"纪念日"暗线压在喜剧底下——她在替 Osako 纪念自己失去的爱情做饭，"not designed for love"因此有了具体所指。

**`wakanadate15`**［起始行 918］：**图书馆诗歌大赛评审——本线最重要的单场景之一**。
- 大赛主题定为 Kumon-mi 这座城市（[1016]）；
- 评审过程群像：Nodoka 的火龙果诗落选（[1048]-[1064]）；Fukuyama 用 love/love 押韵（[1066]-[1072]）；Nakayama 写 Hamori River（[1076]-[1094]）；
- Ami 参赛诗："Summer. Winter. Paradox..."（[1104]-[1107]）；
- **Girl Who Cannot Breathe**（[1110]-[1115]）——无法呼吸的女孩意象首次在本线登场；
- 随即触发**系统旁白爆发**：
> N: Uh-oh! It looks like you might have remembered something! ...This is all just a game! Nothing is real! Nothing is real!（[1122]-[1128]
> N: but if that's true, why is everything so much bigger than you?（[1131-1132]
- kabedon（壁咚）戏（[1139]-[1218]），Wakana 近距离毒舌："You're a lot uglier up close"（[1234]）；
- **三首诗旁白**：
> N: The rest of the day disappears once you let her go...along with the three poems and the words uttered thereafter. Waiting for the chance to suffocate you.（[1240]-[1243]
- 粗体叙述："You try to masturbate when you get into bed, but it doesn't get hard."（[1244]）
- 收束："affection does not rise. But she saw who you really are today."（[1249]-[1250]）
分析：这是全作元叙事浓度最高的场景之一。"记住东西→系统恐慌宣告→'什么都不真实'→'可为什么一切都比你庞大？'"完成了玩家层的直接入侵；而"三首诗……等待窒息你的机会"把 poems 母题从信息载体翻转为威胁实体，并与 Girl Who Cannot Breathe（无法呼吸=被剥夺声音/生命）形成意象闭环。系统判定"好感不升，但她今天看到了真正的你"——本线的亲密逻辑是**暴露而非取悦**。

**`wakanaspecial15`**［起始行 1268］：酒吧 dare 游戏局（成年组）。Rika 揭露自己 42 岁（[1392]）。Wakana 与 Osako 借 dare 进入浴室 BDSM 场景（[1410]-[1562]：Master/kitten 动态、handcuffs [1434]、vibrator [1482]）——见 lust 线概貌。归席后 Osako："Kissing... A million..."（[1600]-[1601]），Wakana 接："166,665 times better"（[1606]）——两人共享一套只有彼此懂的计数语言。Sensei 被完全无视，独自失落（[1614]-[1620]）。
分析：special15 同时展示两件事：(1) Wakana/Osako 的关系深度远超 Sensei 可插入的空间；(2) Sensei 在这条线上始终是"旁观者/闯入者"，这与 spring8 他长期缺勤后的局面互为因果。

**`wakanadate25p1`**［起始行 1640］：桌子告白独白开场（[1685]-[1690]）；转场书店第三分店（[1784]）。核心冲突：**Girl Who Cannot Breathe 调查对峙**（[1816]-[1892]）——Ami 已交了二十首诗给比赛（[1870]-[1873]），Wakana 追问 Sensei：
> w: Why did you stop writing?
> s: Nothing anymore.（[1885]→[1892]
分析：p1 把 date15 的诗歌母题推进为调查线：Girl Who Cannot Breathe 不再只是意象，而是可以被"追查"的对象；同时首次暗示 Sensei 曾经写作、然后停笔——"Nothing anymore" 是他叙事功能枯竭的第一处自供，与 spring7 "There is no more narration."（[4651]）遥相呼应。

**`wakanadate25p2`**［起始行 1911］：道歉戏开场。Wakana 的厌世总纲："I despise every fiber of every person's being"（[2017]）。随后是全线最重要的人物揭秘——**背痛往事**（[2057]-[2134]）：早产、脊柱手术事故留下终身疼痛、富裕家庭、练过 kyudo。Sensei 提及 Osako 时她只回一个字："Don't."（[2174]）。
分析：慢性疼痛是她世界观的生理基础——一个从出生起身体就"出错"的人，自然得出 "not designed for love" 的结论。p2 把毒舌还原为疼痛管理策略。

**`wakanadate25p3`**［起始行 2189］：紫色餐厅重访——她与 Osako 的初次约会地（[2222]），主动带 Sensei 来这里本身就是关系越界的宣言。闲笔：Myspace/top eight 时代的社交记忆（[2262]-[2268]）。价值观陈述：不靠父母、自食其力（[2280]-[2285]）。Imani 退出"拉皮"风波（[2343]-[2374]）；Sensei 直言：
> s: I'm just in love with her.（[2386]
Niki 3P 假想玩笑（[2406]-[2427]）；她披露服药过量住院旧事（[2429]）；收尾引用 **Ecclesiastes 3:1-8**（"凡事都有定期……"）（[2453]）。
分析：p3 完成"创伤清单"的最后一块（过量住院），又以《传道书》收束——"哭有时，笑有时"正是她对自身循环的宗教式注解。date25 三部曲整体构成一次完整的"交付"：身体（p2 疼痛）、历史（p3 过量）、价值观（自食其力）。

### spring 链（学年终章，最长支线）

**`wakanaspring1`**［起始行 2473］：海滩强掳开局（Sensei 把成年组强行拉去海滩）。粗体大写的内心嘶吼 "I'LL NEVER BE ABLE TO DRIVE ONE"（[2581]——对某物的永久性丧失感，具体所指待核）。核心戏：Wakana/Osako 因**孩子问题**争吵（[2688]-[2771]），结尾 Osako 甩出：
> os: Maybe you're the one who needs someone else?（[2771]
分析：spring1 把三角关系的裂痕摆上台面——"你才是那个需要别人的人"。这句话既是 Osako 的反击，也预言了 Sensei 的位置。

**`wakanaspring2`**［起始行 2787］：King's Game/truth or dare 局：dare Akira 吻 Imani（[2923]）；dare Osako 吻我（[2930]）。药物+酒精混服进入 high 状态（[2865]-[2868]）。Imani 的土语告白 "Medɔ wo"（[3009]）。Osako/Wakana 离场散步（[3063]-[3070]）；Sensei 独白自责：
> N: I let my friend get lost at sea（[3085]-[3086]
分析：spring2 是"失控夜"结构：游戏规则强制亲密、药物解除防御、然后有人真的走失。party 结构反复服务于"让角色说出清醒时不会说的话"。

**`wakanaspring3`**［起始行 3097］：开场寄生虫/云的哲学独白（[3101]-[3106]）。Wakana 主动召唤 Sensei 上门（[3130]）——她第一次主动求助。沙发脆弱时刻（[3205] 起）；"you feel like a brother to me"（[3242]）；随即**崩溃拥抱戏**（[3279]-[3320]）：
> w: Hold me tighter, idiot!
> s: normally when I wish for death, I do it in a less cute way（[3295]/[3298]
事后立刻切割："That never happened."（[3331]）；foursome 回忆浮现（[3354]-[3360]）。
分析：spring3 是全线的情感峰值：唯一一次真实的身体安慰，且事后被否认存在——"That never happened" 与循环层的"事件被抹除"形成同构，她的心理机制与世界的运行机制互为镜像。

**`wakanaspring4`**［起始行 3391］：餐厅重访。生日披露：Wakana 10 月 10 日（[3435]）；而 **Sensei 不记得自己的生日**（[3448]-[3449]）——主角没有出生日期，即没有起点。她发出最后通牒："return by end of school year or cyanide"（[3469]-[3477]）。随后是**循环锚点台词**：
> w: when I know the school year won't ever end（[3496]
并以请求童年故事收尾（[3525]）。
分析："cyanide"级通牒+“学年永不结束”并置在同一场景：她的求死条件与循环的时间结构正面相撞——如果学年永不结束，通牒就永远无法兑现，这正是循环层对角色悲剧的机械性囚禁。

**`wakanaspring5`**［起始行 3684］：本线最黑暗的锚点场景。叙述者以迭代幸存者口吻自陈：
> N: Like when I raped Molly or killed Maya.（[3700]
（场景其余细节待核。）分析见第四节咬合点 3。

**`wakanaspring6`**［起始行 4041］：Ami 相关的关键互证场景：
> a: I wrote a million poems for that and Noriko's was better than every single one. ...you wanted to learn more about my mom（[4177]-[4178]
（场景其余细节待核。）分析见第四节咬合点 4。

**`wakanaspring7`**［起始行 4354］：终局倒数。Wakana 宣告：
> w: I don't want children... I think this is the end, Akira. I think the dream is finally over.（[4545]-[4555]
麻木感（[4552]）；自我厌弃清单（[4559]-[4561]）。Sensei 的承诺：
> s: I promise to not stop bothering you until that happens（[4579]
Osako 冷笑话"I also want kids"（[4603]）；药物副作用被当作调情又被否认（[4620]-[4637]）。随后叙述层直接死亡：
> N: There is no more narration.（[4651]
Rika 彩信预告下场戏（[4663]）。
分析：spring7 让"叙事"本身退场——在角色宣布梦终结的同一场里，旁白宣布自己不复存在。文本层与情感层同步坍塌，是三层世界观咬合最紧的时刻之一。

**`wakanaspring8`**［起始行 4671］：办公室晨景终章。Rika nudes 自白（[4691]-[4710]）；关键状态揭示：
> w: until you have the balls to admit to the front office that he isn't ever showing up again（[4719]——Sensei 已长期缺勤
桌内手铐（[4761]-[4765]）；"There is no fixing this"（[4768]）；她的性/修复观：
> w: sex as a whole can not fix anything. It's just a bandage for a bullet hole.（[4832]
Imani 的指控成为她的执念素材（[4809]-[4816]）；Rika 发起 "Operation: Cathy Simms"（Office S8 典故）策划向 HR 举报（[4865]-[4873]），最终以 HR 投诉收场（[4909]-[4910]）。affection 增加（[4919]）。
分析：终章里教师缺席、学生接管办公室、成人组用职场剧手段（HR 投诉）处理感情废墟。"bandage for a bullet hole" 是对整部作品"用性推进剧情"机制的元评论——她看穿了这套引擎，并且拒绝再买账。

## 三、lust 线概貌
Wakana 线无独立 lust 命名 label，成人内容集中于两处：
1. **`wakanaspecial15` 浴室段**（digest [1410]-[1562]）：Wakana×Osako 的 Master/kitten 动态 BDSM 场景（道具含 handcuﬀs [1434]、vibrator [1482]）。叙事功能：具象化两人之间超越 Sensei 的历史羁绊与权力默契，并把 Sensei 降格为旁观者——该场景的"情欲"实际服务于三角结构的权力排位。
2. **foursome 回忆**（`wakanaspring3` [3354]-[3360]）：四人旧事的追述性提及，成人内容段，叙事功能为标记 Wakana/Osako/Imani/Rika 这一成年组早已边界溶解的关系史，解释 spring2/spring3 中众人互动的默认亲密度。

## 四、与主线/元叙事咬合点（三层世界观）

### A. 恋爱表层
1. 三角关系主轴：Wakana×Osako 的历史羁绊（紫色餐厅初遇地 [2222]、浴室场景 [1410]-[1562]、"166,665 times better" [1606]）持续挤压 Sensei 的位置，spring1 "Maybe you're the one who needs someone else?"（[2771]）是表层叙事的转折判词。
2. 智识型亲密：判卷（date1 [216] 起）→诗歌大赛（date15 [918]）→Girl Who Cannot Breathe 调查（date25p1 [1816]-[1892]），两人的每次靠近都以文本为媒介。

### B. 重置循环层
1. **"the school year won't ever end"**（[3496]）：角色亲口说出循环的时间结构，且与 cyanide 通牒同场——循环使一切决断无限延期。
2. **迭代记忆**："Like when I raped Molly or killed Maya."（[3700]）：叙述者记得其他迭代中发生的暴行——Molly 线 blackout 事件（inappropriatecontent）与 Maya 的"裂痕/cycle 将尽"由此获得跨线解释框架。
3. **"That never happened."**（[3331]）：拥抱戏的事后抹除与循环的记忆抹除机制同构；Sensei 不记得自己生日（[3448]-[3449]）则暗示主角本身是被反复实例化、无出生锚点的对象。
4. **Kyoko/Nodoka 母女线交叉**：Nodoka（Kyoko 之女）在诗歌大赛落选（[1048]-[1064]），Tsubasa（Tsukioka 家主母本人）背景下的成年组社交圈与本线持续交叠。

### C. 元叙事玩家层
1. **系统旁白恐慌宣告**："Uh-oh! It looks like you might have remembered something! ...This is all just a game! Nothing is real! Nothing is real!"+反问 "why is everything so much bigger than you?"（[1122]-[1128]/[1131-1132]）：全作中最直白的系统失态瞬间，与 Futaba 线 Sekai "this isn't real"、Maki 线 "made of polygons" 同构。
2. **"the three poems"作为威胁实体**："along with the three poems and the words uttered thereafter. Waiting for the chance to suffocate you."（[1240]-[1243]）：poems 母题从跨层信息载体翻转为猎食者，并与 Girl Who Cannot Breathe（[1110]-[1115]）构成"呼吸/声音被剥夺"意象闭环。
3. **"a million poems"**：Ami "I wrote a million poems for that and Noriko's was better...you wanted to learn more about my mom"（[4177]-[4178]）：将 Ami 绑定为诗歌创造载体，且点明 Ami 亡母与 Wakana 线的调查对象存在关联。
4. **叙事装置的自曝**："Why did you stop writing?"→"Nothing anymore."（[1885]/[1892]）；"There is no more narration."（[4651]）；"sex as a whole can not fix anything. It's just a bandage for a bullet hole."（[4832]）——三条台词分别在"作者""旁白""galgame 引擎"三个层面承认叙事机器的失效。
5. **affection 机制的裸露**：date15 后 "affection does not rise. But she saw who you really are today."（[1249]-[1250]）；spring8 末 affection 增加（[4919]）——好感度数值与真实亲密脱钩的时刻被旁白亲自标注。

## 五、未解伏笔（按可信度排序）
1. **"killed Maya"的迭代**（高）：Maya 在某次循环中被杀？与当前 Maya 的裂痕/cycle 将尽是否因果？（[3700]；细节场景待核）
2. **"three poems"的内容与来源**（高）：date15 中消失的三首诗是否与 Ami 母、Maya 的诗歌密码同源？"suffocate you" 是否指向 Girl Who Cannot Breathe 实体化？
3. **Wakana 与 Ami 母亲的关联**（中高）：Ami 说 "you wanted to learn more about my mom"（[4178]）——Wakana 为何会想了解 Ami 的母亲？
4. **"I'LL NEVER BE ABLE TO DRIVE ONE"**（中）：粗体大写强调的永久丧失，所指为何（驾照？某件童年信物？）（[2581]）
5. **服药过量住院的确切年代与诱因**（中）：[2429] 披露但未展开，是否与某次循环末端行为有关？
6. **Sensei 无生日**（中）：[3448]-[3449] 是设定漏洞还是"主角无本体"的证据？

## 六、label 总表（20 个）
callwakanamorning[1] · callwakanaafternoon[40] · callwakananight[80] · wakananightgen[115] · wakanadive[171] · wakanadate1[216] · wakanadate5[520] · wakanadate15[918] · wakanaspecial15[1268] · wakanadate25p1[1640] · wakanadate25p2[1911] · wakanadate25p3[2189] · wakanaspring1[2473] · wakanaspring2[2787] · wakanaspring3[3097] · wakanaspring4[3391] · wakanaspring5[3684] · wakanaspring6[4041] · wakanaspring7[4354] · wakanaspring8[4671]

## 四′、二轮增补（chap4part2 精读新证据，2026-08-22）

5. **Dorm Wars 障碍赛主持（dormwarssix9，源 3298–3367）**：Wakana 是第六届 Dorm Wars 障碍赛的司仪，开场即自嘲式求死宣言：
   > w: Hello and welcome back to whatever this is. I am here. Again. Because, for some reason, there is not {i}enough{/i} pain in my life and I must subtly seek it elsewhere.
   > w: **My name is Wakana Watabe and I want to fucking die.** And if you are watching this at home, you may take that as an invitation to come and put me out of my misery.
   主持风格全程丧气毒舌（"I am so tired of this place." [3367]），与 Molly/Yumi 的参赛闹剧形成反差；其主持身份说明她在 dormwarssix 群像中已取代部分 Imani 的司仪职能。
6. **嫉妒戏（dormwarssix9，源 3496–3537）**：Sensei 主动搭话，Wakana 全程冷脸——"Go fuck yourself, Arakawa. What do you want?"、"those are the times I hate most of all"（对"让你趴在我肩上哭"的回忆）；核心怨言："I've heard that you're practically **her lap dog** now. Which means you'd have {i}no{/i} problem dumping me if she so much as asked you to."（"her"=Niki，[3508]/[3516] "the childhood friend that you supposedly love so dearly"）；拒绝去洗手间："I've done quite a good job of minimizing my online presence and the last thing I need is **some idol painting a target on my back out of jealousy on {i}her{/i} end**."（[3516]——idol 即 Niki，[3517] 点名）；结尾威胁 "I will have to contact security and say you've been taking inappropriate pictures of the girls in the gym."（[3535]）。**Wakana 是少数敢当面全盘拒绝 Sensei 且掌握其把柄话语权的成年角色**。
7. **与 Sensei 关系的黑暗底色**（源 3525-3534）：s "Some of my worst thoughts come when I'm 'resting.' I'm just trying to distract you from yourself."→w："The thought of being alone with you when that is on your mind does little to make me feel safe."——Sensei 自认独处时会产生"最坏念头"，Wakana 直言感到不安全。
