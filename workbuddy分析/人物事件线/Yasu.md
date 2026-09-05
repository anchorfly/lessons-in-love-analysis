# Yasu 事件线全析

> 源文件：YasuEvents.rpy ｜ 共 26 个剧情 label
> 定位：元叙事枢纽型配角——教会少女／Transference 教团相关者／sanity 机制的具象化载体
> 阅读提示：本文基于 YasuEvents.rpy 逐 label 整理，全部引文为原文直引；lust 线部分场景在源文件中被裁剪（[TRIMMED...]），仅作叙事功能层面的概括，不逐句还原。下文按源文件 label 出现顺序（即剧情推进顺序）分节。

## 一、角色基本盘

Yasu 是《Lessons in Love》中与「教会」强绑定的事件线角色。她的常规事件大多以教堂为舞台展开：从开场诗到教义讲解，从祈祷到与 Sensei 的独处，教堂既是场景也是她的身份本身。在 love 线的语境里，她不是普通的可攻略对象，而是一个「传教者」——她对 Sensei 的接近始终伴随着一套完整的世界观输出：垂死的神、天使、Transference 教义，以及反复出现的 sanity（理智值）概念。

这条线的叙事基调与其他角色截然不同。别的角色线是日常喜剧或情感剧，Yasu 线从第一个 label 开始就在做三件事：布道、解谜、打破第四面墙。开场即以一首关于神之生死的诗定调：

> N: While one god lives, another dies.

随后叙述者以 Godnote／Flynote 这类笔记体对诗句本身进行元评论，明确告诉玩家：这些文本是被设计出来供人解读的。这种「文本自觉」贯穿整条线，使 Yasu 成为三层世界观（恋爱表层／重置循环层／元叙事玩家层）中最直接连通上层的角色之一。

她的核心命题可以概括为一组对立：**神正在死去，而拯救神的教义是 Transference——通过转移完成的仪式。** 教会将对 Transference 的解释明确为「把一种重要资源放到它该在的地方」，与浪漫无关：

> ya: Transference has nothing to do with romance, Sensei. It's taking one important resource and putting it where it belongs.

这决定了 Yasu 线的双轨结构天然咬合：love 线的布道与 lust 线的仪式共享同一套教义语言，性场景在这条线里不是奖励演出，而是教义的实践环节。

同时，Yasu 与 sanity 数值系统深度绑定。在 halloweenyasu1 中出现 sanity 显示为 [[ERROR]] 的异常态（"Yasu's sanity has [[ERROR]"），配合悬浮的 TERMS OF USE 条款文本与一段密文，说明她的存在本身就是游戏系统故障的显影点。

## 二、love 线逐事件脉络（按源文件 label 顺序）

### 教堂系（church → church25）

**church（入口）／churchgen（生成节点）**：教堂场景的入口与日常生成节点，负责维持访问频率与世界搭建。

**church1（初遇）**：Sensei 走入教堂，Yasu 以开场诗迎接。「一神尚存，另一神死去」的诗句由 N 层叙述者吟出，随后 Godnote／Flynote 的元评论把这首诗标记为可被解读的谜面。事件后半段抛出全线的核心设定：「God says no」——某个更高的存在否决了某件事，而 Yasu 自称知道神的状态：

> ya: "God is dying," Sensei.

事件结尾是一段末日式宣告，宣告时间不多、审判将近。这是整条线的基调文件：宗教末日论＋元评论＋对 Sensei 的特殊称呼，三者同时立起。

**church5（入内祈祷）**：Sensei 第二次进入教堂，这次是主动祈祷。入口处的祷文已经透出这条线的残酷底色：

> ya: Blessed be those who give up their eyes...

「放弃双眼者得福」呼应了后文 church10 中的盲人寓言，也预示了「看见」在这条线里的危险属性。事件中段 Yasu 讲述 Angel 的毕业教义——信徒努力击穿旧神的装甲后「毕业」成为天使，暗示教会内部存在某种轮换与晋升结构。事件最重要的信息是 Yasu 关于药物的自我暴露：她承认自己曾在外部机构接受治疗，并给出了停药的理由：

> ya: External forces like medications or narcotics slowly strip the sanity from your mind and your body.

这句话把「停药＝保住 sanity」写成一条明确的因果链。

**church10（anchor 与盲人）**：本事件是教堂系的哲学高峰。开头以 anchor（锚）比喻安定感与依附关系——"a small anchor surgically inserted into every girl I know"。随后 Yasu 完整讲述了盲人与千眼的寓言：一个盲人虽无视力却「看见」了常人看不见的东西，而一个被覆满眼睛的男人「反而和他出生时就一样盲目」。这则寓言是理解全线视觉母题的钥匙——「看」与「被看」、「目击」与「失明」的对立在后续事件中反复回响。事件以一句温柔又不安的叮嘱收尾：

> ya: Remember to sleep facing up tonight.

「今晚要仰面睡觉」——表面是睡姿建议，实则暗示某种夜间降临的危险，是典型的半预言式台词。

**church15（夏虫合唱）**：夏季背景下的过渡事件，以昆虫合唱的声景铺陈教堂周边的氛围（"insectual melodies"、"the sound of insects"）。此事件功能偏抒情与关系保温，推进了两人独处时那种介于布道与闲谈之间的独特张力，为后续更重的仪式性事件蓄势。

**church20 / church25**：教堂系的日常与生成类节点，延续「讲道片段＋谜语碎片」的模式，持续向玩家投放世界观碎屑。

### special／dorm 系

**yasuspecial15**：special 系中教堂之外的特殊接触节点（与教堂系教义内容相呼应）。

**yasuspecial20**：本事件是 Sensei 在办公室的场景。Touka 敲门进来，告知 Yasu 当天拒绝踏入教室、不肯上课，并要求 Sensei 作为她的老师去处理。Sensei 的内心独白甚至希望 Yasu「别再爬到什么东西上去、又开始说方言（speaking in tongues）」——也就是说，本 label 里 Yasu 并未发作言语狂乱，叙述者只是担心她旧态重演。文档此前称本事件含「glossolalia／言语狂乱场景」与「Yasu 以无法辨识的语言发声」与源文不符，应修正为：yasuspecial20 的核心是 Touka 把 Yasu 旷课的问题推给 Sensei，Yasu 本人并未在此发言狂乱。

**yasudorm20 / yasudorm25**：dorm 系将 Yasu 拉入学生日常空间，处理她在宿舍环境中的不适与试探。

**yasudorm30**：本事件展现室友 Touka 对 Sensei 的质问。Touka 直指 Sensei「曾把可怜的 Yasu 半夜带去 God knows where，而她回来时成了一团又哭又丢人的烂摊子」（"that time you took poor Yasu out in the middle of the night to God knows where and she came back a blubbering, shameful mess"）。对话并未澄清 Yasu 的来历，只交代了 Touka 作为室友／看护者对 Yasu 异常状态的察觉与担忧——Yasu 的来历在正文中始终保持悬置。

### spring 系（yasuspring1 → endofyasuspring8）

**yasuspring1–3**：关系升温段，教堂外的约会与对话逐渐取代纯布道场景，Yasu 开始以更私人的口吻谈论神、死亡与她自己的过去，同时继续向 Sensei 输出「时间不多了」的紧迫感。yasuspring1 中 Ami 亦现身于教堂相关场景。

**yasuspring4（白发少女与医疗设施）**：本事件展示一处医疗设施与一位白发少女。需准确指出的是，这位「白发少女」就是 Yasu 本人——源文写 "a young girl with white hair... She'd been pushed in and out of more medical facilities..." ，随后医生称呼她为 "Miss Yasui"，Touka（Miss Tsukioka）则以家属身份与医生争执、要求留在诊室陪伴。事件交代 Yasu 长期就医、服用新药、并自述听到「声音（voices）」。因此这并非「另一个女孩的镜像」，而是 Yasu 自己的求医片段；它与 church5 的服药史直接相连，说明 Yasu 的「看见」能力与其用药史、精神状态互为表里。

**yasuspring5（Touka 求援）**：Touka 打电话给 Sensei，说 Yasu 状态不对、请求 Sensei 帮忙「把 Yasu 变回 Yasu」（"I need your help turning Yasu back into Yasu"）。这是 Yasu 异常加剧、旁人介入救助的过渡节点。

**yasuspring6（Child of Light：Ami 访教堂与 GET OUT）**：Ami 循着传单独自来到 Yasu 的教堂——传单集中出现在她家附近，她自己点破这一反常（"There are fliers all over our neighborhood... Why are you so desperate to appeal to {i}us?{/i}"，YasuEvents.rpy:6537）。动机在结尾说破：亡母遗物箱里有"很像教会广告的东西"（6481），"If this is what my mom believed in, I want to at least know what she {i}saw{/i}"（6720）。途中 Ami 把教义问得毫不遮掩——确认"救赎=内射"后直问乱伦政策，并自己得出结论："Meaning...that my dad is special and your god will let me have a bunch of sex with him?"（6511）；Yasu 称她 "child of light"（6459）、"I knew you would be special, Ami!"（6517）。色彩问答以 hex code 交付结果：Yasu 自报 74d9e9（6617），Ami 的结果是 ff4dd2（6653）。母亲话题是本事件情感核心：Ami 记得母亲的声音 "so sweet that I can still hear it in my dreams"（6677），母亲产后 "found God" 随即 "started hearing things. {i}Seeing{/i} things. Things no one else believed, but things that were {i}very{/i} real."（6683）——Ami 把 Yasu 的处境与母亲并置："Living in what's essentially a different plane of existence from everyone else?"（6684）。事件以触碰收束：Yasu 说要替女孩们「传递信息」：

> ya: Girls are special in His all-seeing blindness. And I've been granted the ability to carry their message and deliver it unto those who need it most.

Ami 立刻点破「这毕竟是我的手，就算能看见什么，也不是在和你妈妈沟通」（6735）。Yasu 正要接话 "you're your mother's daughter. Just like your father is-"（6736，被掐断）时突然僵住，改口 "Get out" 后爆发式重复：

> ya: GET OUT GET OUT GET OUT ... AAAAHHHHHH!!!!!!

值得修正的旧读法：Yasu 看见的不是"自己身侧的异质存在"——她在 yasuspring7 中明确说所见来自 Ami 的手（"This was...this was Ami. Ami and...and something else..."，7113）。Ami 的离场异常从容："You must have seen something terrible. I really didn't mean to scare you."（6772-6773），临走留话 "You don't need to send me my color. But I'd love if you could send me yours. I have a feeling it's beautiful."（6780-6782）——她清楚自己吓坏了对方，全程平静。这一幕是 Yasu 线与 Ami 线的直接交汇，也是 0.60.0 全版本 Ami 的主场景。

**yasuspring7（Ichigo Daifuku：上锁囚室与 Sekai 的证言）**：本事件的设定是教会内一间可从外侧上锁的囚室（场景名 yasulocked 系列），Yasu 在 yasuspring6 之后把自己锁了进去（Touka："Yasu has locked herself inside of the same prison she intended to make us fornicate in"，6872），数日不出、停药、不停念叨 Ami。Touka 深夜电召 Sensei，给出三个并列猜测：Ami 对她做了什么／说了什么／或者 Yasu 自己梦出来的（6886）；Sensei 的反应是 "I don't think I've ever even heard her {i}talk{/i} about Yasu before"（6888）。本事件同时是 Sensei 的活动性幻觉现场：进教堂时满堂人体模型转头耳语，而他 "being conscious enough to know that this is all just in my head"（6905-6906）——清醒地幻觉着。囚室内 Yasu 先以救世仪式乞求性（"Bed me. Claim me..."，6927），再说出 Ami 到访真相：她来是 "To {i}learn.{/i}"，讲的全是亡母临终前听到看到的东西（7075-7076）；"And then I touched her... Hands can be so strange...can't they?"（7085-7086，插入闪回 CG 全是 Ami 事件画面：amibus12／handsareweird2／amihair19）。她看见的不是亡母，而是：

> ya: This was...this was Ami. Ami and...and something else...
> ya: It wasn't just {i}one{/i} something. It was so many of them! ... And the deeper it went, the darker they were! I could feel them inside of me. {i}Fighting{/i} for me.

（7113、7120-7122。）Sensei 先怀疑是 Sekai 亡灵显形（"Ami's mother didn't appear to you, did she? An older woman who looks just like her?"，7106），被 Yasu 否认；此时 se 插入全书最直接的判词：

> se: She's lying. Ami's not involved in any of this. I died before the curse could reach her.

（7126。）说话者自述已死、且以死护住了 Ami，并首次抛出 "the curse" 一词；Sensei 怒问 "What {i}curse?!{/i}"（7131）即被切换进 yasuspring8。本事件另有一处关系定性：Sensei 当面纠正 Touka 的称呼——"She is my {i}daughter,{/i} Touka. Please stop calling her my niece. {i}Please.{/i}"（6948）。

**halloweenyasu1（万圣节：井、ERROR 与密文）**：全线的元叙事核心事件。开场即由 N 层直接向玩家喊话：

> N: ...the game is playing you now.

「现在是游戏在玩你。」这句台词把玩家层的存在摆上台面。随后 Sensei 在许愿井旁（"Drop your wallet into the wishing well"）遭遇一连串系统异常：sanity 数值显示为 [[ERROR]]（"Yasu's sanity has [[ERROR]"），屏幕上浮现 TERMS OF USE 文本（"Please agree to [[TERMS OF USE]..."），以及一行需要自行破译的密文：

> cqn fjuub jan luxbrwp rw!

事件随即以 jump halloweentsuneyo1 收束——Yasu 的异常事件直接把玩家踢进 Tsuneyo 的 Halloween 线，两条线在此处发生硬性咬合。

**yasuchristmalloween1（安静房间／服装）**：Uta、Io 与 Yasu 在安静房间里闲谈 Christmalloween 服装的轻松场景，基调偏日常喜剧。

**yasuchristmalloween2（麦当劳／时间线异常）**：Sensei 与 Yasu 来到麦当劳。Yasu 道歉说「既然我已经吃过药，你应该免受神罚了」（"now that I've had my medicine"），呼应其用药线索；Sensei 则指出本时间线极度错乱、「突然没人记得圣诞节还存在」。这是用药主题与循环／时间线异常的交汇点。

**restofyasumallow（棉花糖活动余波）**：Ayane 与冰淇淋的日常场景之下，埋着一句关于「他」的关键描述——Yasu 说自己只是转述：

> ya: ...I merely relay information from the texts of His eternal diary.

「他永恒的日记」——以旁观者口吻点出某个存在以日记形式无限记录的设定，与全线反复出现的「记录」「重置」「记忆」母题相扣。

**yasuspring8（Heretic）／endofyasuspring8（Transference 仪式）**：全线的终点与总爆发。love 与 lust 在此合并为一场完整的 Transference 性仪式。仪式前 Yasu 与 Sensei 交换了各自"看见"的东西：Yasu 确认 Sensei 的异象是外部真实的（"You've been followed by so many things since we first met."，7151），而 Sensei 以 "None of it's real, Yasu. None of {i}anything{/i} is real... Tricks to enrich {i}my{/i} life at the cost of everyone else's."（7155-7156）回应——把世界定义为"为丰富他的人生而存在"的把戏。Yasu 随即给出她对 Ami 的完整画像：

> ya: She is far more than just {i}Ami.{/i} She's peeled the skin off of arbiters and fashioned it all into pretty dresses that can bend light — adorned with the eyes of the angels themselves. She is heresy itself.

（7176-7177。）并断言 Ami 对她的处境知情且主动："She knew that this would happen. That's why she infected me."（7174）；她反问 Sensei 为何触碰 Ami 却毫发无伤——"How do you touch her without breaking? How have you slept with so many shadows sodomizing her so close by?"（7179-7180），暗示 Ami 周身常年环绕只有 Sensei 看不见的"影子"。Sensei 以性为价码换取情报（"tell me, in the simplest way you can, what makes Ami different from everyone else."，7226），并预约下一步：让 Yasu 用同样方式触碰 Maya——"I just need you to do whatever you did with Ami to Maya."（7231），理由是 "There's something I need to know. Something that affects {i}everyone.{/i}"（7233）。仪式进行中 Sensei 看见角落里的女人并问 Yasu 是否可见，对方答 "There is nothing... Not even me."（7204-7205）——Sekai 的显形对他单方面可见；仪式中段插入 ker／kok 两位天使以希伯来语与英语交谈的见证段落，自述正被"注视／观测"（"That we're being watched? Observed."），并点名三个可能的观测者："The Librarian? To document the downfall for the next?"／"Or Someone Else perhaps."／"Anakim?"（7280-7285）。随后是那句直指循环结构的判词：

> s: Time is repeating itself.

（7386——此时 Sensei 正在仪式中试探 Yasu 对时间循环的认知："And if you know anything about that, Yasu, I don't think I have any choice but to fuck it out of you now."，7392。）事件末尾，N 层叙述者做出一次罕见的自我陈述：自己「没有被审查」（"I am not being censored"，7398）。在一部处处可见 [[REDACTED]] 的作品里，这句「此处未被审查」本身就是最响亮的警报。endofyasuspring8 作为收束节点封存结果，并按前置条件决定 harukaspring5/6 是否被标记为错过（7450-7455）。

## 三、lust 线概貌

Yasu 线的 lust 内容高度仪式化，与其说是情色场景，不如说是教义演示。源文件中多数露骨段落被 [TRIMMED...] 裁剪，但保留的结构足以概括其叙事功能：

1. **Transference 教义的实践化**。从 church1 起，教会教义就把性定义为神与人之间的转移通道。因此 lust 场景的第一功能是把「布道」兑现为「行为」——Yasu 不是在被追求，而是在执行仪式。

2. **ker／kok 双天使的在场**。yasuspring8 的仪式中，两位天使以单音节对话全程见证。他们的存在把性场景重新编码为「被天界观测的事件」，玩家的窥视位置与天使的观测位置重叠。

3. **sanity 与欲望的兑换**。halloweenyasu1 中 sanity 数值直接跌至 [[ERROR]] 态，性在这条线上是消耗理智的燃料，与 church5 的停药逻辑同构：越接近真实，越失去稳定。

4. **审查机制的显形**。被裁剪的段落本身即是文本的一部分——[[REDACTED]] 与 TRIMMED 标记提醒玩家：这条线的「完整性」被上层有意管理，未裁剪的 yasuspring8 因此成为例外而非常态。

## 四、与主线/元叙事咬合点

1. **三层世界的贯通点**。Yasu 线是少数在恋爱表层内部直接谈论「神之生死」并向上两层递话的线：开场诗对应重置循环层的世界迭代（一神死、一神生的轮回），「the game is playing you now」与「not being censored」则是对玩家层（USER1-4）的直接喊话。

2. **sanity 系统**。sanity 是全局数值系统，而 Yasu 是唯一把 sanity 写进台词哲学的角色（药物侵蚀 sanity 的因果链见 church5）。她的 [[ERROR]] 状态示范了系统崩坏时的表现样式。

3. **与 Tsuneyo 线的强制跳转**。halloweenyasu1 结尾的 jump halloweentsuneyo1 是罕见的跨角色线硬跳转，说明作者把 Yasu 与 Tsuneyo 的 Halloween 内容视为同一事件块的两面。（注意：正文中不存在任何支持 Yasu 与 Tsuneyo 有血缘或祖孙关系的文本证据，二者仅在事件调度上相连。）

4. **Ami 线的暗面**。yasuspring6-8 三连是 Yasu 线与 Ami 线的直接交汇：Yasu 触碰 Ami 的手后所见为 "Ami and...and something else... It was so many of them!"（7113/7121）——从第三方感知侧印证了 Ami 的"附着之物"结构（与 specialbonusamiscene 里 Ami 本体自述 "Those aren't me" 互为双源）；她更断言 "She knew that this would happen. That's why she infected me."（7174）、"She's peeled the skin off of arbiters"（7176）。Sekai 之声在 yasuspring7 的证言（"I died before the curse could reach her"，7126）把本线的亡者主题与 Ami 家族线接通，并抛出全作新概念 "the curse"。

5. **时间循环的显性宣言**。「Time is repeating itself」（7386）是全线对重置循环层最直白的确认之一，与 church1 的神之生死诗构成首尾呼应：神的死亡与时间的重复是同一机制的两副面孔。仪式中天使的见证段落（"That we're being watched? Observed."，7280）进一步把"观测者"从 USER 层扩展到天界侧：The Librarian／Someone Else／Anakim 三个名字是被点名却未登场的观测者候选。

6. **跨角色实验的预约**。yasuspring8 结尾 Sensei 预约让 Yasu 触碰 Maya（7231-7233），并称要验证的事 "affects {i}everyone{/i}"——他把 Yasu 的感知当作检测"Ami 异常是否普遍"的工具，这条实验线是 0.60.0 埋给后续版本的接口。

## 五、未解伏笔

1. **Yasu 的真实身份与来处**：yasudorm30 中 Touka 质问 Sensei 把 Yasu 半夜带出去的举动，Yasu 的来历始终未被正文澄清；医疗设施中的白发少女即 Yasu 本人，其长期就医与「声音」的来源仍属开放信息。

2. **「God says no」的对象**：神的否决究竟针对什么——Transference、Sensei、还是玩家的某次操作——没有下文。

3. **死于诅咒之前的女性**：yasuspring7 证言中的亡者（Sekai 之声）保护了谁、死于何种诅咒、与「幽灵母亲」是否同源，均悬置。**"the curse"（7126/7131）本身是什么、如何运作，0.60.0 未给出任何展开**——它连同 se 的断言"She's lying. Ami's not involved in any of this."一起，构成 Yasu 所见与内心声部证词的直接矛盾：两边必有一边在说谎。

4. **Ami 体内的"许多东西"**：Yasu 触碰后所见（"so many of them! Each more perplexing than the rest"）究竟是什么；"arbiters"（7176）是哪些存在；"infected"（7174）的机制与目的均无下文。

5. **天使点名的观测者**：The Librarian／Someone Else／Anakim（7282-7285）三个候选身份全部未登场，观测的目的与方式未知。

6. **触碰 Maya 的实验**：yasuspring8 预约的检测（7231-7233）结果悬置——Maya 体内是否有与 Ami 同类的东西，是后续版本的直接悬念。

7. **密文的全量含义**：许愿井密文只是已显形的碎片，教会系散落的祷文与灵语是否构成更大的可解码文本集，未知。

8. **「His eternal diary」的持有者**：所指的「他」是谁、日记记录的是什么，正文不答。

9. **仰面入睡的威胁**：church10 中「今晚要仰面睡觉」的叮嘱所防范的具体危险从未登场，属于典型的延迟引爆型伏笔。

10. **Angel 的毕业去向**：church5 的天使轮换教义暗示教会与天界之间存在人员流动机制，其运作方式未展开。

11. **「not being censored」之后的文本**：叙述者声明未被审查的那段话，其完整内容与后果被 spring 系收束节点吞没。
> 按源文件检索本角色 label，见 `索引/Yasu索引.md`。
