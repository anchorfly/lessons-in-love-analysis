# Karin 事件线全析

> 源文件：KarinEvents.rpy ｜ 共 28 个剧情 label
> 定位：神田 Karin 是全作"纯善"光谱的极点——恐男、虔诚利他、运动天才、完美长女。她的事件线因此承担着本作最残忍的叙事任务：让系统化、寄生化的恶意一步步碾过全城最后一个"不该被伤害的人"。前半（date/soccer 系列）是一部笨拙温柔的恋爱喜剧；后半（spring1-7）则把同一角色拖入性侵未遂、信任崩塌、附身疑云与元叙事谎言之中，构成全作道德冲击力最强的一条弧线。
> 阅读提示：s=Sensei（主角 Akira）、ka=Karin、ki=Kirin（其妹）、mi=Miku、ay=Ayane、ima=Imani、os=Osako、a=Ami、m=Maya、mo=Molly、n=Noriko、N=旁白、kas=被夺舍状态的 Karin。台词直引保留英文原文并附 rpy 源码行号；lust 相关内容一律抽象为叙事功能描述。

## 一、角色基本盘

- **身份**：熊宫高中二年级（"Right! One year to go." [699]），足球部副队长兼实质运营者，兼修垒球与游泳 [3820]；因分班原因无法进入主角所带班级（"I can't be in your class" [2460]）。
- **家庭**：神田家长女，父母双全但工作繁忙、性格温吞，晚饭多由 Karin操持 [3894-3896]；妹妹 Kirin 是她人生叙事的原点与阴影——"My oldest memory involves the two of us sitting in a playpen together." [1987]，而这段关系在 Karin 的感知里长期是单方面的："Most of the time, it feels like she wishes I would just die." [3950]。
- **能力与人设**：天赋异禀的运动少女（身高、体能均超出同龄人），同时是年级顶尖学霸 [3784]；主动给忘带铅笔的同学备份 [3740]、每天扶老人过马路 [3842]、为全校社团所争抢 [3819-3825]。她自己总结为："I'd do *anything* for *anyone.*" [3905]。
- **核心缺陷**：重度恐男——面对任何男性都会语无伦次甚至当场死机（连远房表亲也不例外 [1950-1951]）；以及由此衍生的低自尊发作："I'm going to die alone with ten cats." [1664]。她的完美主义使一切失败都灾难化：做不好一顿寿司就会推演到"退部—失去奖学金—终身残疾" [1529-1531]。
- **叙事功能定位**：她是主角"猎艳名单"中唯一被叙事者反复标注为"不该碰"的人（"And it is those who have not yet been touched by it who must be left alone." [3144]），因此当 spring2 的侵害仍然发生时，遭受攻击的不只是角色，还有玩家对整个游戏道德底线的预期。

## 二、love 线逐事件脉络

### 路由与占位层（callkarinmorning / karinpool / callkarinafternoon / callkarinnight / soccerfieldkarin）

`callkarinmorning`[1]、`karinpool`[16]、`callkarinafternoon`[20]、`soccerfieldkarin`[92] 均为电话/地点路由器：callkarinafternoon 按 affection 逐级跳转 karindate1→30 [30]-[42]，是典型的周目推进阀门。唯一有实文的是 `callkarinnight`[51] 的夜间通话：深夜来电让 Karin 惊慌失措——"You aren't like...you know..." [73]，主角随即识趣收线 [75]-[81]。这条小场景一次性立住了两件事：Karin 对男性意图的高度警觉，以及主角早期尚存的（表演性的）分寸感。

### 日常泛用事件（karinsoccergen2 / karinnoongen2 / karinsoccergen / karingenafternoon / karingennight）

五个泛用贴负责铺设"教练—副队长"的日常底色：晨练时 Karin 手忙脚乱摆 cone、被主角默默观赏 [106]-[112]；冬日凉亭下抓马尾挡风 [141]；公园聊天中透露"和妹妹不同，她对人生已有清晰规划" [199-200]。这些段落的功能是把"可爱"量化为好感度燃料，同时在叙述者内心独白里持续滴入不适感："how excited I am to ultimately force her out of that shell of hers" [113]。

**`karindate1`**[249]：主角借"了解队员"之名约 Karin 单独夜跑，开场即自我拆穿——"To her life, I mean. Not her. Well, yes her. But not right now. Unless she wants it." [254]-[256]。公园里他谎称需要"one on one sessions"来建立教练关系 [283]，Karlin 则为"居然有点开心"而羞愧（"Is it weird if I'm kind of...maybe a little happy to hear that?" [304]）。秒表陪跑成为二人关系的原型仪式：他不跑步、只计时，而她拼命向他证明自己 [411]-[492]。收尾时主角独白首次亮出真实动机："I want to get closer to *her* specifically... But that's not something she needs to know yet." [526]-[527]，以及一句更阴冷的自我观察："Maybe I just really like when girls get nervous around me?" [566]。

**`karindate5`**[585]：仍是同一公园。"housewife"话题引爆全场——主角随口建议"Why not just become a housewife or something like that?" [711]，Karin 当场烧毁："WHY?! ALL I DO IS RUN AND...KICK!" [751]。她吐露真正焦虑：除了运动一无所有，"There are plenty of other Karin Kanda's out there." [742]。本事件的华彩是她那段即兴未来狂想曲——嫁给女孩、领养孩子、儿子入选曼联、妻子绝症又被行医的儿子治愈 [813]-[837]——一场把"不敢想爱情"折叠进科幻式脑内的白日梦，主角一针见血："You're a bit of a daydreamer, aren't you?" [846]。事件以一句危险的挑逗收束："Then get the wrong idea." [870]。

**`karindate10`**[954]：Karin 第一次穿便服赴约，并献上人生第一次送男生的礼物——饼干，配一套灾难级借口（"made them for my mom and dad! But then I realized they were on a diet!" [1052]-[1053]）。主角精准戳破又放她一马 [1047]-[1049]。两人转入咖啡馆，迎面撞上 Molly 的审判剧场："YOU WILL BURN FOR YOUR SINS! BOTH OF YOU!" [1289]，以及那句半开玩笑的后设吐槽："Molly doesn't take too kindly to unexpected girls showing up and joining the harem." [1299]／旁白补刀"It wasn't."（指玩笑）[1310]。值得注意的是 Karin 在此第一次展现说谎天赋——为主角圆谎时流畅自然 [1269]-[1274]，这个伏笔将在后期变成刺向她自己的刀。

**`karindate15`**[1364]：首次登门。Karin 借"签快递"把主角请进家中，端出巨型寿司宴 [1489]，却误给自己倒了红酒 [1556]。饭桌上主角罕见地交代了记忆问题的运作方式："a lot of it disappeared. And I guess the rest of it could technically disappear again...but only at several really specific moments." [1442]-[1443]；Karin 的回应是瞬间切换成照护模式："I'll wait by your bedside every morning and show you flashcards to remind you of who I am!" [1454]。随后是全线最重要的口误时刻：主角感慨她父母不会同意"their daughter dating a staff member at the school" [1596]，Karin 追问"Are you saying you would...date me?" [1604]，主角内心闪过长串动摇并以一句封存作结："Maybe in a different life." [1614]。Karin 却因此获得短暂自信峰值——"Oh my God! I did it! I flirted with a boy!" [1640]——并在三秒后坠落回"ten cats" [1664]。旁白对她下的判词是本线的题眼："A wholesome girl who wants to find happiness of her own without damaging anyone else in the process... Personally, I don't think something like that is possible." [1701]-[1703]。

**`karinsoccer15`**[1720]：隆冬，练习因停电取消，Karin 却已在寒风里等了半小时——只为"not about anything in particular"地见他 [1806]-[1807]。她借了 Kirin 的杂志学聊天技巧 [1921][1928]，自嘲从没给主角发过一条短信（草稿写满从不发送 [1859]-[1860]）。本事件的深水区有两处：其一，她说出对姐姐罕见的真心话——"she's a fucking huge bitch and I want her to die..." [1842]，连旁白都惊呼"This isn't canon, is it?"，而她回答"It...might be..." [1843-1844]；其二，她交代最古老的记忆只有育婴箱里的妹妹 [1985-1988]，且自述"my memory's been getting kind of weird lately" [1980]。事件顶点是她第一次为自己提出请求："If you're going to be...hugging my sister... That doesn't mean I...have to stop...doing things like this, does it?... I want to keep seeing you." [2044]-[2051]。主角应允的同时，脑内闯入一个来历不明念头："There's a thought stuck somewhere in the back of my head. I can't tell if it's my own." [2063-2064]——寄生合唱团在此完成了对 Karin 线的第一次入侵。

**`karinsoccer20`**[2117]：Miku 主导的校内"冒险"喜剧。三人组（Miku 封主角为 Steve、封 Karin 为 Karli [2293]-[2299]）前往二楼教室取课本，途中 Miku 离场，留下本线最温柔的一场对话。Karin 以教学楼楼层自况人生位置："When you're in the middle, it's like everyone is going to be forced to see you at some point." [2394]——所有人仰望她，无人问她累不累："Her and my parents...they all think I'm some sort of...amazing human being... but still *I'm* the one people are looking up to most of the time." [2442]-[2443]。她列举恐惧清单：蛇、高处、大鱼、通心粉搅拌声、墓地、缆车、梦套梦 [2471]-[2476]，然后落下全文最轻也最重的一句："I'm a little less scared...whenever you're around..." [2488]。

**`karindate20`**[2537]：足球部解散后的第一通电话（此后"教练"外衣消失，约会失去官方借口 [2923]）。Karin 因 Kirin 禁止她参加海滩旅行而愤怒暴食，在餐厅里拍桌咆哮、惊动全场 [2739]-[2745]。这是她第一次对主角倾倒负面情绪，也是主角第一次以"闺蜜位"承接："I wouldn't have come if I wasn't." [2653]。他给出关键判断："The key difference between you and Kirin is that you don't actively want to make other people feel bad." [2803]。事件里还藏着两条暗线：Karin 提及去年夏天的海滩之行却对时间错乱毫无反应，旁白点评"Oh. Okay. I guess there won't be any bigger reaction to the weird blurs in time with Karin." [2665]；以及棒球棍打 Maya 的旧事回响——"Maya hasn't been walking the same ever since." [2670]。结尾 Karin 决意"做自己的主人"去海滩，收获全体顾客起立鼓掌的荒诞礼遇 [2837]。

**`karindate25`**[2920]：Makoto 丧父事件横切入线——游泳部为 Makoto 凑关怀包裹，Imani 直接点名"You and Karin are gonna go out on a date, obviously." [3051]，把两人推上巴士。商场购物途中，叙事进入全 digest 最阴冷的段落：主角凝视长椅上的 Karin，脑内浮现"I think about plucking those valuable gems from out of her sockets and pawning them off for one more gift to a girl more tainted than she is." [3142]。随后是一场关于死亡的对话——Karin 承认"I don't have any...*experience* with death yet"（金鱼 Benjamin 除外 [3173]），主角则给出不祥预言："I'm sure you'll come to experience it someday. And I'm sure that, when you do, you'll learn things about yourself that you've always feared learning." [3183]。归途撞上 Kirin 与 Noriko，Karin 一反常态地正面迎战姐姐 [3220]-[3258]，逼得 Kirin 败退。事件收尾回到那个意象："Among those thoughts are several visions of emerald eyes. And how my desire to pluck them becomes greater each time they appear." [3301]-[3302]——对纯善的占有欲正在从比喻滑向字面。

**`karindate30`**[3316]：正式告白级约会。电话邀约令 Karin 再次挂机爆音 [3330]-[3344]；Kirin 得知后激烈反对——"He's *my* fucking teacher! Find your own adult to suck off if you're that curious about men all of a sudden." [3403]——姐妹战争正式公开化。Karin 化妆赴约，见面即陷入"dream-Sensei"恐慌："This whole day has been a dream and I am going to wake up in five minutes" [3514]。主角连续施压："you're already falling in love with me" [3613]；被反问"Don't you see me as a kid in your eyes?"时，他一边否认 [3687] 一边被旁白当场拆穿："(It doesn't.)" [3689]。他还主动暴露了对 Kirin 的兴趣"who is both younger *and* smaller than you" [3663]，换来 Karin 第一句真正的领土宣言："Don't bring her up anymore. This is *my* date." [3668]。这是 love 线的最高点——也是崩塌前的最后一帧。

### 第四章：spring 系列的坠落

**`karinspring1`**[3735]：视角反转的日常回——全程由第三人称旁白扮演"Karin 的自我介绍"："Hi! I'm Karin Kanda — a second year student at Kumon-mi High!" [3739]，人设关键词是"sunshine" [3743]。她给老师买花、拒绝给同学递答案 [3751][3799]、被各社团哄抢 [3819-3825]，顺带投下一枚世界观炸弹："we all know nationals haven't existed since the barrier was put up." [3826]。扶老人过马路段落里，Mrs. Okazaki 祝她"put it in a box under your bed...and spend it on a wedding one day" [3873]，让她心跳漏拍的"那个人"呼之欲出 [3879]。晚间回家吃闭门羹——Kirin 吃掉她的布丁扬长而去 [3916-3919]——引出那段泣血独白："She's been my best friend ever since she was born. But it feels like, most of the time, she wants to be an only child." [3949]……"I just wish she loved me too." [3973]。注意旁白的两处自我怀疑："Right?" [3832] 与隔行的"Right?" [3837]——完美人设的第一道裂缝是以标点的形式出现的。

**`karinspring2`**[3989]：全作最黑暗的事件之一。KTV 包厢内，主角脑内寄生之声全面接管叙事：先以生理工厂寓言羞辱他 [3999-4004]，再逼他念出被消音的名字"MAYA" [4036]-[4040]，随后 Miku 化身为扭曲玩偶、Maya 以"the main heroine of Lessons in Love. I do the time thing." [4173] 的身份还魂索债——"Hi, I'm Maya — the main heroine of Lessons in Love. You killed me. You killed me, Akira. Millions of years of memories, stripped away by a one night stand." [4178]。寄生体开价："Fill her with your seed so that I may sing again." [4215]。接下来是玩家被迫旁观、无法操作的强袭场景：Karin 缩在角落重复"Please don't hurt me." [4217][4254]，主角的声音已经不是他的——"Do you ever dream of me?... I can be gentle if I have to... No one ever has to know." [4234]-[4248]。他在最后关头挣脱 [4411 事后追述]，而系统弹出讽刺性的假结算："Karin's lust has increased to 1!" [4272]，随后被寄生体亲口揭穿是恶作剧："Oh, and her lust never actually went up. I was just fucking with you." [4373]，并追加天文数字惩罚："Karin's affection has decreased by 1,000,010!" [4372]。事件以状态栏宣判收尾："Akira has gained the status effect [[PARANOID]]!" [4378]，以及主角的哀鸣："I've been talking to myself a lot lately. I wish I knew how to make it stop." [4376-4377]。

**`karinspring3`**[4399]：一周的死寂之后，Karin 主动找上门来——不是原谅，而是审讯。她在门外站了十分钟组织语言 [4483]，随后抛出一串外科手术式的质问：是否早知道她的心意（"Yes." [4614]）、是否被吸引（"Yes." [4624]）、知不知道她的年龄（"...Yes." [4626]）、是否曾想过伤害她（"Not intentionally." [4632]），直至终极问题："Have you been grooming me this entire time?" [4640]，以及"Do you love me, Sensei?" [4648]。主角的回答是一个字："No." [4659]。这个诚实的"不"比任何辩解更具毁灭性，Karin 的判决随之落地："Sensei...I'm sorry, but you'll never be able to love *anyone* like this." [4682]；她承诺保密 [4686]，但要求他远离自己和妹妹 [4687]，最后一句是墓志铭级的告别："You're nothing like the man I thought you were." [4696]。旁白以章节术语埋下续篇钩子："All this one says is that her chapter is still open. And that I was a fool for thinking I could jump to the epilogue." [4701]-[4702]。

**`karinspring4`**[4718]：道场重逢。Karin 出于创伤开始学习自卫术 [4874]-[4881]，Osako 不知情地把主角推上去当陪练 [4762]。Karin 用妈妈教的膝击将他当场放倒 [4834][4845]，完成一场象征性的复仇。随后的对话里她袒露学武动机："I want to be able to do something if that ever happens again. Just lying there and...letting it happen made me feel terrible about myself." [4881]；主角则以退场作答："I'll stop coming here altogether then." [4883]。本事件还揭开了信息泄露链：Kirin 已经从 Miku 的只言片语里拼出真相，并把主角拽到 KTV 逼问过 [4955]-[4968]——受害者想保护的秘密，保护失效了。Karin 的结语苦涩而克制："I really liked spending time with you. Now I'm just...tense." [4990]，离场时没有回头 [5004]。

**`karinspring5`**[5012]：以"乌兹别克斯坦"的白日梦开场——主角读了一首关于帖木儿的诗，决定去"purity 所在之处"寻找活着的理由 [5016]-[5022]。他在 soup kitchen 重逢独自搬运食材的 Karin，接受一套屈辱条约：拎塑料袋、保持五步距离、不许看她 [5097]-[5099]，外加一条玄学威胁："Unless you follow my demands...something bad is gonna happen... I might not even *know* what the bad thing is yet." [5081]-[5083]。途中他罕见地完整剖白了 Ami 父母之死与自己的人格坍塌："Sometimes, I feel like *I* died with them. And that everything that's happened afterward has been some sort of crazy dream I can't wake up from." [5182]。Karin 给出的宽恕条款冷峻清晰："Forgiveness needs to be earned." [5204]。就在此时，叙事突然被一首插入诗劫持——那显然流经 Karin 的意识，却说着不属于她的话："Every day, I slip closer to Him. This infection, this plague, this PARASITE, this MADNESS... has STOLEN the one thing that makes me ME" [5222]；"this worm torn from bodies past and placed into mine brings me NO closer to ENLIGHTENMENT" [5224]；"DO NOT LET IT PASS. DO NOT LET IT REACH HIM." [5225]；直至一句不祥的平静："I can hear salvation come." [5229]。事件尾声，Karin 开出真正的宽恕代价——上楼见她的父母，直面真实世界："You can't face them because you want to keep up the illusion that this is all some sort of fantasy." [5262]。主角的回答是退缩，她只回敬两个字："Coward." [5272]。

**`karinspring6`**[5296]：Kanda 家客厅的双人静物画。开场旁白以极端意象对照姐妹姿态 [5302]-[5312]，并交代 Karin 的矛盾内核：她恨自己的善良——"I wish I was less nice... It makes me weak..." [5340][5346]，却做不到记仇 [5347-5348]。Kirin 主动提出按摩解压 [5386]，一场姐妹按摩戏在暧昧与搞笑之间反复横跳：Karin 舒服到失语，Kirin 内心尖叫"(Screaming internally, horny, and ashamed)" [5472]，两人各自逃进错位的台词 [5416][5436]。Karin 借朦胧状态说出久违的"I miss you, Kirin...and I love you..." [5485]，而 Kirin 在她差点说出"my sister"之前仓皇逃去做作业 [5517]-[5537]。随后镜头跟随 Karin 进入浴室，创伤闪回以存档术语呈现："creating an unfortunate save state that she'd be forced to look at every time she wanted to load up some *other* memory." [5616]。本段直面她的欲望觉醒与其伴生的自厌："Curiosity. Hate. Lust. Betrayal. Admiration. Fear. Everything else — dumped into a blender" [5626]；"Karin Kanda only touched herself once per month... But tonight — it felt like she was bathing in shit." [5638]-[5640]。结算文本由寄生体署名盖章："Karin's affection increases to [karin_love] because she's naive and forgiving and you did this to her." [5649]。

**`karinspring7`**[5660]：终章，也是全 digest 元叙事浓度最高的一集。开场旁白直接对玩家摊牌："One thing, though — if it ever feels like I'm lying, it's probably because I am. And there's probably a reason for that. But what's it to you? What's *anything* to you? You're not even here. And neither am I." [5671]-[5674]。随后宣布本场为虚构翻转剧："we'll bear witness to a fictional scenario in which *she* was the one who flashed him her panties in his office and then subsequently threw her virginity away in a love hotel." [5684]。正片里，Karin 带着"修订版道德准则"上门 [5768]，却在门口撞见 Ami。一段关于"父亲"的对话揭开 Ami 线的深渊：访客名单是"a list of girls that my dad regularly *tutors.*" [5736]、追踪 App [5748]、乃至"I'd marry him if he wanted me to." [5828]。Ami 以毒攻毒地拆穿 Karin 的借口——"You brought him cookies, Karin. Yes you do." [5893]——反被 Karin 第一次正面回击："You're *upset* that I'm here. You're upset that *you're* not involved, so you're involving yourself. *You* admit it." [5905]。两人达成脆弱的和解，Ami 甚至说"I kind of wish you were *my* older sister instead of Kirin's." [5921]。然而事件在 Karin 极度睡眠剥夺的伏笔下急转直下——"Maybe four? Or...three?" [5983]——她倒在 Ami 床上，意识溃散的台词逐字碎裂："That's...really...... Huh...... I feel...... I......" [5991]-[5995]，继而陷入半梦呓："Ah...a......aaaa......aaahh...." [6004]→"A.........aaaaa......am...........bulance............." [6006]→"Hh.........mn............h..........help..........." [6007]。最后的画面定格在一行舞台指示："a: (Sips incestuously)" [6013]，随后跳转 amispring5 [6023]。发生了什么、Ami 做了什么、Karin 是否清醒——全部留白，只留给玩家一行足以窒息的注脚。

## 三、lust 线概貌

Karin 没有任何独立 lust label；她的情欲内容全部以嵌入形态出现在 love 事件内部，且始终与伤害、羞耻绑定，共三类：

1. **寄生体的强制演出**（spring2）：玩家的操作权被旁白实体夺走，"攻略"变成一场无法拒绝观看的犯罪直播。假结算数值（lust+1 随后被撤销、affection -1,000,010）把 galgame 数值系统本身拖出来示众。
2. **受害者的欲望觉醒**（spring6 浴室段）：月度一次的自慰、创伤闪回与"柠檬或盐"般的混杂味觉 [5626]-[5627]，把 lust 写成创伤后应激的一部分——身体先于意志产生了反应，而这正是她最深的恐惧。
3. **越界氛围的悬置**（spring7 结尾）：昏迷、喂食(sip)、乱伦舞台指示——不发生任何明写行为，却通过留白完成最重的冒犯。

整体而言，Karin 线的 lust 从不是奖励，而是对"纯爱攻略"这一类型承诺的系统性质询。

## 四、与主线/元叙事咬合点

1. **足球部兴衰作为结构轴**：Karin 线的存在依赖"主角任教练"这一前提；date25 电话中明确"no longer the coach of the soccer team and can no longer hide these impromptu afternoon meetings behind the guise of supervising her training" [2923]，与 soccer15 中"Ever since the soccer team disbanded"的失落互为镜像 [3604 为 Touka 场景同源表述，此处以 karindate20 的 Kirin 抱怨为证 [2565]。
2. **姐妹双线竞争**：Kirin 对主角的占有（"He's mine and I won't let you take *him* from me too!" [3410]）与 Karin 的觉醒（"This is *my* date." [3668]）构成同族竞合；spring4 揭示 Kirin 甚至先喜欢主角（"when *she* liked you first." [4946]），为两线互相渗透提供接口。
3. **Maya 之死的余波**：spring2 的亡灵清算 [4178]、autopsy 拼图独白 [4188]、date20 的棒球棍玩笑 [2670]，把 Karin 线钉在主线最大惨案的时间轴上。
4. **记忆重置机制的正面自供**："Everything is going to just reset before she makes a decision anyway." [704]——主角在 date5 就向读者承认 Karin 的未来规划毫无意义，这是全作最早期的宿命论自白之一。
5. **屏障世界观**："nationals haven't existed since the barrier was put up." [3826]——以 Karin 的日常口吻确认熊宫与世隔绝的设定。
6. **寄生实体系统**：spring2 的多声道合唱（caps lock guy、/////////////// guy [4214]-[4221]）、[[PARANOID]] 状态 [4378]，与 spring5 Karin 体内"worm"的诗 [5224] 遥相呼应，暗示寄生并非主角专属。
7. **Ami 线的直接汇入**：spring7 整场发生在 Ami 家，以">> jump amispring5" [6023] 物理衔接；Osako 道场线亦由 spring4 收尾跳转 osakospring4 [5009] 衔接，显示 Karin 线在第四章已成为主线换乘站。
8. **Makoto 丧父支线**：date25 全程为其服务（关怀包裹、商场采购、死亡观对话 [3148]-[3183]），是角色间互助网络的节点事件。

## 五、未解伏笔

1. **Kerin 体内的"worm"**：spring5 插入诗明言"worm torn from bodies past and placed into mine" [5224]，且命令式警告"DO NOT LET IT PASS. DO NOT LET IT REACH HIM." [5225]——她是否早已被寄生？"Him"是谁？
2. **完美人设的真实性**：spring1 第三人称自我介绍中连续两次悬空的"Right?" [3832][3837]，加上"if it ever feels like I'm lying"的全局声明 [5671]，共同质疑"阳光 Karin"究竟是人格还是剧本。
3. **记忆异常**："my memory's been getting kind of weird lately" [1980]，且最老记忆止步于育婴箱 [1985-1988]——与主角的记忆病症是否同源？
4. **spring7 的双重虚构声明**：叙述者既承认习惯性撒谎 [5671]，又宣称本场是"fictitional scenario" [5684]——那么"真实"版本的事件是什么？虚构声明本身会不会才是谎言？
5. **结尾留白**：Karin 意识溃散时的"ambulance""help" [6006]-[6007] 与 Ami 的"(Sips incestuously)" [6013] 之后发生了什么，文本永久沉默。
6. **"her chapter is still open"** [4701]：spring3 的绝交并非终点，和解路线的钥匙（上楼见父母 [5252]）至今未被使用。
7. **翡翠眼眸的摘除幻想**：两次出现且强度递增 [3142][3302]——这是比喻、预兆，还是寄生体的购物清单？
8. **"Maybe in a different life."** [1614]：主角对平行可能性的罕见松口，与时间系 Maya 残党形成潜在勾连。
9. **Karin 对主角私人信息的异常掌握**：她知道他没有无限短信套餐，旁白警觉"Why does she know that?" [1112]-[1114]。
10. **"This isn't canon, is it?""It...might be..."** [1843-1844]：Karin 对自身话语是否属于"正史"表现出了不该有的自觉。
11. **Kirin 的按摩失态与身份漂移**："I'm good Kirin now. I've decided to switch personalities." [5331]、中途忘记自己要说什么 [5446]——姐妹线深处另有引擎。

## 六、label 总表

| # | label | 起始行 | 类型 | 一句话概述 |
|---|-------|--------|------|------------|
| 1 | callkarinmorning | [1] | 路由 | 晨间电话入口 |
| 2 | karinpool | [16] | 路由 | 泳池地点入口 |
| 3 | callkarinafternoon | [20] | 路由 | 午后电话，按好感分流至 date1-30 |
| 4 | callkarinnight | [51] | 过渡 | 深夜来电吓退 Karin，主角知趣收线 |
| 5 | soccerfieldkarin | [92] | 路由 | 足球场地点入口 |
| 6 | karinsoccergen2 | [102] | 日常 | 晨练摆锥，观赏型互动 |
| 7 | karinnoongen2 | [133] | 日常 | 冬日凉亭躲风，抓马尾 |
| 8 | karinsoccergen | [164] | 日常 | 观看练习赛，副队长高光 |
| 9 | karingenafternoon | [192] | 日常 | 公园闲谈人生规划 |
| 10 | karingennight | [222] | 日常 | 夜间电话，她已有约 |
| 11 | karindate1 | [249] | love | 秒表陪跑初约会，动机自白 |
| 12 | karindate5 | [585] | love | "housewife"风波与未来狂想曲 |
| 13 | karindate10 | [954] | love | 饼干初礼物，Molly 审判剧场 |
| 14 | karindate15 | [1364] | love | 登门寿司宴，"Maybe in a different life." |
| 15 | karinsoccer15 | [1720] | love | 寒风守望，"I want to keep seeing you." |
| 16 | karinsoccer20 | [2117] | love | 校内冒险，二楼隐喻与恐惧清单 |
| 17 | karindate20 | [2537] | love | 餐厅控诉 Kirin，怒而立志赴海滩 |
| 18 | karindate25 | [2920] | love | Makoto 关怀包裹之旅，摘眼幻想与死亡对话 |
| 19 | karindate30 | [3316] | love | 正式约会，"dream-Sensei"与姐妹宣战 |
| 20 | karinspring1 | [3735] | ch4 | 第三人称日常回，阳光人设首现裂缝 |
| 21 | karinspring2 | [3989] | ch4/lust | KTV 寄生体夺舍，强袭未遂与 [[PARANOID]] |
| 22 | karinspring3 | [4399] | ch4 | 上门审讯，"Do you love me?"→"No." |
| 23 | karinspring4 | [4718] | ch4 | 道场膝击复仇，学自卫的觉悟 |
| 24 | karinspring5 | [5012] | ch4 | soup kitchen 重逢，寄生诗与"Coward." |
| 25 | karinspring6 | [5296] | ch4/lust | 姐妹按摩与浴室创伤闪回 |
| 26 | karinspring7 | [5660] | ch4/元叙事 | 撒谎声明+虚构场景，Ami 家崩溃之夜 |
