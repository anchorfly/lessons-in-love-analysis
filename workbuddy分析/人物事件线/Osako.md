# Osako 事件线全析

> 源文件：OsakoEvents.rpy ｜ 共 19 个 label（14 个剧情 label：osakodojogen、osakodate1、osakodojo1、osakodate15、osakodate20、osakospring1～osakospring9；5 个路由 stub）
> 取实原则：源文中 `if bonus:` 一类双分支只取实际发生的一侧作为事实依据，另一侧不录入。
> 定位：全作少有的、按常识运转的成年人视角。她是 Wakana Watabe 的同居伴侣、空手道教练，也是 Sensei 身边唯一会对他动用物理手段、并且唯一听他亲口承认掠食行为的人。她的线讲的是"一个把自我全部押在伴侣身上的女人如何练习成为自己"，并在一场没有得到回答的求婚与一句 "Wakana, I want kids." 上收束。

## 一、角色基本盘

- **全名 Osako Osaka**（osakodate20 里 Maki 当着 Sensei 的面报出："I never forget a customer, Osako Osaka."）。与 Wakana Watabe 自大学时代起相恋并同居：osakodate1 中她说"I swore back in college that I'd protect her for the rest of my life, even if she didn't want me to"；osakodate15 里她回顾"As soon as I started seeing Wakana, I barely even {i}talked{/i} to anyone else anymore"。
- **职业**：空手道教练，同时在女仆咖啡店打第二份工（osakodate15）。Sensei 的旁白猜测她留着女仆这份工"only keeping to satisfy some sort of sexual desire"——这是叙述者的推测，不是她的自述。
- **身体资本**：先练踢拳、后转空手道，腿法是其专长（osakodojo1："I used to kickbox before starting karate, so I've always considered anything involving legwork my speciality"）。她反复宣称掌握七个能一击致死的压迫点：osakodate1 里是"seven different pressure points on your body that could kill you instantaneously"，osakodojo1 里落地后改成"One of seven ways I know how to kill you in one blow"。
- **竞技梦碎于封锁**：她本想打到全国级别（"Always wanted to try doing something on a national level because I'm definitely good enough"），但"But now that no one's allowed to leave Kumon-mi, that path just...isn't possible anymore"，且看不出城市会很快开放。她对运动员年龄窗口算得很清楚——"The most important resource for pretty much all athletes is our age"——并预计等城市重开时自己已超龄，"I'll be stuck teaching beginners until I can't move my body anymore"。
- **性格两面**：表面毒舌、动手先于动口，暴力对她近乎亲昵（osakodojogen 里她把 Sensei 摔在垫子上坐了整整二十分钟）；内里是长期的低自尊与分离焦虑，她自己说得明白："Just being strong physically doesn't make me strong as a person... I'm actually annoyingly sensitive when it comes to stuff like this." osakospring4 里她给自己下的诊断是"the one with less self-confidence than a rabbit being chased by a fox"。Imani 说她"radiate bottom energy"（osakodate20 转述），她回一句"Takes one to know one"，并未否认。
- **核心弧线**：从"Wakana's Osako"走向自塑。osakodate15 里 Sensei 第一次点破："It just sounds kind of like you stopped existing as {i}Osako{/i} once you met her. Now you're just {i}Wakana's{/i} Osako."她承认这是"my greatest fear of all"，却拒绝因此改变（"fear is something that is meant to be confronted, not avoided"）。osakospring4 她启动"Osako 2.0 — the new, confident and cool model"，目标是"one whose existence doesn't entirely revolve around her partner"。osakospring5 里她对 Noriko 说出一个更朴素的版本："feeling a little more like...someone who doesn't solely exist for someone else would be nice."osakospring6 里她报告了这条路上唯一的收获——学会享受失败："I kind of like this feeling. Failure."
- **社交史**：高中时朋友全是社团里的，大学开始和 Wakana 交往后社交圈收缩到只剩她一人（osakodate15）。osakospring9 里她自己总结困境："it's like my existence is just intrinsically tied to all of you guys"。
- **与 Sensei 的关系是本线的暗骨**：起点是她口中"some asshole-ish creepy guy flirting with the rich girl at my karate class"（osakospring6 原话）；osakospring4 两人把话挑明（Sensei："I {i}want{/i} to be closer."；Osako："Let's...hang out more."）；osakospring6 她成为那个听他亲口说出"Getting a new hobby won't stop me from preying on teenagers, Osako."的成年人。
- **她是怎么进入《The Girl Who Cannot Breathe》的**：靠 Wakana 的痴迷阅读。osakospring2 她说"I've heard basically everything she's ever written now thanks to Wakana"；chap4 的 springtime9 里她补上一句"I read her poetry too, you know? {i}With{/i} you."这部诗集的作者即 Ami 的母亲，其中反复出现一个只被称为"Boy"的形象（chap4 的 springtime9 里 Wakana 说明："There was a recurring subject in the early works of the Girl Who Cannot Breathe — a child known only as 'Boy'"）。她因此成了恋爱层与"作品内作品"之间的那根线。

## 二、love 线逐事件脉络

### 路由 stub（5 个）

osakodojo、callosakomorning、osakodive、callosakoafternoon、callosakonight。前两个是按时间与章节状态分流的道场/电话入口（osakodojo 依 osako_love、章节标记分别跳转到 osakodojo1、karinspring4、osakospringdojogen、osakosummer2dojogen 或 osakodojogen；osakodive 一律跳 osakospringdivegen）；三个电话 stub 在 senseisad 时由 Sensei 主动挂断，否则拨号无人接听、退回原菜单。均无独立剧情。

### osakodojogen — 道场喜剧开场

Sensei 承认自己来道场不是练空手道，而是"slack off and closely monitor all of the girls actually trying to learn a martial art"，指望撞见走光。Osako 的执法方式是当着全班把他摔在地垫上、坐满二十分钟，之后放他一马，直到抓到他盯着她看，便判定"my punishment is nowhere near complete"。这一场确立了她的教学人格：暴力即亲和，且她的暴力有明确的针对性——专门用来惩罚注视。

### osakodate1 — 周年纪念夜谈

起因是 Wakana 第一次主动联系了 Osako 以外的人（"It's the first time Wakana's ever gone out of her way to contact anyone who isn't me"），而那个人是 Sensei，于是 Osako 在周年纪念日当晚把他叫出去"谈谈"。走到便利店之前，两人已经把话说到了本线的核心：

> o: I'm totally in love with Wakana and, despite her tendency to repeat the same thing over and over and over, she's always been a little unpredictable.

她坦白大学时就发誓要守护 Wakana 一辈子"even if she didn't want me to"，并承认自己"a little...defensive"，"Not just with myself but with anything I want to protect"。真正让她不安的是 Wakana 对 Sensei 热络得太快——"Wakana warmed up to you almost right away. Way quicker than she did with me"。她把恐惧说成两件：怕被"偷走"女朋友，更怕 Wakana 自己发现她想要的是别的东西。Sensei 反问：既然真的在乎她，难道不该希望她弄清自己到底想要谁？她的回答是把两件事分开——"I do. But that doesn't mean I'm not going to worry about it as well"。末尾她给出那个判词般的自我描述：

> o: I guess I just think everything right now is a little too good to be true.

便利店内购物段落由旁白收尾：她逛货架的动作"with surgical precision"，说明她常来；而旁白给出一个不设条件的判断——就算两人分手，也能想见 Osako 坐在某处门廊上慢慢老去，脑子里转的仍是 Wakana。临别时她忽然郑重起来，感谢他"being a friend to the girl I love more than anything else in the world"，随即用七个压迫点作威胁收尾——这句话在下一场直接兑现。

### osakodojo1 — 比试、败北与时间循环独白

Sensei 明知她预告了攻击方式（"I'm going to push back on your fist and then attack you from above with a kick"）仍然防不住，颈侧中招倒地，动弹不得。她补上一句"Couldn't? Or {i}didn't?{/i}"，把责任推回给他分心。

倒地之后的闲谈才是本篇的重量所在。Sensei 提到 Touka 家曾想聘请她，她顺势交代了自己为什么留在教初学者：Kumon-mi 没有足够的高级练习者让她以此为生，"so I guess I just followed where the money was"，而她原本的计划是打比赛、"getting better myself instead of helping others get better"。封锁让这条路断了，她把年龄账算得很清楚——每一年都算数，等城市开放时她很可能已经太老。

紧接着是 Osako 线上最锋利的一段旁白。她不知道时间每隔几个月就会被重置、也不知道自己会一直困在与伴侣相同的僵局里，而 Sensei 知道，并且在盘算要不要给她虚假的希望：

> N: I wonder if it's okay to provide someone false hope even when you know things aren't going to work out for them?

他最终选择说"不要现在放弃"。随后那段元叙事独白把个人命运推到普遍命题上：大多数梦想会永远悬浮、永远不获实现，幸运的人提前明白这一点，改立能在更短时间内完成的 goals，"Then, sooner or later- We'll have everything we've ever wanted. The fortunate ones, I mean."其余的人呢——"Maybe they'll be rewritten into someone with a little better luck?"。"被改写"一语正踩在重置机制上。

### osakodate15 — 女仆店与 Hallelujah

Osako 的女仆打工以失败开场：她不肯叫"Master"，"flavor beam"做得敷衍，自己承认对别的客人还算像样，唯独对 Sensei 服务不来——"There's just something about the idea of acting that way to you that makes me throw up in my mouth a little"。Uta 与她一唱一和，用"grandma Osako"把她激到赌气答应下班后同去卡拉 OK。

卡拉 OK 包厢里，她坦白自己几乎不认识榜单上的任何歌——高中时间全给了空手道，大学时间全给了 Wakana，而 Wakana 也不怎么听音乐。她顺势交代了社交史：高中"had a good amount of friends...but they were all, like...club friends. Not people I spent any free time with"；大学"As soon as I started seeing Wakana, I barely even talked to anyone else anymore"。

由这段自述，Sensei 抛出本线的主题句：

> s: It just sounds kind of like you stopped existing as {i}Osako{/i} once you met her. Now you're just {i}Wakana's{/i} Osako.

她承认这是"my greatest fear of all"，但拒绝因此重写自己："fear is something that is meant to be confronted, not avoided"，并且现在的她——"codependent or not"——是她有过的最快乐的版本。她还反驳了"错过"这个前提：那些别人眼中的"fun stuff"，对他们两人从来就不构成选项。

结尾她拿起麦克风，唱了歌单里她唯一认得名字的那首《Hallelujah》，而且是用尽全力在唱。Uta 说"我得去还录像带了"，Sensei 说"我陪你"，两人中途逃场——喜剧收尾之下，这一场真正的落点是：一个几乎不拥有"自己"的人，在人生里唯一能拿出来的独唱曲目，是一首关于失落与残缺的歌。

### osakodate20 — 成人用品店的秘密

在 Maki 的成人用品店里，DildoSaber 的推销闹剧铺满前半场：七色灯光、App 控制、可当防身武器，Osako 全程抗拒（"I don't want the fucking DildoSaber!"）。Maki 一句"I never forget a customer, Osako Osaka."点破她是常客，Osako 随后也承认自己最近一直在刻意回避这家店。

两人走到店外墙边，Osako 在三个条件（不许告诉 Wakana、不许下流、不许再问性别刻薄问题）之后交出秘密。她把问题包装成"输赢"：她每次想主动改变格局，Wakana 就"pulls out an Uno reverse card on me"，转眼又变成 Wakana 在"赢"——"Or I guess...{i}losing,{/i} by most people's standards"——她只想让 Wakana 也"赢"一次，觉得这样不公平，可 Wakana 从未流露过要改变的意思。她随即自我诊断："You know I've got some...dependence issues...and confidence issues"，"I just can't help but feel like I'm doing something wrong"。她说自己已经问过 Wakana，得到的答复是"it's no issue at all"。

Sensei 给出的建议意外地克制：既然当事人已经这么说了，那就"no issue at all"；"the only person you can work it out with is them"，而且"there isn't a single sex toy out there that is going to just magically quell all of the worries you're burdened with at the moment"。散场前 Osako 说了句真心话——"God, I hate having no one else to talk to sometimes"——随后被 Maki 以"这个东西要是被你看见，会改变你对女人的全部认知"为由带走，Sensei 被留在店外。

### osakospring1 — 昏迷后的电话：把人打醒的开端

Sensei 从昏迷中醒来后长期蛰居家中。开场旁白用一整段复沓写他的低落：Ami 不再给他做早餐、不再笑，家里没人知道清洁用品放在哪里、哪种清洁剂该用在浴室瓷砖上，"It's fine, though"反复出现作为句号。

Osako 从 Wakana 手机里偷来他的号码打了过来——"I kind of stole it out of Wakana's phone while she was in the shower this morning"——并且明确要求瞒着 Wakana（"Because I don't want her to know about this"）。她把他叫到当天没有课的道场，二话不说痛打一顿，打完说：

> os: Okay! I feel better now.

她承认这一顿里有一半是为了泄自己的愤（"the reason I went so hard on you today was to get some of my {i}own{/i} anger out"），但当 Sensei 说"我既应得也需要这个"时，她反而觉得无趣——"punishment's only punishment if the person being punished hates it"。于是对话转向剖析：

> s: But that's where we're different. You feel sorry for yourself because you're insecure. I {i}don't{/i} feel sorry for myself at all. I {i}hate{/i} myself. And pretending I {i}don't{/i} makes me feel even worse.

> s: I was {i}trying.{/i}
> s: And just when I felt like I was finally starting to {i}do{/i} better, I was punished for it.

他把自己形容为"reduced to a pawn in some...divine game of chess"。Osako 的应对始终不是安慰而是继续动手，问他要不要再挨一脚，他答"我觉得挺好"。本篇确立了她在全作里的独特位置：唯一会用物理手段对待 Sensei 的成年人，也是唯一不把他当病人哄的人。

### osakospring2 — 美式餐厅：Wakana 在查你

痛殴之后她宣布"I'm kidnapping you"，把他拖进一家连菜单都全是英文的美式餐厅（她解释这是被 Wakana 训练出来的策略："just start picking the first thing I see"）。她替不吃东西的他点了一份猪排套餐并推过去。

正题是 Wakana。Osako 说，自他昏迷以来 Wakana 一直在追查成因："She's scoured like, every single poem your niece has ever written. To the point where even {i}I've{/i} memorized a few of them. And she's starting to sound like some kind of...conspiracy theorist."她本以为他醒来就能结束，结果"Almost nothing's changed"，Wakana 仍然几乎每晚都在拼凑线索。Sensei 承认这事更早就有——"She's been poking her nose somewhere it doesn't belong for a while now"，他在自己出事前已经表达过不适，Wakana 道过歉，他以为她放下了，没想到她把 Ami 也拖了进来。

Osako 顺带把 Wakana 的思维方式讲清楚：学校里看着一板一眼，但遇到弄不懂的东西就会"throws herself at it. Hard. And recklessly"，而且大多时候真能搞明白——"But not this time"。连她都开始猜测 Ami 是不是早就知道、甚至希望这事发生。

谈话转向 Sensei 的自白。他把与 Ami 的关系定性为"codependent"，说她幼年失去父母、自己当时状态很糟，"it was more like {i}her{/i} taking care of {i}me{/i}"；如今 Ami 是他唯一抓得住的东西（"For the first time ever...I feel like I have a purpose"；"Ami's the ledge I'm hanging onto now"），因为他若放手，她会跟着跳下来。接着便是那句判决：

> s: She doesn't deserve to suffer over the choices I've made. She's worked hard and deserves a good life.
> s: She's just broken.

他接着抱怨——若 Wakana 还要继续翻 Ami 的诗、"invading her privacy by dissecting her most personal feelings"，那他——话没说完，Osako 插进来追问："is that really what they are?"并直接把问题挑明：万一 Ami 只是在做她母亲做过的事？她提了书名。Sensei 当场翻脸：

> s: Don't talk about her.
> s: {i}No one{/i} can do what she did.

离店时她喊出关键一问："You're the 'Boy,' right?! The one she always wrote about?! That was you! Wasn't it?!"他沉默。她于是给出安慰——"She can't hurt you anymore... It's over."他答"不，没有结束"。

本篇结算罕见地注明"Osako's affection has increased by 10! But maybe it's just pity!"。随后系统文本宣告"[[DEPRESSION] has worsened"、"He has learned [[GREATER FACADE]"。夜里旁白否掉了她那句安慰：他躺下时"她"就在身边，用食指指甲在他胸口画圈；他什么也感觉不到，却记得从前她把指甲咬得太短、画着同样的圈时划出的血。这段落为"她还能伤人"提供了叙述者层面的证据。

### osakospring3 — 教练办公室：建议你试一次男人

开场是 Imani 与 Wakana 在办公室谈运动会安排：1-A 班被其他班级集体拒绝同场竞技，只能"与自己比"，Wakana 让 Imani 自己想办法，并把"别在有成年男人旁观的情况下走光"作为唯一附加条件。Imani 摔门离开后，镜头转到办公桌下——Osako 正在给 Wakana 口交，而且已经做了约三十分钟。

这场戏表面是情色喜剧，实际是一次关系危机的当庭审理。Osako 一开口就问："You're not enjoying this at all, are you?"她分不清是 Wakana 湿了还是只有自己的口水；Wakana 先玩笑（"Can you not tell by how wet I am?"）、再安抚（"If I wasn't enjoying it, I'd simply close my legs and crush your skull"），最后给出实情：因为旧伤，"It's just harder for me to {i}finish{/i}"，"Orgasms just...they're rare. But just because I don't always {i}finish{/i} doesn't mean I'm not enjoying what we do"。她还说今天叫 Osako 来，本就是为了补偿自己近期的疏忽，因为 Osako 喜欢在半公开的地方做爱。

Osako 不接受这套解释，积怨从"我碰不到你"一路升级：

> os: Like what if you're not actually as into girls as you think you are?

> os: You've never tried it before, Wakana!

Wakana 用同一套逻辑反击："You've never fucked a man either, Osako. Does this mean {i}I{/i} get to start accusing {i}you{/i} of depriving yourself of a more ideal future..."，Osako 以"我不被男性吸引而你被吸引"自我豁免。在 Wakana 逼问"Say it out loud"之后，她说出"I think you have to try it at least once"，Wakana 的回应是把它翻译成另一种罪——"By assuming I've just decided to {i}settle{/i} for a woman? By acting like you know what's better for me than {i}I{/i} do?"——随即下逐客令。Osako 道歉，Wakana 给出最冷的一句：

> w: It {i}sounded{/i} like you were content with just...giving me away to someone else.

她问今晚还回不回家、能不能再谈，Wakana 说"我会下班后打给你"。结算："The couple's mutual affection has decreased by 5!"。这是两人裂痕在数值上的第一次落地。

### osakospring4 — 新发型与 Osako 2.0

Osako 剪了短发。Sensei 立刻把它读成"a breakup move"，她半否认——"Sometimes, a girl just...wants to change up her look"——但随即承认两人现在只是"kind of together"："We're still living in the same house and sleeping in the same bed, but...there are some things that have to change"，而需要改的"mostly on my end"。

于是有了"Osako 2.0"：

> os: So I've started working on Osako 2.0 — the new, confident and cool model who will be able to give her partner tons of love and tons of orgasms.

> os: Regaining my confidence is just one step on the way to a new me — one whose existence doesn't entirely revolve around her partner.

她承认这个动作的动机正是 Sensei 在 osakodate15 说过的话——"has just finally weighed on her a little too much with some of the things I've been saying to her"。至于怎么做，她毫无头绪："All I do apart from letting Wakana put stuff inside me is work. I think I need to...find a hobby or something." Sensei 能提供的唯一共同点只有色情片，于是三人（Osako、Sensei、Maki）聚在 Maki 的"MILF of the Month"俱乐部看本月明星 Reiko Kobayakawa。

观影间隙的对话才是重点。Sensei 说和她在一起很放松，因为"everyone else I know wants to sleep with me"；并第一次把友谊的要求说出口——"We {i}can{/i} be closer. I {i}want{/i} to be closer."被追问动机时，他给出的理由是共犯式的：

> s: It's about me being in the same boat as you. Just instead of it being a relationship that's teetering on the edge, it's everything about me.

Osako 从"你只是在蹭接近 Wakana 的机会"一路退到接受——"No, dude...I appreciate it"，并承认自己判断不了他什么时候是认真的。篇末旁白给出全线最温柔的一句注脚：

> N: But she falls asleep holding someone who sees her, and I fall asleep holding myself.

### osakospring5 — 女巫夜课：互相拖下水

Osako 报复性地拖 Sensei 去市区社区大学上巫术课——"it's {i}my{/i} turn to subject {i}you{/i} to something you're likely going to hate"。课程内容是水晶在法术中的用途、如何在圣坛与晶格上摆放，末尾还有一点占卜与能量疗愈。她自己先声明："I don't like this stuff. I know nothing about it."

课上撞见 Noriko 与 Kirin，后者用假名报名："Stacy Fakename. Eighteen."（同行的 Noriko 被她登记成表亲 Joanna）。Kirin 把 Osako 的气质比作 Otoha，Osako 的回应是给自己定位："I'm just, like...Girl C...a background character. There's nothing about me that really stands out."她还说自己高中活跃在社团、但绝不是那种受欢迎的人，"I didn't even really start {i}thinking{/i} about romance and stuff until college"。

Noriko 顺着这个自贬给出了本线的主题提法：

> n: It's not unheard of for side characters to get spinoffs where {i}they{/i} get to be the star!

Osako 接过去的话朴素得刺人：

> os: I don't know if I'd say I'm trying to become the {i}main{/i} character. But feeling a little more like...someone who doesn't solely exist for someone else would be nice.

Noriko 断言这两人能彼此救（"both of you can help each other"），Osako 答"Because we both clearly need it"。中间还有 Osako 对 Noriko 与 Sensei 关系的一句准确的刺穿——"Something tells me you'd have turned out just fine with {i}or{/i} without him"。一行人最终因扰课被讲师当场逐出教室，占卜环节没能上成。

### osakospring6 — Sara's 酒馆：掠食者的自白

夜课失败后两人转去 Sara 的酒吧。Osako 先报告新学到的能力——享受失败：

> os: I kind of like this feeling. Failure. Trying things out and then looking back on them and thinking it was funny I ever expected it to work in the first place.

她说这次尝试"isn't really about Wakana. Or love. Or...security or stability"，而是"about {i}me.{/i}"。随即把这句话递回给 Sensei：

> os: Akira.
> os: You're not a failure.

她说自己已经和 Imani 谈过，知道 Sensei 在考虑离开教职，并给出一条她自己的准则："If I had to choose between my own personal happiness and the dojo, I'd choose myself every time."她明确说过自己不介意——"walking away from something because it's what's best for {i}you{/i} doesn't make you a failure"。但当 Sensei 绕回"我走不掉"时，她点破了另一层：他之所以肯帮她，恰恰是因为这给了他一个不必改变自己的借口——"I pity the type of mind that can see what needs to be done to enact the changes you need and just...not even make an attempt to do the same."

于是有了那句无法收回的话：

> s: Getting a new hobby won't stop me from preying on teenagers, Osako.

她的反应分层呈现了一个正常人接住这种真相的全过程。先是同时出现的两种情绪："I'm both proud of you and hate you for admitting that at the same time."然后是告发的代价——"Do I side with my morals and do what's right? Do I ruin a friend's life and, by extension, ruin a bunch of other lives in the process?"，具体是"a girl would lose her father a {i}second{/i} time. My partner would lose her best friend. My {i}other{/i} friend would lose the man she's rapidly falling for"，末了才用玩笑兜住（"worst of all, {i}I'd{/i} lose my witchcraft buddy"）。她还说自己早有预感："I had a thousand red flags to soften the blow. I'd just hoped it would never be something that became so {i}real.{/i}"最后是最诛心的诊断：

> os: They like you more, so they're giving you every benefit of every doubt that has ever existed.

Sensei 随即宣布"我想我会辞职"，她把界线划得很清楚："They're important to you...and that's okay. It's everything else you're doing that's not."离场前两人约定继续一起上课："This doesn't have to just be for me anymore. We can figure shit out together."

归途插入一段刺目的意识闪回：夜色里传来 Kaori 与 Nao 的日常说话声，他意识到自己夺走了 Nao 的第一次之后几乎没再看过她——"I took her first time and have barely looked at her since"，"She probably doesn't even realize what happened"，最后一句是"One more word and I would have kicked down the door."

### osakospring7 — 道场避难所：Niki、Ayane 与母亲的课题

Sensei 刚与 Imani、Rika 三人行完（Osako 的开场白：你刚和 Imani、Rika 上了床，从烘干机里捞起裤子就直奔我这儿），逃到道场求庇护兼求建议。本篇信息量最密。

关于 Niki：Osako 说她是在酒吧听说那件事的——"I'm talking about your fucking idol ex-girlfriend and how she caught you screwing her fucking sister"——而且 Niki 是当着她的面说的；两人就此结识，"we created a new martial art just to get back at you"。她追问："{i}Do{/i} you feel bad, Akira? Or are you only just saying that because you were caught?"Sensei 答"我本来就想被抓"，她先是以为在开玩笑，听完他解释 Niki 从小就为他放弃整个人生、分手后反而成了世界级偶像，她反问了一个他答不上来的问题："What does it matter how much a person can accomplish if they're miserable while doing it?"

关于是否坦白：她拒绝替他拿主意（"I can't tell you whether or not it's a good idea to burden anyone else with the information you have bestowed unto me"），只提醒他这两人其实已经半猜到了（"It's honestly miraculous those two haven't {i}already{/i} figured it out"）。而在他自陈"想要的东西到手了还是停不下来"之后，她给的命名是："I'm pretty sure they call that 'addiction' in the real world."

关于 Ayane：她报告 Ayane 近来几乎不来道场、来了也魂不守舍，并给出判断——"either she's given up on hiding it, or it's just so powerful that she {i}can't{/i}"。Sensei 顺势推她去当那个角色：Ayane 没有母亲、唯一接近母亲的人"already belongs to someone else"，而 Osako 是"a cool, older woman who knows her and teaches her about things"。她的第一反应是划清界限——"I teach her self-defense. That's not even remotely similar to motherhood"——被追问后说出真正的抗拒：

> os: I don't think I'm really cut out for, like...{i}motherly{/i} stuff if that's the role I'm supposed to be filling right now.

Sensei 回"我觉得你会是个好妈妈"，她用那个只有读过诗集的人才叫得出的称呼回敬：

> os: Yeah, because you know all about proper parenthood, {i}Boy.{/i}

这句话触发了一组闪回画面（源文在此连续闪过 yasumcdonalds 系列的两帧背景后又切回道场），随后她说自己也说不清，只希望 Ayane 快点好起来。本篇同时搭起两条线：Ayane 缺一个能说话的成年人，以及 Osako 自己对"母亲"这个位置的抗拒与未承认的欲望。

### osakospring8 — 花束与空床：Ayane 的"丢了什么"

Osako 提着便利店买的花束登门，Ayane 甚至不知道她怎么找到的——"Akira told me after I asked him what was going on with you. And don't give me {i}too{/i} much credit for coming since he was the one who ultimately pushed me to do this"。她把礼物解释成朋友教她的习惯："A friend of mine got me into the habit of trying to cheer people up with gifts."

Ayane 对自己的状态给出了一段极其精确的描述：她确证这不是通常意义上的抑郁（"I'm definitely depressed...but I don't have depression"），而是

> ay: that feeling you get when you hop off of a train and keep thinking that you accidentally left something behind.

她补上更关键的半句：

> ay: But the weirdest part is that I feel like I've felt this way before. That I've had this exact conversation before. Just with someone else where you are now.

她还说自己像是忘了"怎么快乐"，连想到快乐都会内疚；房间里贴满了她偷拍的 Sensei 睡照。Osako 承认自己也有同款空洞——"I'm the same way too, you know. Just with {i}purpose{/i} as a concept"。

话题随后滑向生育。Ayane 问她想不想要孩子，她先用"我不可能是母亲，我对小孩一窍不通"挡，Ayane 指出那是另一回事（"You can be horrible with them and still want them"）。她于是层层加码：不自信、孩子会彻底改变生活、以及最关键的一条——Wakana 讨厌小孩，"She'd never agree to this. She'd be signing her life away, and I don't blame her for that at all."Ayane 当场拆穿她的回避方式：

> ay: But...they {i}want{/i} it to happen. And you still won't even say that.

她沉默后吐出半句，然后逃走：

> os: But in a perfect world...
> os: Where none of that is true...
> os: Where it's no longer impossible...

Ayane 临别还想把话说完——"If you {i}do{/i} want to be a mom...but Miss Watabe {i}doesn't...{/i}maybe you two are-"——被她直接掐断："Actually, on second thought, I don't think I should hear this."门关上后，Ayane 独自对着空房间说：

> ay: Thank you for the flowers...

### osakospring9 — 求婚与悬置的答案

开场旁白用"吃飞机的法国人 Michel Lotito"写 Osako 的心脏下沉：这位法国艺人花了两年吃掉一整架 Cessna 150 飞机，靠的是异食癖与消化金属的能力；旁白把这个怪喻接到 Osako 身上——"And this is where the French and Japanese part ways. Because Lotito would have said the thing. And Osako would have chickened out and just gotten the surgery."她心里仍有一部分在问：如果不把那对翅膀烧掉，它们能带她飞多远。

她回到与 Wakana 同住的公寓，手里还替 Wakana 取了处方药。屋里有烛光晚餐、Wakana 穿着礼服等着她——是她们的结婚纪念日，而她忘了。Wakana 说这顿饭靠的是一位与 Akira 某个学生有关的校友的人情（"I just looked up a certain alumni with relations to one of Akira's students"），搬家具、送酒的事则由 Tsukioka 家的仆人代劳。

晚餐谈话把前面几场全部回收了一遍：Wakana 问她去看 Ayane 的结果（她转述 Ayane"feels sort of like she lost something"，Wakana 评"How very {i}teenager{/i} of her"）；处方药是她进门第一句话交代的（"I stopped by the supermarket on the way back to grab your prescriptions"）；提到 Osako 的巫术课与 MILF 俱乐部时说"you're trying at least. And I'd be lying if I said I wasn't proud of you"；还提到 Rika 事后发来的几条醉后短信，以及 Ami（她称其为"Arakawa {i}Jr.{/i}"）居然敢当面说她会是个好母亲。Osako 为自己在 Wakana 沉迷诗集那阵子不够耐心而道歉，并许诺"我会做得更好"。她也再次说出现在的困境：

> os: It's like an annoying gossip paradox. I think I just need more friends.
> os: The way it is now, it's like my existence is just intrinsically tied to all of you guys.

随后 Wakana 因身体无法下跪而请她"假装我跪着"，念诵一段长篇告白（"I don't love you as if you were a rose of salt, topaz, or arrow of carnations that propagate fire. I love you as one loves certain obscure things, secretly, between the shadow and the soul."），并说要成为"the nightshade that both cures you and kills you"。接着是：

> w: No matter who you become and what you resemble when you emerge from this cocoon, my love for you will not fade. It is impossible for you to not be beautiful to me.

> w: I humbly ask you to spite the Japanese legal system with me and become my bride.
> w: Osako, will you marry me?

四行省略号之后（Wakana 说"You're not answering."），Osako 给出的既不是 yes 也不是 no：

> os: Wakana, I want kids.

> w: Oh.

画面随即切入 "fin"，本 label 结束并跳回章节日程。她的答案被留在了源文之外。

## 三、lust 线概貌

Osako 线的情欲内容集中在三处，全部服务于关系叙事而非奖励回路。

其一是 osakodate20 的成人用品店：DildoSaber 的闹剧之下，是一次关于"谁在服务谁"的坦白——她想让 Wakana 也"赢"一次，玩具只是焦虑的替身，而 Sensei 明确否掉了玩具能解决焦虑这条路。

其二是 osakospring3 的教练办公室：一场被打断的口交写成一次失败的谈判，高潮能力的不对等最终引爆"你要不要试试男人"这颗关系炸弹，并以"mutual affection has decreased by 5"落地。

其三是散落各处的身份喜剧：她反复声明对男性零性趣（osakodate1 里"even if I did like dudes, you're too much of a wimp"；osakodate15 里对 Uta 的"还是不是完完全全的蕾丝边"答"Still a lesbian, but thanks for checking"），Sensei 则以"Hey, we both like women, don't we?"自我安慰；MILF of the Month 观影（osakospring4）把三人放在同一间屋子里检验这条边界，结果是她承认 Kobayakawa"really {i}is{/i} hot"，但仍把"和 Rika 上床"当成比"和他上床"更有可能的选项。欲望在本线里始终是测量亲密与权力的仪表盘，不是目的地。

## 四、与主线/元叙事咬合点

1. **正常人的对照组**：osakodojo1 的旁白明确说她"has no idea that time is being reset every few months"，因此她对 Sensei 的每一次反应——愤怒、恐惧、权衡要不要告发——都是在一个被循环扭曲的舞台上按常识做出的反应。
2. **被告知的成年人**：osakospring6 里 Sensei 亲口向她承认"preying on teenagers"。按她自己的判断，同辈成年人中只有她知道这件事——"No one our age knows. Wakana doesn't know. Imani doesn't know. Rika doesn't know. So now {i}I{/i} have to be the one who knows."她的沉默及其理由，构成这条线对故事伦理最直接的质询。
3. **"Boy"与《The Girl Who Cannot Breathe》**：她在 osakospring2 当面指认 Sensei 就是诗集里那个"Boy"，在 osakospring7 用"{i}Boy.{/i}"回敬。她进入这个文本层的路径是 Wakana 的痴迷阅读，而非她自己的经历——这一点让"诗"与"恋爱"两层得以在她身上交汇。
4. **循环的旁观证据**：osakodojo1 的独白里，Sensei 盘算要不要给她虚假的希望，并以"Maybe they'll be rewritten into someone with a little better luck?"点题；她的运动员年龄窗口被封锁一点点吃掉，正是重置机制对普通人生活的静默碾压。
5. **cocoon 意象的跨线共用**：求婚誓词里"when you emerge from this cocoon"用的"茧"，与本作其他线里的同一意象共用一套语汇——naospring1 里 Amber 提出的"茧"交易（"All she'd need to do is survive the cocoon"）、naospring2 里 Sensei 打趣的"hair cocoon"、ayanenew3 与 mikudorm45p2 里用茧自裹的描写、yasuchristmalloween2 里"Others, I feel more like a cocoon"。蜕变与重塑在本作里是同一个问题的不同问法。
6. **Ayane 母职缺口的承接者**：osakospring7 里 Sensei 劝她去当 Ayane 身边那个"可以说话的酷姐姐"，osakospring8 里她照做了（Ayane 亲口说出地址来自 Akira）。而她自己未说出口的育儿欲望，与 osakospring9 里那句"I want kids."指向同一个未落地的方向。
7. **封锁期的设定锚点**："no one's allowed to leave Kumon-mi"是她口中世界物理边界最直白的一次陈述，直接解释了为什么一个够格打全国赛的运动员只能教初学者。

## 五、未解伏笔

- **求婚悬案**：面对"Osako, will you marry me?"，她的回答是"Wakana, I want kids."，而 Wakana 只回了一声"Oh."。OsakoEvents.rpy 到此为止（随后切入 "fin" 并跳回章节日程），这段对话的下一句没有出现在源文中。
- **两人的关系形态**：osakospring3 之后他们仍同住、同床，Osako 称之为"kind of together"，并说"需要改变的东西主要在我这边"。这个"改变"最终走向修复、分手还是第三种形态，源文未答。
- **告发的选项**：osakospring6 里她把代价逐条列了出来（"a girl would lose her father a second time. My partner would lose her best friend..."），但没有做出选择，也没有说要告诉 Wakana 或 Imani。
- **退教的决定**：Sensei 在 osakospring6 说"我想我会辞职"，Osako 的回应是把界线划在"女孩们对你重要，这没问题；有问题的是别的部分"。这个决定是否兑现，源文未交代。
- **诗集与"Boy"**：《The Girl Who Cannot Breathe》的作者即 Ami 的母亲，她在 Ami 失去母亲前后消失（chap4 的 springtime9 里 Wakana 明说"she {i}was{/i} Ami Arakawa's mother"）。"Boy"在书中是被当作"muse"的 recurring subject；Osako 与 Wakana 都指认 Sensei 就是那个人，但这一指认在源文中从未被 Sensei 承认或否认——他只说过"No one can do what she did"。
- **竞技梦**：若城市重开，超龄的她还能不能回到赛场；而在一个会被"rewritten"的世界里，这个问题本身是否有效。
- **七个压迫点**：Osako 多次宣称知道七个能一击致死的位置，并在 osakodojo1 里真的用其中一个放倒了 Sensei。这个数字是夸张还是有实据，源文没有给出验证。

> 按 label 检索本角色全部出场，见 `索引/Osako索引.md`。
