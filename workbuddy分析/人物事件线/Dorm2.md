# Dorm2Events.rpy 全析（宿舍二楼事件集）

> 源文件：`游戏文本/Dorm2Events.rpy`（13787 行，85 个 label）。跨文件依赖：`utamaid*`/`bathhouse*`/`nodokalibrary*`/`otohapark*`/`toukastreets*`/`christmastwo*`/`toukaarchery*`/`church*`/`kirinsoccer*`/`norikospecial*`/`convenience*`/`norikodate*`/`otohadate*`/`makotospring*`/`yasuspring*`/`rindorm50special` 等标记由对应角色线写入；`endofweekday`/`endofsat`、`mollymastx`/`kotatsux`/`kirinalmostx`/`norikounderx`/`restofnorikorestx`/`noodlesheadpat` 等分流目标定义在其他文件。
> 定位：宿舍二楼是全游戏"日常表层最厚、meta 渗透最深"的舞台之一——一半是刷好感的房间模板，另一半埋着天坑、重置循环与第四面墙崩坏的直接证词。
> 本文件 `bonus` 双分支密集出现（约 40 处），本文只把 `bonus == True` 一侧当作事实依据；所有 love/lust 数值与 label 跳转均按源文录入。

## 一、群像基本盘

**楼层与房间表**（`doorknock2` 菜单逐条列出）：Room 6 = Molly & Tsuneyo、Room 7 = Uta & Io、Room 8 = Otoha & Nodoka、Room 9 = Touka & Yasu、Room 10 = Kirin & Noriko。

**入口结构**。`dorm2monday` / `dorm2tuesday` / `dorm2wednesday`（另有 thursday/friday/weekend）是二楼工作日入口 hub，按 `mollysad`、`day288`、`chapthreeactive`、`christmas7` 切换背景图，并挂载菜单项 "Knock on a door"（→ `doorknock2`）、"Talk to Molly"（→ `mollyfirsthall`/`mollyhall`）、"Talk to Otoha"（`day288` 后，→ `otohafirsthall`/`otohahall`）与 "First Floor"（→ `dormmonday`）。`doorknock2` 按房间二次分菜单，每项显示当前好感度数值；房间未解锁时直接回 "This room is not yet available."。

**各房间路由器**（好感度阈值与跨线依赖，全部按源文）：
- `mollydorm`：`molly_love >= 5 and mollycafe1 == True` → `mollydorm5`；`>= 10 and mollycafe10 == True` → `mollydorm10`；`>= 15 and christmas7 == True` → `mollydorm15`；`>= 20 and mollycafe20 == True` → `mollydorm20`；`>= 30 and rindorm50special == True` → `mollydorm30`；否则 `mollydormgen`（另有 `mollyspring2 == True` 时的 "Blowjob" → `mollybjrep` 项）。
- `tsuneyodorm`：`tsuneyo_love >= 5 and ramen1 == True` → `tsuneyodorm5`；`>= 10 and ramen10 == True` → `tsuneyodorm10`；`>= 15 and ramen15 == True` → `tsuneyodorm15`；`>= 20 and day247 == True` → `tsuneyodorm20`；`>= 25 and secondbeach18 == True` → `tsuneyodorm25`；`>= 40 and otohaspring7 == True` → `tsuneyospring7`；否则 `tsuneyodormgen`。
- `utadorm`：`uta_love >= 5 and utamaid5 == True` → `utadorm5`；`>= 10 and day != 2` → `utadorm10`；`>= 15 and utamaid10 == True` → `utadorm15`；`>= 30 and utamaid25p2 == True` → `utadorm30`；`>= 40 and utadate35 == True and wakanadate25p3 == True` → `utadorm40p1`；否则 `utadormgen`。
- `iodorm`：`io_love >= 5 and bathhouse5 == True` → `iodorm5`；`>= 10 and iofirsthall == True` → `iodorm10`；`>= 15 and bathhouse10 == True` → `iodorm15`；`>= 25 and bathhouse25 == True` → `iodorm25`；`>= 35 and bathhouse35p2 == True` → `iodorm35`；否则 `iodormgen`。
- `nodokadorm` / `otohadorm`：`nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True` → `nodokadorm1`（搬入欢迎会）；`nodoka_love >= 5 and nodokalibrary5 == True` → `nodokadorm5`；`>= 15 and yasudorm20 == True` → `nodokadorm15`；`>= 40 and makotospring5 == True and yasuspring8 == True` → `nodokaspring1`；`otoha_love >= 5 and otohapark5 == True` → `otohadorm5`；`>= 20 and christmasfive8 == True` → `otohaspring4`；否则对应 `dormgen`。
- `toukadorm`：`touka_love >= 1 and toukafirsthall == True` → `toukadorm1`；`>= 5 and toukastreets5 == True` → `toukadorm5`；`>= 10 and christmastwo20 == True` → `toukadorm10`；`>= 25 and toukaarchery20 == True` → `toukadorm25p1`；否则 `toukadormgen`。
- `yasudorm`：`yasu_love >= 10 and yasufirsthall == True and toukadorm5 == True and makotowinterbeach4 == True` → `yasudorm10`；`>= 20 and church20 == True` → `yasudorm20`；`>= 25` → `yasudorm30`；否则 `yasudormgen`。
- `kirindorm`：`kirin_love >= 10 and day271 == True and utadorm5 == True and iodorm5 == True` → `kirindorm10`（依赖 Uta/Io 双线各完成一段才能推进）；`>= 15 and kirinsoccer20 == True` → `kirindorm15`；`>= 20` → `kirindorm20`；`>= 25 and norikodorm25 == True` → `kirindorm25`；否则 `kirindormgen`。
- `norikodorm`：`noriko_love >= 5 and kirindorm10 == True and convenience1 == True` → `norikodorm5`；`>= 10 and convenience5 == True and kirindorm20 == True` → `norikodorm10`；`>= 20 and norikospecial20 == True` → `norikodorm20`；`>= 25 and convenience25 == True` → `norikodorm25`；`>= 30 and norikodate30 == True and otohadate20 == True` → `norikodorm30`；否则 `norikodormgen`。

通用事件层面：走廊初遇事件（以 firsthall 结尾，如 `nodokafirsthall`、`toukafirsthall`）与房间事件（以 dormN 结尾）按好感度解锁；部分角色另设以 hallgen 结尾的走廊通用事件（`nodokahallgen`、`toukahallgen` 等），以 dormgen 结尾的通用房间事件为可无限重复的低门槛模板。

**Room 6（Molly & Tsuneyo）**。Molly 是跑团 DM（"SEVEN VIOLET FUNGUS APPEAR! ROLL FOR INITIATIVE!" 的喊话会穿透墙壁传到隔壁），用游戏内性癖谈论逃避现实，自称 ADHD——"There's not a lot of space on my hard drive so I need to constantly delete things to make place for new ones."；深层动机由旁白说破："It seems that Molly is willing to do virtually anything in order to separate herself from the real world."。Tsuneyo 是 rules 怪谈体质：面无表情、鲸鱼癖、把宿舍当成拉面馆（"Every house is a noodle house if you try hard and believe in yourself."），与一只鸟（Noodles）绑定。

**Room 7（Uta & Io）**。Uta 的房间以"垃圾场"著称——Kirin 口中的 "the garbage dump that is Uta and Io's room"。Uta 的家庭背景在本层逐步揭开：为照顾祖父 Ushibori 而搬到 Kumon-mi（祖父癌症扩散到脑部、失去语言能力后去世），另有语焉不详的 "other stuff"（母亲一系 "the long line of debilitating diseases"）；facetime 线补充兄弟因杀人未遂入狱（受害者未死，刑期还有"几年"）。Io 则是本层最暗的角色：药物依赖、四个美工刀、对 Uta 救赎性的依附。

**Room 8（Otoha & Nodoka）**。Nodoka 是"天才过载"型角色：连续失眠、咖啡因过量、全知式炫学，其发作演出直接接入 Ami 觉醒同源的音乐与图像资源。Otoha 表面是吐槽役，实际处于严苛的家庭监控之下——父母知道宿舍地址，"一个错误动作就可能一切结束"，她用 "leash"（皮带）自我形容。Otoha 还承担 Rin 线的侧写功能。

**Room 9（Touka & Yasu）**。Touka：Tsukioka 财阀继承人，因父亲只有两个女儿而被迫以长女身份继承家业，傲娇外壳下是"想交真朋友"的正常女孩。Yasu：自称天使候补的宗教狂角色，能听见"以太低语"，是 Kumon-mi Academy 天坑的目击者，也是教堂场景 New Hope Cathedral 的解锁人。两人同居本身就是喜剧装置。

**Room 10（Kirin & Noriko）**。同日转入的同居组。Kirin：毒舌能量饮料成瘾者，坚称自己"只会有性吸引力、不可能动真心"，实际是自我欺骗大师。Noriko：Sensei 的童年旧识，粉色头发、口袋刀、"疯狂眼神"组合拳，主动承认会尾行 Sensei 回家，是 Maya 公开敌视的对象。两人搬入当天就立下分赃式"契约"。

## 二、逐房间事件脉络

### 2.1 Room 6：Molly 与 Tsuneyo

`mollyfirsthall`：NEET 戒断喜剧+邪教梗。她自称每周必须"在走廊里站一小时"来打破 NEET  mold，进而兜售宿命论（"Believe in the me that believes in you!"），宣布成立 "Cult of Molly"，入会条件是要 Sensei 八盎司血（"That is enough to perform the ritual."）。

`tsuneyofirsthall`：鲸鱼学讲座（蓝鲸寿命 80-90 年如数家珍），并立下规矩——"Being alone in a room with a boy is something I'm supposed to avoid."，同时留下伏笔 "I tend to cave under pressure."

`tsuneyodorm5`（首访房间，`tsuneyo_love += 1`）：开场是把宿舍当成拉面馆的误会（"Business hours don't start for another thirty minutes."）；房间导览展出羊驼藏品与一幅巨大的拉面肖像（来历不明："It simply arrived here one day"）。正题是守密/勒索：她交代父亲"训练她杀过很多东西"（"We would snap their necks and pluck their bodies clean of feathers"），并留下全句 "If he knew I was alone in a room with a man, he would have you executed."；Sensei 求她保密，她的回应是平静的不可能规则——"But if I break the rules, all of my teeth will turn to liquid."，最终以勒索达成妥协（"This is starting to sound like extortion." / "It is, more or less."），而她不承认是为了 Sensei："I'm doing it for Noodles."（"You participated in naming him"——Noodles 是她与 Sensei 共同命名的鸟）。结尾旁白确认两人关系拉近。

`mollydorm5`（`molly_love += 1`）：万圣节题材的伏笔段（`bonus == True` 时她正在自慰，Sensei 误闯）。

`mollydorm10`（`molly_love += 3`，本房间数值最高的一场）：跑团交易段。她提出用"万圣节派对服装的幕后一窥"交换 Sensei 在她变身期间回避——报价逐步升级为 "It is six girls, Sir."，并补充 "The costumes are rather form fitting as well. If you look closely enough, you can see {i}everything{/i}, Sir."；Sensei 接受前顺手保留反悔权，Molly 于是 "Roll for persuasion."，骰出天然 20——"Brigid's bosom, it's a natural twenty."——判词落在条款本身："You win your wonky barter clause, Sir."。她的深层动机也在此交底：愿意 "do virtually anything in order to separate herself from the real world"（跑团、交易、性癖谈论全是麻醉剂）。

`mollydorm15`：本文件最大的破墙小品之一。Sensei 进门前的转场被一整段伪赞助商广告接管——自称 Selebus 的旁白用 Raid: Shadow Legends 广告腔连播数十行，中途自己戳穿："Lessons in Love, I mean. Not Raid: Shadow Legends."，并补刀 "the chances of anyone reading this are slim to none"。（`molly_love += 1`）

`mollydorm20`（`molly_love += 1`）：`bonus == True` 分支跳 `mollymastx`，本文件内只留分流。

`tsuneyodorm10`（`tsuneyo_love += 1`）：该线的小高点，细节以规则怪谈式对话推进（`bonus == True` 分支另走成人内容）。

`tsuneyodorm15`（`tsuneyo_love += 1`）：Molly 帮 Tsuneyo 试穿亲手制作的角色服装（对应场景图 `tsuneyocos20` / `tsuneyocos21`）的日常支线；`tsuneyodorm20`/`tsuneyodorm25`（各 `tsuneyo_love += 1`）继续拉伸该线的怪谈质感。此线的功能是把"宿舍日常"的地面凿开一道裂缝：在这个世界里，身体的规则本身并不可靠。

### 2.2 Room 7：Uta 与 Io

`utafirsthall`：闲聊段，Uta 自述仍在熟悉环境（"Reminds me a lot of Nara but with less wildlife and more...tamed life."），并抛出对 Sensei 的信任（别的老师会偷她东西/是"偷偷瞟人的那种变态"，视分支而定）。

`iofirsthall`：开场即定调——Io 坐在走廊地上"换空气"，提议跟 Sensei 互换外套与位置（"You can hang out here and watch movies in my bed or something."）；她提到自动售货机上那只从没动过的怪鸟，Sensei 不戳破（"You will learn the true nature of that animal in time."——即 Noodles）。

`utadorm5`（`uta_love += 1`，解锁 `iodorm5`）：`utadorm` 系列首段。背景故事讲述中藏着一处异常信号：Sensei 的话说到一半莫名停顿——"I stop talking mid-sentence, though I'm not sure why."——这是循环层干扰叙事者的典型表现。facetime 事件透露家庭全貌：兄弟因杀人未遂入狱（电话那头是 "a person who has literally attempted murder"，"He'll probably get out in a couple years since the person didn't actually die"）、祖父之死（"At least before the cancer spread to his brain and he lost the ability to speak." / "RIP grandpa."）、母亲一系的 "long line of debilitating diseases"。

`iodorm5`（`io_love += 1`，依赖 `utadorm5 == True`）：Io 单独相处段。

`utadorm10` / `utadorm15`（各 `uta_love += 1`）：Uta 线主体推进；`utadorm20`（`uta_love += 1`，并置 `utanumber = True`）拿到电话号码。

`iodorm10`（`io_love += 1`）之后，`iodorm15`（`io_love += 1`）是全文件最黑暗段落之一：服药后神志不清的 Io 爬上 Sensei 的膝盖，说出 "Because you're my last bastion of hope for adults in this world."，自嘲为 "a weightless, overmedicated cockroach with a grand total of two bras and four boxcutters"；结尾旁白宣判："Io is practically dead already."（其后接 "And there is no one who deserves rest quite like the dead."）。她的四个美工刀与药物依赖在此线贯穿。

### 2.3 Room 8：Nodoka 与 Otoha

`nodokafirsthall`：Nodoka 在读《Lolita》（"'Lolita.' Are you familiar with it?"），直问 Sensei 能否爱上远比自己年轻的人，并以 "Remember that when the time comes for you to become my own Humbert Humbert." 收尾；她还带来情报：Futaba 说 Sensei 曾经是作家（"Futaba tells me you used to be a writer, Sensei."）。

`otohafirsthall`：确立宿舍"没有规则"的荒诞（"Rules? I'm not even sure if these dorms have rules." → Otoha 反驳 "Surely there have to be like...{i}some{/i} rules?" → Sensei "Just make up your own rules if you want them so much."）；被追问 "How did you get hired as a teacher?" 时装傻搪塞（"There's no answer to why there aren't any rules in the dorms, is there? Acknowledge my role here the same way..."）。她点出 Rin 线的侧写："she's different with you than she is with anybody else. Myself included."

`nodokadorm1` + `otohadorm1`（搬入欢迎会，各 `+1` love）：Nodoka 当众"测试" Sensei，把好感度系统说破——"To max out your relationship with everyone around you would equate you to a king, wouldn't it?"，随即抛出纯 meta 一句："Perhaps this entire world is nothing like either of us perceive it to be?"；事后她自称只是在评估 Sensei 误伤女孩们的概率。Otoha 把 Sensei 拉出门解围，并顺势请教 Rin 的感情问题，担忧自己是 "I'm just the flavor of the month or something"。本段旁白留下名句："The correct answer is that both smiles are impossible to maintain." "Because this world is miserable." "And smiling at all is pointless when smiles die faster than anything known to man." "And yet-" "And yet they're still so inexplicably beautiful."

`nodokadorm5`（狂躁发作，`nodoka_love += 1`）：Sensei 独对数日未眠的 Nodoka，她反复念 "It's wrong. It's so wrong." → "IT DOESN'T MAKE SENSE! IT IS INCOMPLETE!"。演出层面插入静电音效、闪切图片 `ayhh6`、播放 BGM `amiawake.mp3`（与 Ami 觉醒事件同曲）。她展现天才式全知（梭罗遗言、丰臣秀吉卒年、锗电子排布脱口而出），声称 "I see everything. I hear everything."；Sensei 偷看她的笔记本——上面没有文字，只有稚拙的"房子"涂鸦。结尾低语："I see everything..."（`{size=-15}` 小字号收束）。

`otohadorm5`（睡衣夜，`otoha_love += 1`）：Otoha 吃甜甜圈与香肠面（Sensei 戏称 "sausage fest"），电视卡在"一张奇怪的房子图片"上（第三次"房子"意象，关机后自己恢复）。妈妈来电时 Sensei 用歌词捣乱几乎害她被接回家：

> o: One wrong move and that could all come to an end. My parents know the address of this place and they could come get me at any moment.

> o: There won't {i}be{/i} a future if you keep doing stuff like that.

Sensei 的回应是一句冷得刺骨的玩笑："Just kill them."。Otoha 以学费受制于人反驳（"They're the ones paying my tuition. I can't just...not listen to them anymore."），最终以 1000 日元罚金和甜甜圈交换达成和解。结尾旁白罕见地温柔："It was a surprisingly refreshing night, all things considered."。本事件还带出 Molly 的跑团 DM 身份与 Rin 因怕丢脸禁止 Otoha 参加的信息。

### 2.4 Room 9：Touka 与 Yasu

`toukadorm1`（`touka_love += 1`）：首访吐槽 Yasu——回家后一动不动坐着不说话、凌晨三点对白板耳语、放弃关灯；Touka 认真发问 "Am I going to die tonight?"。喜剧点：Sensei 调侃她睡的是情趣酒店同款震动床，而她坚称那只是具备 "rapid sleep mode technology" 的高级进口床；情急之下喊出的保镖名单里居然有 Yumi（"Mother?! Yumi?!"，并承认 Yumi 比 Sensei 更令她害怕）；随口表示可以让家人 "in a matter of minutes" 暗杀 Sensei。信息点：Makoto 私下给她做了个性化讲义，Touka 以为是对所有人都有的待遇——Makoto 助手身份的延伸证据。结尾 Touka 派司机送 Sensei 回家。

`toukafirsthall`：走廊初遇。Touka 直接把 "hanging out" 解读为对年轻女孩有不良癖好，Sensei 全盘承认并加一句 "You'll get used to it. ...it will feel totally normal in no time at all."。伏笔两枚：她说自己 "I can not risk losing yet another teacher due to my inability to maintain my composure"（气走老师的传闻）随即慌忙改口；家中有三间卧室、带人参观需要 "special preparations"（"I don't think we've ever allowed anyone like you into the manor before"）。Io 坐在走廊地上冷眼旁观，用眼神问 "Why are you talking to {i}her{/i} of all people?"

`yasufirsthall`（解锁教堂）：本文件最重要暗线之一。Yasu 宣布 "Romance is out of the question until my wings grow in"，随后引出天坑：

> ya: But I saw it with my own eyes, Sensei. The reckoning.

> ya: The hole that swallowed everything.

Sensei 追问是否指 Kumon-mi Academy 后，Yasu 只回了一个词："{i}Slip.{/i}"——说漏嘴的自我确认（"It's an answer. One I can share with you the moment you open your eyes."）。她邀请 Sensei 去只有"被选中者"才能进入的 sanctuary（"I'm choosing you right now."），并抛出神社指控："Then why do you reek of a {i}shrine?{/i}"。事件以系统提示解锁："Congratulations! You may now visit New Hope Cathedral!"，以及一张从手套里取出的旧报纸剪报塞进 Sensei 手心（"Yasu takes one of her gloves off and removes an old newspaper clipping that she had been carrying around in there for some reason."）——内容未揭晓。

`toukadorm5`（睡衣夜，大小姐卸壳，`touka_love += 1`）：她哭诉融入困难——"I am a {i}real{/i} girl with {i}real{/i} feelings." "And I would very much like {i}real{/i} friends so I don't have to spend so much time sitting in my room by myself."，并交代家族设定：Tsukioka 家可追溯至江户时代初期，家训是每位男性家主只生两孩（"bearing no more than two children per every male figurehead"）、长子继承一切；父亲只有两个女儿，继承责任落到长女头上——

> to: The disease of being born a woman to someone who, more than anything, wanted a male heir.

她也自陈退路是被拿去联姻（"surrender myself to the male heir of some other family with even greater power than ours"）。她误信 Ayane 所言、以为 Sensei 将与 Ayane 成婚（"I can only imagine how excited you are to be married into the Amamiya family."，Sensei 反驳 "Didn't I tell you to not believe anything Ayane says?"——道场线咬合）。结尾旁白确认她还在用 Sensei 教的自动售货机 power pose，"And so excited for her to find out from a very confused classmate that she has been making herself look like an idiot for quite some time now."

`yasudorm10`（`yasu_love += 1`）：meta 密度最高的房间事件之一。开场旁白玩图像把戏：闪切 `realtoukaimage`（皱眉的 Touka），配合 "If you pay close attention to the image in front of you..."，是给细心玩家的图像层信号。正片是 Yasu 的神学独白：灵魂不是幻影，若身体只是容器，意识可以存进世界本身；死后意识存在于叠加在现世之上的"第二位面"（"There is a second plane of existence that lies directly on top of our current plane."），"To die is to disappear. And since it's impossible to fully vanish, there is no death."。核心是她对 Sensei 的恐惧宣言：

> ya: You exist as both my greatest fear and my greatest hope. For all that I am will surely rely on you before you are ready to be relied on.

> ya: But because I can not feel you.

她能感知世间一切低语，唯独感知不到 Sensei——Sensei 是这个世界感知力的盲点。末世预告收尾："Before long, the snow will melt. The seasons will change. And His slumber will come to its end."

### 2.5 Room 10：Kirin 与 Noriko

`kirinfirsthall`：Kirin 吐槽 Noriko 放了两小时摇滚，解释自己为何拖到进班才搬宿舍（家里远、讨厌巴士与人群、"People suck."），并为对姐姐 Karin 的态度被 Sensei 点破而炸毛。她直球发问 "Do you want to fuck Ami?"，Sensei 装傻岔开；Kirin 还怀疑 Ami 半夜偷听，建议装摄像头、提议留宿抓现行。

`norikofirsthall`（重逢+拿号码）：Noriko 暗线核心事件。领养/皮带梗铺底后转入正题——她等了多年只为 Sensei 重新走进她的生活，并给出旧记忆佐证：

> n: There's no need to add "apparent" to that, Sensei. It definitely happened and it was a huge part of all of our lives.

> n: Even if you don't remember it right now, I'm sure you will in time.

更重磅的是 Maya 旧识揭露：Sensei 曾同时教 Noriko 和 Maya（"That's why Maya and I turned out so darn smart."），而 Sensei 完全不记得，只记得 Maya 警告他"Noriko 是邪恶的、会毁掉一切"。Noriko 提出可以靠打工和给姐姐做 PA 养活两个人、让他彻底辞职；索要手机号码时在自己名字旁加爱心 emoji、在姐姐 Maya 名字旁加呕吐 emoji——姐妹战争定调。她还立下裸照互发的口头协议，并预告"如果你和别人上床我可能会知道"。

`kirindorm10`（Room 10 首访，契约摊牌，`kirin_love += 1`；解锁条件同时要求 `utadorm5` 与 `iodorm5`）：Noriko 版条款："Kirin gets to have your dick and I get to have your heart. And also your dick."；以及野心宣言："I am going to shatter your harem and make you love me and only me."。Kirin 的自我规训：只许有性无爱、拥抱不许享受，违约后果由 Noriko 执行——"I get to dissect her."。Kirin 自我欺骗式独白："me actually 'liking' someone? That's just not possible."，Sensei 心里清楚她 "prematurely agreed to something she wasn't exactly 100% behind"。

`kirindorm15`（被炉电影夜，`kirin_love += 1`）：三人挤被炉看 Noriko 的"艺术电影"——钉死窗户的房子里，五个女孩围着厨房桌沉默地吃灰色食物（"There are five girls in a house together, gathered around a small kitchen table." / "The windows around them are boarded and they're eating a strange gray substance piled high on their plates." / "No one is saying or doing anything."）。Noriko 说她从来没看完过："It's weird. I've actually never finished it." "Something always comes up in the middle and I have to leave."——强烈暗示她在上一个循环看过结局，或每次都在结局前被重置打断。`bonus == True` 分支随后跳 `kotatsux`。

`kirindorm20`（`kirin_love += 1`）：Noriko 意外不在，Kirin 独处未遂亲密事件，全部张力来自"契约不许动感情"这一条：她要求 Sensei 大声明说"我是来陪 Kirin Kanda 一个人的"，又嫌他说得不真诚。`bonus == True` 分支跳 `kirinalmostx`。

`norikodorm5`（散步谈心，`noriko_love += 1`）：开场旁白再次点破重置结构——Sensei 亲近 Noriko 的理由之一是她是 "the sole creature in this universe that the girl responsible for resetting it hates"，直接指认 Maya 与世界重置的关联；紧接两句叙事者自白："I was placed here to do as I please."。散步中 Sensei 向 Noriko 解释世界重置观："when someone fades away, the world stops existing... No one disappears. They just get recycled."；预测各人反应——"Ami and Ayane would take it the worst. Maya would throw a party."。Noriko 的 meta 台词密集："Can you just like, hurry up and remember me already?"；"You know those memories are what my character arc is based around!"。途中插入静电闪切 `yumis2`，Sensei："I feel like I almost remembered something."。当 Sensei 说 "I'm not the same person-" 时，Noriko 打断："You are."。旁白总结失败原因时说得明白：他曾希望这些话能让 Noriko 察觉 "the world resetting and memories being wiped" 的可能，但她只觉得像动漫或没听过的宗教。

`norikodorm10`（洗衣日常，`noriko_love += 1`）：Sensei 顺走她口袋里的 500 日元（"I find 500 yen in one of her pockets and keep it to myself to invest it in Shiba Inu."——柴犬币梗）。`bonus == True` 分支跳 `norikounderx`。

`norikodorm25`（餐厅约会——全文件压轴，`noriko_love += 3`）：Noriko 请客回请那顿 Niki 的四星晚餐，要讲 "my side of the story"。Kaori 服务员的超现实点单插曲后，Noriko 完整讲述"你消失之后"的过去：她曾把每周去旧城区那栋破楼见 Sensei 视为城堡——"for a few hours every week, it was the most beautiful place in the whole wide world."；后来 Maya 出现，"the castle for two turned into a castle for three."；她每靠近一步 Sensei 就退远一步，直到某天他彻底消失。她全城寻人，终于在巴士车窗瞥见他——此处文本被逐字涂黑（多处 `[[redacted]`），她看到的是 Sensei 与某人在一起的画面，内容被强制遮蔽。紧接着第四面墙崩坏：

> n: {b}STOP PLAYING LESSONS IN LOVE{/b}

> N: ///////////////////EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS

> N: ///////////////////PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT AS A THANK YOU FOR YOUR CONTINUED SUPPORT AS WE ATTEMPT TO REPAIR YOUR CONNECTION

菜单弹出 "Would you like to phone?"，唯一选项 Phone 通向 `restofnorikorestx` 续篇。谁在阻止玩家听到这段往事，是本文件最大的未解之谜。

### 2.6 通用模板层（dormgen / hallgen）

通用房间模板均可无限重复，统一 `love += 1`，并按 `chap4active`/`day` 跳 `endofsatch4`/`endofweekdaych4` 或 `endofweekday`/`endofsat`。其中两段旁白公然玩弄叙事权：`toukadormgen` 里——

> "I convince Touka to leave her family and become my sex slave. She obliges and, within moments, we are naked."（`bonus == True` 一侧；另一侧是 "open up an Arby's with me"）
> "Just kidding."
> "I never convince her to do any of that and, instead, decide to just head home."

——同一段旁白先写出幻想再亲手撤销，是对"玩家意淫权"的自嘲；旁白还不忘自辩 "I need to be the center of her affinities because this is a world made for me."。`yasudormgen` 则让 Sensei 在黑暗中陪一个微笑站立的女孩坐一晚（"I ask her to turn the lights on because I feel incredibly uncomfortable just watching her stand there smiling, but she refuses."），并认真怀疑她床底下藏着宗教仪式工具（"I absolutely would not be surprised if there were some weird religious ritual tools tucked away under her bed"）。走廊模板 `toukahallgen` 里 Touka 见面第一句是 "Please make no sudden movements or I will call the police."，`yasuhallgen` 的开场白则是传教："Do you have a moment to hear about our lord and savior?"。

## 三、成人内容概貌（叙事功能抽象）

本文件的成人/准成人内容以三种形态存在，均服务于关系结构而非单纯的福利（`bonus == True` 一侧；非 bonus 侧多为纯日常或玩笑）：

1. **契约型**：Room 10 的 "friends with benefits" 条款（Kirin 只性无爱、违约解剖警告）与 Noriko 的裸照互换协议，把亲密行为写成明码标价的合同——性在这里是权力分配的语言，Kirin 每一次强调"我不会动心"都是反向 flag。
2. **被打断型**：`otohadorm5` 的性玩笑被家长来电拦腰斩断，`kirindorm20` 的未遂亲密被契约焦虑冻结——成人氛围反复在临界点被外部力量（家庭监护/自我规训/契约条款）掐灭，暗示欲望在这层叙事里始终不被允许自然落地。
3. **被系统遮蔽型**：压轴事件里 Noriko 的叙述被成片 `[[redacted]` 涂黑，并直接打出 "STOP PLAYING LESSONS IN LOVE"，随后系统以 "EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS"、"PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT..." 过渡到 `restofnorikorestx` 续篇——当亲密叙事即将触及真相时，试图切断它的不是人物也不是道德，而是"系统"本身。

## 四、与主线/元叙事咬合点

1. **Kumon-mi Academy 天坑**：Yasu 的 "The hole that swallowed everything" / "{i}Slip.{/i}" 是全文件最硬的天坑证词；转学生群体（Uta、Io）被暗示为天坑吞没旧校前的关联者。
2. **三层世界的贯穿**：恋爱表层（契约、约会、被炉）／重置循环层（Noriko 没看完的房子电影、Sensei 在 Uta 场景中话说到一半停顿、牙齿变液体的规则怪谈）／元叙事玩家层（Nodoka 的"刷满好感即成神"、`norikodorm25` 的 STOP PLAYING 直呼其名、`mollydorm15` 的伪广告劫持）在本文件各自都有落点。
3. **Maya/Noriko 旧识闭环**：`norikofirsthall` 揭示 Sensei 曾同时家教二人；`norikodorm5` 旁白指认 "the girl responsible for resetting it hates" Noriko——Maya 的敌意有了世界观级别的动机。
4. **Sensei 的异常性**：Yasu"我感知不到你"（"But because I can not feel you."）、Nodoka 笔记本上的房子涂鸦、`norikodormgen` 的 "It's possible that's just this body's old memories banging against the bars of the prison I forced them into"——灵魂/记忆与身体分离、被强制压制的设定在此坐实。
5. **"房子"意象三连**：Nodoka 笔记本的涂鸦、Otoha 电视卡住的房子画面、Kirin 房"五女孩灰食之屋"电影——指向同一未揭晓原型。
6. **Ami 觉醒机制**：`nodokadorm5` 使用 `amiawake.mp3` + `ayhh6`，将 Nodoka 的过载发作与 Ami 觉醒事件绑定在同一演出语言上。
7. **跨线依赖**：`nodokadorm15` ← `yasudorm20 == True`；`kirindorm10` ← `utadorm5 == True and iodorm5 == True`；`norikodorm5` ← `kirindorm10`；`norikodorm10` ← `kirindorm20`；`norikodorm25` ← `convenience25`；教堂场景 New Hope Cathedral 由 `yasufirsthall` 解锁——本层是多条角色线的中继站。
8. **Rin 线侧写**：`otohafirsthall` 的 "she's different with you than she is with anybody else. Myself included."、`otohadorm1` 的 "flavor of the month" 担忧、`otohadorm5` 的跑团禁令。
9. **Makoto 线**：`toukadorm1` 的私下讲义。
10. **Niki 旧恋情确证**：`norikofirsthall` 由当事人妹妹之口盖章 "It definitely happened and it was a huge part of all of our lives."

## 五、未解伏笔

1. **Yasu 手套里的旧报纸剪报**内容未揭晓——她说是"所有烦恼的答案"。
2. **Noriko 在巴士上看到的人是谁**：redaction + STOP PLAYING 强制中断；续篇在 `restofnorikorestx`。
3. **"Would you like to phone?"的电话打给谁**：系统故障式演出暗示存在干预叙事的外部存在。
4. **"房子"原型的真身**：涂鸦/电视画面/艺术电影三处呼应，尚未揭晓。
5. **Nodoka 发作为何使用 Ami 觉醒同款资源**：两者机制的共同来源未明说。
6. **Yasu 的雪融倒计时**："His slumber will come to its end"——季节转换与"祂"的身份。
7. **Touka"气走 yet another teacher"的具体历史**：话头即断。
8. **双版本 Touka 图像**（`realtoukaimage` vs `toukaolddis8`）的完整含义。
9. **Io 的自毁倾向**（四个美工刀、"practically dead already"）的后续。
10. **Uta 的家庭线**：兄弟杀人未遂入狱、母亲一系接连恶疾、亡祖父之死等背景尚未充分展开。
11. **Kirin 的 "dissect her" 违约条款**：黑色玩笑还是真 flag。
12. **Noriko 自述"角色弧线基于记忆恢复"**：她的下一阶段（向父母姐妹证明自己没疯）尚未发生。
13. **Sensei 曾是作家**（Futaba 情报，经 Nodoka 转述）与旧补习班岁月的全貌。

---
> 按源行号检索本角色 label，见 `索引/Dorm2索引.md`。
