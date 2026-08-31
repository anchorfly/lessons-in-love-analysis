# Touka 事件线全析

> 源文件：ToukaEvents.rpy ｜ 共 26 个剧情 label（含 2 个路由入口、3 个电话占位、1 个过渡节点，实际叙事 label 20 个）
> 定位：Tomonori 与 Tsubasa Tsukioka 的长女、Tsukioka Foundation 的继承人，生活在封闭城市 Kumon-mi。她与主角之间是全游戏落差最大的一条线——不是穷女孩仰望老师，而是主角被拖进一座金丝笼。这条线的叙事引擎是双向的：她学习平民世界的规则，主角则被迫承认自己对她的情感既包含欲望也包含依赖。
> 阅读提示：台词直引保留英文原文，以 `label` 名为唯一锚点，不标行号；`to`=Touka、`tb`=Tsubasa（其母，主母本人）、`tk`=Tsukasa（其妹）、`s`=Sensei、`N`=旁白、`n`=Noriko、`t`=Tsuneyo、`ya`=Yasu、`mak`=Makoto、`ka`=Karin、`q`=未知实体；lust 内容按叙事功能抽象概括，不复述细节。

---

## 一、角色基本盘

- **身份**：她自述 "as the eldest daughter of Tomonori and Tsubasa Tsukioka"（`toukadorm25p1`），是 Tsukioka Foundation 的继承人（`toukaspring3` 中她以 "the heir to the Tsukioka Foundation" 自称）。母亲 Tsubasa 即主母本人；父亲 Tomonori 在家族泳池之夜缺席，Tsubasa 的原话是 "Seeing as your father was unable to attend"（`toukadorm25p2`）。
- **教养轨迹**：自幼被课程填满——她咆哮 "There were so many lessons about forks! Why?!"（`toukadorm25p1`），并因主角分不清沙拉叉与汤匙而反复取笑他。她有一架"漆着自己名字的直升机"——"I have a helicopter with my name painted on it."，追问之下答 "It was a present for my tenth birthday."（`toukaspecial15`，**十岁**生日）。
- **性格底色**：极度天真但绝非愚笨。她对常识的无知来自真空环境，而非智力——她自己把一切归因于运气与出身："Because I'm lucky...and happened to be born into a family that had already carved out a sizable part of this world."（`toukaspecial15`）。她"极其厌恶撒谎"："I utterly despise lying and found no reason to in this situation."（`toukastreets1`）。需要说明的是，Tsubasa 那句 "she's actually quite the little genius for her age...Her memory is near photographic as well" 说的对象是**妹妹 Tsukasa**（`toukaspecial15`，以 `tb` 说出、回应主角对 `tk` 的评价），与 Touka 无关。
- **核心矛盾**：金丝笼的门一直开着，她却从未想过离开——"What can not be seen is the cage that keeps me from taking flight." / "The most depressing part is that the door of that cage has been open this entire time. And I've been perfectly capable of leaving it."。她的自我认知是继承来的："Decades and decades of customs and expectations and *rules* flow through my blood like crocodiles in the Nile."（均见 `toukadorm25p1`）
- **对主角的态度演变**：从"被捉弄的试验期学生"（她主动称之为 "A trial period it is, then..."，`toukastreets1`）→ 唯一让她感到"无力"的人（旁白 "I'm likely the first person she's ever felt powerless against."，`toukaspecial15p3`）→ 直白告白 "I *like* you."（`toukaspring2`）。
- **关键关系网**：Yasu 是她的宿舍室友（`toukadorm10` 中 Tsubasa 称 "Touka's roommate"；`toukaspring3` 中夜里应声的正是 Yasu），并被她当面称为 "my best friend"（`toukaspring7`）。与母亲 Tsubasa 亲密却渐生裂痕——她指责母亲对自己隐瞒公寓计划的细节（`toukadorm25p3`）。与 Tsukasa 疏离且互相刺伤（`toukadorm25p2`）。与 Makoto 在 `toukaspring3` 中因这次成人用品店之行正面交锋。

---

## 二、love 线逐事件脉络

### `toukastreets` ／ `toukaarchery`（路由）
纯跳转入口。`toukastreets` 按 `touka_love` 与前置标志分流至 `toukastreets1`、`toukastreets5`、`toukaspecial15`，条件不满足时落到 `toukastreetsgen`。`toukaarchery` 按 `tsubasa_love`/`touka_love` 分流至 `tsubasadate20`、`toukaarchery20`，再按 `chap4active`／`chapthreeactive` 落到 `toukaspringarcherygen` 或 `toukasummer2archerygen`。可见 Touka 的日常事件挂在"街道"与"弓道场"两套地点系统下。

### `calltoukamorning` ／ `calltoukaafternoon` ／ `calltoukanight`（电话占位）
三个占位分支：若 `toukablock == True` 则拒绝拨号并退回电话菜单；否则拨号后无人接听，同样退回菜单。唯一的例外是第四章的下午分支会跳 `toukaspringnoongen`。

### `toukastreetsgen`（泛用晨间散步）
占位性质的泛用事件：主角陪 Touka 逛城讲解常识。价值在旁白的两句定性——"there's an overwhelming feeling of her desire to learn and to understand"，以及黑屏后紧接着的转折 "Or die in the process, because living isn't that easy."，再以 "I wonder what will happen?" 收尾。该段位于 `if bonus` 块之外，两个版本共有。

### `toukastreets1`（自动售货机初遇）
清晨主角撞见 Touka 与"peasant drink dispenser"搏斗。她坦白此行目的：母亲要求她融入社会。主角随即展开全游戏最经典的恶作剧——谎称售货机是声控的、需要念咒语，咒语末尾一句是：

> s: And surrender my rights and my body to the man beside me.

Touka 一字一句跟读直到察觉，当场落泪："I trusted you and you took advantage of me."主角发现她用的纸币破旧不堪——钱来自 Uta。他替她投币买了盒装绿茶，两人坐上长椅。她坦言与男教师在公共场合独处的不道德感，并提到自己在道场见过主角和 Ayane 在一起。事件以"trial period"协议收尾，她还特别要求不要再叫她 princess——"That word bothers me even more than your compulsion to keep addressing me by different names."
**分析**：初遇事件一次性立住了整条线的三根支柱——她的天真可欺、她的绝对诚实、以及主角"利用天真"的掠食者姿态。她哭泣不是因为被骗钱，而是因为信任被滥用；这个细节让后续所有"她其实什么都懂"的反转都有了根。

### `toukastreets5`（旧城区之旅）
雪天的第二次散步。Touka 承认仍在等主角，并暴露她至今相信售货机咒语是真的。主角故意把她带去最深处——旧城区："Not a theme park. Just a low income area where people even worse off than me live."她的第一反应是 "Is this...some sort of theme park? What am I looking at here?"，随后得知班上的 Tsuneyo、Chika 等人就住在这里、还在照顾一名免疫缺陷的小女孩时当场落泪，并向一位流浪老人分零食。
此处出现本线最诡异的一处文本：屏幕闪过一串十六进制：

> N: 73 75 64 64 65 6e

解码为 **"sudden"**。紧接其后场景无过渡地切到 Noriko 的便利店，主角自述记忆断裂："I remember walking around with Touka, but I don't really remember anything about coming over here."——这是主角"断片"机制在本线的一次显性发作，且用密文做了标记。
便利店内 Touka 把陈列的安全套当糖果差点吃掉（该段在 `if bonus == True:` 分支内）。回程旁白给出罕见的温柔评价："And a side that, while overwhelmingly naive, is still endearing."

### `toukadorm10`（宿舍夜访·睡衣派对搅局）
主角敲开 Touka 宿舍门，却发现 Tsubasa 在场——母女每月一次的 "monthly slumber party" 被他撞破。为掩饰来意，玩家在三个选项（体育／经济／畜牧）中任选其一编造"辅导"借口，其中畜牧一项引发"Touka 勒死小猫"的荒谬指控（主角原话是抱怨她 "strangling all of the kittens we bring in for educational purposes"）。Tsubasa 半信半疑："You know I don't actually buy that. Right, dear?"Touka 只能低声说 "*Run.*"
本事件埋了两处设定：其一，Tsubasa 追忆全家度假屋时提到 "the joyous ruckus caused by an expensive band of animatronic animals"，主角因此发愁该拿什么给 Touka 展示"平民的夏天"——"平民暑假体验课"就此立项，直接引出 `toukaspecial15`。其二，Tsubasa 顺口说 "I quite like Touka's roommate actually. Her reaction to seeing the manor for the first time was adorable."——这位室友即 Yasu。

### `toukaspecial15`（全家地铁之旅·上）
暑假体验日，主角等来的却是 Tsukioka 全家。Tsubasa 盛装出席、脖子上戴着家徽，被指出过于隆重时答 "I...can't simply leave the crest at home like Touka and Tsukasa do. Not as the wife of the Tsukioka Foundation's chairman."Tsukasa 点名要坐地铁："What screams 'poor people' louder than a bunch of sweaty commoners paying money to get crammed into a rectangular metal box underground?"
车厢内闹剧连连后，Touka 与主角并肩坐下，先说 "I have many things that others could only dream of due to no hard work or...work *at all* on my own."，接着是一段自我剖白：

> to: I'm a [teenage]girl on the cusp of becoming a woman and I don't even know how to ride the subway or...what the other girls in my class do to celebrate their summer vacations.
> to: I'm entirely hopeless when torn out of my element.
> to: And yet all you do is toy with me.

主角的反应是装作没听见——

> s: Sorry. Did you say something? I wasn't paying attention.

她的回击是 "Rude. I was attempting to have a moment with you."，并正告他母亲是她生活的一部分、他必须接受。事件结尾，她注意到："You called me Touka again."——名字梗第一次被她反用来表达亲近。

### `toukaspecial15p2`（娱乐区·三分支）
列车到站，全家走上地面，"a flood of multicolored light overtakes us- they realize just how out of place they are in this world."Tsubasa 惊问 "This isn't one of those 'Red light districts' I've heard about, is it?"随后进入三分支选择：

- **Touka 分支**：格斗游戏教学。她菜得惊人，主角放水让她赢——"that pride is quickly healed by the sight of her literally jumping for joy."
- **Tsubasa 分支**：酒吧闲谈。Tsubasa 自述年轻时擅长弹珠台、也曾偷偷溜出去玩，感慨 "It oftentimes feels that I may have...wasted away my youth to some extent."
- **Tsukasa 分支**：招募主角当管家（所有管家必须叫 Jeeves），并以"将来可以帮你埋尸"的条件成交。她顺口透露："She says you're the best teacher she's ever had."——Touka 在家里如此评价主角。

### `endoftoukaarcade`（过渡节点）
全家好感度各 +1，跳转 `toukaspecial15p3`。

### `toukaspecial15p3`（塔可摊与归途）
"railing" 双关闹剧、墨西哥塔可摊（Touka 指着某处问 "I believe that is the...taco bone?"），以及塔可摊老板兄长"被女生躲避球砸死"的黑色插叙之后，是本事件真正的核心：归途旁白里主角第一次严肃自问她为什么喜欢他，并给出一个冰冷的答案：

> N: I'm likely the first person she's ever felt powerless against.
> N: Maybe that powerlessness excites her.

随后 Touka 主动谈起童年："No. I wouldn't say any of my childhood was wasted."她承认希望当年有更多选择由自己做，但拒绝把那些年称为浪费——因为那等于否认现在的自己。她还追问主角是否认为她是个好人，并给出另一句时间感很强的话：

> to: Only a small portion of my life will be spent in this state, you know.
> to: I'll be an adult for the vast majority of my time on this planet.

——这句的所指由她紧随其后的一行明确限定为"少女期只占人生一小段"，与死亡无关。事件以她罕见的柔软收束："deep down in this...*suspiciously hard* chest of yours, there is a heart."

### `toukaarchery20`（弓道场的质问）
清晨弓道练习，Tsuneyo 在场自报 "I am Tsuneyo Tojo, slayer of shapes!"。Touka 对主角近期频繁出入弓道场、并与她母亲过从甚密表达不满。主角以史上最差开场白破局："Just so you know, I haven't boned your mom."
随后主角向她和盘托出 Tsubasa 的公寓计划——以及 "Chika...kind of thinks that we're dating."。Touka 的回应冷静得可怕，一针见血指出他不愿让 Chika 搬近的真实心理，然后奉上建议：

> to: Then, I think you need to grow up.
> to: Every last bit of it makes *your* life worse and everyone *else's* life better. That is essentially a narcissist's Kryptonite.

事件结尾旁白做了一段自嘲式的比喻：把烦恼想象成液体，说 Tsubasa 的皮肤是疏水的——"And the fourth is wrapping back around to my liquid problems and finalizing the comparison by telling you Tsubasa's skin is hydrophobic." / "Her daughter's is not."旁白自己也标注了这段比喻 "may or may not be symbolic in some sort of way"。
**分析**：这是 Touka 第一次以成年人姿态反向教育主角。她不天真，她只是没见过世界。

### `toukadorm25p1`（赴庄园路上的金丝笼独白）
Touka 盛装邀请主角同行去庄园处理"重要事务"（她以为的家庭会议）。途中对话是全线的灵魂段落。她先抱怨 fork 的课程，随后自述被预定的人生："I suppose you could even say I lack the freedom to discover who I am on my own as it was already predetermined the moment I entered this world."以及那句核心比喻：

> to: What can not be seen is the cage that keeps me from taking flight.
> to: The most depressing part is that the door of that cage has been open this entire time. And I've been perfectly capable of leaving it.
> to: Decades and decades of customs and expectations and *rules* flow through my blood like crocodiles in the Nile.

话题转向联姻：主角提起 Tsubasa 说过曾为她物色过 "suitors"，她的回答冷硬——"I would have followed through with it if it needed to be done."但紧接着给出关键反转：

> to: You see, there's no one here who could elevate our family any further. At least not with the city closed-off. So I'm free to marry someone I love instead.

封城反而解除了政治联姻的义务，"为爱结婚"第一次成为她的可选项。段末她拿 Tsukasa 打趣主角的取向，引来妹妹本人登场。

### `toukadorm25p2`（婚约闹剧·泳池房）
偷听了全程的 Tsukasa 身着泳装杀出，宣布 "I am getting engaged."，理由是 "if it would get Onee-sama and Mother to begin taking me seriously, so be it."这场闹剧撕开了姐妹关系的旧伤："you never make mistakes because you're the apple of Mother's eye and *I* am just the butt of all of your jokes."以及那句直白的 "Is Jeeves a lolicon?"
前往泳池路上旁白捕捉到 Touka 的异常："What *is* surprising, though, is Touka's sudden shift in demeanor."，并明说 "I doubt it's jealousy or fear that I would *actually* take her sister's uncallused hand in marriage, but it's definitely *something*."——文本给出了排除项（不是嫉妒、不是恐惧），但没有给出答案；这份情绪 "dissipates the moment chlorine meets our nostrils"。泳池边 Tsubasa 打招呼时脱口而出 "Oh! Girls. And Ak- *ahem.*"——主母又一次险些叫出主角真名。

### `toukadorm25p3`（复制道场·膝枕·母女浴谈）
"重要事务"原来是 Tsubasa 安排的家庭泳池之夜（她对女儿撒了谎）。Touka 把主角带进宅邸内一比一复制的道场——"I have not only replicated the dojo we had our first encounter in, but I have grown so familiar with it over time that it is now like a second home to me."其用途是练习社交。
比试中她一记踢击将主角踢晕，醒来时正躺在她的膝枕上——"My head is rested on the lap of a beautiful girl- who's gently stroking my hair and completely ignoring the fact that she knocked me unconscious with a single kick just moments ago."随即被家人打断。
夜间母女泡汤戏是本线最惊悚的设定揭露：Tsubasa 以近乎教唆的口吻鼓励女儿与主角发生关系——"I simply mean that knowing he trusts you will make it easier for the two of you to sleep together."，并透露按摩员工服务是这个家族世代相传的传统："This goes back generations and generations, Touka. It's not a new thing."Touka 的回答掷地有声：

> to: This tradition...ends with me.

同一场戏里，Touka 还当面拆穿了母亲把公寓楼改作 Chosokabe 姐妹安置点的计划，Tsubasa 则用 "We're...*partners* of sorts." 形容自己与主角的关系，并补了一句 "Though, I doubt he'd say the same if you were to ask him."

### `toukacamp1`（露营深夜来电）
野营中的主角深夜致电 Touka，以"pepperoni fucking"订餐恶作剧开场，母子俩（Touka 与接电话的家人）认真讨论起这道"菜"与配送时间。玩笑退潮后是全线最坦诚的电话：

> s: I kind of just wanted to hear your voice.

但 Touka 随即清算他被"冻结"两个月间对她的忽视——"Apology for setting my mind ablaze during your two month absence."，并逼他表态。两人谈定 90/10 的分工方案，约定周六的"谢罪约会"，最后她却不肯挂电话：

> to: Stay on the line a little longer.

旁白的收尾冷酷而准确："I want to keep her close. Just as a different sort of tool than I'm used to."

### `toukaspring1`（谢罪约会）
周六之约从互相尴尬的电话开场——主角干脆挂断重来："I hang up so I can completely restart this phone call in a way that is hopefully much less awkward."地点是"那个"自动售货机——"There's only one vending machine that holds any sort of significance for us"。她单方面宣布这就是约会："if that word does not accurately describe what's truly happening here, you can internalize it, for doing the opposite will only make me feel unwanted."
午餐时的"疼痛"对话是本线哲学浓度最高的片段：

> to: But it's also because of you that I'm beginning to understand what "pain" is at all. And I can't quite tell if I like it or not.
> to: The parts where it feels good.

餐厅里她提出正式请求：让主角停止理会她母亲——"Sensei...all I want is for you to stop giving her the time of day."并点出一件她认为不对劲的事：Tsubasa 对她私生活突然产生全方位兴趣，"she rarely expressed any interest in that until I began spending time with *you*"。她有猜测但不能在餐厅里说——悬念留待 `toukaspring7` 引爆。席间还有一则炸鸡梗：她把某样东西认错，主角纠正 "That is fried chicken, Touka."

### `toukaspring2`（庄园卧室·告白与"母亲"炸弹）
开场大段旁白自我剖白：他反复告诫自己 "Touka Tsukioka is a girl. Not a woman. Not a mother. She's a girl. Plain and simple."，却又承认身体与恐惧都在把他推向她——"It's an endless cycle of fear and love, spearheaded by a girl who doesn't even know the power she wields."
回到庄园后，Tsubasa 当着女儿的面引爆主角私下说过的话："You've already made it quite clear to me that you have no such intentions with Touka. What with seeing her more as a 'mother figure' and all. Correct?"Touka 心碎离场："Good night, Sensei. I apologize for misinterpreting just what sort of *relationship* we had."母女争执后主角进房收拾残局，被 Touka 反扑压倒在床上。她逼问到底，主角坦白这种错位感知的来处："I was feeling lost and scared and you were just...the one I looked for."于是有了全线最直接的告白：

> to: I *like* you. And maybe this is inappropriate for me to say as your student, but that's not stopping anyone else and it just isn't fair if I'm the only one keeping it to myself at this point.

她同时划出底线："There needs to be something for *me*." / "I'm happy to give, but not without something in return. And what I want in return is far more intimate than a lap pillow."主角的回答诚实得残忍："I can't change the way I see you. But I also can't deny the fact that I want to fuck your brains out."她接受了这个畸形的平衡，并索要一个新的称呼收尾：

> s: Call me Akira from now on.
> se: Come to bed, Aki-kun.

同一场戏里，Tsubasa 曾问过主角一句："has Touka shown you where to find our massage parlor yet?"
**分析**："Akira" 真名在此首次由主角亲口授予 Touka——与她母亲屡次失口喊出 "Ak-" 形成镜像：这对母女在争夺同一个名字的使用权。

### `toukaspring3`（Makoto 视角·成人用品店）
本集以 Makoto 为视点人物，开场旁白直接打破第四墙吐槽剧情节奏——"We're well past due for a reset by now"，并演示性地"让一本书吞掉 Makoto 再吐出来"，声称这样就能制造事端。正题是 Touka 乔装（台词署名先为 `q`）光顾宫村家的成人用品店，被要求先跳"色情舞蹈"、又被安利 NordVPN，随即被 Makoto 当场点名："Why are you here, Touka?"——理由是全世界只有她会中这个圈套。
来店的原因被她自己说破：上网流量并不私密，"it was quite difficult having to explain my search history to my overly-curious mother."她想找"教育材料"，最终只带走绿茶。在 Makoto 房里，Makoto 自称与主角有多年的性关系——"I've been having sex with him for years."，并直言 "Which is why I'm hoping you fail."。Touka 仓皇告辞，回到宿舍后在床尾暗格里翻找尺寸匹配的玩具——"she checks to make sure her roommate is asleep before unlocking a secret compartment built into the foot of her bed"，结果不小心启动了一个，把自己吓到，最后"She once again goes to sleep without using any of them."
**分析**：本集以喜剧外壳完成了两件事——确认 Touka 已进入性觉醒的临界状态，以及通过 Makoto 之口向玩家（和 Touka）展示主角情史的规模。

### `toukaspring4`（新希望教堂地下）
Yasu 以"仪式"为名把两人骗进教堂地下，誓言内容是 "Make a baby!"。闹剧之下是两条暗线：其一，Touka 提到 Yasu 的精神分裂——"If I had to take a wild guess, I imagine it's due to some *other* strange ritual or game Yasu's schizophrenia has induced."；其二，主角察觉她有事瞒着——"Is something going on with Tsukasa?"，她拒绝透露，理由冰冷而精准：

> to: You're the type of man who destroys everything he touches. There is *nothing* that is safe with you.

随后是 Yasu 信仰体系的总爆发：谎言被拆穿后她崩溃嘶喊 "I don't understand anything! I'm a useless messenger! A broken doll! I don't deserve your kindness! I don't deserve your love!"。主角临别时请她向 "Etinsib Ziwa"（她的神）带话——"tell Etinsib Ziwa I'd like to actually speak with him some day."

### `toukaspring5`（客厅问答·冒名顶替者）
上半场：Touka 正式向母亲询问关于主角的事，Tsubasa 话锋突变——

> tb: Your charade is as flimsy as a wet paper bag, darling. Why not drop the act now and show me who you really are?

坐在她对面的"Touka"是一个标注为 `q` 的未知存在。Tsubasa 冷静应对："You think I wouldn't recognize someone masquerading as my own daughter?"q 问出 "Are you happy here?"，自称 "wanted to save the world"，Tsubasa 反问 "**Which one?**"，并说："It's been decades since the last time I encountered one of you."随后的谈判内容被旁白刻意跳过（"Blah, blah, blah. Then some stuff happened."）。
下半场视角切回 Touka：她与 Karin 讨论"附身"现象，称这在全班几乎是常识——"It's practically common knowledge to all of us at this point that he has bouts of...*decreased* identity. Though, the reasons for this remain as elusive to me as ever."她还补了一句让旁人难受的自评：主角在她面前很少那样表现，"*Probably* because he thinks I'm his mother and is comforted by my existence. I hate it."Karin 的反应高度可疑——先否认 "No!"，随后改口 "...maybe."，被 Touka 点破 "You *have* witnessed it, haven't you?"；场景结束后只剩她一句 "Maybe...he doesn't..."，旁白则以一句 "Uh-oh." 收尾。本集结束时 Touka、Yasu、Karin 三人好感各 +1。
**分析**：本集是 Touka 线与游戏终极谜团的接口：q 实体、主母的超自然知识、Karin 的隐藏知情、主角的身份切换，四线在同一集交汇。

### `toukaspring6`（公寓同居日常）
Touka 以 "Jessica" 这一化名霸占主角的公寓（还雇人打扫、添置了地毯），坚持 "Who's Touka? My name is Jessica."，Yasu 同在。冰箱里的安全套（主角一句"用后要冷藏"的玩笑）与《电锯惊魂3》观影构成日常喜剧底座。核心时刻有两个：其一是看电影时她若无其事地牵住他的手——"it's a bigger step than even sex for me"；其二是她的恐怖片美学宣言，实际是对主角的判词：

> to: Even more so in scenes that seem otherwise normal and tonally light. Because, just like in reality, it's what lies *beneath* the surface that is normally the most disturbing.
> to: And I could see myself falling for a monster under the right circumstances.

Yasu 则贡献了新怪谈素材 "Wilford Blackhole Hands"，并在听说主角知道这个名字后警告他别去神社："You shouldn't go there. It's *bad.*"临别时 Yasu 说明自己留下是为了提高概率——"the likelihood of Touka receiving your light goes *way* up if I am not around to ruin things!"

### `toukaspring7`（夜行·债务动机·未竟告白）
开场是恋尸癖玩笑，顺带回收了售货机咒语与冷藏安全套两个旧梗——"I also talked you into thinking condoms need to be refrigerated just a couple of hours ago."中段 Touka 给出对母亲执念的分析框架：

> to: It seems almost *debt-*motivated to me. Similar to the ways in which she's apparently attached to Yumi's mother.

主角追问"她欠 Yuki 什么债"，Touka 承认母亲不愿谈过去，但断言 "I actually think she'd be quite distraught if anything happened to either you or *Yuki*."
随后是重磅爆料：

> to: It was just a rumor. Quite a morbid one, at that. Something about her body being buried beneath my family's sakura tree.

主角失态。Touka 补充：传闻不实——"It's not true. My mother assured me of it."——但 Ami 母亲留下的一首诗写到葬于樱花树下，"led *Nodoka* of all people to my family's manor."她顺势追问："Is Ami *your* daughter? Or are you really just her uncle?"，得到斩钉截铁的否认 "She's *not* mine."
接着她直面 Tsukasa 的婚约危机，并提出方案：不必真的越界，只要让世人（包括 Tsubasa 自己）**相信**已经越界就够——"Perhaps it's more important for people to *believe* that you and Tsukasa have crossed some sort of line than it is for you to actually *cross* it?"随后以《Twilight》设问：

> to: If someone you cared for was dying, and the only way to *save* them was by sinking your fangs into their flesh, could you do it?
> to: It would just also change the person you bit for the rest of their life.

主角反问"为什么是我"，她答："you *are* a part of us, Sensei. *Akira.*" / "Whether you like it not, we've already abducted you. We're just kind enough to let you roam around on your own."
本集后段另有一条分支：若 `tsukasaspring6 == True`，两人夜行至高处看夜景，谈笑间以"吸血鬼"比喻互相试探；否则走另一段对话——她说 "I feel as if there's something I want to say here. And that, in another life, I probably could. Probably *would.*"，主角回 "I've questioned everything over the last thirty seconds and just don't really think I have it in me to actually do that now."，并提起她"可以上任何屋顶，除了最重要的那一座"却拒绝解释；她答 "For I feel quite compelled to say something very stupid right now."——两人各自守住了各自的秘密。两段之后共用同一收尾："We stay up there for another hour or two, just looking out at the lights and wondering if and when they'll turn off."

### `toukaspring8`（小巷·自动售货机）
开场旁白先讲了一大段"我把她送回公寓、各自道别"的抒情段落，然后自我拆穿：

> N: I am a liar.
> N: None of that ever happened.

真实情况是——"We *did* get within several blocks, though, and are now pressed against a vending machine in an unassuming alley just seconds after encountering it."月与尘的比喻体系贯穿全场（"But I, the moon, and she, the dirt, have little in common but the ways in which we glow"），随后是本线尺度最大的亲密场景（互抚、手指等），两人还拿自动售货机继续打趣。主角开出"忍住五分钟"的条件，结果被 Yasu 开门打断——"Four minutes and forty-five seconds..." / "Could you really not just...round up?"
结尾三连值得记录：Touka 的 affection 与 lust 同时上涨；Yasu 高呼 "Congratulations on being one step closer to salvation!"；Touka 回以一句：

> to: Are you *sure* we need to save him too?

---

## 三、lust 线概貌

Touka 的 lust 内容几乎全部内嵌于 love 事件，未独立成篇，其叙事功能可归纳为五类：

1. **无知型喜剧**（`toukastreets1` 的咒语、`toukastreets5` 把安全套当糖果、`toukaspring3` 的成人用品店、`toukaspring6` 的"安全套要冷藏"）：用她的性知识真空制造笑点的同时，持续量化她与常人世界的距离。
2. **权力翻转型**（`toukadorm25p3` 踢晕后的膝枕、`toukaspring2` 中被她扑倒压在床上）：她在这类场景中主动夺取主导权，与她"从小到大几乎一切都被安排"的处境形成对照。
3. **试探边界型**（`toukaspring2` 的卧室对峙、`toukaspring7` 的言语擦边）：每次身体推进都与情感条件同步定价——她的原话是 "There needs to be something for *me*." / "I'm happy to give, but not without something in return."
4. **传统批判型**（`toukadorm25p3` 的浴室对话）：核心不是欲望，而是世代相传的按摩员工制度。Touka 的 "This tradition...ends with me." 是全线最响亮的反抗宣言。
5. **完成态型**（`toukaspring8` 的小巷）：作为 love 线累积的泄洪口存在，而它被 Yasu 打断、被"五分钟之约"卡住的结构本身就是叙事判断——这段关系还没到"完成"的时候。

---

## 四、与主线/元叙事咬合点

1. **"Akira" 名字的争夺**：Tsubasa 在 `toukadorm25p2` 失口喊出 "Oh! Girls. And Ak- *ahem.*"，主角则在 `toukaspring2` 将真名主动授予 Touka（"Call me Akira from now on."）。名字成为母女暗中角力的信物。
2. **q 实体入侵**（`toukaspring5`）：冒充 Touka 的存在、主母"几十年前遇到过你们这类"、以及被旁白跳过的谈判，直接接入游戏的超自然主线。Tsubasa 那句 "Which one?" 表明她口中的"世界"不止一个。
3. **主角的"身份切换"被第三方命名**：Touka 在 `toukaspring5` 中称之为 "bouts of...*decreased* identity"，并说这在全班已是常识——把主角的叙事断层（如 `toukastreets5` 里那段走进便利店的记忆空白）从私人怪癖升格为公共现象。Karin 在同一场景的可疑反应为其个人线预埋钩子。
4. **Ami 母亲之谜**：`toukaspring7` 中樱花树下的遗体传闻（Touka 转述母亲的说法是假的）＋遗诗引 Nodoka 登门，把 Tsukioka 家的庄园变成了主线丧葬谜团的物理坐标。
5. **Tsubasa 与 Yuki 的旧债**：Touka 用 "*debt-*motivated" 概括母亲对主角与对 Yumi 之母 Yuki 的态度，这是理解 Tsubasa 全部干预行为（公寓计划、对主角的兴趣）的钥匙形伏笔。
6. **世代传统**：`toukadorm25p3` 中 Tsubasa 透露按摩员工服务"传了好几代"，并在 `toukaspring2` 问主角 "has Touka shown you where to find our massage parlor yet?"。这条家族制度线是 Touka 唯一的公开反抗对象。
7. **元叙事自指**：`toukaspring3` 整集以"书"为主体的第四墙演出、旁白对 mantis shrimp 的加注（"That last line makes more sense if you know about mantis shrimp"）、以及 `toukastreets5` 的十六进制密文 "sudden"，使本线成为元叙事密度最高的角色线之一。

---

## 五、未解伏笔

1. **Tsubasa 与主角的真实关系**：Touka 所说的"债务"究竟指什么？Tsubasa 自称与主角是 "partners of sorts"，却又补一句 "I doubt he'd say the same if you were to ask him."
2. **q 实体与主母的交易**：`toukaspring5` 中被旁白跳过的谈判内容——q 想要什么，Tsubasa 答应了什么？
3. **Tsukasa 的婚约安排**：Touka 提出"让世人相信越界已发生"的方案是否奏效；母亲为何"不得不这样做"，对方家族能提供 Tsukioka 家没有的什么东西。
4. **樱花树下的遗体**：传闻真伪（Touka 转述母亲断言不实）、遗诗全文、Nodoka 调查的现状。
5. **Etinsib Ziwa**：Yasu 之神是否会对主角"想当面聊聊"的请求作出回应。
6. **"最重要的那一座屋顶"**：主角说她可以上任何屋顶、除了那一座，所指何事，他随即收回——与他的过去直接挂钩。
7. **Yasu 的病例**：Touka 提到"Yasu 的医生"，却未说明她去看的是什么病、诊断由谁作出。
8. **Karin 的知情程度**：`toukaspring5` 中她对"附身"的过度反应与前后矛盾，指向其尚未揭开的秘密。
9. **Touka 的两难**：她宣称传统止于自己，又主动走进"怪物"的逻辑——当家族义务与个人欲望正面冲突时她会选哪边，这是本线留给终局的提问。

---
> 按源行号检索本角色 label，见 `索引/Touka索引.md`。
