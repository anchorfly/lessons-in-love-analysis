# Tsukasa 事件线分析

> 源文件：`游戏文本/TsukasaEvents.rpy`（4253 行，16 个 label）。跨文件核实：`chap4hub.rpy`（`endofsatch4`、`endofweekdaych4`、`nightch4`）、`chap4.rpy`（`christmasfive5`）、`ChinamiEvents.rpy`（`chinamispring5`）、`TsubasaEvents.rpy`（`tsubasaspring5`）、`script.rpy`（`afterschoolevent`）、`OtohaEvents.rpy`（`otohaspring6`）。
> 定位：Tsukioka 家次女。源文中她自称 "the second born in a family that typically only produces one heir"；Tsubasa 称她 "my youngest daughter"。
> 变量对照：`tk`=Tsukasa、`to`=Touka（姐姐、家族继承人）、`tb`=Tsubasa（母亲）、`s`=Sensei/Akira、`se`=Sekai（幽灵旁白、Ami 的母亲）、`a`=Ami、`c`=Chika、`ch`=Chinami、`n`=Noriko、`o`=Otoha、`u`=Uta、`i`=Io、`ay`=Ayane、`ima`=Imani、`mal`=Malvin（幻觉）、`taco`=墨西哥卷饼摊贩。
> 全文锚点为 label 名。`TsukasaEvents.rpy` 内 `bonus` 一词出现 0 次，不存在成人版／和谐版双分支，本文件所有内容按源文单线录入。
> 家族事实（已核验，不因本文件内容而改变）：Tsukasa 是 Tsukioka 家次女，不是 Ami 的母亲；Ami 的母亲是 Sekai；Nodoka 的母亲是 Kyoko；Otoha 读的是 Sekai 的诗（见 `OtohaEvents.rpy` 的 `otohaspring6`，Otoha 对 Ami 谈 "your mom's poetry"）；Karin 是 Kirin 的姐姐。

## 一、角色基本盘

Tsukasa Tsukioka 是 Tsukioka 家次女，姐姐 Touka 是 Tsukioka Foundation 的继承人——她自己说得很清楚："Onee-sama is the family's heir."

她的自我定位在三个 label 里被反复说出口，措辞一次比一次重：`tsukasaspring2` 里是 "As the backup heiress to the Tsukioka Foundation, I'm used to being the 'failsafe.'"；`tsukasaspring3` 里是 "I'm just a failsafe, remember? Disposable. You could lock me in a cage and none of my family would even know about it for months."；`tsukasaspring5` 里是 "The name 'Tsukioka' is far too big for a walking back-up plan like me... So maybe a new one will suit me better?"。这些说法的机制是家族继承顺位与包办婚姻，源文没有任何超出家族层面的解释。

"failsafe" 这个词不是她自创的：她说是从宅邸里那些没立缄口誓言的仆人私下交谈中听来的，并据此判断"我在这里不受欢迎"。她同样不被允许上学——按她的转述，母亲认为她比同龄女孩"太超前"、又太小而不能和姐姐同校，所以只能在家听"无聊的老人们谈无聊的事"。

她管 Sensei 叫 Jeeves，并要把他收编为 "Jeeves Tsukioka the Thirteenth"；Sensei 则回敬她 Tsurumi、Tsukasarumi 等错名。表层性格是毒舌、好胜、以财富与阶级自居、对性话题异常直接；与这份攻击性交替出现的，是她反复确认"有没有人真的想要我"。

## 二、love 线逐事件脉络

### 1. 电话路由：`calltsukasamorning` / `calltsukasaafternoon` / `calltsukasanight`

这三个 label 只做条件路由，本身没有剧情：
- `calltsukasamorning`：当 `tsukasa_love >= 1`、`tsubasaspring1 == True`、`tsukasaspring1skip == False` 且 `tsukasaspring1 == False` 时，才跳 `tsukasaspring1intro`。
- `calltsukasaafternoon`：当 `tsukasa_love >= 1`、`tsukasaspring2 == True` 且 `tsukasaspring3 == False` 时，才跳 `tsukasaspring3`。
- 三者若 `tsukasarefused == True` 就只回一句 "No."；若 `senseisad == True` 则说 "I don't want to call her right now..."；否则一律"无人接听"，退回 `callmorning` / `callafternoon` / `callnight`。

也就是说，路线推进由数值与已完成标记决定，而不是"她主动来电"这么简单。

### 2. `tsukasaspecial1`：「National Tsukasa Day」

开场是 Sensei 的牢骚：他接到 Imani 通知，有个"节日"要求他全班在场，否则他和 Imani 都可能丢工作。Tsukasa 随即宣布这天是 "National Tsukasa Day"，是她父亲为她设立的，要到下周三才结束；她让裁缝照姐姐的制服做了一套，混进公立学校"亲眼看一看平民圣地"。

本 label 的主体是群像喜剧：Imani 连出三题考她——世界最古老城市（她答大马士革，并补上耶利哥之争和母亲在 Kumon-mi 封闭前的旅行见闻）、富士山高度（3776 米，父亲答应买下山坡给她盖小屋）、谁住在北极（她答圣诞老人的作坊，众人拼命拦住 Sensei 别拆穿圣诞老人）。

中段 Chika 出现（她记得的 "Mother's onsen" 的平民女孩）。Tsukasa 差点当众说出 onsen 那场"特殊游戏"，被 Chika 捂住嘴；随后她要求把姐姐 Touka 也带去 Chika 家——"It wouldn't be fair if I got to experience something like that firsthand and she did not."。Chika 顺势把 Sensei 也拉进来当保姆，本 label 以 Sensei 答应照看 Chinami 和 Tsukasa 收尾。

### 3. `tsukasaspecial1p2`：办公室里的等待

她拒绝随车队回家，坚持要母亲亲自来接："I'm making Mother come here to get me on her own."。在等待中她说出自己不需要最高等教育的理由："I'm the second in line to inherit the Tsukioka family business, so it's not like I have to get the highest form of education when my older sister is going to be the one to take over."。

关于父亲：她说父亲总在忙，她靠对讲机联系他（"Santa brought me a walkie talkie a few years ago so I could talk to Papa whenever I wanted"），父亲不许她白天打他的手机。她把自己的性格归因为"第二个出生在一个通常只出一个继承人的家庭"的副作用。Sensei 的内心独白把她与"另一个谈起父亲就会失神的女孩"对照，并承认自己"还没那么在乎她"。

Tsubasa 赶到，为幼女道歉。Tsukasa 说 "I didn't want to go home with someone being paid to care about me."，并索要母亲答应过放学后一起吃的冰淇淋；Tsubasa 的回答是："I'm not sure if we'll have time anymore, dear."。收尾时 Sensei 承认对她产生了同情——"她不再只是我想象中那个傲慢的废物"。数值：`tsukasa_love += 5`，跳 `afterschoolevent`。

### 4. `tsukasaspring1intro`：接或不接

Sensei 拨通电话。若 `sawchinami == True` 且 `tsukasachosen == True`，进入 `tsukasaspring1`；否则他在她接起的瞬间挂断，并给出一长段自我定性（"Which is what I am. Danger. To her. To myself."、"lest the cycle continues"），随后设置 `tsukasaspring1skip`、`tsukasaspring2skip`、`tsukasaspring3skip` 与 `tsukasarefused`，跳 `nightch4`。这条拒绝路线会一次性锁死 spring1 到 spring3。

### 5. `tsukasaspring1`：面试、传送与《麦田里的守望者》

她接起电话，号码是 Tsubasa 以防他重操家教旧业给的。她要求"面试"，限他十分钟内到场、还得穿得体面。所谓"传送"是她让他闭眼想象，场景便直接切进宅邸——她承认是自己做的，但拒绝解释原理，说要等"婚后"再透露。

她的卧室有两层，她打算将来继承姐姐那间五层的；她有 143 名随从（因为七个"辞职"了），随从立过缄口誓言、只用手势交流。

文学是这场戏的核心：她一口气读完《麦田里的守望者》，给出"主人公的理想主义与犬儒并置"的读法；Sensei 在此产生闪回错位，脱口 "It's 'Sensei' while we're here, Noriko."，并对她说 "You reminded me of someone else just now."——她以为是姐姐 Touka。收尾画面停在两人的膝盖相触与 Sensei 的侵入性旁白。数值：`tsukasa_love += 1`，跳 `tsukasaspring2`。

### 6. `tsukasaspring2`：樱花厅、"failsafe" 与失控

本 label 以一段高度风格化的 Sensei 内心独白开场（血与落日、埋在阁楼地板下的笔记本），随后切回樱花树下的对话。

她先问"今天之后你还会继续教我吗"，先贬他"相当无聊"，再承认："It's better than walking by myself."、"even if you're boring, you're still less boring than an imaginary friend."。

核心对白紧随其后：她说 "As the backup heiress to the Tsukioka Foundation, I'm used to being the 'failsafe.'"，Sensei 直接制止："Don't call yourself a 'failsafe,' Tsukasa. You're better than that."。她解释这个词来自宅邸里没立缄口誓的仆人："They say all sorts of things to one another when they think no one's listening. And what I've learned from that is that I'm not very popular around here."，并补一句 "So do remember to be very nice to me even if I am your second choice."

她还讲起宅邸闹鬼的传闻：有人说女鬼是宅子初建时的园丁、死在那棵树下；也有人说她与那棵树在被移来之前就有联系、至今仍埋在树下，"the only reason she's haunting us is because her baby wasn't buried with her"。

本 label 的转折是 Sensei 的失控：内心那句 "I'm gonna fuck you so hard." 溢出成实际动作，他伸手摸了她的头，她问 "Jeeves, why are you touching my head?"，接着是门砰然关闭、他的喘息，以及一段十六进制字符串（解码为 "And this little piggy cried wee wee wee all the way home"）。数值：`tsukasa_love += 3`，随后按星期跳 `advancetotuesch4` 等推进日期的 label。

### 7. `tsukasaspring3`：平民公寓与「Take it」

开场旁白把"打电话"写成一层套一层的欲望（"I want you to want me to do it"），紧接着自己拆台："Except it's not okay at all." / "None of this is."

电话里 Sensei 说 "Lessons in Love"，触发 `theend` 卡与 "Thank you for playing!"，随后改口成"一般意义上的课"。她的"平民房间"是雇设计师照"普通平民女孩"布置的，成果包括盔甲、水晶吊灯和一整箱现钞（为了叫披萨）。

她先"开除"他，再改聘他为 "associate executive literary entertainment coordinator"，理由很直接：他只在她谈书时露出过佩服的样子。两人由此讨论文学与科学之别——她最爱的书是《秘密花园》，读起来的感觉是 "Free"；Sensei 说文学里有"人性"这一层，并承认自己当家教本是想"理解人"。

转折从这里开始：她说从没有人给过她这么多注意，"You could use me for anything you want and nobody would even care."；然后是 "I'm just a failsafe, remember? Disposable. You could lock me in a cage and none of my family would even know about it for months."，并逐句升级到 "Even if it's something evil."、"We can do it right here."、"{b}You can lock me in a cage.{/b}"，最后问出一句 "Do you...like me?"。

菜单二选一：「Pull the plug」→ `tsukasarefused = True`、`tsukasa_love += 1`；「Take it」→ `tsukasa_love += 5`。两条分支都把 `tsukasaspring3` 置为 True，随后按 `day` 跳 `endofsatch4` 或 `endofweekdaych4`。

### 8. `christmastsukasa1`：圣诞派对上的出头

开场在 Uta 张罗的圣诞卡拉 OK 与 Otoha 的斗嘴之间（"You're a terrible friend." / "I'm a terrible girlfriend too, apparently."），Malvin 的幻觉指点他去陪"那个在圣诞派对上独自看书的小女孩"。Sensei 的内心给出处境：Tsubasa 把 Tsukasa 丢给他照看，而在这里她只是"Touka 的妹妹"。

她的开场白是："I'm just trying to decipher some ancient runes that will help me cast a spell to make everyone care about me."，并在等母亲的短信与来接她的直升机。三人玩起"说出圣诞愿望"：Touka 想要"一个不把她当母亲看的老师"，Tsukasa 想要姐姐最爱的马（换来 Touka 一句 "I will cut you into pieces, you petulant whelp."），随后改口说真正想要的是"更懂穷人"。

Touka 一句失言——"I don't think it's absurd to say she 'doesn't belong' in your world"——把她击穿："Nobody wants me here."、"I don't belong here...or there or...anywhere. That's how afterthoughts work and...that's what I am."

分支条件是 `tsukasaspring3 == False`：
- 该条件成立时，她道别离场，Touka 与 Sensei 都没有追（旁白：Touka 想追却没动，因为她"一向是个糟糕的说谎者"），`tsukasa_love += 1`。
- 否则 Sensei 拦下她："But I want you here."，让 Touka 走开，并用一句 "Tsukasa, shut up." 把她噎住；她结结巴巴说出第一句 "Thank you..."，并说 "You...make me feel like...somebody actually does want me sometimes."；Sensei 答 "I'm not being paid for it, Tsukasa."。她离场前说："I think...things can only go down from here..."，`tsukasa_love += 10`。

两分支都跳 `christmasfive5`。需说明：Otoha 在本 label 中只是派对上与 Sensei 互相挖苦的朋友，本 label 内没有任何关于 Tsukioka 家关系网或诗歌的对话。

### 9. `tsukasaspring4`：目击之后，向 Chika 请教

本 label 全篇是第三人称、以 Tsukasa 为视角的叙事。她在 Chinami 房里做算术，却反复想起"几天前一个大男人把她房间当情人旅馆用"时听到的湿黏声响——即她目击了 Sensei 与某个女人在自己房里发生关系（本文件未点名对方是谁）。

她先问 Chinami "what do you know about sex?"，把 Chinami 吓得不轻；她不敢问母亲或姐姐，因为"她们大概会对 Jeeves 发火"，也因为"I feel like I...wasn't supposed to see that."。于是她对 Chika 谎称是在"家族的生殖系统讲座"里看到的，追问 "What does 'sex' feel like?"；Chika 答 "Two thousand."，并给出完整解释："Sex feels good because it's all about establishing a connection with someone you really care about."

被 Chinami 追问为什么突然沉迷"脏东西"，她说漏了真正的动机："she's already trying to arrange a marriage for me. Asking her questions about sex now might make her speed up the process."——这句话在下一个 label 里被完整展开。

### 10. `tsukasaspring5`：包办婚姻与 "walking back-up plan"

场景仍在 Chinami 家，隔壁是 Chika 与 Sensei。Tsukasa 以"科学必须反复验证"为名，缠着 Chinami 一起搜片：她输入 "Boy...fucks...girl."，找到 Pornhub，点开《Hung Stud Fucks GF's Little Sister》。她把看片当成预习——"if he's an adult, I don't want to be blindsided by not knowing what I'm doing when it comes to all this stuff."

关键交代接踵而来："My mom's trying to set up an arranged marriage. It's a pretty normal thing in rich families. And it'll help her get rid of me faster, so..."、"This is the one thing I can control, though."、"It's my duty. And...the first chance I've ever had to be useful."。Chinami 反问她为什么不拒绝，她说："I can. But why would I?... Onee-sama is the family's heir. No one in the manor cares about me. And Mother was part of an arranged marriage too when she was younger."，然后是那句 "The name 'Tsukioka' is far too big for a walking back-up plan like me... So maybe a new one will suit me better?"

她最后一句是："Without knowing what I do want...there's no point trying to fight back against the life that was chosen for me."；Chinami 哭着承诺要想办法把她留下。收尾她看着屏幕说："I just wish I got to ask him some of my questions first..."。本 label 无数值增减，跳 `chinamispring5`，由 Chinami 线承接。

### 11. `tsukasaspring6`：宅邸性教育课与追出来的坦白

开场已在冲突中：Sensei 对 Tsubasa 说 "The most of what?!"。Tsubasa 把这事包装成"要为 Tsukasa 人生的每一面做准备"，并逼 Sensei 当着她的面答疑，还把 Touka 也叫来——Touka 当场掏出一本笔记、"over a hundred questions"。

问答链条一路升级：性是什么感觉 → "There's a clear best part and it's not penetration." → 口交不是吹气而是吮吸 → Tsubasa 反问"男人平均该坚持多久" → Tsukasa 问 "Do you not have sex with Father?"，Tsubasa 答 "I do not. But you never heard me say that, do you understand?"，并补上一句 "sex doesn't always have to be about love."。

随后 Tsukasa 说 "Ugh, fine. Then you two leave me no choice. I'll do it."，并补一句"只要 Jeeves 同意，我读过同意很重要"；她的理由是 "I don't know what I want. I don't know what I'm supposed to want."。她还要求现场演示，甚至提议把 Chika 叫来——"Jeeves does it with her all the time."。Tsubasa 顺势说最合适的演示对象是 Touka，Touka 当场拉走 Sensei，骂她们把他当玩物："This man is not your plaything. He's an intelligent, creative, and kind human being who desperately wants to be better."

追出来之后是全线的情感高点。她喘着问："Did I do...something wrong?! What...was it?! Tell me...and I'll...do better...next time!"；"I really want...to learn!...I don't...want to be...useless anymore!"；"Onee-sama is...the heir! Mother is...Mother! And I'm just...a tool! Which is fine! That part...is fine! But if I am...to be a tool...I at least...want to be a good one! I want to...grow up now!"

面对 Sensei 的劝阻，她说："This is the one chance I've ever had to do something good for this family. If you take that from me, I will never forgive you."；他答："That sounds better than never being able to forgive myself for not trying."。她问 "Why are you nice to me at all? You have no reason to be."，他答：他知道在她这个年纪"被救"是什么感觉，并说 "Not all wings are made equally. Some are much sharper than others."

收尾旁白：Touka 把他送到门口，Tsukasa 含泪目送；"But I will be back. Whether I want to be or not. And I will slice up one more fledgling so badly that it will have no choice but to return to its nest forever."。数值：`tsukasa_love += 10`、`tsubasa_love += 5`，跳 `tsubasaspring5`。

### 12. `tsukasaspring7`：与 Chinami 的接吻实验

场景在 Chika 家，开场是 Chika 出门上班前的姐妹斗嘴（Netflix 被取消、不许碰 Niki 墙）。Tsukasa 提到家里的异样："Onee-sama changed her phone wallpaper to Jeeves and my mom kissed my ear the other day."，并说那大概是母亲第一次亲她，"It didn't feel like how I thought it would."

她用"每月十万日元 Netflix 费"换取 Chinami 转述 Chika 的性教育内容；她真正追问的不是操作，而是动因——她把在片里和现场看到的归纳为 "a compulsion?"。

接着她提出要和 Chinami 接吻，理由是要在嫁给某个陌生阔人之前弄清自己喜欢谁："I don't want to wait until I'm married to some random rich guy to find out who I like! My time is running out quicker than even yours is!"；"I don't have the luxury of waiting! I need to grow up now or everything I know is going to get way scarier and way harder!"

Chinami 反问她为什么非这样不可，她答："You think I'd be doing this if I was happy with how things are? No. I'm doing this because it's something new. Something I've seen make other people happy. So why not me?... Why can't I?"

接吻时她照着"参考片"用舌头，把 Chinami 吓得跳开；她的结论是 "I didn't hate it! But I didn't really love it either...so I'm not really sure what this means for me for going forward."。末尾她一句 "Fine. Then I guess I'll just have to practice with Jeeves." 换来 Chinami 的惨叫。旁白作结："That wouldn't be the last time the two of them kiss — just the last time for a while. ... The experiment worked somehow. Just not in the way that was intended."。本 label 无数值增减，跳 `endofsatch4` 或 `endofweekdaych4`。

### 13. `tsukasaspring8`：玩偶军团与 THE VOID

开场（周六 6:42 AM）把她前一晚的初吻写成行情："stocks in Tsukasa Tsukioka's virginity had rapidly soared to a new all-time high"，小字自嘲说在她"自我保护本能"启动、意识到不该跟一个被母亲告知对自己有欲望的成年男性学性事之前，还有得涨。

她先后求助三人：Touka（让她在门口站满一分钟后关门）、Tsubasa（正要带 Yuki 去看医生，建议 "Have Akira show you, then."，她反对："If Jeeves is attracted to me... it's important that I maintain a distinguished and civilized guise in his presence!"）、以及一个墨西哥卷饼摊贩（"Miss, this is a taco stand."）。

回到房间，她对 "Plush-pal Armada" 训话，要从中选出一个与她"性交"的对象。候选逐一淘汰：Trixie（资深但没看好同伴，且是女孩）、Glockenspiel（太小）、Cantaloupe（说了反犹脏话，被罚去用肥皂漱口）、Steve（龙，把女性称"货品"）。最后 Tank（一个红色外星人玩偶）因承认 "I'm unworthy, princess Tsukasa!" 而胜出。

过程被写得很具体：睁着眼时"没什么感觉，只是尴尬"；闭眼想象另一个人时感觉才来——"With Jeeves."。她磨掉了 Tank 肚子上的一颗纽扣，然后是全段的核心句："That's when it finally hit. That instinctual urge to fill a certain void within her. That sinking feeling that she'd feel more full with a true partner. With a specific partner. With Jeeves." 以及 "if THIS felt THAT good then HOW would it feel once THE VOID HAS BEEN FILLED?"

她在临近高潮时自己停下了：因为"这像是她不被允许做的事"，说不出为什么；随后躺着感到内疚、恶心、异常潮湿。收尾是她握着手机，叙事停在"扣住扳机、瞄准一只熟睡长颈鹿的头"与"可长颈鹿是站着睡觉的"。数值：`tsukasa_lust += 1`，跳 `tsukasaspring9`。

### 14. `tsukasaspring9`：Ami 的示范课与 "Farewell, lolicon."

开场（周六 1:23 PM）续用股票比喻，说她的"处女性股价"已经滞涨，并给出解释："It's not the product we wanted. It was just the idea of the product."

周六 2:45 PM，Sensei 从"性成瘾匿名互助会"回家，玄关多了一双鞋——Ami 把 Tsukasa 放了进来。Tsukasa 开门见山：她来是想问自慰，但 Ami 决定帮她；她还说漏自己在床上是想着他，并当面问 "Is it true what Mother says? That you've been attracted to me this whole time and have only been keeping it a secret for legal purposes?"

场面由 Ami 全盘主导：她让 Tsukasa 捂住耳朵，命 Sensei 脱裤子；Tsukasa 提出 "Does this not border on lack of consent?"，Ami 答 "It's called dubious consent, and it's the best kind."。期间 Sekai（`se`）的幽灵旁白插入嘲讽。Ami 边做边讲：大阴茎需要的是 "extra care."；吞咽意味着"谢谢你选择我、谢谢你被我吸引"，吐掉意味着"你恨他们"；还讲到支配与服从的角色偏好，并建议她对他"尽可能顺从"。

Tsukasa 全程提问——味道、"You...intend to f....finger me, Jeeves?"、"Is it Chinami too? ... Do you masturbate often? Should I be sending you pictures of myself to assist with that?"——并在他射精时伸手碰了一下，得出 "Oh, you're very attracted to me. Mother was right as always."

她道别并保证保密，临走留下那句 "Farewell, lolicon."。余下两人：Sensei 突然扑上去，与 Ami 反复互说 "I love you"，收在 "AND THEN EVERYONE LIVED HAPPILY EVER AFTER..." 与 `theend` 卡。数值：`tsukasa_lust += 1`、`tsukasa_love += 1`、`ami_lust += 1`、`ami_love += 1`、`god_love += 1`；按 `day` 跳 `endofsatch4` 或 `endofweekdaych4`。

## 三、lust 线概貌

Tsukasa 的 lust 数值只增加两次：`tsukasaspring8` 的玩偶自慰（+1）与 `tsukasaspring9` 的旁观与触碰（+1）。

两次都不是她与 Sensei 发生性行为：spring8 的对象是玩偶 Tank，想象对象是"Jeeves"；spring9 是她旁观 Ami 为 Sensei 口交，直到最后才伸手碰了一下。

语言主动权始终在她手里：她用提问、定价（每月十万日元换 Chinami 的"课程"）、命令（"I apologize for my interjection. Please proceed."）推动场面。但两次都在临门一脚处抽身——spring8 因为"这像是不被允许的事"而中断，spring9 以一句 "Farewell, lolicon." 离场。

值得注意的是，lust 段落与 love 段落讲的是同一件事：spring8 的 "void" 与 spring3 的 "failsafe"、spring5 的"我想变得有用"是同一套自我描述的两面——她把"被填满"和"被需要"当成同一个目标。

## 四、与主线咬合点

1. **"failsafe / backup heiress / walking back-up plan"**：三处说法（`tsukasaspring2`、`tsukasaspring3`、`tsukasaspring5`）互相呼应，机制是家族继承顺位与包办婚姻，源文没有给出家族层面以外的解释。
2. **幽灵线与樱花树的传说**：`tsukasaspring2` 里仆人口中的女鬼传闻（死于树下／与那棵树在移来之前就有联系／"因为她的孩子没有和她葬在一起"）与 Sensei 身边的 Sekai 旁白在同一 label 内并置；Sekai 在 `tsukasaspring9` 里以 `se` 直接发言。
3. **跨线收束**：`tsukasaspring6` 结束跳 `tsubasaspring5`（母亲线），`tsukasaspring5` 结束跳 `chinamispring5`（Chinami 线），`christmastsukasa1` 两分支都跳 `chap4.rpy` 的 `christmasfive5`，其余多数 label 按 `day` 跳 `chap4hub.rpy` 的 `endofsatch4` / `endofweekdaych4`——后两个 label 的内容都是"回房倒头就睡、活着真累"，然后推进到下一天，属于通用的收尾节点，并非某条角色线的结局。
4. **"THE VOID HAS BEEN FILLED"**（`tsukasaspring8`）：这里的 void 是字面意义上的性欲空洞，叙事明确写成"想被 Jeeves 填满"。
5. **"Farewell, lolicon." 与随后的告白**（`tsukasaspring9`）：同一 label 内，Ami 与 Sensei 的互诉 "I love you" 发生在 Tsukasa 离场之后。

## 五、文本未交代之处

- `tsukasaspring4` 中被 Tsukasa 撞见的女方身份，本文件未点名。
- `tsukasaspring1` 的"传送"原理：她明确说要等"婚后"才透露，本文件未解释。
- `tsukasaspring8` 结尾她握着手机要打给谁：叙事只写到"瞄准一只长颈鹿的头"与"长颈鹿是站着睡觉的"，没有后续。
- 包办婚姻的对象、时间与能否拒绝：本文件只给了她的态度（"我可以拒绝，但我为什么要拒绝"），没有细节。
- 她与 Chinami 的接吻（`tsukasaspring7`）：文本明说"不是最后一次"，但后续不在本文件内。

> 按 label 检索本角色事件，见 `索引/Tsukasa索引.md`。
