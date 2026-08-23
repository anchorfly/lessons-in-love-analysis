# Touka 事件线全析

> 源文件：ToukaEvents.rpy ｜ 共 29 个剧情 label（含 2 个路由入口、3 个电话占位、1 个过渡节点，实际叙事 label 23 个）
> 定位：Tsukioka 财团长女、家族继承人、"全熊本市最富有的少女"。她是全班（乃至全镇）阶级落差最大的一条线——不是穷女孩仰望主角，而是主角被拖进一座金丝笼。Touka 线的叙事引擎是"驯化与被驯化"的双向过程：她学习平民世界，主角则被迫直面自己对她日益复杂的情感投射。这条线同时是全游戏埋设**死亡倒计时伏笔最深**的角色线。
> 阅读提示：台词直引保留英文原文并附 rpy 源码行号；`to`=Touka、`tb`=Tsubasa（其母，主母本人）、`tk`=Tsukasa（其妹）、`s`=Sensei、`N`=旁白、`n`=Noriko、`t`=Tsuneyo、`ya`=Yasu、`ka`=Karin、`mak`=Makoto、`q`=未知实体；lust 内容按叙事功能抽象概括，不复述细节。

---

## 一、角色基本盘

- **身份**：Tomonori 与 Tsubasa Tsukioka 的长女，Tsukioka Foundation 推定继承人。注意：其母 Tsubasa 就是主母本人，而非"监护人"。父亲 Tomonori 长期缺席，被描述为忙于"过渡期"事务（[977]）。
- **教养轨迹**：自幼被课程填满——持叉礼仪、钢琴、法语、叉子名称与摆放位置（[2947]-[2953]，她自己咆哮 "There were so many lessons about forks! Why?!"）。五岁生日收到漆着自己名字的直升机（[1561]-[1563]）。
- **性格底色**：极度天真但绝非愚笨——她对常识的无知是真空环境造成的，而非智力问题。Tsukasa 评价她 "she's actually quite the little genius for her age" 时虽在说妹妹自己，但 Touka 的摄影级记忆与快速学习能力同样成立。她"极其厌恶撒谎"（[283]），这使她成为全游戏少数对主角保持彻底诚实的角色。
- **核心矛盾**：金丝笼的门一直开着，她却从未想过离开——因为教养让她"想留在笼中"。"The most depressing part is that the door of that cage has been open this entire time."（[2983]）她的自我认知是"继承来的"："Decades and decades of customs and expectations and *rules* flow through my blood like crocodiles in the Nile."（[2986]）
- **对主角的态度演变**：从"被捉弄的试验期学生"（[427] 她主动称之为 "a trial period"）→ 唯一让她感到"无力"的人（旁白推断 "I'm likely the first person she's ever felt powerless against." [2375]）→ 直白告白 "I *like* you."（[4943]）。
- **关键关系网**：Yasu 是她的受监护人与"最好的朋友"（[6656]）；与母亲 Tsubasa 关系亲密却渐生裂痕（母亲对她生活的全面渗透）；与 Tsukasa 疏离且互相刺伤；与 Makoto 因圣诞礼物与公寓事务走近。

---

## 二、love 线逐事件脉络

### `toukastreets`[1] ／ `toukaarchery`[11]（路由）
纯跳转入口：前者分流至 streets1/streets5/special15/streetsgen 四条街道事件，后者分流至 tsubasadate20、archery20 及两个泛用弓道场景。说明 Touka 的日常事件挂在"街道"与"弓道场"两套地点系统下。

### `toukastreetsgen`[21]（泛用晨间散步）
占位性质的泛用事件：主角陪 Touka 逛镇讲解常识。价值在旁白的两句定性——"there's an overwhelming feeling of her desire to learn and to understand"（[30]），以及紧随其后的冷幽默转折 "Or die in the process, because living isn't that easy."（[38]）——本线第一次出现与"活不到那时"相关的阴影。

### `toukastreets1`[96]（自动售货机初遇）
清晨主角撞见 Touka 与"peasant drink dispenser"搏斗（[108]）。她坦白此行的目的：母亲要求她"融入社会"（[141]）。主角随即展开全游戏最经典的恶作剧——谎称售货机是声控的、需要咒语：
> s: Hear my call, peasant drink dispenser. ... And surrender my rights and my body to the man beside me.（[209]-[217]）

Touka 一字一句跟读直到察觉，当场落泪："I trusted you and you took advantage of me."（[235]）主角发现她用的纸币破旧不堪——来自 Uta（[269]-[270]）。他替她投币买了盒装绿茶，两人坐上长椅。她坦言与男教师在公共场合独处的"不道德感"，并透露已从 Ayane 处听闻其对主角的感情（[373]-[375]）。事件以"trial period"协议收尾（[427]-[433]），她还特别要求不要再叫她 "princess"——"That word bothers me even more than your compulsion to keep addressing me by different names."（[460]）
**分析**：初遇事件一次性立住了整条线的三根支柱——她的天真可欺、她的绝对诚实、以及主角"利用天真"的掠食者姿态。她哭泣不是因为被骗钱，而是因为信任被滥用；这个细节让后续所有"她其实什么都懂"的反转都有了根。

### `toukastreets5`[484]（旧城区之旅）
雪天的第二次散步。Touka 承认仍在等主角（[498]），并暴露她至今相信售货机咒语是真的（[511]）。主角故意把她带去最深处——旧城区贫民窟："Just a low income area where people even worse off than me live."（[608]）她的第一反应是问"这是主题公园吗？"（[607]），随后得知班上的 Tsuneyo、Chika 就住在这里、还在照顾免疫缺陷的小女孩时当场落泪，并向熟睡的流浪老人分零食（[683]-[697]）。
此处出现全 digest 最诡异的一处文本：
> N: 73 75 64 64 65 6e（[710]）

十六进制解码为 **"sudden"**。紧接其后场景无过渡地切到 Noriko 的便利店，而主角自述记忆断裂："I remember walking around with Touka, but I don't really remember anything about coming over here."（[745]）——这是主角"断片/失忆"机制在本线的一次显性发作，且用密文做了章节标题式的标记。
便利店内 Touka 把陈列的安全套当糖果差点吃掉（[785]-[796]），羞耻到极点。回程旁白给出罕见的温柔评价："And a side that, while overwhelmingly naive, is still endearing."（[855]）

### `toukadorm10`[874]（宿舍夜访·睡衣派对搅局）
主角照例敲开 Touka 宿舍门，却发现 Tsubasa 正在场——母女每月一次的 "monthly slumber party"（[1055]）被他撞破。为掩饰来意，玩家在三个选项（体育／经济／畜牧）中任选其一编造"辅导"借口，每个选项都引发一场闹剧（包括"Touka 勒死小猫"的荒谬指控，[995]-[1003]）。Tsubasa 半信半疑："You know I don't actually buy that. Right, dear?"（[1232]）Touka 只能低声说 "*Run.*"（[1235]）
本事件埋了两处重要设定：其一，Tsubasa 提到全家度假屋里有"an expensive band of animatronic animals"（[1121]）——熊本市之外的世界细节；其二，"平民暑假体验课"就此立项，直接引出 special15 全家出行。另外 Tsubasa 顺口说出对 Yasu 初见庄园反应的欣赏（[1094]），暗示 Yasu 早就是 Tsukioka 家势力范围的延伸。

### `toukaspecial15`[1265]（全家地铁之旅·上）
暑假体验日，主角等来的却是 Tsukioka 全家——Tsubasa 盛装出席（脖子上挂着家纹，[1348]），Tsukasa 穿着挑衅 T 恤坚持"扮穷人"。Tsukasa 点名要坐地铁："What screams 'poor people' louder than a bunch of sweaty commoners paying money to get crammed into a rectangular metal box underground?"（[1378]）
车厢内闹剧连连后，Touka 与主角并肩坐下，说出全事件线最重要的一段独白：
> to: I have many things that others could only dream of due to no hard work or...work *at all* on my own.（[1570]）
> to: I just wish I had more than five years left to live...（[1580]）

而主角的反应是——
> s: Sorry. Did you say something? I wasn't paying attention.（[1584]）

他**装作没听见**。这句"还剩不到五年生命"是整条线乃至整个游戏最大的死亡倒计时伏笔，主角选择无视既是自我保护也是叙事上的刻意悬置。事件结尾她注意到："You called me Touka again."（[1614]）——名字梗第一次被她反用来表达亲近。

### `toukaspecial15p2`[1636]（娱乐区震惊·三分支）
列车坐到终点站，全家走出地面，被五彩灯光淹没——他们误入了从未见过的娱乐街区（原型接近 Rin 同款街机所在的区域，[1648]）。Tsubasa 惊问是不是 "Red light districts"（[1662]）。随后进入三分支选择：

- **Touka 分支**：格斗游戏教学。她菜得惊人，主角最终放水让她赢——"that pride is quickly healed by the sight of her literally jumping for joy."（[1927]）
- **Tsubasa 分支**：酒吧闲谈。Tsubasa 自述年轻时擅长弹珠台、也曾"偷偷溜出去玩"，感慨 "It oftentimes feels that I may have...wasted away my youth to some extent."（[1991]）两人交换联系方式时主角开玩笑担心丈夫监听，Tsubasa 认真回应 "perhaps it would be best if we didn't share that information with one another at all."（[2026]）——半开玩笑地说出了真话。
- **Tsukasa 分支**：招募主角当管家（所有管家必须叫 Jeeves，[2098]），并以"将来可以帮你埋尸"的条件成交（[2134]-[2140]）。她顺口透露关键信息：Touka 在家里说主角是她"有史以来最好的老师"（[2106]）。

### `endoftoukaarcade`[2169]
过渡节点：全家好感度各+1，跳转 p3。

### `toukaspecial15p3`[2180]（塔可摊与归途）
"railing" 双关闹剧（[2189]-[2194]）、墨西哥塔可摊（"taco bone" 惨案，[2306]-[2314]）、以及塔可人兄长"被女生躲避球砸死、葬礼只有我一人参加"的黑色插叙（[2267]-[2268]）之后，是本事件真正的核心：归途旁白里主角第一次严肃自问"她为什么喜欢我"，并得出一个冰冷的答案：
> N: I'm likely the first person she's ever felt powerless against. Maybe that powerlessness excites her.（[2375]-[2376]）

随后 Touka 主动谈起童年："No. I wouldn't say any of my childhood was wasted."（[2405]）紧接着抛出另一句时间敏感的话：
> to: Only a small portion of my life will be spent in this state, you know.（[2420]）

表面指"少女期只占人生一小段"，与 [1580] 并读则构成第二重死亡阴影。事件以她罕见的柔软收束："deep down in this...*suspiciously hard* chest of yours, there is a heart."（[2436]）

### `toukaarchery20`[2482]（弓道场的质问）
清晨弓道练习，Tsuneyo 在场表演"slayer of shapes"（[2510]）。Touka 对主角近期频繁出入弓道场、并与她母亲过从甚密表达不满（[2526]-[2528]）。主角以史上最差开场白破局："Just so you know, I haven't boned your mom."（[2610]）
随后是一场信息量极大的对话：主角向她和盘托出 Tsubasa 的公寓计划——以及 Chika 以为两人正在交往的事实（"Chika...kind of thinks that we're dating." [2694]）。Touka 的回应冷静得可怕，一针见血指出他不愿让 Chika 搬近的真实原因（怕她撞见其他女孩离开房间，[2754]-[2755]），然后奉上建议：
> to: Then, I think you need to grow up.（[2743]）

并补刀："Every last bit of it makes *your* life worse and everyone *else's* life better. That is essentially a narcissist's Kryptonite."（[2763]）事件结尾的水喻（Tsubasa 的皮肤"疏水"、女儿的不会，[2784]-[2785]）再次强调母女同构而质地不同的主题。
**分析**：这是 Touka 第一次以"成年人姿态"反向教育主角。她看穿他的能力在此全面展示——她不天真，她只是没见过世界。

### `toukadorm25p1`[2800]（赴庄园路上的金丝笼独白）
Touka 盛装邀请主角同行去庄园处理"重要事务"（实为家庭会议）。豪车途中的对话是全线的灵魂段落。她自述被预定的人生："I lack the freedom to discover who I am on my own as it was already predetermined the moment I entered this world."（[2965]）以及那句核心比喻：
> to: What can not be seen is the cage that keeps me from taking flight. The most depressing part is that the door of that cage has been open this entire time.（[2982]-[2983]）

话题转向联姻：Tsubasa 曾为她物色"suitors"（[3059]），她的回答冷硬到令人心惊——"I would have followed through with it if it needed to be done."（[3071]）但当主角追问时她说出关键反转：
> to: You see, there's no one here who could elevate our family any further...So I'm free to marry someone I love instead.（[3095]-[3096]）

封城反而解除了政治联姻义务——"为爱结婚"第一次成为她的可选项，而她不确定自己是否做得到。段末她拿 Tsukasa 打趣主角的取向（[3121]），引来妹妹本人登场。

### `toukadorm25p2`[3134]（婚约闹剧·泳池房）
偷听了全程的 Tsukasa 身着泳装杀出，宣布 "I am getting engaged."（[3181]）——对象是主角，理由是"If it would get Onee-sama and Mother to begin taking me seriously, so be it."（[3161]）这场闹剧的真正价值在于撕开了姐妹关系的旧伤："you never make mistakes because you're the apple of Mother's eye and *I* am just the butt of all of your jokes."（[3196]）以及那句直白的 "Is Jeeves a lolicon?"（[3217]）
前往泳池路上旁白捕捉到 Touka 的异常："What *is* surprising, though, is Touka's sudden shift in demeanor...But whatever that *something* is dissipates the moment chlorine meets our nostrils."（[3257]-[3259]）——嫉妒？不安？文本拒绝命名。泳池边 Tsubasa 打招呼时脱口而出 "Oh! Girls. And Ak- *ahem.*"（[3266]）——主母又一次险些叫出主角真名。

### `toukadorm25p3`[3555]（复制道场·膝枕·母女浴谈）
"重要事务"原来是 Tsubasa 安排的家庭泳池之夜（她对女儿撒谎，[3293]-[3295]）。Touka 把主角带进宅邸内**一比一复制的道场**——"I have not only replicated the dojo we had our first encounter in, but I have grown so familiar with it over time that it is now like a second home to me."（[3396]）她甚至把日常生活场景都复制进宅邸用于练习社交："How else am I meant to practice interacting with others in such locations?"（[3444]）
比试中她一记踢击将主角踢晕，醒来时正躺在她的膝枕上，旁白罕见地写下纯粹的亲密时刻："As my eyes lock onto hers, there is a moment of intense intimacy that can't really compare to anything else."（[3481]）随即被家人打断。
夜间母女泡汤戏是本线最惊悚的设定揭露：Tsubasa 以近乎教唆的口吻鼓励女儿与主角发生关系，甚至透露按摩员工服务是这个家族"传了好几代"的传统——"This goes back generations and generations, Touka. It's not a new thing."（[3833]）Touka 的回答掷地有声：
> to: This tradition...ends with me.（[3834]）

当晚母女各自回到房间，平行蒙太奇式地互相想着对方（[3884]-[3894]）——这段关系扭曲又真实。

### `toukacamp1`[3922]（露营深夜来电）
野营中的主角深夜致电 Touka，以"pepperoni fucking"订餐恶作剧开场（母子俩认真讨论起这道"菜"，[3963]-[3965]）。玩笑退潮后是全线最坦诚的电话：
> s: Because I don't have one...I kind of just wanted to hear your voice.（[4022]-[4027]）

但 Touka 随即翻脸清算他被"冻结"两个月间对她的忽视："If one second I'm important to you and the next I'm not, how is that any different than the more *playful* ways in which you tug at my strings, Sensei?"（[4128]）她提出著名的 90/10 分工方案（[4138]-[4142]），约定周六"谢罪约会"，最后却不肯挂电话：
> to: Stay on the line a little longer.（[4244]）

旁白的收尾冷酷而准确："I want to keep her close. Just as a different sort of tool than I'm used to."（[4250]-[4251]）

### `toukaspring1`[4270]（谢罪约会）
周六之约从互相尴尬的电话开场（[4306] 主角干脆挂断重来）。地点是"那个"自动售货机——"There's only one vending machine that holds any sort of significance for us"（[4337]）。她单方面宣布这就是约会："if that word does not accurately describe what's truly happening here, you can internalize it, for doing the opposite will only make me feel unwanted."（[4370]）
午餐时的"疼痛"对话是本线哲学浓度最高的片段：
> to: But it's also because of you that I'm beginning to understand what "pain" is at all. And I can't quite tell if I like it or not.（[4474]）
> to: The parts where it feels good.（[4476]）

餐厅里她提出正式请求：让主角停止理会她母亲——"all I want is for you to stop giving her the time of day."（[4560]）并点出诡异事实：Tsubasa 对她私生活突然产生全方位兴趣，"she rarely expressed any interest in that until I began spending time with *you*"（[4577]）。她有猜测但不能在餐厅里说（[4579]）——悬念留待 spring7 引爆。

### `toukaspring2`[4627]（庄园卧室·告白与"母亲"炸弹）
开场大段旁白自我剖白：他反复告诫自己 "Touka Tsukioka is a girl. Not a woman. Not a mother. She's a girl."（[4635]），却又承认身体与恐惧都在把他推向她——"It's an endless cycle of fear and love, spearheaded by a girl who doesn't even know the power she wields."（[4646]）
庄园卧室门口 Tsubasa 精准拦截，并当着女儿的面引爆主角私下说过的话："You've already made it quite clear to me that you have no such intentions with Touka. What with seeing her more as a 'mother figure' and all. Correct?"（[4756]）Touka 心碎离场："Good night, Sensei. I apologize for misinterpreting just what sort of *relationship* we had."（[4786]）
母女争执后主角进房收拾残局，被 Touka 反扑压倒在床上。她逼问到底，主角坦白这种错位感知始于万圣节之夜："I was feeling lost and scared and you were just...the one I looked for."（[4929]）于是有了全线最直接的告白：
> to: I *like* you. And maybe this is inappropriate for me to say as your student, but that's not stopping anyone else and it just isn't fair if I'm the only one keeping it to myself at this point.（[4943]-[4944]）

主角的回答诚实得残忍："I can't change the way I see you. But I also can't deny the fact that I want to fuck your brains out."（[5017]-[5018]）她接受了这个畸形的平衡，并索要一个新的称呼收尾：
> s: Call me Akira from now on.（[5061]）
> se: Come to bed, Aki-kun.（[5084]）

**分析**："Akira" 真名在此首次由主角亲口授予 Touka——与她母亲屡次失口喊出 "Ak-" 形成镜像：这对母女在争夺同一个名字的使用权。

### `toukaspring3`[5107]（Makoto 视角·成人用品店）
全游戏元叙事最激进的单集之一：开场旁白直接打破第四墙吐槽剧情节奏（"We're well past due for a reset by now" [5115]），甚至让一本书吞掉 Makoto 再吐出来演示"如何制造事端"（[5128]-[5141]）。正题是 Touka 乔装光顾宫村家的成人用品店——她因搜索记录被母亲发现（[5224]、[5738] 呼应）而急需线下咨询，却被 Makoto 用假"色情舞蹈"与 NordVPN 恶搞桥段反复戏耍。Makoto 随后声称与主角有多年的性关系（"He's screwed me so many times by now..." [5393]），并直言希望 Touka 失败（[5427]）。Touka 仓皇告辞，回家后在床尾暗格里翻找尺寸匹配的玩具，把自己吓到，最终"再一次没有使用它们就入睡了"（[5475]）。
**分析**：本集以喜剧外壳完成了两件事——确认 Touka 已进入性觉醒的临界状态，以及通过 Makoto 之口向玩家（和 Touka）展示主角情史的黑洞规模。

### `toukaspring4`[5494]（新希望教堂地牢）
Yasu 以"仪式"为名把两人骗进教堂地下牢房，誓言内容是 "Make a baby!"（[5591]）。闹剧之下是两条重磅暗线：其一，Touka 透露医生们始终诊断 Yasu 为精神分裂，但她自己已不再相信（"I...don't. Not anymore at least." [5701]），而 Yasu 最有效的那家机构"以前见过类似病例"（[5702]）；其二，她欲言又止的家务机密——与 Tsukasa 有关（"Is something going on with Tsukasa?" [5756]），她拒绝透露，理由冰冷而精准：
> to: You're the type of man who destroys everything he touches. There is *nothing* that is safe with you.（[5766]-[5767]）

牢房内的权力拉扯以她主导的挑逗收场（[5812]-[5845]），随后是 Yasu 信仰体系的总爆发：谎言被拆穿后她崩溃嘶喊 "I'm a useless messenger! A broken doll! I don't deserve your kindness!"（[5905]-[5906]）。主角临别时请她向 "Etinsib Ziwa"（她的神）带话，说想当面聊聊（[5931]）——主动靠近超自然线的关键动作。结尾那只"彩色玻璃眼睛的兔子玩偶"一路目送他回家（[5939]）。

### `toukaspring5`[5971]（客厅问答·冒名顶替者）
上半场：Touka 正式向母亲询问关于主角的事——她怀疑他与 Yasu 共享某种 "divine significance"（[6051]），并知道母亲研究过他的过去（[6056]）。Tsubasa 先是用黄段子搪塞，随后话锋突变：
> tb: Your charade is as flimsy as a wet paper bag, darling. Why not drop the act now and show me who you really are?（[6093]）

坐在她对面的"Touka"是一个标注为 `q` 的未知存在。它承认伪装（[6101]），Tsubasa 冷静应对："You think I wouldn't recognize someone masquerading as my own daughter?"（[6107]）并直接发问 "what use do you have for Akira?"（[6110]）。q 问出 "Are you happy here?"（[6121]），自称 "wanted to save the world"（[6125]），Tsubasa 反问 "**Which one?**"（[6126]）——主母不仅知情，而且几十年前就遇到过这类存在："It's been decades since the last time I encountered one of you."（[6132]）随后的谈判内容被旁白刻意跳过（"Blah, blah, blah. Then some stuff happened." [6151]）。
下半场视角切回"真"Touka：她与 Karin、Yasu 讨论"附身"现象，称主角会周期性发生 "bouts of...*decreased* identity"（[6213]）。Karin 的反应高度可疑——过度追问细节后又否认目击（"No!...maybe." [6229]-[6235]），并低声说 "Maybe...he doesn't..."（[6245]）。旁白回归时只留下一句 "Uh-oh."（[6260]）
**分析**：本集是 Touka 线与游戏终极谜团的接口：q 实体、主母的超自然知识、Karin 的隐藏知情、主角的身份切换，四线在同一场景交汇。

### `toukaspring6`[6271]（公寓同居日常）
Touka 以"Jessica"化名霸占主角的公寓（还雇人打扫、送了地毯），Yasu 同在。冰箱藏安全套骗局（[6345]-[6349]）与《电锯惊魂3》观影构成日常喜剧底座。核心时刻有两个：其一是看电影时她若无其事地牵住他的手——"it's a bigger step than even sex for me"（[6488]）；其二是她的恐怖片美学宣言，实际是对主角的判词：
> to: It's what lies *beneath* the surface that is normally the most disturbing. There's this man I know who presents himself as a regular teacher when, in all actuality, he's an incorrigible monster...（[6511]-[6513]）
> s: Yet here you are holding his hand.
> to: Why, yes. But I *like* horror. And I could see myself falling for a monster under the right circumstances.（[6514]-[6525]）

Yasu 则贡献了新怪谈素材 "Wilford Blackhole Hands"（肩上有电视、腹中有婴儿，[6533]-[6538]）与神社警告（"You shouldn't go there. It's *bad.*" [6541]）。临别时 Yasu 说明自己留下是为了提高"Touka 接受你的光芒"的概率（[6569]）——她的神谕持续为这段关系背书。

### `toukaspring7`[6608]（天台·Twilight 比喻·未竟告白）
本集是 love 线的巅峰。开场是恋尸癖玩笑（回收售货机咒语与冷藏安全套两个梗，[6634]-[6649]），中段 Touka 给出对母亲执念的分析框架："debt-motivated"（债务驱动，[6678]），并把 Yuki 母女牵扯进来——Tsubasa 对 Yumi 之母似乎也负有某种旧债（[6680]）。她追问主角是否早就认识 Tsubasa，触及他的禁区时他拒绝谈论家人（[6700]）。
随后是核弹级爆料：
> to: It was something about Ami. Her mother, specifically...Something about her body being buried beneath my family's sakura tree.（[6797]-[6805]）

主角失态。Touka 补充细节：Ami 母亲遗留的诗写到"葬于樱花树下"，正是这首诗把 Nodoka 引到了 Tsukioka 庄园（[6813]）。她顺势追问 Ami 是否其实是主角的女儿（"Is Ami *your* daughter? Or are you really just her uncle?" [6829]），得到斩钉截铁的否认。
接着她直面 Tsukasa 婚约危机，并提出"吸血鬼方案"：
> to: If someone you cared for was dying, and the only way to *save* them was by sinking your fangs into their flesh, could you do it?...It would just also change the person you bit for the rest of their life.（[6868]-[6870]）

——她在暗示：也许让世人（乃至 Tsubasa 自己）*相信*越界已经发生，就足以解决问题（[6859]-[6862]）。她提醒他 "you *are* a part of us, Sensei. *Akira.* Whether you like it not, we've already abducted you."（[6874]-[6875]）
天台夜景中两人距离无限接近告白：
> to: I feel as if there's something I want to say here. And that, in another life, I probably could. Probably *would.*（[6908]）
> s: Yeah. Which is really unfortunate, because I've questioned everything over the last thirty seconds and just don't really think I have it in me to actually do that now.（[6912]）

双向错过。当他说"有些真相会让你的人生确定无疑地变得更糟"时（[6921]），她答 "I feel quite compelled to say something very stupid right now."（[6923]）——两人各自守住了各自的秘密。

### `toukaspring8`[6942]（小巷·自动售货机）
开场旁白先撒谎再拆穿："I am a liar. None of that ever happened."（[6963]-[6964]）——真实情况是他们根本没回到公寓，在几条街外的自动售货机小巷里吻在一起。月与尘的比喻体系贯穿全场（[6945]-[6957]），随后进入本线尺度最大的亲密场景：互抚、隔衣、手指、以及被打断两次的手机（一次是 Tsubasa 的夺命连环call，[7140]-[7180]）。主角开出条件：忍住五分钟就在户外完成（[7216]），结果 Yasu 开门终结了一切（[7230]）。
结尾三连值得记录：affection 与 lust 同时上涨（[7261]-[7262]）；Touka 对 Yasu 的救世宣言回以一句 "Are you *sure* we need to save him too?"（[7254]）——她已经完全接受了"怪物爱人"的自我定位。

---

## 三、lust 线概貌

Touka 的 lust 内容几乎全部内嵌于 love 事件，未独立成篇，其叙事功能可归纳为五类：

1. **无知型喜剧**（streets1 的咒语、streets5 的"糖果"、spring3 的成人店、spring6 的冷藏安全套）：用她的性知识真空制造笑点的同时，持续量化她与常世界的距离。
2. **权力翻转型**（dorm25p3 的膝枕压制、spring4 牢房挑逗 "If I ask you to *come*...what do you do?" [5819]）：她在亲密场景中系统性夺取主导权，是其"笼中人唯一能掌控的东西就是笼外人"这一心理的外化。
3. **试探边界型**（spring2 卧室对峙、spring7 天台的言语擦边）：每次身体的推进都与情感的坦白同步定价——"There needs to be something for *me*. Do you understand what I'm saying?"（[4968]）
4. **传统批判型**（dorm25p3 浴室戏的核心不是欲望而是世代相传的按摩员工制度，[3812]-[3834]）：lust 场景被用来曝光 Tsukioka 家族把女性身体制度化的历史，Touka 的 "This tradition ends with me" 是全线最响亮的反抗宣言。
5. **完成态型**（spring8 小巷）：作为 love 线累积的泄洪口存在，其被双重打断的结构本身就是叙事判断——这段关系还没到"完成"的时候。

---

## 四、与主线/元叙事咬合点

1. **死亡倒计时**：[1580] "more than five years left to live"、[2420] "only a small portion of my life will be spent in this state"、streetsgen [38] "Or die in the process" 三处构成递进的时间阴影。主角在 [1584] 的装聋是全游戏对死亡伏笔最直白的回避行为——他知道些什么，或者害怕知道。
2. **"Akira" 名字的争夺**：Tsubasa 两度失口（[3266] "Ak- *ahem.*"、[4800] "Whatever do you mean, Akira?"），主角则在 spring2 将真名主动授予 Touka（[5061]）。名字成为母女暗中角力的信物。
3. **q 实体入侵**（spring5）：冒充 Touka 的存在、主母"几十年前遇到过你们"、以及被跳过的谈判（[6151]），直接接入游戏的超自然主线。Tsubasa 的 "Which one?"（[6126]）暗示她对"多个世界"有所认知。
4. **主角的"身份切换"被第三方命名**：Touka 称之为 "bouts of...*decreased* identity"（[6213]），并说全班早已视为常识——把主角的叙事断层（如 streets5 的记忆空白 [745]）从私人怪癖升格为公共现象。Karin 在同一场景的可疑反应（[6215]-[6245]）为其个人线预埋钩子。
5. **Ami 母亲之谜**：樱花树下的遗体传闻＋遗诗引 Nodoka 登门（[6805]-[6813]），把 Touka 家族的庄园变成了主线丧葬谜团的物理坐标。
6. **Tsubasa 与 Yuki 的旧债**（[6678]-[6680]）：主母对平民母女的"债务动机"执念，是理解她全部干预行为（公寓计划、对主角的兴趣）的钥匙形伏笔。
7. **元叙事自指**：spring3 整集以"书"为主体的第四墙演出（[5111]-[5141]）、旁白对 mantis shrimp 的注释（[6285] "That last line makes more sense if you know about mantis shrimp"）、以及 Hex 密文 "sudden"（[710]），使本线成为元叙事密度最高的角色线之一。

---

## 五、未解伏笔

1. **"五年"从何而来**：Touka 为何认为自己活不过五年？（[1580]）是家族遗传病、契约代价、还是她知晓某个针对自己的安排？主角为何选择装作没听见？
2. **Tsubasa 与主角的真实关系**：债务的对象是什么？"partners of sorts"（[3672]，dorm25p3 浴室戏中提及）的具体内容、"has Touka shown you where to find our massage parlor yet?"（[4839]）的未尽之言，均未揭晓。
3. **q 实体与主母的交易**：spring5 中被旁白跳过的谈判内容（[6151]）——q 想要什么，Tsubasa 答应了什么？
4. **Tsukasa 的婚约安排**：Touka 说母亲"不得不这样做"却不知原因（[6765]），对方家族能提供 Tsukioka 家没有的东西——这个东西是否存在？
5. **樱花树下的遗体**：传闻真伪（Tsubasa 断言不实 [6813]）、遗诗全文、Nodoka 调查的现状。
6. **Etinsib Ziwa**：Yasu 之神是否会对主角的"面谈请求"（[5931]）作出回应。
7. **"那片重要的屋顶"**：主角说有些屋顶"除了最重要的那一座"她都可以上去（[6920]-[6921]），所指何事，他随即收回——与他的过去直接挂钩。
8. **见过"第二个 Yasu"的机构**：哪家设施、之前的病例是谁、与 Yasu 的"天赋"有何关联（[5702]-[5705]）。
9. **Karin 的知情程度**：spring5 中她对"附身"的过度反应与前后矛盾（[6215]-[6245]），指向其尚未揭开的秘密。
10. **Touka 的欲望终点**：她宣称传统止于自己（[3834]）、又主动走进怪物的逻辑（spring7-8），当"五年"与"爱情"冲突时她会选哪边——这是本线留给终局的终极提问。

---

## 六、label 总表

| # | label | 起始行 | 类型 | 一句话概要 |
|---|-------|--------|------|-----------|
| 1 | toukastreets | [1] | 路由 | 街道事件分流器 |
| 2 | toukaarchery | [11] | 路由 | 弓道事件分流器 |
| 3 | toukastreetsgen | [21] | 泛用 | 泛用晨间散步，首现死亡阴影 |
| 4 | calltoukamorning | [52] | 占位 | 晨间电话占位 |
| 5 | calltoukaafternoon | [66] | 占位 | 午后电话占位 |
| 6 | calltoukanight | [82] | 占位 | 夜间电话占位 |
| 7 | toukastreets1 | [96] | love | 售货机初遇·咒语恶作剧·绿茶长椅 |
| 8 | toukastreets5 | [484] | love | 旧城区震撼·Hex"sudden"·安全套乌龙 |
| 9 | toukadorm10 | [874] | love | 宿舍夜访撞上睡衣派对·暑假企划立项 |
| 10 | toukaspecial15 | [1265] | love | 全家地铁之旅·"五年"死亡伏笔 |
| 11 | toukaspecial15p2 | [1636] | love | 娱乐区震惊·三分支（Touka/Tsubasa/Tsukasa） |
| 12 | endoftoukaarcade | [2169] | 过渡 | 全家好感+1，跳转 p3 |
| 13 | toukaspecial15p3 | [2180] | love | 塔可摊·"无力感"理论·归途夜话 |
| 14 | toukaarchery20 | [2482] | love | 弓道质问·Chika 真相·"你需要长大" |
| 15 | toukadorm25p1 | [2800] | love | 金丝笼独白·解除的政治联姻 |
| 16 | toukadorm25p2 | [3134] | love | Tsukasa 婚约闹剧·泳池房的异常沉默 |
| 17 | toukadorm25p3 | [3555] | love | 复制道场膝枕·母女浴谈·世代传统 |
| 18 | toukacamp1 | [3922] | love | 露营深夜来电·90/10 协议 |
| 19 | toukaspring1 | [4270] | love | 谢罪约会·疼痛论·请他远离主母 |
| 20 | toukaspring2 | [4627] | love | "母亲"炸弹·告白·授予真名 Akira |
| 21 | toukaspring3 | [5107] | 元叙事/love | Makoto 视角·成人店·书的独角戏 |
| 22 | toukaspring4 | [5494] | love | 教堂地牢·造婴誓言·Etinsib Ziwa |
| 23 | toukaspring5 | [5971] | love/元叙事 | q 冒名顶替·主母识破·Karin 异动 |
| 24 | toukaspring6 | [6271] | love | 公寓同居·牵手大于性·怪物美学宣言 |
| 25 | toukaspring7 | [6608] | love | 天台·樱花树传闻·Twilight 吸血鬼方案 |
| 26 | toukaspring8 | [6942] | love/lust | 小巷售货机·双重打断·lust 首涨 |
