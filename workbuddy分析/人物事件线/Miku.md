# Miku 事件线全析

> 源文件：MikuEvents.rpy ｜ 含大量剧情 label（以下按事件脉络择要分析）
> 定位：足球部出身的前运动少女，丸山家幸存者。表层是精力过剩、口无遮拦、性知识贫乏却觉醒极快的开心果，内层是目睹父母被枪杀的 PTSD 患者——拔发、怕巨响、解离，靠 Io 的来路不明药片维持运转。她是全书少数**玩过《Lessons in Love》本体游戏**的角色，元叙事咬合最深的角色之一。
> 阅读提示：本文件为纯中文分析，事件标题即源 label 名（如 `mikupool`、`mikuinvite1`），按 label 名回溯源文与行号见 `索引/Miku索引.md`；成人内容仅做叙事功能概括；mi=Miku、s=Sensei、mak=Makoto、maki=Maki、a=Ami、i=Io、f=Futaba、ka=Karin、N=旁白。

## 一、角色基本盘

- **身份**：Kumon-mi 高中生，足球部成员直至社团解散；与 Makoto 同宿舍、互为室友兼好友（源文 MikuEvents 直述 "Best friends, actually! Roommates too."）。两人各自与 Sensei 发展出情感线，Makoto 在 dorm45 段主动表示更接受 Sensei 追求 Miku——这是理解本线「三人透明共同体」的前提，但"共享恋人同盟"并非源文明示的契约关系。
- **家庭创伤（本线核心解明）**：幼年家中遭两名窃贼入室抢劫，双亲被枪杀，她当时躲在床下、全程听见枪响，事后爬出才发现父母双双身亡。这是她怕巨响、拔发癖（trichotillomania）与解离倾向的唯一根源。
- **病理与药物**：长期服用 Io 私下提供的来路不明药物（"Dr. Io" 是她的戏称）；泳池药物过量事件后经 Makoto 介入转向正规治疗。
- **表面性格**：自称 "Champion of Justice and Soccer"；对 Sensei 的感情定位长期锁死在 friends-with-benefits，直到终章才主动请求升级。性觉醒写得像副作用：先有欲望的生理证据，再补感情的认知。
- **元层级位置**：在 Maki 店里被要求试玩本作游戏前半小时以熟悉商品——角色玩自己的游戏，这一设定使她成为三层世界观（恋爱表层／重置循环层／玩家层）的活体接口。
- **关键变量**：miku_love / miku_lust 在系统中多次直接显示，密度居全书前列。

## 二、love 线逐事件脉络

### 入口桩

**mikupool**泳池入口、**soccerfield**足球场初遇，两枚场景桩确立她的运动少女形象。**callmikumorning**／**callmikuafternoon**／**callmikunight**三段电话桩按好感分流，维持「随时可约」的初始框架。

### 邀请分支

**mikuinvite**／**mikuinvitegen**／**mikuinviteaff**邀请上门三变体，是 invite1/invite2 的前身结构。

### 足球部系列

**mikusoccergen2** → **firsttimesoccer** → **soccer2to4** 完成入部仪式：Sensei 被拖进球队当 "Coach"，该称呼日后进入 lust 线的命名树。随后是标准好感爬塔：**soccer5**、**soccer10**、**soccer15**、**soccer20**、**soccer25**、**soccer30**。soccer25 内嵌一段标志性喜剧：储物间清洁戏中 Miku 骑上 Sensei 肩膀够球，*"Is this what it feels like bein' a tall person?"*，Futaba 的身材玩笑穿插其间——肢体喜剧之下是她对身高差＝权力差的天然敏感。**soccer35** 社团线收官，此后足球部解散，养成主场让位给宿舍。**mikuwinterbeach1** 冬季沙滩特别事件插在 soccer30 与 soccer35 之间。

### 宿舍三角的确立

**mikudorm45**／**mikudorm45p2** 全线上半的结构转折：Makoto 得知 Miku 与 Sensei 的关系后的三角谈判。Miku 亲吻 Sensei 被 Makoto 知晓，两人达成「不互相隐瞒」协议：

> mak: I'm more comfortable with the idea of you romantically pursuing Miku than any of the other girls.（
> mi: The whole reason I wanted to do somethin' like this is so we wouldn't hurt each other's feelings...（

这确立了贯穿全线的「三人共同体」：Makoto 先行、Miku 跟进、彼此透明。mikudorm45p2 尾部藏着一次重要的情绪泄洪：Miku 说想忘记某事，Sensei 以茧与羽化作答——*"her wings fuse to her chrysalis"*，并邀她去商场挑衣服当作约会。「想忘记」的具体所指此处按下不表，成为悬置到 spring 阶段的钩子。

### invite 线与第四墙忏悔

**mikuspecial50** 五十级特殊事件承接过渡。**mikudorm50** 之后进入 **mikuinvite1** 与 **mikuinvite2**——本线第一个成人事件：Miku 主动上门要求「回礼」，*"fair is fair and I'm the only one who's gotten some so far"*（mikuinvite2）。事件旁白罕见地打破第四墙直接向玩家忏悔：

> N: Right now, a high school freshman is on her way to my house because I am going to do things to her. And *she* is going to do things to me.

事件同时埋下两条暗线：其一，mikuinvite2 的叙述者提及，去年万圣节在 Sensei 酒店房间发生的事，Miku 似乎并不记得（"it doesn't seem like Miku remembers that"，为叙述者口吻而非 Miku 台词）；其二，同一事件中还出现 Valium 与「that one Halloween that landed the two of us in hot water」的线索，指向一个从未正面还原的万圣节之夜。

### 泳池过量事件

**mikupool55**：Miku 在池边意识涣散近乎昏迷，Karin 误判为疲劳。Sensei 不送医务室的真实理由是自利推理链——怕 Makoto 发现他早就知情，反复自我催眠 "I am making the right choice"，甚至预先把责任推给 Io："It will be Io's fault."。背回宿舍后误拨电话给 Ami，说出全书罕见的自我暴露：

> s: That's my name. Just it isn't. My real name is Akira. Hello.（

与 Ami 的通话里他形容自己 "Everywhere and nowhere"（此前他先误拨到别人，随即主动再致电 Ami）。苏醒后的 Miku 处于药物残余状态，主动提出以初夜「回报」并被拒；她随即暴露真实动机——医生之所以不能去，*"Because they'll make me talk!"*：她怕的不是治疗，是被问出父母的事。

### 创伤总解明

**mikudorm55p1**／**p2**：p1 承接过量余波，p2 正面引爆身世——窃贼、枪声、母亲的身体、床下的整夜。拔发、怕巨响、解离在此获得统一解释；转向正规治疗的决断也在 Makoto 主导下完成。本段之后，Miku 的所有「过度活跃」都完成了重新编码：那不是性格，是症状的代偿。

### spring 系列

**mikuspring1** 与 **mikuspring2** 处理创伤披露后的关系重建：Sensei 自认救了她一命，两人第一次以「非炮友」的身份相处，节奏刻意放慢。**mikuspring3** 宿舍战争运动会动员章，贡献全书最长的冗长标题笑话（SMUS-DDW:NBA 式命名），群像喜剧为高压剧情强制降压。**mikuspring4** 与 **mikuspring5** 推进日常约会与信任积累，love 值弹窗落在 spring3 尾声。

### 命名与元叙事接口

**mikulust5** lust 低阶节点之后，**mikunaming** 成为全线最特殊的章节：两人正式讨论「该怎么称呼彼此与这段关系」，"Coach" 命名树在此展开；同段她在 Maki 店里试玩了《Lessons in Love》本体——她评价自己正在经历的这款游戏，玩家层与角色层在同一场戏里重叠。**mikupostnaming** 处理命名后的微妙期：称呼变了，关系的重量也随之变了。

### 秘密公寓与终章

**mikuspring6**：Miku 搬进 Sensei 的秘密公寓，豆芽菜晚餐的贫穷喜剧之下压着两条重线——其一是「new Maki」抑郁线：Maki 得知 Sensei 与两个女儿都上了床后崩溃，转而对女儿实施管束，Miku 被夹在这户人家的地震带正中央；其二是 grooming 辩论，Sensei 以 *"any girl who has been groomed would likely say"* 的句式自我辩护又自我怀疑——这段话是全局对「教师—学生恋」伦理问题最直白的正面处理。

**mikuspring7** 终章。电影夜，Moby Dick 引文贯穿始终作为捕鲸与执念的框架隐喻；Sensei 的内心独白冷不防摊牌：*"I don't love Miku. And Miku doesn't love me."*——紧随其后的是 forced coming-of-age 独白，承认这段关系里没有人在以正确的方式长大。lust 场景以「仅 tip 进入」的分寸收束，把越界停在一厘米之外。情感终点由 Miku 亲口敲定：

> mi: ...Is it okay if I call you my boyfriend from now on?（

从 friends-with-benefits 到 boyfriend 的请求，是全书少数由女方主动完成的命名仪式。事件跳转 endofsatch4／endofweekdaych4，主线锚点合拢。

## 三、lust 线概貌

本线欲望内容分散在 invite 系列、**mikulust5** 与 spring7 终场，被裁剪标记覆盖的部分可抽象为四种叙事功能：

1. **等价交换的入门**：invite2 的「回礼」逻辑把性表述为账目，与她运动员式的规则感同构——先立规矩，再破规矩。
2. **药物的幽灵**：多个欲望场景发生在药物残余期内（ Valium、- 过量后的「回报」提议），欲望的知情同意问题被反复摆在台面上，构成对 Sensei 的持续控诉。
3. **命名的洗白机制**：mikunaming把称呼系统当作欲望的再包装流水线——换一个名字，同一件事就从交易变成了恋爱，这正是 lust 线对 love 线的反讽馈赠。
4. **一厘米的伦理刻度**：spring7 的 tip-only 场景把「没有完全越界」本身写成内容——它既是克制也是欺骗，取决于读者站在哪一层看。

## 四、与主线/元叙事咬合点

- **主线锚点**：spring7 结尾双跳转（endofsatch4／endofweekdaych4）使本线与周六／工作日主日历硬挂钩。
- **角色玩游戏**：她在 Maki 店里试玩《Lessons in Love》本体，是三层世界观中最露骨的一次层间穿透——玩家看着角色评价玩家的行为。
- **Akira 之名**：泳池过量夜的电话事故让 "My real name is Akira"落在她这条线，而非任何主线章——主角身份危机的第一块实证碎片交给了她保管。
- **Ami 通道**："Everywhere and nowhere" 的通话把她与 Ami 的神秘气质线并联，姐妹般的「不在场者」意象共享。
- **Io 医药暗线**：她的药片来源接入 Io 的地下供给网络，与多条角色线的药物问题同源。
- **Maki/Makoto 家庭线**：「new Maki」抑郁与管束使本线成为母女震中的记录仪，Makoto 线的一半重量在本线过秤。
- **秘密经济**：invite2 的泄密示范了情报在本世界的传播速度——一个秘密经 Miku 之口抵达 Kirin，再由 Kirin 进入更广的交换网络。

## 五、未解伏笔

- **她想忘记的事**：dorm45p2 尾部的「想忘记」始终未指名——它与万圣节失忆夜是否同体，悬而未决。
- **万圣节酒店之夜**：Valium、失忆与服装线索指向的那一夜从未正面还原。
- **Io 药片的成分与来源**：只确定了「来路不明」，处方权、成瘾性与 Io 的动机全部悬置。
- **父母枪案**：两名窃贼的下落、案件是否告破，文本保持沉默。
- **"Everywhere and nowhere"**：这句自我形容与 Ami 线的同款气质是否指向同一设定层，无定论。
- **boyfriend 之后**：命名仪式完成于版本末尾，这段关系的下一形态尚未开演。
> 按源行号检索本角色 label，见 `索引/Miku索引.md`。
