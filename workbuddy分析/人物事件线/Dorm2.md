# Dorm2Events.rpy 重写分析（宿舍二楼事件集，基于 reread digest 全量精读）

文件范围：`Dorm2Events.rpy`。宿舍二楼住户分区：Room 7 = Uta & Io，Room 8 = Nodoka & Otoha，Room 9 = Touka & Yasu，Room 10 = Kirin & Noriko；Molly 与 Tsuneyo 亦居于此层。本层是全游戏"日常表层最厚、meta 渗透最深"的舞台之一：一半是刷好感的房间模板，另一半埋着天坑、重置循环与第四面墙崩坏的直接证词。

---

## 一、群像基本盘

**入口结构**。`dorm2monday` / `dorm2tuesday` / `dorm2wednesday` 是二楼三个工作日入口 hub，按剧情进度切换背景并挂载 Knock on a door、Talk to Molly、Talk to Otoha 等菜单项。走廊初遇事件（以 firsthall 结尾，如 `nodokafirsthall`、`toukafirsthall`）与房间事件（以 dormN、dormgen 结尾，如 `utadormgen`、`toukadormgen`）按好感度解锁；部分角色另设以 hallgen 结尾的走廊通用事件（如 `nodokahallgen`、`toukahallgen`），以 dormgen 结尾的通用房间事件为可无限重复的低门槛模板。

**Room 7（Uta & Io）**。Uta 的房间以"垃圾场"著称——Kirin 口中的"the garbage dump that is Uta and Io's room"。Uta 的家庭背景在本层逐步揭开：为照顾祖父 Ushibori 而搬到 Kumon-mi，另有语焉不详的 "other stuff"（如母亲一系接连的恶疾）；facetime 线（utadorm 中的通话事件）补充兄弟因杀人未遂入狱、亡祖父死于脑癌。Io 则是本层最暗的角色：药物依赖、四个美工刀、对 Uta 救赎性的依附。

**Room 8（Nodoka & Otoha）**。Nodoka 是"天才过载"型角色：连续失眠、咖啡因过量、全知式炫学，其发作演出直接接入 Ami 觉醒同源的音乐与图像资源。Otoha 表面是吐槽役，实际处于严苛的家庭监控之下——父母知道宿舍地址，"一个错误动作就可能一切结束"，她用 "leash"（皮带）自我形容。Otoha 还承担 Rin 线的侧写功能（Rin 对 Sensei 态度特殊、不让 Otoha 参加 Molly 的跑团）。

**Room 9（Touka & Yasu）**。Touka：Tsukioka 财阀继承人，因父亲只有两个女儿而被迫以长女身份继承家业，傲娇外壳下是"想交真朋友"的正常女孩。Yasu：自称天使候补的宗教狂角色，能听见"以太低语"，是 Kumon-mi Academy 天坑的目击者，也是教堂场景 New Hope Cathedral 的解锁人。两人同居本身就是喜剧装置：一个怕黑怕到凌晨三点对着白板耳语，一个是把室友当家具的半昏迷修女。

**Room 10（Kirin & Noriko）**。同日转入的同居组。Kirin：毒舌能量饮料成瘾者，坚称自己"只会有性吸引力、不可能动真心"，实际是自我欺骗大师。Noriko：Sensei 的童年旧识，粉色头发、口袋刀、"疯狂眼神"组合拳，主动承认会尾行 Sensei 回家，是 Maya 公开敌视的对象。两人搬入当天就立下分赃式"契约"：Kirin 得身体，Noriko 得心。

**Molly & Tsuneyo**。Molly 是跑团 DM（"SEVEN VIOLET FUNGUS APPEAR! ROLL FOR INITIATIVE!" 的喊话会穿透墙壁传到隔壁），用游戏内性癖谈论逃避现实，自称 ADHD——"硬盘空间不足所以必须不停删除东西"。Tsuneyo 的宿舍线从勒索/守密事件起步，随后进入"牙齿变成液体"式规则怪谈对话，最终以"为了 Noodles（她与 Sensei 共同命名的鸟）"为由答应保密；她另有 Molly 协助试衣的 cosplay 支线（`tsuneyodorm15`）。

---

## 二、主线逐事件脉络

### 2.1 入口 hub 与通用模板

`dorm2monday`、`dorm2tuesday`、`dorm2wednesday` 构成入口层，内部按条件跳转至各房间事件。通用模板层面，`toukadormgen` 里旁白公然玩弄叙事权："I convince Touka to leave her family and become my sex slave... Just kidding. I never convince her to do any of that."——同一行旁白先写出幻想再亲手撤销，是对"玩家意淫权"的自嘲。`yasudormgen` 则让 Sensei 在黑暗中陪一个微笑站立的女孩坐一晚，并认真怀疑她床底下藏着宗教仪式工具。走廊模板中，Touka 见面第一句是"Please make no sudden movements or I will call the police."，Yasu 的开场白则是传教："Do you have a moment to hear about our lord and savior?"。

### 2.2 Tsuneyo 线（勒索 → 规则怪谈 → 妥协）

Tsuneyo 的宿舍事件以守密/勒索情境开局：Sensei 求她别把独处一事告诉会"处决"他的父亲，她却以"若打破规则，我所有牙齿都会变成液体"这种平静的不可能规则回应，并以"为了 Noodles（她与 Sensei 共同命名的鸟）"为由答应保密，形成一段勒索式妥协。该线在 `tsuneyodorm10` 达到一个小高点，另由 `tsuneyodorm15` 中 Molly 帮 Tsuneyo 试穿亲手制作的角色服装（对应场景图 `tsuneyocos20` / `tsuneyocos21`）的支线补充日常侧面。此线的功能是把"宿舍日常"的地面凿开一道裂缝：在这个世界里，身体的规则本身并不可靠。

### 2.3 Molly 线（跑团、骰子与交易）

Molly 的标志性场景围绕桌游展开：D20 骰出天然 20 时她喊出 "Brigid's bosom, it's a natural twenty"，随后是一场涉及六名女孩紧身衣的交易谈判，合同里带着明显的"wonky barter clause"（不靠谱的以物易物条款）。她的深层动机在自白中说破：愿意"做 virtually anything 来把自己和现实世界隔离开"——跑团、交易、性癖谈论全是麻醉剂。她同时是本层的声学背景板，跑团喊话会穿墙，构成 Room 8 事件的串场笑点。

### 2.4 Room 7：Uta 与 Io

Uta 房间路由器 `utadorm` 按 uta_love 分级跳转。Uta 的背景故事讲述中藏着一处异常信号：Sensei 的话说到一半莫名停顿——"though I'm not sure why"，这是循环层干扰叙事者的典型表现。facetime 事件透露兄弟因杀人未遂入狱（电话那头是"a person who has literally attempted murder"）与亡祖父死于脑癌。Io 的 `iodorm15`是全文件最黑暗段落之一：服药后神志不清的 Io 爬上 Sensei 膝盖，说出 "Because you're my last bastion of hope for adults in this world."，自嘲为"a weightless, overmedicated cockroach with...four boxcutters"；结尾旁白宣判："Io is practically dead already. And there is no one who deserves rest quite like the dead."

### 2.5 Room 8：Nodoka 与 Otoha

`nodokafirsthall`：Nodoka 在读《Lolita》，直问 Sensei 能否爱上远比自己年轻的人，并以"Remember that when the time comes for you to become my own Humbert Humbert."收尾。她还带来情报：Futaba 说 Sensei 曾经是作家。

`otohafirsthall`：确立宿舍"没有规则"的荒诞（Sensei 自己也解释不清为何被雇用）；Otoha 点出 "Rin 对你和对别人不一样，包括对我"。

`nodokadorm1` + `otohadorm1`（搬入欢迎会）：Nodoka 当众"测试"Sensei，把好感度系统说破——"To max out your relationship with everyone around you would equate you to a king... Perhaps even a god."，随即抛出纯 meta 一句："Perhaps this entire world is nothing like either of us perceive it to be?"事后她自称只是在评估 Sensei 误伤女孩们的概率。Otoha 把 Sensei 拉出门解围，并顺势请教 Rin 的感情问题，担忧自己是"I'm just the flavor of the month"。本段旁白留下名句："both smiles are impossible to maintain. Because this world is miserable."

`nodokadorm5`（狂躁发作）：Sensei 独对数日未眠的 Nodoka，她反复念"It's wrong. It's so wrong."→"IT DOESN'T MAKE SENSE! IT IS INCOMPLETE!"。演出层面插入静电音效、闪切图片 `ayhh6`、播放 BGM `amiawake.mp3`（与 Ami 觉醒事件同曲）。她展现天才式全知（梭罗遗言、丰臣秀吉卒年、锗电子排布脱口而出），声称"I see everything. I hear everything."；Sensei 偷看她的笔记本——上面没有文字，只有稚拙的"房子"涂鸦。结尾低语："I see it... I see everything..."

`otohadorm5`（睡衣夜）：Otoha 吃甜甜圈与香肠面（Sensei 戏称 "sausage fest"），电视卡在"一张奇怪的房子图片"上（第三次"房子"意象）。妈妈来电时 Sensei 用歌词捣乱几乎害她被接回家：

> o: One wrong move and that could all come to an end. My parents know the address of this place and they could come get me at any moment.

> o: There won't {i}be{/i} a future if you keep doing stuff like that.

Sensei 的回应是一句冷得刺骨的玩笑："Just kill them."。Otoha 以学费受制于人反驳（"They're the ones paying my tuition."），最终以 1000 日元罚金和甜甜圈交换达成和解。结尾旁白罕见地温柔："It was a surprisingly refreshing night, all things considered."。本事件还带出 Molly 的跑团 DM 身份与 Rin 因怕丢脸禁止 Otoha 参加的信息。

### 2.6 Room 9：Touka 与 Yasu

`toukadorm1`：首访吐槽 Yasu——回家后一动不动坐着不说话、凌晨三点对白板耳语、放弃关灯；Touka 认真发问"Am I going to die tonight?"。喜剧点：Sensei 调侃她睡的是情趣酒店同款震动床，而她坚称那只是具备 "rapid sleep mode technology" 的高级进口床；情急之下喊出的保镖名单里居然有 Yumi；随口表示可以让家人"in a matter of minutes"暗杀 Sensei。信息点：Makoto 私下给她做了个性化讲义，Touka 以为是对所有人都有的待遇——Makoto 助手身份的延伸证据。结尾 Touka 派司机送 Sensei 回家。

`toukafirsthall`：走廊初遇。Touka 直接把"hanging out"解读为对年轻女孩有不良癖好，Sensei 全盘承认并加一句"You'll get used to it. ...it will feel totally normal in no time at all."。伏笔两枚：她说自己"已经气走 yet another teacher"随即慌忙改口；家中有三间卧室、带人参观需要"special preparations"。Io 坐在走廊地上冷眼旁观，用眼神问"Why are you talking to {i}her{/i} of all people?"。

`yasufirsthall`（解锁教堂）：本文件最重要暗线之一。Yasu 宣布"Romance is out of the question until my wings grow in"，随后引出天坑：

> ya: But I saw it with my own eyes, Sensei. The reckoning.

> ya: The hole that swallowed everything.

Sensei 追问是否指 Kumon-mi Academy 后，Yasu 只回了一个词："{i}Slip.{/i}"——说漏嘴的自我确认。她邀请 Sensei 去只有"被选中者"才能进入的 sanctuary，"I'm choosing you right now."，并抛出神社指控："Then why do you reek of a {i}shrine?{/i}"。事件以系统提示解锁："Congratulations! You may now visit New Hope Cathedral!"，以及一张从手套里取出的旧报纸剪报塞进 Sensei 手心——内容未揭晓。

`toukadorm5`：睡衣夜，大小姐卸壳。她哭诉融入困难："I am a {i}real{/i} girl with {i}real{/i} feelings. And I would very much like {i}real{/i} friends"，并交代家族设定：Tsukioka 家可追溯至江户时代初期，家训是每位男性家主只生两孩、长子继承一切-；父亲只有两个女儿，继承责任落到长女头上——

> to: The disease of being born a woman to someone who, more than anything, wanted a male heir.

她误信 Ayane 所言、以为 Sensei 与 Ayane 有婚约（道场线咬合）。结尾旁白确认她还在用 Sensei 教的自动售货机 power pose，"And so excited for her to find out from a very confused classmate that she has been making herself look like an idiot for quite some time now."。

`yasudorm10`：meta 密度最高的房间事件之一。开场旁白玩图像把戏：闪切 `realtoukaimage`（皱眉的 Touka），配合"If you pay close attention to the image in front of you..."，是给细心玩家的图像层信号。正片是 Yasu 的神学独白：灵魂不是幻象，若身体只是容器，意识可以存进世界本身-；死后意识存在于叠加在现世之上的"第二位面"；"To die is to disappear. And since it's impossible to fully vanish, there is no death."。核心是她对 Sensei 的恐惧宣言：

> ya: You exist as both my greatest fear and my greatest hope. For all that I am will surely rely on you before you are ready to be relied on.

> ya: But because I can not feel you.

她能感知世间一切低语，唯独感知不到 Sensei——Sensei 是这个世界感知力的盲点。末世预告收尾："Before long, the snow will melt. The seasons will change. And His slumber will come to its end."-。

### 2.7 Room 10：Kirin 与 Noriko

`kirinfirsthall`：Kirin 吐槽 Noriko 放了两小时摇滚，解释自己为何拖到进班才搬宿舍（家里远、讨厌巴士与人群、"People suck."），并为对姐姐 Karin 的态度被 Sensei 点破而炸毛。她直球发问"Do you want to fuck Ami?"，Sensei 装傻岔开；Kirin 还怀疑 Ami 半夜偷听，建议装摄像头、提议留宿抓现行。

`norikofirsthall`（重逢+拿号码）：Noriko 暗线核心事件。领养/皮带梗铺底后转入正题——她等了多年只为 Sensei 重新走进她的生活，并给出旧记忆佐证：

> n: There's no need to add "apparent" to that, Sensei. It definitely happened and it was a huge part of all of our lives.

> n: Even if you don't remember it right now, I'm sure you will in time.

更重磅的是 Maya 旧识揭露：Sensei 曾同时教 Noriko 和 Maya（"That's why Maya and I turned out so darn smart."），而 Sensei 完全不记得，只记得 Maya 警告他"Noriko 是邪恶的、会毁掉一切"。Noriko 提出可以靠打工和给姐姐做 PA 养活两个人、让他彻底辞职；索要手机号码时在自己名字旁加爱心 emoji、在姐姐 Maya 名字旁加呕吐 emoji——姐妹战争定调。她还立下裸照互发的口头协议，并预告"如果你和别人上床我可能会知道"。

`kirindorm10`：Room 10 首访，契约摊牌。Noriko 版条款："Kirin gets to have your dick and I get to have your heart. And also your dick."；以及野心宣言："I am going to shatter your harem and make you love me and only me."。Kirin 的自我规训：只许有性无爱、拥抱不许享受，违约后果由 Noriko 执行——"I get to dissect her."。Kirin 自我欺骗式独白："me actually 'liking' someone? That's just not possible."，Sensei 心里清楚她"prematurely agreed to something she wasn't exactly 100% behind"。

`kirindorm15`（被炉电影夜）：三人挤被炉看 Noriko 的"艺术电影"——钉死窗户的房子里，五个女孩围着厨房桌沉默地吃灰色食物-。Noriko 说她从来没看完过："Something always comes up in the middle and I have to leave."——强烈暗示她在上一个循环看过结局，或每次都在结局前被重置打断。事件随后进入成人分支。

`kirindorm20`：Noriko 意外不在，Kirin 独处未遂亲密事件，全部张力来自"契约不许动感情"这一条：她要求 Sensei 大声明说"我是来陪 Kirin Kanda 一个人的"，又嫌他说得不真诚。

`norikodorm5`（散步谈心）：开场旁白再次点破重置结构——Sensei 亲近 Noriko 的理由之一是她是"the sole creature in this universe that the girl responsible for resetting it hates"，直接指认 Maya 与世界重置的关联；紧接两句叙事者自白："I was placed here to do as I please."。散步中 Sensei 向 Noriko 解释世界重置观："when someone fades away, the world stops existing... No one disappears. They just get recycled."-；预测各人反应——"Ami and Ayane would take it the worst. Maya would throw a party."-。Noriko 的 meta 台词密集："Can you just like, hurry up and remember me already?"；"You know those memories are what my character arc is based around!"。途中插入静电闪切 `yumis2`，Sensei："I feel like I almost remembered something."。当 Sensei 说"I'm not the same person-"时，Noriko 打断："You are."。旁白总结失败原因时说得明白：他曾希望这些话能让 Noriko 察觉"the world resetting and memories being wiped"的可能，但她只觉得像动漫或没听过的宗教-。

`norikodorm10`：洗衣日常，随后进入成人分支；Sensei 顺走口袋里的 500 日元投资柴犬币。

`norikodorm25`（餐厅约会——全文件压轴）：Noriko 请客回请那顿 Niki 的四星晚餐，要讲"my side of the story"。Kaori 服务员的超现实点单插曲后，Noriko 完整讲述"你消失之后"的过去：她曾把每周去旧城区那栋破楼见 Sensei 视为城堡——"for a few hours every week, it was the most beautiful place in the whole wide world."；后来 Maya 出现，"the castle for two turned into a castle for three."；她每靠近一步 Sensei 就退远一步，直到某天他彻底消失-。她全城寻人，终于在巴士车窗瞥见他——此处文本被逐字涂黑（多处 `[[redacted]`），她看到的是 Sensei 与某人在一起的画面，内容被强制遮蔽。紧接着第四面墙崩坏：

> n: {b}STOP PLAYING LESSONS IN LOVE{/b}

> N: ///////////////////EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS

> N: ///////////////////PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT AS A THANK YOU FOR YOUR CONTINUED SUPPORT AS WE ATTEMPT TO REPAIR YOUR CONNECTION

菜单弹出"Would you like to phone?"，唯一选项 Phone 通向 `restofnorikorestx` 续篇。谁在阻止玩家听到这段往事，是本文件最大的未解之谜。

---

## 三、成人内容概貌（叙事功能抽象）

本文件的成人/准成人内容以三种形态存在，均服务于关系结构而非单纯的福利：

1. **契约型**：Room 10 的"friends with benefits"条款（Kirin 只性无爱、违约解剖警告）与 Noriko 的裸照互换协议-，把亲密行为写成明码标价的合同——性在这里是权力分配的语言，Kirin 每一次强调"我不会动心"都是反向 flag。
2. **被打断型**：`otohadorm5` 的性玩笑被家长来电拦腰斩断，`kirindorm20` 的未遂亲密被契约焦虑冻结——成人氛围反复在临界点被外部力量（家庭监护/自我规训/契约条款）掐灭，暗示欲望在这层叙事里始终不被允许自然落地。
3. **被系统遮蔽型**：压轴事件里 Noriko 的叙述被成片 `[[redacted]` 涂黑，并直接打出"STOP PLAYING LESSONS IN LOVE"，随后系统以"EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS"、"PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT..."过渡到 `restofnorikorestx` 续篇——当亲密叙事即将触及真相时，试图切断它的不是人物也不是道德，而是"系统"本身。

---

## 四、与主线/元叙事咬合点

1. **Kumon-mi Academy 天坑**：Yasu 的"The hole that swallowed everything / Slip." 与 Touka 的"everything the sinkhole claimed" 互证——转学生群体都是天坑吞没旧校前的关联者。
2. **三层世界的贯穿**：恋爱表层（契约、约会、被炉）／重置循环层（Noriko 没看完的房子电影、Sensei 在 Uta 场景中话说到一半停顿、牙齿变液体的规则怪谈）／元叙事玩家层（Nodoka 的"刷满好感即成神"、`norikodorm25` 的 STOP PLAYING 直呼其名）在本文件各自都有落点。
3. **MayaNoriko 旧识闭环**：norikofirsthall 揭示 Sensei 曾同时家教二人；norikodorm5 旁白指认"负责重置的女孩"恨 Noriko——Maya 的敌意有了世界观级别的动机。
4. **Sensei 的异常性**：Yasu"我感知不到你"、Nodoka 笔记本上的房子涂鸦、`norikodormgen` 的"this body's old memories banging against the bars of the prison I forced them into"——灵魂/记忆与身体分离、被强制压制的设定在此坐实。
5. **"房子"意象三连**：Nodoka 笔记本的涂鸦、Otoha 电视卡住的房子画面、Kirin 房"五女孩灰食之屋"电影——指向同一未揭晓原型。
6. **Ami 觉醒机制**：nodokadorm5 使用 `amiawake.mp3` + `ayhh6`，将 Nodoka 的过载发作与 Ami 觉醒事件绑定在同一演出语言上。
7. **跨线依赖**：nodokadorm15 ← yasudorm20；kirindorm10 ← utadorm5 + iodorm5；norikodorm25 ← convenience25；教堂场景 New Hope Cathedral 由 yasufirsthall 解锁——本层是多条角色线的中继站。
8. **Rin 线侧写**：otohafirsthall 的"Rin 对你不一样"、otohadorm1 的"flavor of the month"担忧、otohadorm5 的跑团禁令。
9. **Makoto 线**：toukadorm1 的私下讲义。
10. **Niki 旧恋情确证**：norikofirsthall 由当事人妹妹之口盖章"It definitely happened"。

---

## 五、未解伏笔

1. **Yasu 手套里的旧报纸剪报**内容未揭晓-——"所有烦恼的答案都在那张纸上"。
2. **Noriko 在巴士上看到的人是谁**：redaction + STOP PLAYING 强制中断-；续篇在 `restofnorikorestx`。
3. **"Would you like to phone?"的电话打给谁**：系统故障式演出暗示存在干预叙事的外部存在。
4. **"房子"原型的真身**：涂鸦/电视画面/艺术电影三处呼应，尚未揭晓。
5. **Nodoka 发作为何使用 Ami 觉醒同款资源**：两者机制的共同来源未明说。
6. **Yasu 的雪融倒计时**："His slumber will come to its end"——季节转换与"祂"的身份。
7. **Touka"气走 yet another teacher"的具体历史**：话头即断。
8. **双版本 Touka 图像**（`realtoukaimage` vs `toukaolddis8`）的完整含义。
9. **Io 的自毁倾向**（四个美工刀、"practically dead already"）的后续。
10. **Uta 的家庭线**：兄弟杀人未遂入狱、母亲一系接连恶疾、亡祖父死于脑癌等背景尚未充分展开。
11. **Kirin 的"dissect her"违约条款**：黑色玩笑还是真 flag。
12. **Noriko 自述"角色弧线基于记忆恢复"**：她的下一阶段（向父母姐妹证明自己没疯）尚未发生。
13. **Sensei 曾是作家**（Futaba 情报，经 Nodoka 转述）与旧补习班岁月的全貌。

---
> 按源行号检索本角色 label，见 `索引/Dorm2索引.md`。
