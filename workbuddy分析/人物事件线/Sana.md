# Sana 事件线全析

> **源文件**：`游戏文本/SanaEvents.rpy`（文中简称"本文件"）。分支跳转目标另见同目录 `animatedscenes.rpy`、`inappropriatecontent.rpy`、`headpatcentral.rpy`、`DormEvents.rpy`、`chap4.rpy`。
> **label 总数**：36（本文件内定义的 label）
> **定位**：全班"最纯洁"表象之下埋得最深的角色。她的线既是校园恋爱叙事，也是本作元叙事实体（pareidolia 及其造物）出场最密集的舞台。
> **阅读提示**：`sa:` 为 Sana，`s:` 为 Sensei，`sar:` 为 Sara，`q:` 为海滩与夜路的神秘女孩，`k:` 为 Kaori，`tt:` 为 tree tickler，`peggy:` 为 Pegasus，`kb:` 为 Knife Boy，`vpa:` 为异界广播，`yu:` 为 Yuki，`ay:` 为 Ayane，`ni:` 为 Niki，`maki:` 为 Maki，`os:`/`w:` 为 Osako 与 Wakana，`to:`/`ya:` 为 Touka 与 Yasu，`r:`/`f:`/`mo:` 为 Rin、Futaba、Molly。本文只记录 bonus == True 分支的内容。

---

## 一、角色基本盘

Sana Sakakibara 的自我介绍是她人物设定的官方清单：

> sa: Sana Sakakibara...part time bartender and full time student. Resident of...dorm number two. Ayane's best friend. A...member of the light music club.
> sa: A girl who...really likes you and...is having a really hard time accepting that?

核心要素：二号楼宿舍居民、Ayane 的挚友兼室友（sanaspring6 里 Ayane 当面称她 "my naked roommate"）、轻音部成员、母亲 Sara 的酒吧里的兼职调酒师。

酒吧的来龙去脉在 firsttimebar 里交代清楚：店是外祖父母开的，母亲住在楼上，Sana 现在住在宿舍；店里只进本地酿酒厂的酒，客人只剩角落几个抽烟的老太太。Sana 说"没有客人我妈就没多少钱"，打碎东西宁愿从自己工资里扣（bar5）；叙述者由此推断"Sana 的爸爸看来也不在画面里"，并猜测是母女二人在撑这家店。bar35 里 Sensei 要投诉时直接说 "Where is Sara? I need to speak to the owner."

Sara 是她生活里最重要的成年人，也是她既依赖又回避的人。bar10 是两人第一次见面：Sara 一直以为 Sana 的老师是个女人，当场把电话号码塞给 Sensei，并说女儿坚信"Sensei 绝不会让坏事发生在我身上"。此后 Sara 的形象一路加厚——bar15 她在吧台后面给女儿灌酒；bar30 她说"她今天不舒服，所以我给了她唯一对我有效过的药"（Sensei 反问："你用酒精给你女儿治病？"）；bar40 Sana 说母亲独自把兄妹俩带大，一提到哥哥就转移话题。在 sarasex 已发生的存档里，Sana 的怨气说得更直白（sanaspring3）："凭什么我妈能和你上床，我却要假装听不见你们每次上楼时床在响？"

家庭结构里有一个空位：哥哥 Shota。firsttimebar 里 Sensei 夸她的工作服合身，她答"那是……我哥的"，追问"他不在了吗"时她封口："这不是我现在想谈的事。"bar30 她酒后把话说开：那件制服"was"他的，"He's gone now"，而母亲每次话题一碰到他就岔开，"我们从来没有真正谈过"。bar40 她把这件事量化为"我们家三分之一被带走了"。sanaspring1 里她说自己反复做那种梦——"我能听到我哥的声音，但我从来见不到他"；sanaspring4 里这个只闻其声的哥哥在梦境异界以 Knife Boy 的形象现身。

至于生父，源文给出的是两条各自独立的信息，并未在文本中合并为同一人：bar20 里 Sara 顺着 Sensei 那句"如果你的老师开始约你妈，你不会觉得别扭吗"接话，承认自己高中时和老师有过一段秘密恋情（"如果我们两个人都在和他约会，那才会别扭"），话说到一半自己掐断，"这绝对不是我现在想跟你聊的事"。bar40 里 Sana 说的是另一个轮廓：父亲对她母亲不忠、年纪大很多、"在她上学时就对她很好，所以大概只是很会操控她"，母亲是在 Sana 出生后才发现他同时交往别的女生。

表层性格是极致的社交焦虑：说话满布省略号、无法眼神接触（bar5 叙述者明说"她没有能力进行眼神接触"）、用头发遮住一只眼睛（bar30 她说"我刚才一直把头发拨到一边，是为了催眠你"；sanainvite1 里她补一句"我又把眼睛遮起来了，因为我觉得你会兴奋"）。她还有一处没解释的禁忌——bar5 说"我不太喜欢镜子"，被问原因时以"有点私人"挡开。

她对自己的定位远比表象复杂。ayanesanabeach2 里她说：

> sa: There are things I want. Things I want that everyone else gets to have while I sit in the background. Unremarkable and exceedingly average.

bar55 里 Sensei 几乎原样把这组词砸回她脸上（"one of the most unremarkable and exceedingly average human beings I have ever encountered"），她当场反问"你是在说我无聊吗"。

同时她又坦承自己从来就不纯洁：

> sa: But I've never...actually been like that...
> sa: I've always been a pervert...but it got so much worse this summer...And now, it's like I can't get enough...

叙述层给她的时间线钉了两个钉子：ayanesanabeach4 的旁白说她十一岁发现了色情制品，"她现在偶尔还会看那第一个视频"；sanaspring3 里她把"变本加厉"的时间点指名为"今年夏天"。

恐惧与欲望在她身上同根而生。她怕独处、怕自己"看见东西"（ayanesanabeach4 里她凌晨给母亲打电话，说"我只是现在不想一个人"，并反问母亲"你还会……看见东西吗"），却又被夜色吸引——sanaspring4 开场就说深夜游荡是她睡不着时的固定习惯，"夜里这条街的样子让她兴奋，所以她一直回来"。同一段里她仰望最高那栋楼，估算从顶上掉到地面要多久："She didn't want to die. She just wanted to know what death felt like."

对变化的憎恶是她的底层代码，sanaspring3 里她说得很干脆：

> sa: I don't like change. I've never liked change.

## 二、love 线逐事件脉络

### 1. 电话永远无人接听

callsanamorning / callsanaafternoon / callsananight 三个时段事件构成一组刻意的空拍：三个 label 文本完全相同——Sensei 在手机里点下 Sana 的名字、等她接听、一串省略号、然后是 "She doesn't."，最后跳回各自的 callmorning / callafternoon / callnight。

这与 ayanesanabeach3 结尾的自问互为对照：Sensei 被赶出门后想发短信道歉，却"不知道为什么到现在还没有她的电话号码"。sanaspring4 补充了另一侧——Sana 倒是"特地向室友要来了他的号码"，但唯一一次真正用上，是某晚忍不住打电话求他来"压一压她的荷尔蒙"。

### 2. sanainvite / sanainvitegen / sanainviteaff：邀请与手指

sanainvite 是玩家主动邀约的入口，只有两行判定：`sanainvite1 == False` 时跳 sanainvite1，否则跳 sanainvitegen。

sanainvitegen 里电话被接起来了（"Hello?..."），Sana 上门后 Sensei 问"你想做什么"，菜单 sanainvmenu 给出四个方向：Hang Out (Raise Affection) → sanainviteaff；Thighjob (Raise Lust) → sanainvitethighjob（在 animatedscenes.rpy）；Cowgirl Sex (Raise Lust) → sanainvitecowgirl（同文件，需 `christmalloween6 == True` 才显示）；Headpat → sanaheadpat（在 headpatcentral.rpy）。

sanainviteaff 是纯爱侧的代表场景。Sana 掏出 Switch 爬到 Sensei 怀里打游戏，他从背后抱着她，注意力却从屏幕移开：

> N: I stare more at her fingers and try to forget, admiring the slender fleshworms that guide her on-screen body.
> N: I silently thank the beings that brought her into existence.
> N: I can name one of them. But for the other, all I can do is understand.

"能说出其中一个的名字，另一个只能去理解"指的是把她带到世上的两个人——母亲 Sara 是他叫得出名字的那一个，父亲是那个他只能"理解"却无从指认的缺席者。场景结束 `sana_love += 3`。

### 3. 酒吧系列（firsttimebar → bar55）

酒吧是 Sana 线的主舞台。sanasbar 是整个系列的调度中心：它按 `sana_love` 与一串前置 flag 逐级解锁 bar5→bar55，全部走完后按章节状态转交 sanaspringbargen（chap4generics.rpy）、sanasummer2bargen（chap3generics.rpy）、saraspring4（SaraEvents.rpy）或 bargen2，兜底是 bar2to4。

- **firsttimebar**：Sensei 第一次夜访，撞见 Sana 在吧台后面。他开始以"教社交技巧"为名固定造访，临走把一把硬币留在吧台上不结账，并坦然承认这是"某种形式的贿赂"。
- **bar2to4 / bar5**：bar2to4 是纯过场（"几乎看不出进步"）。bar5 里他设计了一场"角色扮演"——假装自己是难缠的客人点一份店里根本没有的意面，把 Sana 逼哭；这句 "spaghetti" 后来成了两人之间的长期梗（bar35、bar45、sanasexnaming 里都被翻出来）。
- **bar10**：Sara 首次登场。Sensei 一开始把她认成"老了十五岁的 Sana"。Sara 自报家门、塞电话号码、当着女儿的面暧昧地试探；Sana 的一句"Sensei……绝不会让坏事发生在我身上"让 Sara 立刻读出了别的意思。
- **bar15**：母女二人在店里喝到断片。Sana 昏倒在 Sensei 腿上，他把她抱上楼安置好，转身发现 Sara 不见了；随后 Sara 在卧室喊"把门锁上"——bonus 分支下此处直接跳 sarabarfirstx（inappropriatecontent.rpy）。
- **saramissionaryanim**：这一场 Sana 根本不在。叙述者到店发现"Sana 今晚不上班"，于是和 Sara 聊怎么招徕生意，"聊了大概五分钟就变成互相调情"，bonus 分支下跳 saramissionaryanimx（animatedscenes.rpy）。它是 Sara 线的事件，被挂在 Sana 的名字下只是因为发生在同一间酒吧。
- **bar20**：Sara 派 Sana 和 Sensei 去"侦察"一家生意红火的竞争对手。结果那是一家全服务餐厅，而端盘子的正是 Kaori——Sana 被她那套"迷你人类独眼巨人"的称呼吓到崩溃。席间 Sana 暴露了自己执意要替母亲跟来的真实原因，情绪失控喊出"你们两个想独处随时都能独处，我拦不住！你们都是成年人！"；出门时 Sensei 回头，发现 Sara 脸上的笑已经没了。
- **bar25**：Maki（Makoto 的母亲、成人用品店店主）进店，说出 Sara 是她店里的常客（"如果我每卖给她一根dildo 都能拿到一美元，我早开两家分店了"），并随口一句"你和你那变态的妈妈真不一样"。Sana 因此把话题拐去玩"问答游戏"。Sensei 被问"用一种蔬菜形容你的人生观"，答"番茄"——"外面看着总是好好的，可有的时候你咬一口，里面已经烂透了"；Sana 沉默片刻后说"你这么一说……我好像也同意"，并补上"这也是我不喜欢番茄的原因之一"。轮到 Sensei 提问，Sana 说想打鼓："Maybe there's a...drummer inside of me that's just dying to come out some day?" 她紧接着又自我否定："显然这种事永远不会发生。"（bar55 里 Sara 偷偷给她买了架子鼓作为提前的圣诞礼物。）
- **bar30**：醉酒专场。开场即点破母女关系的用药逻辑——Sara 因为"Sana 今天不舒服"提前打烊，给了她"唯一对我有效过的药"。真正的重头在酒后：Sana 追问那个"白头发的女孩"对 Sensei 说过的话（"她说你见到了 God……是真的吗，Sensei？"），并说对方提到"某个 Sana 认识的人很幸福"，她猜"大概是我哥"，由此第一次把哥哥的事说出口——"他走了"、"我们从来没有真正谈过"、"我每天都穿着他的衣服上班，可这连一场对话都没能开启"。她也在这里第一次对母亲表现出带刺的嫉妒：Sensei 一句"你妈确实很可爱嘛"，她直接离席去拿酒。结尾 Sensei 把她安置在沙发上，上楼发现 Sara 已经昏睡。
- **bar35**：Wakana（Ms. Watabe）和 Osako 来店里喝酒。Sensei 把这当作 Sana 的"实地测验"，Sana 全程顶住了没哭。席间 Osako 顺口提到"某个在道场训练的金发女孩"，Sana 由此知道 Sensei 也在练空手道，当场说"我也想学空手道"，紧接着改口"我是说，我想和你一起学"。
- **bar40**：Sana 主动开口请 Sensei 陪她走回宿舍。这是她第一次提这种要求。路上话题滑向她的家庭：她说 Sensei 是她"最接近父亲形象"的人，可"关于我爸，我只知道妈妈告诉我的那些"；她说父亲不忠、母亲"一直很天真，大概是被他牵着走"；她说母亲一个人把兄妹俩带大，"那一定很辛苦"，所以她不愿意逼母亲谈过去；她说"我们家三分之一被带走了"，而母亲选择的应对方式是"否认有时候是个挺好用的工具"。收尾的叙述者独白把三个人摆成几何图形：Ayane、Sara、Sensei 构成一个三角形，Sana 被困在中间，想出去就得弄断一条边，可弄断一条边三角形就塌了——"所以，就跟她母亲一样，她什么也不改。她待在原地，等别的一切自己解决。"事件末尾 `bar40 = True` 后跳 sanadorm40（DormEvents.rpy）。
- **bar45**：酒吧雇了 Yuki 当新员工，Sana 负责培训（店里根本没有调鸡尾酒的原料）。对话里冒出一条时间线裂缝：Sana 说"我最近还一个人去你家过夜了"，而 Sensei 明确记得"上一次重置让那次过夜从未发生过"——Ayane 也是这么说的，而且他从天台回来时 Sana 确实在宿舍。Sana 的回应只有一句"很奇怪，我明明记得我跟她聊过"。她也在这里给出了自己的成长总结：母亲"没把我的属性点加在口才上"，但"现在我多了一个能帮我练这项的队友"。
- **bar50**：酒吧终于来了真正的顾客（虽然全员点的东西都做不出来）。Sara 宣布"Sakaki-bar-a 重新登顶"，要拉所有人骑 Yuki 的摩托去老区吃拉面；Sana 和 Sensei 都留下看店。Sana 上楼拿 DVD 十分钟没下来，Sensei 上楼去看——bonus 分支下此处跳 funnydildox（inappropriatecontent.rpy）。
- **bar55**：Kaori 又来店里打工。Sensei 当着 Kaori 的面把 Sana 定性为 "unremarkable and exceedingly average"，说她"完全不需要融入，因为她本身就是背景的一部分"，并宣布"你的人类程度测试已经结束"。这次对话炸出了两件事：Sana 加入了轻音部，Sara 得知后当场激动到要"为了你烧掉整个 Kumon-mi"。一场关于"最喜欢的幼崽动物"的胡话之后，叙述层出现明确的故障文本——"INCORRECT RESPONSE PROVIDED. THE EVENT WILL NOW REVERT TO ITS PREVIOUS STATE."——画面倒回重来；随后 Sara 与 Yuki 买鼓的对话也被同样的杂音切断。事件收在"毕业"上：Sana 说自己不配毕业、但"如果你觉得我没事，那我大概就没事"。夜里 Sana 在 Sensei 第三、四杯啤酒时离开，而他"没有看到她走"。

### 4. ayanesanabeach2：附身、表白与 q 的登场

这是全线的第一道断层。海滩上 Ayane 与 Sensei 独处后，Sensei 去找整日躲在树荫下打游戏的 Sana。夜色里的 Sana 忽然变得陌生而大胆：

> sa: Then... Why not belong to *me?*
> sa: I don't want to be average anymore. I want to be fun. Exciting. Someone like Ayane or...or Rin.

她还抛出一句关于时间的不可能的话——"你和我都认识五六个学期了"——被 Sensei 抓住破绽反问 "Who are you?"。Sana 背出那份自报清单（"part time bartender and full time student...A girl who...really likes you"），空气凝固，她骂了句 "Oh, God damn it."，画面随即崩闪，神秘女孩 `q:` 取代了她：

> q: I'm surprised you know me *at all.* Those memories aren't supposed to stick.

q 承认自己刚才"借用"了 Sana，但拒绝"附身"这个说法——"我没有溜进任何人的身体。我从头到尾都是我。你看到 Sana，是因为你想看到她；你一意识到你从头到尾就没看见她，你就看不见她了。"她还说自己平时"只是试穿她们的衣服，很少觉得有必要亲自上场演戏"。

随后她开始撕世界的表皮：

- 她点名 Ami 与 Niki 是"变形者"嫌疑最大的两个——"如果我打算去猎变形者，我会从这两个开始，而不是那个有不良习惯的矮个子安静女孩"。
- 她给 Sensei 的走神起了名字："Another one of your thingamajigs."——他本来是去找 Sana 的，半路脑子就空了。
- 她描述无数个平行的他："Grooming teenage girls in parallel universes...plunging life itself into a lecherous, endless bout of chaos!"
- 她确认这个时间线"时间同时向后和向前流动……就像 Ayane 说的那样"。
- 她拒绝被认成 God（"完全错了，差得远，0/10"），也拒绝变成 Ayane——"Don't wanna. Don't like feeling what she feels."
- 她临走前说 Sensei 大概会再次忘记她，然后留下一句请求：

> q: Name me after your favorite flower.

事件末尾 `ayanesanabeach2 = True`，画面停在 youdiditlol 上停七秒，直接接 ayanesanabeach3。

### 5. ayanesanabeach3：电影之夜的两条岔路

回程 limo 上叙述者意识到自己又丢了一段记忆（"我能感觉到这一天有一部分消失了"）。Ayane 以要回家拿万圣节服装材料为由，把送 Sana 回宿舍的任务塞给 Sensei；Sana 提醒他"Ami 不喜欢你离她超过五英尺"。

两人看电影，五十分钟的静默拉锯成为全线张力最集中的场景。叙述者的内心独白一路滑坡——从"要不要搂住她"滑到对她身体的赤裸盘点，中途冒出一句关键自问："她会步她母亲的后尘吗？在某个年长男人的触碰下崩塌？"到第五十分钟，菜单出现：

- **"Put your arm around her"**（需 `sarasex == True`）：他伸手揽住她，她主动把手放到他大腿上；接吻前的一瞬——

> N: I lift her chin to kiss her.
> N: And for a brief moment—
> N: I am finally able to see her eyes.

那一眼让一切急刹车。她连声喊停："Stop stop stop stop stop stop stop!"、"你……你必须走了，现在。"、"And I don't even...remember how we..." Sensei 被赶出门，站在夜空下自问：

> N: But...
> N: Was that even Sana at all?
> N: And if not...what would that mean?

随后他又补了一句，解释自己为什么连道歉短信都发不出去——"我到现在还是没有她的电话号码"。紧接着画面闪回室内，出现一整段只有 Sana 声音的文本（"MMM! MMM! MMM!"……"Sensei...Sensei...Sensei!!! How did we........Why......can't I........"），`sana_love += 5`，事件结束。ayanesanabeach4 开场时 Sana 气喘吁吁地说"那……那太奇怪了"、"它不知从哪儿就来了"、"我觉得我可能断片了"。

- **"{b}LEAVE! DON'T DO IT! PLEASE!{/b}"**：电影放完，什么也没发生。Sana 自己开口："你该回去了，Sensei……可是，"——

> sa: But this...
> sa: Was nice...
> sa: It was really nice...

系统提示 `sana_love += 10`，置 `ayanesanabeach4skip = True`，并附两句挽歌式旁白——"{i}You dream of her and only her.{/i}" / "{i}But you're unsure if you'll ever dream that way again.{/i}"，然后直接推进到次日。

### 6. ayanesanabeach4：pareidolia 现身

凌晨一点，惊魂未定的 Sana 打电话给妈妈要求回家睡。独自走夜路的她遭遇了 q 最完整的怪物形态：先是一段命令式的巨体宣言——

> q: OFFSPRING
> q: FORGET THE TOUCH OF THE SUN
> q: ...
> q: PRAISE BE

其中夹带关于母亲的关键证词：

> q: LAY YOURSELF DOWN THE SAME WAY YOUR WHORE MOTHER DID.
> q: I CAN STILL HEAR HER SCREAMS
> q: I CAN STILL TASTE HER FLUIDS

随后叙述层本身开始崩解：先是长达数十秒的无字画面与杂音，接着打字乱码（"I HAVE TOLD YOU TIME AND TIME AGAIN!!! THERE ARE SO MANY MOONS and I manmwedfbns ASDAJSDFHTRIRED OF FUCKING CARDBOARD CUTOUT"），巨型 disembodied heads 闹剧（Sara 与 Sensei 的头在半空做"舌头动作"），肉块工厂瞬移，途中还插进一句直接对玩家的喊话——"it is of utmost importance that you {b}IMPREGNATE AYANE{/b} and just never fuck Sana at all"。

最终一个自称叙述者的声音接管了一切，全小写、无标点，并给出了它的名字：

> N: so allow me to give you a hint.
> N: actually, scratch that- how about a name instead?
> N: you can call me pareidolia.

pareidolia 自述"随着日子过去，我变得更强，能做的事更多"、"我可不是唯一一个在成长的"；它说现在还说不上站在玩家这边，"但我确实觉得眼下合作对双方最有利"，并宣布"我要把你的屏幕变黑了"。它替 Sana 清障——"我已经帮她穿过了前面那道屏障，她现在安全了"。

然后把故事缝回正常：Sara 抱住脸色惨白的女儿，逼她复述"那都是你脑子里想出来的"（"Sana，我需要你亲口告诉我你明白了！我要听你说那全是你脑子里的事！"），并许诺 "I won't lose you too..."。官方解释越是斩钉截铁，pareidolia 的收尾低语越显得毛骨悚然——"that's all there is to it."（重复两遍）、"this is all in your head. nothing is real. you can trust me. you {i}have{/i} to trust me. for i'm the only one who wants to use you for good."

事件最后，系统文本自己卡了壳：

> s: Sana's affection has increased to-
> s: ...what?
> N: GOODNIGHT

### 7. sanaspring1：废墟上的同行

Sensei 陷入自毁式的抑郁。开场独白把处境说得很白："这整趟旅程就是一场猜字谜，我在里面假装自己没有毁掉这个世界。这场游戏我输了。"Rin、Futaba、Molly 轮流劝他，他自己拿"被卡车撞"和"上吊"开玩笑，被 Rin 喝止。

此时是 Sana 主动开口，要求单独陪他去酒吧上班：

> sa: A...Actually...would you want to...walk with me? I have work, so...I'm not going back to the dorms just yet...

Molly 想跟着去，被她挡回去："我只是……想只有 Sensei。"

两人独处后，叙述者对这段关系的定义发生了质变："She's a girl I can kind of just exist with."——紧接着被自己否定："No she's not. I can't exist with her at all."（这句否定出现在一串闪回画面之后。）

Sana 交出了自己的怪梦："我一直做些很奇怪的梦，梦里我能听到我哥的声音，但我从来见不到他。而我确实看到的东西，根本没法描述。"她说这些梦让她开始怀疑"也许人生不止于此"，"也许只是拼命维持现状是在浪费时间——说不定我明天就被人捅死了，这一生结束了我却从来没有爱过任何东西"。

### 8. sanaspring1 尾—sanaspring2：未来之家与两个月

Sana 反问 Sensei 失去过什么，他答："It was horrible. I'd kill to have it back." 随后他说出自己也做了同一个梦——梦里是多年以后，所有人都走了，只剩 Sana 一人：

> s: You'd come to my house...make me dinner...have sex with me...then you'd curl up in a ball and sleep by my side until it was time for you to go back home.

她追问细节，他报出那栋房子的清单：橱柜是蓝色的，地板是棋盘格，门边的 PA 广播会播报天气并提醒他"永远不要离开"，窗户被钉死，水槽前有一块丑地毯，每周会出现一次鱼。她听完只说了一句：

> sa: It might be the only future I ever get to have with you.

sanaspring2 开场，叙述者把她的变化摆上台面，并给出两个互斥的解释——"要么她已经把我的一部分吃下去了……要么她被附身了。我只是很难相信这叫'成长'。"

此后是那"两个月"的清算：Sara 见到他第一句话就是"我还以为要再孤独两个月"。当晚 Sensei 坦白自己在暂停教书，"要不是为了 Sana 的软肋和 Ami 的另一处软肋，我大概根本不会来"。Sana 补上 Ami 的近况——"她今天在课上发表了一整篇演讲，说我们所有人都在想办法把她从 Sensei 身边偷走……里面可能还提到了一点……嗯……肢解？"Sara 提出由自己来当 Ami 的母亲角色，被 Sensei 以"她只会理解成你想借机接近我"婉拒。

三人喝酒到 Sara 先倒下。Sana 立刻开始引诱他——"她不会醒的……你喝了酒，所以你要是做了个'坏'决定也不算太奇怪"、"你的手指比我的大得多，能伸得比我更深"。Sensei 的回答是一句完全不相干的问题：

> s: What happened at the Halloween party?

得到的回答是一记反钩子：

> sa: You... You don't... You don't remember?...

Sana 随即补了一句要害："那天晚上你一直在跟一个根本不在的人说话。"

### 9. sanaspring3：Halloween 的补课与全面沦陷

Sana 以低声耳语的方式向失忆的 Sensei 还原了 Halloween 夜：她主动爬上他的膝、解内衣、自渎、乞求，"你看着我玩了一两分钟，直到我开始求你帮忙你才动手"。中途 Rin 推门进来——

> sa: I didn't care if she watched...she could have stayed if she wanted...but she felt uncomfortable, so...she gave us some privacy...and closed the curtain...

事后她揭穿：Rin 根本没离开，"她留在帘子后面，把一切都听了下去"。她把动机也摊开：

> sa: How come Ayane gets to have sex with you when I just have to use my hands?

在 sarasex 已发生的存档里，还有更刺的一句：

> sa: How come my *mom* gets to have sex with you while I have to pretend I don't hear the bed creaking every time you two go upstairs?

她的自我剖白毫不含糊："I don't like change. I've never liked change."——但自省之后她承认那些让她"想缩成一团"的情绪其实是嫉妒，"如果一切都要变，那站着不动、什么都不做才会让我觉得恶心"。Sensei 的抵抗只剩一句诚实的警告——"Falling for me won't do anything but hurt you in the long run."——以及随即的全面溃败（"I am weak."）。

行为进行时的两段独白完成了对这段关系最狠的定性：

> N: There are many girls in "my" class who have felt like daughters to me at times. But Sana is the one among all of them that felt *possible.*

> N: This is the life I wanted. But I did not *want* to want it. And I did not want *her* to want me.

结尾她说了句意味深长的话——"我大概不该再用 Ayane 的笔记本了，保险起见"——然后说服他留宿。事件末跳 chikaspring2（ChikaEvents.rpy）。

### 10. sanaspring4：梦境异界——Pegasus、Knife Boy 与 Kaori

深夜游荡的 Sana 先听见 q 的声音（"Psst..." "They say my limbs are long enough to reach the sky and back. What do you think about that?"），随即被童话怪物 tree tickler 缠上：

> tt: They call me the tree tickler. My fingers are perfect for that sort of thing.

她求救喊出 "Sensei!...Help me!"，赶来的"Sensei"却因为 tree tickler 声称"许可证我办了"而当场放弃抵抗。她坠入一个异界——

> N: Sana Sakakibara had fallen through the map and wound up in another realm — a place where dreams come prior to sleep. But that's only because it's a place that sleep has not found yet.

那里有穹顶上画的假天空、广播通知她四天后出席 "Transpacific Sadness Symposium"，并循环播放获奖歌曲 "Ad Infinitum"。两头的 Pegasus 现身：

> peggy: I AM PEGASUS, PEERLESS GOD OF FORGIVENESS.

他开价"你说出什么名字的东西都归你，只要你向我宣誓"，她当场开出愿望：

> sa: I want my teacher to fall in love with me.
> sa: If you're saying you'll grant me a wish, I wish for him to fall in love with me and for everyone else to give up. Can you make that happen?

Pegasus 要她脱衣躺进沙里，话没说完就被打断——

> q: You shouldn't listen to him. He's lying to you.

Knife Boy 登场，是 Shunned（被放逐者）。Sana 认出了他的声音：

> sa: Shota?...

他每违反一条规则就被插进一把刀——"They add a knife for every rule I break. It really hurts."他被放逐的原因指向母亲：

> kb: She's the reason I'm shunned here.
> kb: They always talk about how she broke the rules and how much of a {i}whore{/i} she is.

广播插叙：Sana 陪他聊了三个小时，坦白了自己最近的性探索，然后动手替他拔刀——第一把顺利拔出且没有新刀补位。她一把一把拔下去，直到真相浮出：

> N: You see, without knives, there can be no Knife Boy. So the legend that kept him anchored to this realm went poof...

外壳碎裂后孵出的却是失去全部记忆、自称 Akira、还坚称自己"有个很漂亮的女朋友"的 Sensei。她还来得及叮嘱他"离 Kirin 远点，她会伤你"。神使 Kaori 随后现身，为拔刀之事发出判决式的警告：

> k: Your wish was admirable — but your subsequent actions when saving Knife Boy leave much to be desired.
> k: It'd be a shame to be the one who erases you.

本章结束时画面只剩 Sana 的一句 "A chicken?..."，事件结束（`sanaspring4 = True`）。

### 11. sanainvite1 / sanainvite2：Niki 在门外

电话邀约、上门、初夜——却被提前回家的女友 Niki 搅局。Sensei 谎称"我又开始做家教了"，Niki 坚持要"观摩"。为了脱身，Sana 临场编造自己是女同性恋、对 Sensei "觉得恶心"——

> sa: Actually think he's...kind of gross and...way too old...
> sa: I'm actually...not interested in boys at all...and...

表演天衣无缝，反而引出 Niki 对 Ami 性向的一连串试探（"她自己说不喜欢女生，但我觉得那是装出来的"、"那你觉得 Ami 怎么样？她要是能开始暗恋一个跟她没有血缘关系的人，对她会很健康"）。Sana 被逼着接话："如果 Ami 愿意的话，我……我不介意……跟她交往……不过我想慢慢来。"

Niki 去洗澡后两人终于结合。高潮瞬间 Sensei 再次发生现实置换：

> N: I can smell hot pot.
> N: I can feel linoleum pressed against my back as a girl, one much older now, rides me with the same passion and fervor I was in the midst of experiencing just moments ago.
> N: In this moment — I am home.
> N: I am happy.

并在此幻觉中说出了 "I think I love you."。清醒后的 Sana 冷得像另一个人：

> sa: Sensei, you...don't *love* me.
> sa: But I'm flattered you...felt good enough to maybe *think* you did for a second or...

内射引发的恐慌让她喊出全线最残酷的一句自我认知：

> sa: You came inside of me?! Seriously?! Are you out of your mind?!
> sa: I'm in high school, Sensei! Are you trying to turn me into my mom?!

Niki 中途推门进来一次（"Something is suspicious again."），被 Sensei 用"Sana 听到你洗澡害羞了"糊弄过去；Sana 落荒而逃，临走把《Lord of the Flies》说成《Lord of the Size》。

本章结尾，系统文本直接对玩家喊话：

> N: *You aren't meant to be together!*
> N: *She's merely doing her job.*

紧接着又是两条——"{i}But on the bright side, you can invite her over whenever you want now!{/i}" / "{i}Hope you're ready for her to ride your dick off!{/i}"。结算 `sana_love += 1`、`sana_lust += 1`、置 `yukiblock = True`。

### 12. 海滩六人组与命名之夜（beachsixsana1 → sanasexnaming）

集体海滩假期的寻人段落里，Touka 与 Yasu 的怪谈式对话再次暗示世界正在渗水：Yasu 说"我能听见你的血管，一英里外"，并提到"现在我知道不该把人锁进什么地方了——就跟刚才那行漂浮的字幕说的一样"；Sensei 问"那东西还在飘吗？它之前好像一直在针对 Ayane"。

Sana 把 Sensei 拽到一处公共区域，自己脱得精光，理由很直接——"我整整一个星期没用手指了，你要是敢走，我就喊你强奸我。"

sanasexnaming 是一个 `renpy.input` 输入框：Sana 请求 Sensei 给她一个"这种情况下"对他的称呼。程序对若干输入做了特殊回应：

- **sensei**：她抗议"你刚才明明说想换个称呼"，被他一句"我们达成妥协了"堵回去，直接进入 endofsanasexnaming。
- **sara**：她连珠炮似的追问"你想让我用我妈的名字叫你？……可你没有阴茎啊？……你是想让她长一根吗？"，逼他重选。
- **ayane**：她说"想让 Ayane 加入我们可以直接问她，不用偷她的名字"，同样被驳回。
- **sana**：她威胁"我要喊强奸了"，然后反将一军要求他叫自己 Daddy。
- **daddy / papa / father / dad**：她立刻接受——"我从来没见过我爸，得把缺掉的那些年补回来"，并补一句"我的第一直觉一直就是这么叫你，只是大多数时候我忍住了，因为我想跟你一起高潮"。
- **oniichan / onii-chan / big brother / big bro**：她答应，但先问"这是因为妹控属性，还是你对快哭的女孩更硬？"，随即卡住——"可是 Sensei……你永远没法取代他的位置……我爱他，跟爱你的方式不一样。"
- **shota**：整段最重要的分支。她脸色一变——"你从哪儿听来这个名字的？……是我妈告诉你的吗？"Sensei 说那只是个名字，她答"对我来说不是"。随后她抛出一句与主线同频的提问：

> sa: Do you ever feel like someone else is making choices *for* you?

- **spaghetti**：画面进入数十帧的高频闪切与噪音，恢复后 Sensei 只说 "No, Sana. It never is."，然后重选。
- **其他任何输入**：她照单全收。

endofsanasexnaming 是本文件里最露骨的一场。Sana 跪下同时为自己服务，Sensei 一边骂她"你妈是不是也这样"一边把她抵在墙上；Touka 与 Yasu 就在不远处讨论沙滩排球赛，Yasu 说"我错了……听见东西并不好"，并向 Touka 借耳机。收尾时 Sensei 逼她承诺：

> s: Then...never...
> s: LEAVE...ME!!!!!

内射之后，她说：

> sa: I'm not......going anywhere......

结算 `sana_lust += 1`，末尾跳回 chap4.rpy 的 beachsixsexmenu 菜单。

### 13. sanaspring5 / sanaspring6：终章的双螺旋

sanaspring5 承载着两颗炸弹。第一颗是 Yuki 的癌症确诊——Sensei 亲口告诉她，"所以 Yuki 崩溃、退回老样子的时候别跟她计较"。第二颗是时间觉知：Sana 转述自己在上一场 Christmalloween 派对上和 Yumi 的一整段对话，"就是关于时间，还有问我最近有没有注意到什么在变"。叙述者随即意识到"连 Nodoka、连 Uta 都在某种程度上察觉了这套时间把戏，Sana 大概也不远了"。

中段 Sana 收起性欲，只要求他搂着她。她说自己确实"十年前就看见我们在一起了"，然后问出那句足以推翻整个恋爱表层的问题：

> sa: Would you believe me if I said we've been here before?

她承认自己的嫉妒"只比 Ami 的弱一点"，并坦白"我不怪你在我长期装难追的时候跟我妈上床——她是次优选择。你该高兴的是现在两个都能有"。顺着这条线她提出母女三人行的设想，并当场用语言和手把他逼到答应——Sara 下楼的一声 "Sana?" 把一切打断，事件跳 yukispring7（YukiEvents.rpy）。

sanaspring6 以 Ayane 试穿 Miss Watabe 旧衣开场——那批衣服是 Watabe 送给 Sana 的，大半对她太大，于是两人玩起了换装。整场是三个人互相调侃的双关语竞赛。结尾 Ayane 问"你期待看到我和 Sana 长大的样子吗"，画面开始闪切，Sana 一字一顿地念出一段粗体宣言：

> sa: BUT I WILL ALWAYS BE THERE, WAITING FOR THE CHANCE TO STRIKE AND TAKE WHAT IS RIGHTFULLY MINE.
> sa: WILT LIKE A FLOWER. BURN LIKE THE SUN.
> sa: AND WHEN IT ALL GOES AWAY, REMEMBER — IT DIDN'T HAVE TO BE LIKE THIS.
> sa: IT COULD'VE BEEN ME.

之后是 threeflowers 与数段黑屏。Ayane 不知何时睡着了，而 Sana 还醒着，头靠在他肩上。叙述者感知到房间里多了一个存在：

> N: But there is a presence in this room.
> N: A fourth one.
> N: That's either been here for some time or crept in when I opened the door.
> N: It wears the same dress she does.
> N: Whispers things into my ear that come out garbled.
> N: Gargled.

Sana 线在无人退场的房间里收束：

> sa: I love you.
> sa: There...
> sa: *I* said it this time.
> sa: You and me...
> sa: Will be together forever...
> sa: No matter where...
> sa: No matter when.

## 三、lust 线概貌

Sana 的 lust 内容有三层容器。第一层是菜单：sanainvitegen 的 sanainvmenu 把 Hang Out（→ sanainviteaff，标注 Raise Affection）、Thighjob（→ sanainvitethighjob，Raise Lust）、Cowgirl Sex（→ sanainvitecowgirl，Raise Lust，需 `christmalloween6 == True` 才出现）、Headpat（→ sanaheadpat）四条并列，把情感与欲望明码标价。第二层是各 bar 事件末尾的分流：bar15、saramissionaryanim、bar50 在 bonus 分支下分别跳 sarabarfirstx、saramissionaryanimx、funnydildox，全部落在 `animatedscenes.rpy` 与 `inappropriatecontent.rpy`。第三层是本文件内直接写出的性行为场景：sanainvite2（客厅初夜）、endofsanasexnaming（海滩公共区域）、以及 sanaspring3（万圣节之夜的口述与补完）。

lust 线在功能上是一台可无限重入的往复机：sanainvite2 的结算文本明说"you can invite her over whenever you want now!"，并用 affection/lust 两条数值条替代情感进展（`sana_love += 1`、`sana_lust += 1`）。

真正值得注意的是 lust 线对人物的反写功能。传统 galgame 里羞怯角色的欲望爆发是奖励，而 Sana 线把它写成了病理报告：她的索求语言充满自毁词汇——sanainvite1 里她进门第一句就是 "You can go as hard as you want without having to worry about my safety."；sanainvite2 里她说 "This might be putting it lightly, but I want you to *destroy* me."；sanaspring5 里她给自己的诊断是 "I'm an insatiable pervert and sex-addict in training."

内射那次（sanainvite2）她给出的理由是 "Are you trying to turn me into my mom?!"——恐惧直接指向母亲，而不是指向道德。sanaspring2 里叙述者已经把她的突变摆成两个互斥解释——"要么她吃下了我的一部分……要么她被附身了"——而这条疑问在此后的任何事件里都没有获得裁决。

## 四、与主线/元叙事咬合点

1. **pareidolia 的官方注册地**。神秘叙述者在本线 ayanesanabeach4 中正式自报姓名 "you can call me pareidolia"，并完成三项声明：随时间变强（"i become stronger. i become capable of more things"）、并非唯一成长者（"i'm not the only one growing"）、自称要"使用"玩家且"只有我想把你用在好的地方"（"for i'm the only one who wants to use you for good"）。它也是本线唯一一处直接对玩家发言、并声称能改写画面的实体。
2. **q 的三次现身与一次转述**。ayanesanabeach2 里她冒充 Sana 并与 Sensei 长谈；ayanesanabeach4 里她以巨体形态发出命令式宣言，并在同一场里由 pareidolia 接续自名；sanaspring4 里她先在夜路上以 "Psst" 现身搭话，随后在异界打断 Pegasus——"You shouldn't listen to him. He's lying to you."。此外 bar30 里 Sana 转述过"那个白头发的女孩"的话（"她说你见到了 God"），说明那次相遇留下的记忆在角色之间是共享的。它对世界规则的透露密度（记忆不应留存、时间双向流动、平行宇宙的他者）冠绝各角色线。
3. **Sensei 的断片被命名**。"thingamajigs" 一词由 q 说出（"Another one of your thingamajigs. You walked off to find Sana and, somewhere along the way, your mind went blank."），把主线反复出现的黑屏走神从氛围升格为机制。
4. **对玩家的直接喊话**。ayanesanabeach4 里 "it is of utmost importance that you IMPREGNATE AYANE"、pareidolia 操纵屏幕（"i'll be turning your screen black now"）与收尾的 "this is all in your head. nothing is real. you have to trust me."，以及 sanainvite2 结算时的 "You aren't meant to be together! She's merely doing her job."，都是越过第四面墙、把玩家钉在共犯席上的元叙事动作。
5. **shapeshifter 嫌疑人名单**。q 点名 Ami 与 Niki 为最可疑的模仿体，并且明确把 Sana 排除在外——"那些我会从她们两个开始，而不是那个有不良习惯的矮个子安静女孩"。
6. **重置循环层的证词**。bar45 里 Sana 记得一次"根本没发生过"的过夜；sanaspring5 里 "Would you believe me if I said we've been here before?" 与 Yumi 的时间觉知对话；sanaspring6 结尾的"第四个存在"与 garbled 耳语——循环层的泄漏已经从环境异常升级为人格级入侵。
7. **梦境异界与 Head Office**。sanaspring4 的 Transpacific Sadness Symposium、Knife Boy 提到的"several high-ranking gods from the Head Office"、Kaori 的 erase 判决，展示了一个凌驾于校园之上的官僚化神界，与主线中的"神"概念互相指涉。

## 五、未解伏笔

1. **生父之谜**。bar40 里 Sana 说父亲年纪比母亲大很多、不忠、在她出生后母亲才发现他另有女人；bar20 里 Sara 承认自己高中时和老师有过一段秘密恋情。两条信息从未在文本里被确认为同一个人，那具从未露面的身体仍只有一个轮廓。
2. **Shota 的死因与规则**。哥哥怎么死的、Knife Boy 说的 "Mom broke the rules" 究竟指什么——Sara 极力掩埋的过去至今没有下文。bar50 里叙述者一度猜测"如果她哥是在回家路上被杀的"，但那只是他的推测，没有任何角色确认过。
3. **q 拒绝变成 Ayane 的原因**。"Don't like feeling what she feels."——Ayane 身上有什么感觉是它不愿承受的？
4. **附身还是成长**。sanaspring2 的 "Either that or she's been possessed." 从未获得裁决；电影之夜被那一眼打断的亲吻、Halloween 的断片，都是悬案。
5. **花之名**。"Name me after your favorite flower."——q 得到名字了吗？这个名字与后续任何花意象是否同源？（sanaspring6 结尾闪过 threeflowers 画面。）
6. **未来之家**。蓝橱柜、棋盘格地砖、警告"不要离开"的 PA 广播究竟是预言、记忆还是循环的样板间？（sanaspring1 里 Sensei 说这是"梦"，也可能是"妄想"。）
7. **Halloween 之夜的真相**。Sensei 当晚 "blacked out"，而 Sana 说他"一直在跟一个根本不在的人说话"，完整事件链仍缺失。
8. **sanaspring6 的第四个存在**。穿同样裙子、耳语 garbled/gargled 声音的身影是谁？"IT COULD'VE BEEN ME" 的主语是谁？
9. **Yuki 的癌症**。诊断由 Sensei 在 sanaspring5 说出，与时间觉知对话同期出现；疾病是否也是世界故障的一种表现，源文没有回答。
10. **Sana 与 Ami**。sanainvite1 里 Niki 追问之下，Sana 说"Ami 愿意的话我不介意和她交往，只是想慢慢来"；sanaspring2 里 Ami 在课上发表"要把其他女生肢解掉"的演说。这两条线至今没有交集。
11. **bar45 的记忆分歧**。Sana 记得的过夜与 Ayane、Sensei 的记忆不一致——究竟是谁的记忆被改写，还是被重置抹掉的那一次另有版本？

> 按 label 检索本角色全部事件，见 `索引/Sana索引.md`。
