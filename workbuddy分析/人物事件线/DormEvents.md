# DormEvents 宿舍线全析

> **源文件**：`_tmp_digest/reread/_reread_DormEvents.txt`（对应游戏脚本宿舍事件集，digest 共 16551 行）
> **label 总数**：172 个
> **定位**：本文件是全作体量最大的角色群像事件集之一，承载十条角色支线（Chika／Yumi／Ayane／Sana／Makoto／Miku／Rin／Futaba／Ami／Maya）在女生宿舍内的全部好感度事件、成人回放入口，以及文件末尾一组完全脱离恋爱表层、坠入元叙事底层的实验性恐怖 label（roomwithclocks 系列）。
> **阅读提示**：正文按"群像基本盘 → 逐事件脉络 → 成人内容概貌 → 主线咬合点 → 未解伏笔 → label 总表"组织。三层世界观贯穿全文——恋爱表层（学生与老师的日常喜剧）、重置循环层（世界被反复重置、记忆即危险）、元叙事玩家层（USER1–4、Teacher、God 直接向玩家喊话）。所有英文引文均为原文直引，括注 digest 中保留的原脚本行号。

---

## 一、群像基本盘

宿舍系统的骨架是一个日程循环壳加十个角色 hub。`dorms`（[1]）是总跳转表，`firstdorm`（[17]）是教学关：只有 Room 4 的 Rin 与 Futaba 可以进入，其余房门直接嘲讽玩家——

> s: Learn to read!（教学关提示语）

未解锁的房间会提示将在教学关后开放，同时界面上直接显示当前 `[rin_love]`／`[futaba_love]` 数值——好感度作为可读数值被明示给玩家，这本身即是元叙事层的一次轻微破框。

`dormweekend`／`dormmonday` 至 `dormfriday`（[105]–[300]）构成星期循环节拍器，`doorknock`（[336]）是敲门通用反馈。随后是一组 `*firsthall`／`*hall` label（[629]–[2383]），为 Yumi、Maya、Miku、Futaba、Rin、Chika、Makoto、Ayane、Ami、Sana 十人各配"首次走廊遭遇＋重复走廊遭遇"两段小场景。它们大多一两句带过式地立住人设：Yumi 的吧台戏确立其"pack 里的 outcast"身份，而主角的内心独白已经毫不掩饰地暴露了恋爱表层的真实底色——

> N: thinking about having sex with her（[2406]）

十位角色的宿舍线深度差异极大：Chika／Yumi／Ayane／Sana／Makoto／Miku 六条线以每 5 点好感度一个事件的节奏推进到 35–50 级；Rin／Futaba 线采用 `*firstvisit`＋`6to9` 区间＋逢十事件的混合结构；Ami／Maya 线最短却承担了最重的元叙事任务，并在结尾接入了整个文件最黑暗的部分。

## 二、主线逐事件脉络

### Chika 线（chikadorm，[2431] 起）

hub 提供 Hang out 与 Fingering／Handjob 回放入口。`chikadormgen`（[2480]）为通用挂机事件。`chikadorm5`／`10`／`15`／`20`（[2556]／[2917]／[3416]／[4856]）逐级推进 Chika 与主角的亲密关系，从试探性的房间相处走向身体接触，节奏是标准的恋爱表层喜剧升温曲线。`chikafingerreplay`／`chikahjreplay`（[5153]／[5180]）为成人回放的轻量包装层。

### Yumi 线（yumidorm，[2455] 起）

`yumidormgen`（[2518]）之后，`yumidorm5`（[3811]）是 Yumi 找兼职的核心喜剧：Sana 提议女仆咖啡厅，换来 Yumi 的暴怒——

> yu: DO I LOOK LIKE MAID CAFE MATERIAL?!（[4596]

最终改为普通咖啡厅，且工作地点正是 Rin 打工的那家店（[4638]），两条支线在此完成一次安静的缝合。`yumidorm10` 到 `yumidorm35`（[4126]–[6261]）持续以 Yumi 的暴脾气—傲娇轴心推进，兼有家庭线（与其母 Yuki 的恶劣关系）作为暗流。

### Ayane 线（ayanedorm，[6662] 起）

Ayane 线是恋爱表层里最早露出獠牙的一条。`sanadorm` hub（[6689]）之后，`sanadorm5`（[6713]）先给出 Sana 线的开场：Sensei 以 "educational purposes" 为借口强行拜访学生房间，Sana 紧张到结巴——

> sa: I don't...think it's normal for...teachers to come to their students' rooms...（[6738]

这句台词由受害者的嘴说出，却精准描述了玩家的所作所为，是全作自我意识的典型样本。

Ayane 线在 `ayanedorm20`（[8611]）迎来病娇宣言的高潮：

> ay: Because you're all I have.
> ay: I am addicted to you.（[8755]
> ay: It's your fault that I fell in love.（[8762]

归罪句式把责任反扣在主角身上，与玩家操控事实形成互文。`ayanedorm30`（[10665]）延续到与 Touka 的道场冲突后续：主角扮富人混入道场，Ayane 则说出全作最令人不安的情话之一——

> ay: But you're my peasant（[10812]
> ay: I'd probably accept the risks that come with murder if it means staying together with you.（[10833]

Todd、master Arakawa 等道场人物在此被引入外部主线。`ayanedorm5`／`10`／`15`／`25`／`35`（[7312]／[7607]／[7911]／[9988]／[11892]）填充两级之间的梯度，`ayanedormgen`（[8124]）为通用事件。

### Sana 线（sanadorm，[6689] 起）

从 `sanadorm5` 到 `sanadorm45`（[6713]–[12400]），Sana 线走的是社恐少女逐步卸防的长弧。`sanadorm50`（[12787]）以枪战式的幽默敲门开场，随后呈现 Sana 以头发遮眼、Sensei 假装不认识她的尴尬名场面，是这条线喜剧与哀伤混合气质的缩影。

### Makoto／Miku 线（makotodorm [13177]／mikudorm [13219] 起）

两线共享室友结构。`makotodorm5`（[13348]）与 `mikudorm5`（[13713]）分别开场；`mikudorm25`（[14851]）里的健身房调情给出 Miku 线的招牌语气——

> mi: stealing the job I was put on this earth to do（[14906]
> mi: Makoto's boobs aren't big（[14937]

`mikudorm35`（[16532]）即 mikudormfreak 事件本体：Sensei 说服 Miku 接受"评判身材"，Miku 的抵抗以玩笑形式说出——

> mi: I don't wanna have friggin' sex, Sensei. The only position I know is the backwards cowboy.（[16831]
> mi: I don't mind if you touch me...just...not down below（[16836]

Makoto 撞见后暴怒驱逐（"I SAID GET OUT!"[16873]），事件跳转至收尾 label `endofmikudormfreak`（[16864]）。`mikudorm40`（[16943]）处理余波。Makoto 线的 `makotodorm20`／`25`（[15523]／[15930]）以及四个 replay 入口（[14619]–[14739]）维持该线的常规推进，`mikudormfingeranim`（[14739]）为 Miku 线动画回放入口。

### Rin 线（rindorm，[17291] 起）

`rinfirstvisit`（[17714]）与 `rindorm6to9`（[17962]）铺陈初期关系；`rindorm15`（[18789]）给出闯入风波——

> ri: I am very, very, very, very, VERY mad at you.（[18887]
> ri: Everyone in our class has officially seen my boobs.（[18937]

自嘲式消化羞耻是 Rin 的标准防御机制。`rindorm35`（[20721]）安排了 Chika 与 Rin 的单独谈话：主角主动退出，旁白点出 "Rin's been hiding from Chika ever since the beach"（[20998]），而 Rin 的内心只有一句 "{i}Please...don't...{/i}"（[20988]）；Chika 的关心（"The Rin I know is bubbly and full of life"[21032]）撞在一堵沉默的墙上，为后续爆发埋雷。

`rindorm50`（[23274]）表面是 Rin 与新女友 Otoha 的双吉他甜饼：Rin 公开点评 Otoha 外貌、宣布 "We refuse to grow up"，甚至拿 "you haven't already stuck his fingers inside" 开主角的玩笑（[23371]）。但 Otoha 离场后对话急转直下——Rin 承认与 Molly 正处于冷战（因 Molly 强吻未遂），并以一段近乎临床描述的抑郁独白收尾：

> ri: All of a sudden-
> ri: It's just nothing.（[23634]–[23640]

`rindorm50special`（[23657]）是整条宿舍线最黑暗的事件：Molly 在 Sensei 陪同下登门和好，推门却撞见 Rin 满臂鲜血的自割现场——

> mo: That's...so much blood...
> ri: Felt like it.（[23818]–[23820]
> ri: It never ends, Sensei. The pain isn't even pain anymore. It's just...numb.（[23866]–[23868]

Rin 随即陷入对 Otoha 关系的恐慌性掩盖（"I have to be wanted. I need her to want me. I can't lose her now"[24064]），最后反复追问 "Why can't I feel anything?..."（[24092]）。Futaba 深夜赶来重新包扎，旁白补上一刀："It looks like she's had practice... What a terrible thing to become experienced at."（[24101]–[24104] 附近）。自割史、药物抗拒（"Lifejacket means pills"[23978]）、"Some people just aren't allowed to be happy I guess"（[24001]）共同构成 Rin 线的精神病理侧写。

### Futaba 线（futabadorm，[17315] 起）

`futabafirstvisit`（[17357]）开局，`futabadorm6to9`（[18006]）至 `futabadorm40`（[22499]）逐级推进，四个 replay（[19999]–[20091]）提供成人入口。`futabadorm45`（[22904]）是本线的重头戏：Futaba 为逃避主角长期泡在健身房，主角上门寻找时从 Rin 处得知 Yumi 的母亲 Yuki 也去了健身房（且 Nodoka 对这位 "scary but also hot blonde lady" 有意，[23103]–[23141] 附近）。一段长达数十行的镜子意识流独白（凡尔赛镜厅 357 面镜子的呓语，[23232]–[23264] 附近）突然中断于一行十六进制——

> N: 74 68 69 73 20 69 73 20 6e 6f 74 20 77 68 61 74 20 79 6f 75 20 74 68 69 6e 6b 20 69 74 20 69 73（解码为 "this is not what you think it is"）（[23021]

紧接着 Futaba 当场精神崩溃尖叫。Yuki 得知女儿长期霸凌 Futaba 后代女道歉（"she's a prick and that...she'll just do shit like that sometimes"[23100]），而主角坚持当场揭底的做法反遭 Futaba 怒斥 "You're the worst"（[23253] 附近）。当夜 Futaba 却主动登门道歉，旁白给出全作罕见的温柔注脚："Sometimes, people apologize just so they can hold onto things they're afraid of losing."（[23298]）。

### Ami 线（amidorm，[24128] 起）

Ami 线以侄女—监护人关系为表、以共谋式依恋为里。`amidormgen`（[24183]）为通用事件；`amidorm5`（[24305]）借 Maya 拦门立起 Ami／Maya 室友轴，房间里 Sailor Moon 海报、Emily Dickinson 诗句与路边捡来的沙发构成 Ami 的自画像，结尾主角摸门框想起易淤体质的母亲——"I miss her a lot sometimes."（[24587] 附近），第一次暗示主角自身的前史空洞。

`amidorm10`（[24592]）是恋爱表层与禁忌欲望正面相撞的一集：Maya 外宿，Ami 以怕黑为由邀 Sensei 同床。叙述者用一整段机械隐喻为自己开脱——"machine hearts and mechanical brains- all incessantly malfunctioning...we might be able to make one whole machine"（[24875]–[24877] 附近）——随后 Ami 发问：

> a: Will you lose yourself with me?（[24941]

选项分支（Yes→`amidormtouchx`／Hugging／拒绝回答）让玩家亲手决定越界深度，而拒绝分支里 Ami 的回应冷得可怕："Because you never know when I might want to stop playing them."（[24999] 附近）。

`amidorm15`（[26306]）的深夜买菜单以韭葱恶作剧调味，却在长椅上滑入哀伤：Ami 暗示两人关系早已 "progressed past the point of us being just family"（[26486] 附近），主角内心拒绝——"The two of us can't be anything more than this... She doesn't need the only person she has left in the world taking advantage of her"（[26513]–[26516]）——然后以一句 "Let's go on a vacation."（[26531]）收场。这个临时起意的度假承诺被 Ami 立即扩大成全班旅行，成为海滩篇的直接引信。

`amidorm20`（[27413]）让 Ami 到女仆咖啡厅应聘，Uta 的奈良鹿枪杀家史冷笑话与蝴蝶效应讨论（"a butterfly flapping its wings could... Tornadoes and stuff"[27757] 附近）并存。`amidorm25`（[27819]）的沙发拥抱戏里，Ami 摊牌打工的真实动机是逼 Sensei 承认需要她（"Just a last-stitch effort to get you to admit how much you need me"[28015] 附近），事件末尾的好感度提示字符串崩坏为一长串 x 与乱码（[28160]），系统层面先于人设层面露出了裂缝。

`amidorm40`（[29117]）是 Ami 线的元叙事引爆点：同一场景的两套文本并行闪现（"Where we go when we die" 与 "what you ate for lunch today" 交替划掉重写，[29284]；"put my underwear back on" 与 "finish eating this watermelon" 并置，[29302]–[29303]），玩家被明示眼前场景至少存在两个版本。随后 Ami 把 Maya 锁在门外，展开对过去的盘问："You never tutored Maya, Sensei. She wasn't one of your students."（[29538]–[29539]）——直接戳穿主角记忆与 Maya 说辞的矛盾，并以三连问收束："Do you know what {i}is{/i} real, though? The past you have with me."（[29579]–[29580]）。Makoto 与 Maya 回归后，事件以主角一句 "What exactly happened tonight?"（[29662]）悬置。

### Maya 线（mayadorm，[24158] 起）

`mayadormgen`（[24260]）立住 Maya 的人设基调：赶不走、厌恶男性、以宇宙哲学为盾。`mayadorm5`（[25058]）的午夜搬箱是这条线的仪式性场景——一只写着 "Don't Open" 的箱子、两英里夜路、巷子自动贩卖机里一罐勾起既视感的半糖冰咖啡（"This is the only vending machine in town that sells that. So chances are you've just been here before."（[25493] 附近）。`mayadorm10`（[25451]）的暖桌戏里 Maya 第一次半撕破脸："Did being reincarnated scramble your brain or something?"（[25712]），并宣告 "We can never be {i}anything.{/i}"（[25724]）。

`mayadorm15`（[25847]）的两英里章鱼烧之旅中，Maya 从闲聊突然切入警告模式："What do you think would happen if those cycles were to converge?... Would something like that break you?..."（[26157]–[26165]）——循环收敛的概念在此首次以具体威胁的形态出现。`mayadorm20`（[26667]）的第二只箱子戏给出 Maya 最接近剖白的一刻："You carried a burden. It's different."（[26897]），以及叙述者对重置事实的直接确认："You'd think after resetting the entire world, the two of us might have bonded somewhat... I'm sure she's reset the world countless times by now."（[26995]–[26997]）。事件以四行删除线诗句收尾："THE FUTURE IS BRIGHT... Or prepare to be swallowed by it."（[27019]–[27023]）。

`mayadorm25`（[27040]）难得地纯然搞笑：Maya 带主角去她常光顾的女仆咖啡厅，Uta-chan 的 "FLAVOR BEEEEEEEAM"（[27368])与 Maya 的全程毒舌形成二重奏，同时埋下 Ami 日后在此打工的接口。`mayadorm30`（[28246]）是情报量最大的一集：Noriko Nakayama 被 Maya 定性为危险人物——"She's also a hyper obsessive stalker who has been looking for you for years now."（[28287]）；记忆量与存续直接挂钩——"The more you remember, the less likely it is for you to continue living."（[28322]）；而主角房间那本神秘日志的作者被揭晓正是 Maya 本人："I attempted to make myself as unappealing as possible by saying you didn't know anything about me... But I suppose I am just that irresistible after all."（[28548]–[28549]）。雪夜蒙眼引路一场，把"信任 Maya＝靠近真相＝靠近死亡"的悖论推到台前。

`mayadorm35`（[28627]）是 Maya 线的崩溃顶点。主角开始出现视觉幻觉（"If I look at you, something bad will happen."[28828]），文本插入一段掐死雏鸟的血腥寓言与 "A bird lays its nest on top of me" 的变形感知（[28856]–[28899] 附近）；Maya 察觉主角正在"看见东西"，情急之下提出以身相替——"Do you want me instead?... Will that be enough to keep you away from her?..."（[28934]–[28935]）——随即意识到主角连勃起功能都已随人格一同失灵（"It's...not even hard?..."[29006]），最终以正坐（seiza）姿势彻底封闭自己（[29072]–[29073]）。此处 "her" 几乎确指 Noriko：两个知情人争夺对同一个失忆者的解释权。

### roomwithclocks 系列（[29683]–[31081]）：宿舍底层的异空间

`roomwithclocks`（[29683]）名义上是某扇门的背后，实际上是整个文件的地下室。主角敲响五号宿舍的门后被拖入一间挂满无指针时钟的房间，被缚于腐椅之上，白蚁从木缝涌出啃食手臂；一名被称为 six 的少女以日语循环发问（"ようこそ！元気ですか？幸せですか？"（[29778]–[29781]），身体沦为白蚁女王产卵的容器。文本在极端色情与极端恐怖之间反复横跳，随后接连闯入三个元叙事人格：

- **Teacher**（te）：自称 "before my next appearance in chapter two"（[29935]），发表一篇讽刺布道式的"正确性教育"，中途突然卡壳——"...I'm sorry. Class is cancelled for the rest of the day."（[29967]–[29968]）；
- **Sev**（sev）：以脱口秀主持人姿态采访主角 "how you've managed to avoid violently raping anyone thus far"（[30004]），并透露观众视角的存在（"some of our viewers who are just tuning in now"（[30003]）；
- **USER2**：系统消息 "//USER2 WOULD LIKE TO OPEN CONVERSATION WITH YOU //DO YOU ACCEPT?"（[30051]–[30052]），接受后对方仅打出 GREETINGS 即因 "ISSUES WITH 'NETWORK'" 断线（[30070]）。

此后文本全面乱码化（[30091]–[30098] 的 zalgo 字符倾诉 "i want to go home"），插入一首 "Jungle gym" 童谣（[30100]–[30103]），six 的台词转为凯撒密码（解码后包括 "there is no god. god is dead. we're the only ones left. hey. hey. look at me. will you trust me?..."（[30267]–[30271]），最终以三个选项 God／Is／Dead 收束进 `restofthenewthing`（[30288]）：一颗温热的蛋、一句圣餐式的 "Body of Christ. Amen."（[30340]–[30345]），以及系统祝贺 "Congratulations! You learned! Go learn more! Become stronger! Smile always!"（[30385]–[30390]）。

`lettert`（[30432]）是可选支间：夏日雪原上立着聚光灯照射的巨型字母 T（主角自称最讨厌的字母，疑似指涉 Todd 或 T 开头的更高存在），six 隔音发问 "You've been born twice and yet question the snow?"（[30464]）。拒绝靠近则错过内容，旁白自嘲 "the world becomes a safer place because I didn't see any nudity and nudity is bad"（[30498]）。`ticktock`（[30516]）将时钟房间日常化为可反复造访的据点：six 的名字以十六进制给出（61 6d 20 69 20 6f 6b 61 79＝"am i okay"），她自述 "she isn't really like you and me... She is an emissary of HOPE"（[30536]–[30545]），离场时系统留言达到直白的顶点："Everything you believe in is fake! The only real thing is Kumon-mi! All that happens here is gospel!"（[30624]–[30626]）。

`trinity1`（[30646]）是该系列的终章：Ami 在主角注视下脱衣变形、被熟悉少女（Maya）的手指引入酸液溶解成色块，随后二人以赞美诗口吻宣布带主角 "ON A LUXURIOUS JAMAICAN CRUISE" 又立即承认要等第二个海滩更新（[30740]–[30743]）——元叙事层的更新计划吐槽直接写进梦境。Ami 的独白在此达到全文件情感峰值："I'd do anything for you. I'd even rewrite the world. But, sadly...that's not something I have the power to do. That's something only God can do."（[30858]–[30865]）。场景切换至凌晨三点，Maya 带主角来到废弃校舍前三盏聚光灯下的孤树，讲授三位一体（"there are three gods, but also only one god"（[31015]），然后闭上眼说出判词——

> m: God is dead. So we'll never have to worry about three all at once. But, if for some strange reason, one day we do- I hope that you will choose the least callous of them.（[31041]–[31044]

系统立即以错误信息反驳："//ERROR //GOD IS NOT DEAD //HE RISES //SLEEPS AMONG US //RAPES THE ONES WE LOVE... //PRAISE BE"（[31052]–[31064]），并结算出一项前所未有的数值："Your affection with God has increased to [god_love]! It will change nothing!"（[31072]–[31073]）。

## 三、成人内容概貌

宿舍线的成人内容以 replay label 形式挂在各角色 hub 下，正文内仅以入口＋一句触发语呈现，其叙事功能可抽象为三类：

1. **进度仪式型**：Chika（finger／hj）、Makoto（hj／finger／bj／miss）、Futaba（hj／bj／boobjob／finger）、Ami（finger／hj／missionary／bj）的回放入口均以"敲门—稍等—进来吧"的三步微场景包装（如 `amifingerreplay` [26247]–[26253]），随后结算 lust 数值。它们的功能是把恋爱表层的好感度进度兑换为可见的身体进度，维持"养成有回报"的玩家契约。
2. **边界协商型**：mikudormfreak（`mikudorm35` [16532]）是唯一一个把性行为本身写成谈判现场的常规事件——Miku 以 backwards cowboy 的无知笑话、'not down below' 的限定条款参与协商，Makoto 的撞破则把三人关系的张力实体化。Ayane 线的 `ayanemissreplay`／`ayanebjreplay`／`ayanecowgirlrep`（[8198]／[8224]／[9963]）同理，回放的不是动作而是 Ayane 占有欲的再现。
3. **越界焦虑具象型**：Ami 线的成人入口全部服务于同一主题——血缘与欲望的相互污染。`amidorm10` 里同床邀请前的机器心脏独白、`amidorm40` 里 "pin me down and ravage me in the middle of[school] one day and I'd lay there and take it like the good girl I am"（[29510]–[29511] 附近）这类台词，把"侄女主动献祭式顺从"写成主角道德焦虑的镜像；roomwithclocks 系列则更进一步，将色情描写本身扭曲为恐怖装置（白蚁女王、钉上墙的 six、"I want to pet the cat" 的强迫性复现 [30100]–[30168]），宣告恋爱表层的欲望语法在底层已彻底失效。

## 四、与主线/元叙事咬合点

1. **重置循环的多次实证**：Maya 线提供了循环层最密集的证词——"I'm sure she's reset the world countless times by now."（[26997]）；`mayadorm15` 的循环收敛警告（[26157]–[26165]）；`mayadorm30` 将记忆量与生存挂钩（[28322]）。Futaba 线的镜厅独白以十六进制密文（[23021]）预告"这不是你以为的东西"，与循环层的信息封锁机制同构。
2. **记忆政治的三方角力**：Maya（制造假日志、要求切断 Noriko，[28544]–[28559]）、Ami（质询辅导往事、强调"与我共有的过去才真实"，[29538]–[29593]）、Noriko（被双方一致妖魔化的第三方知情者）围绕失忆主角的解释权展开拉锯，宿舍线实质上是主线"我是谁"问题的分战场。
3. **元叙事人格的直接登场**：roomwithclocks 系列让 Teacher（预告第二章登场，[29935]）、Sev（观众访谈框架，[30003]）、USER2（连接请求，[30051]–[30070]）依次出场，配合 "[totaldays] days"（[30042] 附近）的游戏内计时变量与 `[god_love]` 数值（[31072]），把 Ren'Py 的引擎变量本身变成了叙事材料。
4. **宗教—创世话语**：trinity1 的三位一体讲义、"God is dead" 判词与系统 "//GOD IS NOT DEAD" 反驳（[31041]–[31064]），加上 six 作为 "emissary of HOPE"（[30545]）的身份，为全作的造物主悬念（谁在重置世界、God 是否就是玩家或开发者）铺设了宿舍侧的神学地基。
5. **跨线缝合**：Yumi 兼职店与 Rin 打工店的绑定（[4638]）；Ami 的度假提议引出全班海滩旅行（[26531]–[26554]）；女仆咖啡厅先后承接 Yumi 求职笑柄、Uta 登场、Ami 打工三条支线；Futaba 崩溃事件牵出 Yuki—Yumi 家庭线与 Nodoka 迷恋年上女性梗（[23109] 附近）。

## 五、未解伏笔

1. **Noriko Nakayama 的真实面目**：Maya 称其为追踪主角多年的偏执跟踪狂（[28287]）并坚称"你曾在她身上消失过"（[28564]–[28565]），但全部定性出自 Maya 之口；Ami 则从未听说过主角辅导过 Maya。三方说辞无一互证，真伪悬置。
2. **箱中之物**：`mayadorm5`／`20`／`30` 反复出现的 "Don't Open" 箱子始终未被打开（[25124] 附近、[26724] 附近），其 contents 与 Maya 深夜往返学校的真正目的一样保持封闭。
3. **主角的前世与死因**：`amidorm5` 里对母亲的怀念（"My mom said I was kind of like a banana. I miss her a lot sometimes."（[24582]–[24587] 附近）与 `mayadorm20` 里 "Have you given up on referring to them as your brother and his wife?"（[26840]）共同指向一段主角自己都无法访问的家史；Ami 父母"直到她七岁才去世"的表述（[29213] 附近）与孤儿设定之间的缝隙同样未被填平。
4. **six 的身份**："am i okay" 的名字、"born twice" 的质问（[30464]）、HOPE 使者的自我定位（[30545]），以及 jungle gym 童谣与凯撒密码求救，都指向某个被困于底层的具体角色，但文件内未给出姓名锚点。
5. **USER2 的断线与 "TIME REMAINING: 2"**（[30070]–[30072]）：连接协议、倒计时含义、以及 USER1／3／4 是否存在于其他文件，均无内部解答。
6. **Rin 自割的后续**：`rindorm50special` 结束于包扎与掩盖承诺（"I'll stop for Otoha"[24069]），既未告知 Otoha，也未触发任何求助机制——这条线以危机进行时的状态悬在半空。
7. **好感度系统的异常**：`amidorm25` 结尾 affection 字符串崩坏为 xxx… 与乱码（[28160]–[28161]），`trinity1` 出现 `[god_love]`（[31072]）——数值系统自身开始"生病"，暗示界面层亦是被操纵的对象。
8. **巨型字母 T**（[30447]）：夏日降雪、聚光灯与"我最讨厌的字母"的自我陈述，指向某个尚未在宿舍线内现身的存在。

## 六、label 总表

| label | 原行号 | 内容一句话 |
|---|---|---|
| dorms | [1] | 宿舍 hub 总跳转表 |
| firstdorm | [17] | 教学关：Room 4 可进，其余房间嘲讽玩家并显示好感度 |
| dormweekend | [105] | 周末日程壳 |
| dormmonday–dormfriday | [124]–[300] | 工作日日程循环壳（五个 label） |
| doorknock | [336] | 通用敲门反馈 |
| yumifirsthall/yumihall | [629]/[706] | Yumi 走廊首遇/复遇（吧台 outcast 立像） |
| mayafirsthall/mayahall | [740]/[864] | Maya 走廊首遇/复遇 |
| mikufirsthall/mikuhall | [902]/[1028] | Miku 走廊首遇/复遇 |
| futabafirsthall/futabahall | [1063]/[1203] | Futaba 走廊首遇/复遇 |
| rinfirsthall/rinhall | [1239]/[1399] | Rin 走廊首遇/复遇 |
| chikafirsthall/chikahall | [1436]/[1590] | Chika 走廊首遇/复遇 |
| makotofirsthall/makotohall | [1631]/[1773] | Makoto 走廊首遇/复遇 |
| ayanefirsthall/ayanehall | [1813]/[1995] | Ayane 走廊首遇/复遇 |
| amifirsthall/amihall | [2032]/[2206] | Ami 走廊首遇/复遇 |
| sanafirsthall/sanahall | [2244]/[2383] | Sana 走廊首遇/复遇 |
| chikadorm | [2431] | Chika 线 hub（Hang out＋finger/hj 回放入口） |
| yumidorm | [2455] | Yumi 线 hub |
| chikadormgen | [2480] | Chika 通用挂机事件 |
| yumidormgen | [2518] | Yumi 通用挂机事件 |
| chikadorm5/10/15/20 | [2556]/[2917]/[3416]/[4856] | Chika 好感度 5→20 递进事件 |
| chikafingerreplay/chikahjreplay | [5153]/[5180] | Chika 成人回放入口 |
| yumidorm5 | [3811] | Yumi 找兼职：女仆咖啡厅提案被怒斥，改咖啡厅，绑定 Rin 打工店 |
| yumidorm10–35 | [4126]–[6261] | Yumi 线 10→35 递进事件（六个 label） |
| ayanedorm/sanadorm | [6662]/[6689] | Ayane/Sana 线 hub |
| sanadorm5 | [6713] | Sensei 以 educational purposes 拜访，Sana 结巴 |
| sanadorm10/15/20/25/30/35/40/45/50 | [6954]–[12787] | Sana 线 10→50 递进（九个 label）；50 为枪战玩笑敲门＋遮眼名场面 |
| ayanedorm5/10/15/20/25/30/35 | [7312]–[11892] | Ayane 线递进（七个 label）；20 为病娇告白高潮，30 为道场/Touka 后续 |
| ayanedormgen/sanadormgen | [8124]/[8161] | 两线通用挂机事件 |
| ayanemissreplay/ayanebjreplay/ayanecowgirlrep | [8198]/[8224]/[9963] | Ayane 成人回放入口 |
| makotodorm/mikudorm | [13177]/[13219] | Makoto/Miku 线 hub |
| makotodormgen/mikudormgen | [13246]/[13296] | 两线通用挂机事件 |
| makotodorm5/20/25 | [13348]/[15523]/[15930] | Makoto 线递进事件 |
| mikudorm5/10/15/25/30/35/40 | [13713]–[16943] | Miku 线递进（七个 label）；35 即 mikudormfreak 本体，40 为余波 |
| endofmikudormfreak | [16864] | mikudormfreak 收尾 label |
| makotohj/finger/bj/missreplay | [14619]–[14713] | Makoto 四个成人回放入口 |
| mikudormfingeranim | [14739] | Miku 动画回放入口 |
| rindorm/futabadorm | [17291]/[17315] | Rin/Futaba 线 hub |
| futabafirstvisit/rinfirstvisit | [17357]/[17714] | 两线首次拜访事件 |
| rindorm6to9/futabadorm6to9 | [17962]/[18006] | 两线 6–9 好感度区间事件 |
| futabadorm10/15/25/30/35/40/45 | [18048]–[22904] | Futaba 线递进（七个 label）；45 为健身房崩溃＋镜厅独白＋道歉夜 |
| futabahj/bj/boobjob/fingerreplay | [19999]–[20091] | Futaba 四个成人回放入口 |
| rindorm10/15/20/25/30/35/40/45/50 | [18533]–[23274] | Rin 线递进（九个 label）；15 闯入风波，35 Chika 谈话，50 Otoha 甜饼转抑郁 |
| rindorm50special | [23657] | Molly 登门撞见 Rin 自割现场，全线最黑暗事件 |
| amidorm/mayadorm | [24128]/[24158] | Ami/Maya 线 hub |
| amidormgen/mayadormgen | [24183]/[24260] | 两线通用挂机事件 |
| amidorm5/10/15/20/25/40 | [24305]–[29117] | Ami 线递进（六个 label）；10 同床邀请，15 度假约定，40 双重现实＋过去盘问 |
| mayadorm5/10/15/20/25/30/35 | [25058]–[28627] | Maya 线递进（七个 label）；5 搬箱仪式，15 循环收敛警告，30 日志揭秘＋Noriko 警告，35 崩溃之夜 |
| amifingerreplay/amihjreplay | [26246]/[26276] | Ami 成人回放入口 |
| amimissionaryanim/amibjrep | [26603]/[26642] | Ami 动画回放入口 |
| roomwithclocks | [29683] | 无指针时钟异空间：白蚁、six、Teacher/Sev/USER2 依次登场 |
| restofthenewthing | [30288] | 时钟房间终局：蛋、圣餐、"Congratulations! You learned!" |
| lettert | [30432] | 可选支间：夏日雪原巨型字母 T 与 six 的 born twice 质问 |
| ticktock | [30516] | 时钟房间日常化据点；six 名字为 hex "am i okay"；"Everything you believe in is fake!" |
| trinity1 | [30646] | 终章：Ami 变形/酸溶幻境、三位一体讲义、"God is dead" vs //ERROR、[god_love] 结算 |

---

*全文完。基于 `_reread_DormEvents.txt` 全部 16551 行逐段通读整理，共覆盖 172 个 label。*
