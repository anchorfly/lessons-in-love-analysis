# Ami Arakawa 事件线梳理（AmiEvents.rpy，v0.55，11454 行 / 52 label）

> 全文已按 500 行/块完整精读，无跳读。所有结论均标注 label 名与大致行号；无法确认处明确标注"不确定"。

---

## 一、角色基本盘

- **身份**：Sensei 的"侄女"，同住；第二章起在女仆咖啡厅打工（amisroom20→amisroom25）。第四章（chap4active）后公开以"Dad"称呼 Sensei（amicamp2），并反复暗示自己可能是他亲生女儿。
- **表面性格**：极度黏人、以照顾 Sensei 为人生全部意义（"It's me who is the caretaker. It's me who lives to serve." amilust60 行8159）；自称"ultimate niece"；对情敌有清单和威胁史（切手指喂鸭、威胁杀人 amisroom20/amispring2）。
- **深层状态**：长期精神崩坏。第三章末（amispring1）彻底爆发：剪发、持剪刀刺伤 Sensei 手掌、被系统标记 `[BEDRIDDEN]`；Sensei 同时获得 `[DEPRESSED]`——**系统文本直接写出真名 "Akira Arakawa"**（行8708）。amicamp1/2 为修复线：露营、认父、`[DEPRESSION]`/`[PARANOID]` 减弱。
- **meta 感知**：Ami 是全游戏对世界本质知情度最高的角色之一。她知道 timeloop（amiinvite4 被告知）、知道"游戏该怎么玩"、自称"main heroine"、"walls don't work the same for me"（amispring5 行11246–11253），并在第四章宣称下一轮的 Sensei "will be saved"，这一轮的会 "suffer until the credits roll"（行11148–11151）。
- **关键变量**：ami_love / ami_lust 双轨；amifingered（初体验前戏分支）；ami_virgin；bonus（成人内容开关，非 bonus 分支大量用"accountant 会计"梗替换）；amiblock（崩坏后拒接电话/锁事件）；god_love（仅 amilust35 中 +1，指向 Wishing Well 神明体系）。

---

## 二、love 线逐事件脉络

### 第一章～第二章（日常积累）

- **firsttimeamisroom**（439）：搬来后第一个早晨。Ami 边打扫边给失忆的 Sensei 当"NPC 导游"；名台词 "I'm all you'll ever have because I'm also all you'll ever need."（行589）；"如果你交女朋友我就烧了这栋房子"（行603）。+1 love。
- **amisroom3to4**（690）：做早餐聊韩剧的纯日常。+1。
- **amisroom5**（714）：新开美式餐厅约会；Kaori 服务生首登场（自封"Goddess of Gluttony"、胸口蜘蛛纹身、把两人误当情侣、反复叮嘱 "Protect this tiny human"）。Ami 结尾说 "I kind of like her, though... I just kind of...do."（行1031–1034，无理由好感，微妙的违和感）。+1。
- **amisroom10**（1054）：Ami 在房里组 Smashmouth 翻唱乐队（非 bonus）；bonus 分支 jump amibrax。+1。
- **amisroom15**（1121）：一整天宅家看动漫马拉松；晚上 Sensei 洗澡时若 amifingered==True 则 Ami 跟进浴室 → 直接衔接 amisfirsttime；否则安然睡去。+1。
- **amisfirsttime**（1572）：初体验路由器。bonus→x 变体；非 bonus 分支是荒诞文本（"A ghost opens the door and I need to fight it off..." 行1579–1581），但**仍设置 `ami_virgin = False`**——用搞笑文本遮盖事实推进。
- **amisroom20**（1599）：商场。1000 日元羞辱性零花钱梗；Sensei 提议她去女仆咖啡厅打工；Ami 威胁 "I will cut your fingers off and feed them to ducks"→"我养了一支食人鸭军队藏在宿舍后面"（行1881–1884）；结尾悄悄说 "Now I have to add another name to my list."（行1936，名单伏笔）。+1。
- **amisroom25**（1966）：Ami 在家试穿女仆装、练习叫 "Master"。+3。

### 邀请系列（amiinvite1–4）

- **amiinvite1**（2088）：Sensei 打电话"邀请 Ami 来她自己家"（喜剧梗）。进入 Sensei 房间后 Ami 回忆过去：旧 Sensei 是颓废宅、"rotting food and discarded tissues from all of our tears"（行2282）；随后 **Ami 念出十六进制 `61 6c 62 61 74 72 6f 73 73`（=ASCII "albatross"，信天翁，《古舟子咏》意象）**，紧接系统文本 CONNECTION WEAK→TESTING→RESTORED（行2315–2328）。Ami 提到教室午睡醒来不认识她的旧事："It's like you were a different person all of a sudden."（行2336）；旁白补充其父母死于车祸——"her parents were turned into a roadside sculpture of steel and shattered bones"（行2340）。处女分支 Ami 半梦半醒请求亲密接触后入睡；结尾 "Stay with me forever, [amimaster]. Stay with me forever and I'll make you happier than anyone has ever made anyone in the history of the universe."（行2438–2439）。+3。
- **amiinvite2**（2466）：电话直球约"来我房间看看会发生什么"；解锁邀请菜单的 lust 选项。+1 lust。
- **amiinvite3**（2531）：Ayane 来家过夜、买冰淇淋。"Sensei Love Squad" 二人组成立；重要对话：Ayane 说 "I've known Ami since elementary school and I'd never even heard of that Noriko girl until she walked into class"（行2731–2732，记忆空洞）；Ami 对 Niki 失踪多年的合理性发起攻击："how someone can just happen to lose somebody they claim to care about for as long as she lost Sensei... Do you think you'd ever lose Sensei for that long? Because I know I wouldn't."（行2749–2751）。深夜旁白陷入 joy/sorrow 循环哲学（"Think nothing, but feel everything... Praise be." 行2859–2862）。+1。
- **amiinvite4**（6780，第三章）：开场旁白异常（强迫重复 "I love my niece"、血咖喱玩笑）。Ami 抱怨被 Maya/Ayane 排挤、Makoto 泄密；**Sensei 直接说出 timeloop 真相："Your first year of high school is never going to end. You and everyone else are caught in a timeloop"**（行7104–7107）；Ami 拒绝相信，且她的反驳台词被强制原样重复三遍（行7120–7136，展示"重置打断对话"机制）；场景硬重置回开头 "Curry? You never make curry."

### 章节节点事件

- **amimaid30**（2928）：女仆咖啡厅。Ami 自称"第三受欢迎的女仆"，第一名保密——"I don't know if she's ever coming back anyway"（行3134，缺勤伏笔，与 amidate50p4 中 Uta 缺勤呼应但不确定是否同一人）；自卑情结大爆发（对比 Uta）。+1。
- **amidate35**（3272）：商场买泳装。巴士错过梗；"cute girl magic" 解释刘海；Molly 客串讲 Sada Abe 切阳具典故（bonus，行3396–3401——为 Ami 后续"留住男人"话题埋阴森注脚）；Chika 店内试衣间，Ami 用"你不是亲叔叔"话术操纵 Chika 放行（旁白："This fucking demon." 行3497/3507）。试衣间后半按 ami_virgin 分叉；bonus 分支 Ami 正式要求交往："You and me are gonna be together forever cause that's how things are meant to be"——**Sensei 拒绝**；旁白形容她随后的微笑 "held together by Scotch tape and glue"（行3760 附近）。
- **amidate50**（3816）：扫墓。Ami 穿亡母旧裙；static+flash 连续切换（her1–her11）；**母亲亡灵实际回应了她**（se 角色台词）："I miss you too, my sweet girl... I'm always here, though. Even if you can't see me."（行4018–4048）；Ami 崩溃大哭后要求"真正的约会"。+3。
- **amidate50p2**（4177）：动漫店。Molly/Tsuneyo 客串；Molly 也幼年丧母，与 Ami 相拥共情（"I lost my mom when I was little, too"）；Ami 买的漫画《My Sweet Prince》是叔侄题材（自我投射）。
- **amidate50p3**（4499）：咖啡馆。Ami 朗读原创诗 "My Life With You"（"A room full of sunshine- that's my life with you"）；随即 static+spiderbug 场景切换——**Ami 摔碎玻璃杯后完全失忆，不记得刚才读诗的事**，徒手捡碎片割伤手（行4777–4854）。这是"她的时间也在被打断"的最直接证据。
- **amidate50p4**（4865）：超现实巴士之旅（"bus that's moving backwards"）；上帝/天空城堡话题；**呼吸密码 "One. Two. One. Four. Eight."**（行5079 附近）；Saki 以 "REAL HUMAN FEMALE" 身份出现、卡在重复台词 "Greetings, you who are highly favored! The Lord is with you."（×4，路加福音天使问候语）；Ami 说 "Sometimes, I wish you knew how to drive"（车祸伏笔，行5079–5084）；Uta 缺勤伏笔（"She was supposed to work today, too, but she just kinda...didn't show up" 行5124–5127）；**结尾系统文本 `///////////////////////USER1 HAS SUCCESSFULLY LOGGED IN`**（行5170）。
- **aminew1**（5183）：与 Maya/Ayane 咖啡店日常；"quadrouple" 笑点；两女私下谈论 Sensei 会忘记 Ami 生日（"He's not going to remember at all, is he?" "There's always next year."——"next year"在循环世界里是残酷玩笑）。
- **aminew2**（5482）：**全文件最重要 meta 事件**。warble 系列黑色小人打破第四面墙："Congratulations! You have made it to one of many landmarks in the fantastic journey that is Lessons in Love!"（行5561 起）；Sensei 明确自认知："She is a character in a video game that I have somehow found myself inside of"；会说话的盆栽 plant7；marsh warbler 独白 "No one ever cares that I am not the real me. I am just a player in a game." 与重复五遍的 "I want to feel it again"；济慈《夜莺颂》"Do I wake or sleep?"；**Ami 反过来照顾崩溃的 Sensei："We'll forget together. We'll survive together. We'll grow together."**；结尾 jump day60。

### 第三章末～第四章（崩坏与重建）

- **amispring1**（8281）：**大崩坏事件**。开场是 Giles Corey "虫"寓言：1692 年石刑压死的巫术犯胸腔里有靠祈祷之力变硬的虫，虫死后神力散入水中——"We have all drunk from the water. Now, we all have worms inside of us. And every time we talk to God, we're only making them stronger."（行8302–8304）。随后 Ami 唱《Daisy Bell》登场，**剪掉了长发**（"Cut it off and sold it... It's the night before Christmas, boy... I sold it for you."——《麦琪的礼物》戏仿，称 Sensei 为 "Jim"）。场景在多个现实间闪烁：教室放学、"re-introduce you to Kumon-mi! A super normal town"（教程戏仿）、规则三连 "keep your hands off all of your students! BUT YOU DIDN'T FOLLOW THE RULES, JIM!"。核心控诉：
  - "YOU COULD HAVE LISTENED! YOU COULD HAVE FOLLOWED ME LIKE YOU SAID YOU WOULD!"（行8421）
  - 头发像妈妈的，指控 Sensei 曾咀嚼亡母头皮上的头发 "You wanted to feed your worm."（行8429）
  - "**NOTHING MAKES SENSE HERE! IT'S NOT SUPPOSED TO! YOU'RE SUPPOSED TO TREAT THIS LIKE A GAME! YOU'RE SUPPOSED TO GET ME PREGNANT! YOU'RE SUPPOSED TO REACH THE EPILOGUE!**"（行8458–8459）
  - "AMI'S NOT A BAD GIRL! AMI'S A GOOD GIRL! AMI'S THE ULTIMATE NIECE! ... LOVE LOVE LOVE LOVE LOVE LOVE AMI!"（行8469）＋旧场景快速 flash 蒙太奇
  - 挣扎中双刃剪刀刺入 Sensei 手掌（stab.mp3，行8512–8517："I NEED TO CUT THE WORM OUT"）
  - 事后否认："It was the worm! It wasn't me! I'm a good girl!"
  - **母亲亡灵再现**："What have you done to my darling little girl?"（se，行8596）
  - "The worms need to be together."（行8614）；提及 scissor angel 与 Heaven's Web（行8620）；"this world may have already come to an end. And this is all that's left."（行8621）
  - amifingered 分支：Sensei 开始合理化"让 Ami 取代失去的爱"；非 fingered 分支："Should I just give in and be with Ami after all?... This is hell. But it's right where I belong."（行8647–8657）
  - 系统结算：Ami 获得 `[BEDRIDDEN]`；**"Akira Arakawa has obtained the status effect [[DEPRESSED]"**（行8708–8714，末尾 "And the worm will feed once more."）；当晚梦见 clockwater 床上只剩一个盒子。设 amiblock/senseisad，jump dellaslump。
- **amicamp1**（8718）：修复起点。门之诗（"The hallway of life is door upon door..."）；**旁白预告车祸**："Or I am going to be hit by a car on the way home and Ami will be left with no one but a girl who only wants her because she shares my blood."（行8731–8732，同时暗示 Niki 对 Ami 的执念源于血缘）；Sensei 提出露营、宣布要当真正的父亲："You've been deprived of a relationship like that for half of your life... It's no wonder you act so fucking insane all of the time."（行8865–8866）；婚礼誓词式对答 "For better or for worse? / In sickness and in health? / ...I accept you, flaws and all."（行8933–8937）；"I will build you a world where nothing can hurt you anymore."（行8917）。**独居 coda：Ami 独自与看不见的对象商量**（"And who was he talking about just now?... No, I don't think it was you." 行8980–8982；"And if it doesn't work?... That's easy. I can chop it off." 行8998–9003——对象不明，极阴森）。+1，jump saracamp1。
- **amicamp2**（9013）：露营。Sara 已把 Ami 剪坏的头发修短；公开场合 "I love you, Ami."；日落散步谈上帝：Ami 相信苦难是神的考验，为了"giant sky castle"的限量席位（行9235–9243）；**循环自觉**："there are probably tons of conversations we've had before that we're going to forget about and then have again."（行9262–9264）；"Do you think our answers will ever change?" "I don't think there's anything off limits for change now that my hair is completely gone."（行9265–9270）；正式获准叫 "Dad"；**两个重磅炸弹**：①"Do you think my first dad would be okay with it? Because I've tried asking him, but... I never really get a response."（行9334–9335，她在向亡父问话？）②"There's always the chance that I could be, like...your actual daughter anyway, right?... I already know you loved my mom, so... It wouldn't be crazy if I was your real daughter anyway! Right?!"（行9344–9357，Sensei 语塞，话题被封存）。结算：`[DEPRESSION]`/`[PARANOID]` 减弱；amifingered 时授予称号 "[[(ALLEGED) DAUGHTER-FUCKER]"。+10 love。
- **halloweenami1**（9481）：万圣节。旁白称 Maya 为 "the tragic tale of Maya Makinami (or the one who wears her skin)"（skinwalker 措辞，行9487）；Ami 以魔法少女 "Sakura Sunlight"（"seven and a half steps ahead"）姿态追到神社安慰失恋的 Maya；中段旁白退化成押韵打油诗甚至直接对屏幕前的玩家喊话（行9589–9598）；随后 Ami 摊牌：**她早就知道 Maya 和 Sensei 的关系**——"Do you really think I wouldn't catch on to my best friend in the whole wide world fucking my uncle while I'm home sometimes?"（行9618）；更爆出她多年来贴门偷听、跟着节奏同步自慰（行9695–9709，注意此处她称 Sensei 为 "your father"——即以女儿自居）；最后提出契约：要么一起"用皮带拴住他"，要么三人同行，"It will never be only you again. Not for the rest of our lives."；Maya："I'm in."（行9740）。
- **amispring2**（9747）：Niki 豪华轿车旅行（带 Noriko 当" bonding 润滑剂"）。捆绑笑话开场；**Ami 故意提 Sara 刺激 Niki 吃醋**（行9803–9839，计算性行为）；"pregante" 拼写梗；Niki 离开后 Ami 向 Noriko 亮出真实立场：反对 Niki 取代亡母——"I'm talking about my mom. The same one I've always had... There are things she can still teach me from wherever she is now."（行9952–9966）；"being 'broken' is just an Arakawa family trait. We're all like that."（行9981）；Noriko 感到她"突然聪明得可怕"（行9986）；Noriko 交心 "I shouldn't care, but I do."；Sensei 被 Noriko 偷偷邀来，衣柜躲藏喜剧；Ami 主动牺牲自己引开 Niki："The time has come...for Ami Arakawa... To do something good..."（行10124–10125）。
- **amispring3**（10138）：**第四章最重的剧情事件**。回程 Shiritori/Karuta 缓冲后，Sensei 把 Ami 叫进房间对质——Ami 承认帮 Niki 找到了他们，且承认就是想让 Niki 搬走。争吵全面引爆：
  - **母亲死因真相（文本内最大爆料之一）**："POEM AFTER POEM AFTER POEM! VOICES, VOICES, VOICES! IT'S NO WONDER SHE COULDN'T BREATHE WITH A NOOSE LIKE THAT AROUND HER NECK!!"（行10456）；"she was practically dead for a whole fucking year before that while her mind was being overrun by who the fuck knows what! And you could have done something! You could have listened! Because I know you read the poems! But you didn't understand them! You didn't believe them! No one did!"（行10464–10465）——即母亲并非单纯"事故身亡"，死前一年已被"声音/诗歌"吞噬，而 Sensei（Akira）选择压抑与无视。
  - "Don't fucking talk to me about praying, Dad! ... I will not lose you to some fucking worthless God as well!"（行10435）
  - "YOU happened to me! I'm like this because of YOU!"（行10515）；"Do you have ANY idea how fucking HARD it is for a seven year old to raise TWO PEOPLE when you're in your fucking THIRTIES and can't even raise YOURSELF?!"（行10522）
  - "Despite all of that... I have never stopped living for you. The one thing I have left. But sometimes?... I feel like you'd be happier if I died too."（行10532–10536）
  - 摔门而去 "Somewhere I won't be a fucking burden anymore!"；Sensei 独白发现连亡灵都不再出现（行10558）；最终躺进 Ami 的床、注意到衣柜里露出的笔记本（行10576–10579，未开启的伏笔）。结算 noriko_love+1、amiblock，系统文本 "Everyone else has abandoned you..."，jump yukispring5。
- **amispring4**（10594）：lust 事件（见第三节），但结尾是全文件最极端的文本崩坏：Ami 的 "Daddy" 呼喊逐轮退化为键盘乱码，最后一词归于 "father."；旁白只剩 "I sex." "I cum." "MORE."；收束于五遍 "I love my daughter." 与一句 "Is this my daughter?"（行10889–10899）。四项数值各 +10。
- **amispring5**（10918）：**自创节日 Father Appreciation Day**。开场 "Lucy, I'm house"（I Love Lucy+amispring1 "I am house" 回环）。Ami 的"礼物"是**下药绑架 Karin 捆在椅子上**送给 Sensei（"Drugs! The same stuff that guys give to girls at bars..." 行10977）。两条分支（按 amifingered）在逼问中滑向同一个 meta 核心：
  - 非 fingered 分支：Ami 点破主线秘密设施——"keeping some little girl holed up in a secret sex dungeon for months if not years is probably kidnapping by legal definition"（行11138，指被囚的 Maya）；"Know. Knew. There's nothing that eludes me, Dad."；"you still refuse to play the fucking game how it's meant to be played because you're a baby-back bitch who's turned off by polygons"（行11146）；"the next one? And the one after that? They'll fuck me. They'll fuck me hard. And in turn, they will be saved. But you? You will fucking suffer for this. And I will make sure of it until the credits roll."（行11148–11151）
  - fingered 分支：被问及为何笃定 Sensei 终将堕落，答 "To complete the collection, obviously."……"Because walls don't work the same for me that they do for you. I'm special. I'm the main heroine."（行11245–11253）
  - 两分支同以 Sensei 的 "How much of this do you know?... For real?..." 与 Ami 的 "Fuck me and I'll tell you." 收口；Sensei 最终把她扑倒捆起来作为回敬（ami_love −10）；Karin 傍晚苏醒被送走；结尾对峙："you'll no longer be my daughter." / "Acknowledge me." / "Can you say it back, please?"（×2，又是强制重复句式）→ 被迫回答 "I love you too..."。Sensei 睡沙发，"I'll untie Ami in the morning."

---

## 三、lust 线概貌（抽象概括，不复述露骨文本）

lust 线共 8 个 label：amiinvitethighjob / amiinvitereverse（amiinvitegen 菜单入口，131/152）、amilust15（3782）、amilust35intro（6075）→amilust35（6267）、amilust50intro（7627）→amilust50（7727）、amilust60intro（8020）→amilust60（8080），外加 amispring4（10594）。特征：

1. **meta 密度与性场景正相关**。几乎每个 lust 场景都伴随 static+flash、系统文本或叙事者崩坏：amilust35skip 的拒绝分支甚至直接弹出系统警告 "WARNING: You are playing Lessons in Love incorrectly. Please start a new game and have sex with Ami Arakawa immediately. Failure to do so may result in unexpected errors, game crashes, or worse." 并切入 "theend" 场景硬停 60 秒（行6062–6065）——游戏机制层面把"与 Ami 发生关系"写成通关条件。
2. **文本退化是核心表现手法**。amilust35 中 Ami 台词变成大写混乱体（"I CAN FEEL THE LIGHT OF LAST SUMMER RE-ENTERING MY BODY THROUGH MY FLESH CREVICE"），旁白退化为 "I keep doing the sex to Ami probably idk"；amispring4 将该手法推至极限（乱码→"father."→"I sex."）。
3. **Ami 始终是主导者与仪式执行者**。amilust50 中她要求 Sensei 把她当作刻薄的 Maya 对待（"I no longer care who is real and who is make-believe"），场景中途插入疑似 Maya 本人的台词制造真身/扮演混淆，结尾旁白 "It's that Maya smells a lot like Ami today... And it happened again. I did a bad thing."（行7996–8007）——暗示 Sensei 在 lust 状态下分不清双姝。
4. **amilust60 是"caretaker 疯狂"的完成态**：全程以第三人称病态叙事包裹（把日常照护写成"驱魔仪式"），穿插 Xoanon 插叙——它从水里捞起一具身体、用羊皮巾擦干、在笔记本上写下 "Blessed be those who live to protect. Who live selflessly, helplessly, and full of regret." 然后 "awaits the next reset"（行8171–8175）；旁白直接写出 "her uncle, Akira"（行8265）。冷冻柜里的收藏罐被注明"还有几个更重要的用途，但 Ami 要求 AUTO-PILOT 不要写出来"（行8221）。
5. **god_love 变量全文件仅在 amilust35 中 +1**（行6445 附近），把 lust 线与 Wishing Well/神明观测体系挂钩。

### 好/坏叔叔标识（amifingered / ami_virgin 双 flag）

源码以两个布尔 flag 显式区分"好叔叔/坏叔叔"路线，**是否夺走 Ami 的处女**是核心标识：

- **初始值（好叔叔默认）**：`amifingered = False`（definitions.rpy:1629）、`ami_virgin = True`（definitions.rpy:1640）。
- **分岔点 = amidorm10**（DormEvents.rpy 宿舍 Ami 线）：Ami 直问 "Will you lose yourself with me?"，三选项："Yes"（bonus 跳 amidormtouchx）/ 非 bonus "Hugging you, I guess" → `$ amifingered = True`（DormEvents.rpy:24961）——自此进入"坏叔叔"状态；**"..." 是唯一保持好叔叔的入口**（DormEvents.rpy:25044，`amifingered` 显式保持 False）。非 bonus 文本以"拥抱"抽象带过并弹系统提示 "This may make an impact on the story going forward..."（游戏明示此 flag 改变后续剧情）。
- **单向门 = amisroom15**（AmiEvents.rpy:1121 浴室夜）：`if amifingered == False`（行1536）→ 平凡入睡、事件无害结束；否则进入 `amisfirsttime`（行1572）→ `$ ami_virgin = False`（行1585；bonus 版 inappropriatecontent.rpy:2678）——**夺走处女的落点**。选择权实质在 amidorm10，浴室夜无回头路。
- **后续影响**：
  1. 事件门控：`amisroom25` 要求 `ami_virgin == False`（AmiEvents.rpy:12）；**Maya 神社线 `shrine30` 同样要求 `ami_virgin == False`**（MayaEvents.rpy:18；进度校验 newchecker.rpy:2041、screens.rpy:3980 同步该条件）——坏叔叔状态是 Maya 线推进的硬前提。
  2. 事件内分支定制对话：`amiinvite1` 中 True 分支 Ami 埋怨 Sensei"不肯碰我/因为是家人所以有问题吗"（行2367 起）、False 分支直接进入亲密话题（行2149/2161）；`amispring5`（行10918，"父亲感谢日"事件）中坏叔叔版 Ami 自封 "main heroine"（行11253）。完整对照见 `../05_好叔叔与坏叔叔分支全对照.md`。
  3. **跨角色道德状态位**：`amifingered` 被 Io、Futaba、Chika、Dorm2、Noriko（×9）、Niki、Nodoka、Molly、Maki 等十余个文件的条件分支引用——其他角色的事件台词与走向会随好/坏叔叔状态改变；`ami_virgin` 还影响 ChinamiEvents.rpy:1490、ch2script.rpy:7272 与 animatedscenes.rpy:2926–3052 的动画场景文本分支。
  4. 同组 flag（同一定义区，definitions.rpy:1627–1656）：`ayane_virgin`（ayanedorm10，DormEvents.rpy:7660）、`makoto_virgin`（script.rpy:2376/2912/32510）、`chika_virgin`（ChikaEvents.rpy:3637）、`kirin_virgin`（script.rpy:2914）。唯 Ami 的 flag 同时挂 `amifingered` 前置门与跨角色引用网，道德权重最高。
- 唯一直接使用"好叔叔"措辞的源文在泛型日常：chap4generics.rpy:606 "because that's what good uncles do"（此时 Ami 卧床相伴的语境）；"bad uncle" 无字面出现，好/坏之分完全由 flag 结构实现。

---

## 四、与主线的咬合点

1. **真名 Akira 的多处锚定**：amispecial50 亡女友称他 "Aki-kun"（行7338）；amilust60 旁白 "her uncle, Akira"（行8265）；amispring1 系统文本 "Akira Arakawa has obtained the status effect [[DEPRESSED]"（行8708）。
2. **重置机制的微观展示**：static.mp3+flash 全文数十次；CONNECTION WEAK 断线序列（amiinvite1 行2317–2328）；USER1 HAS SUCCESSFULLY LOGGED IN（行5170）；Xoanon "awaits the next reset"（行8175）；amiinvite4 同一台词强制重复三遍＝"对话被上游打断"的现场演示；amispring5 "Can you say it back, please?" ×2 同款。
3. **游戏自认知链**：warble 小人（aminew2）→ Sensei "She is a character in a video game" → Ami "YOU'RE SUPPOSED TO TREAT THIS LIKE A GAME! ...REACH THE EPILOGUE!"（amispring1）→ "turned off by polygons"/"until the credits roll"/"play the game instead of letting it play you"（amispring5）→ "I'm the main heroine"（amispring5）。Ami 的知情程度远高于其他角色，且她把"下一轮的 Sensei 会顺从"当作确定事实。
4. **车祸暗线**：父母死于车祸（"roadside sculpture of steel and shattered bones" amiinvite1 行2340）；amidate50p4 "Sometimes, I wish you knew how to drive"；amicamp1 开头旁白直接预演 Sensei 被车撞的剧本——三处共同指向主线中的白色汽车/车祸事件。
5. **母亲之死重解**：amispring3 爆料母亲死前一年被"voices/poems"吞噬（"A NOOSE LIKE THAT AROUND HER NECK"），Sensei 读过诗却拒绝相信——与 amidate50 亡灵能正常对话、amispring1 亡灵谴责 Sensei 形成互证：Arakawa 家的女性死后并不"离开"。
6. **血统疑云**：amicamp2 Ami 直球提出 "I could be your actual daughter anyway, right?"，Sensei 不置可否只说"以后再谈"——与主线"Ami 疑为 Sensei 与 Sekai 之女"的推断在文本内形成正面对接口；另注意 halloweenami1 中 Ami 已以 "your father" 称呼 Sensei。
7. **神明观测体系**：Wishing Well 的 gods 目击 caretaker 行为（amilust60 行8169–8170）；scissor angel 与 Heaven's Web（amispring1 行8620）；god_love 计数（amilust35）；Ami 的虔诚信仰（amicamp2 天空城堡论）与其"worm/God 使虫变强"的民间神学（amispring1 开场寓言）互相咬合。
8. **Kyoko/十六进制等暗线**：amiinvite1 的 hex "albatross"（信天翁＝负罪感意象，Coleridge）；amispecial50 的 letmeout 逐字母场景（l/e/t/m/e/o/u/t，谁被困？结合 amispring5 的"地下室小女孩"可知至少有一人在墙后求救）。
9. **Maya—Ami 共生结构**：halloweenami1 揭示 Ami 多年偷听并策划三人契约；amispring5 显示 Maya 已被囚禁而 Ami 全知；amilust50 的"扮演 Maya/真身混淆"说明两人的边界在叙事层被刻意糊化。

---

## 五、未解伏笔清单

1. **hex "albatross"**（amiinvite1 行2315）：为何由 Ami 口述？信天翁具体指谁的罪？
2. **呼吸密码 "One. Two. One. Four. Eight."**（amidate50p4）：未解。
3. **letmeout**（amispecial50）：求救者是墙内的 Maya 还是别的存在？
4. **amispring1 结尾梦境**：clockwater 床上空无一人、只剩 "a box"——盒子是什么？
5. **Xoanon 从水里捞起的人**（amilust60 行8171）：身份未明。
6. **收藏罐"更重要的用途"**（amilust60 行8221）：被 AUTO-PILOT 按 Ami 要求隐去。
7. **USER1 是谁**（amidate50p4 行5170）：登录的是玩家、Maya 还是别的？
8. **秘密的第一名女仆**（amimaid30 行3131–3134）："she's never coming back anyway"——是谁、去了哪？（与 Uta 缺勤是否同源不确定）
9. **Ami 的信息来源**：她如何知道重置、epilogue、polygons、"collection"？文件内无解释。
10. **"my first dad... I never really get a response"**（amicamp2 行9334–9335）：Ami 在向谁问话？亡父？还是另一存在？
11. **amicamp1 结尾独白对象**（行8976–9003）：Ami 与看不见的存在讨论露营计划，"he's never called himself that before"（指 Dad 称呼），失败预案是 "I can chop it off"——对象与所指均未解。
12. **Ami 是否亲生**（amicamp2）：Sensei 回避，悬置。
13. **amispring3 衣柜里的笔记本**（行10576–10579）：Sensei 注意到但未翻开。
14. **Uta 缺勤**（amidate50p4 行5124–5127）：与 8 可能相关，不确定。
15. **"another name to my list"**（amisroom20 行1936）：Ami 的名单内容从未完整揭示。

---

## 六、label 总表（52 个）

| # | label | 行号 | 类型 | 一句话概括 |
|---|-------|------|------|-----------|
| 1 | amisroom | 1 | 路由 | 按 ami_love 分档进入房间事件 |
| 2 | amiinvite | 17 | 路由 | 邀请事件入口 |
| 3 | amiinvitegen | 32 | 日常/菜单 | 电话邀请"来你自己家"+选项菜单 |
| 4 | amiinviteaff | 85 | 日常 | 同床聊天回忆，+3 love |
| 5 | amiinvitethighjob | 131 | lust 存根 | bonus→x 变体，否则 +3 lust |
| 6 | amiinvitereverse | 152 | lust 存根 | 同上 |
| 7 | amimaidhub | 173 | 路由 | 女仆咖啡厅事件分发器 |
| 8 | callamimorning | 185 | 路由 | 早电话（amiblock 拦截） |
| 9 | callamiafternoon | 195 | 路由 | 午电话，可触发 amidate35 |
| 10 | callaminight | 258 | 路由 | 晚电话 |
| 11 | amimaidgen | 310 | 日常 | 女仆咖啡厅探班，+1 |
| 12 | amigenafternoon | 344 | 日常 | 游戏掉率吐槽+按摩，+1 |
| 13 | amigennight2 | 372 | 日常 | 圣诞后版本：无言并躺，+1 |
| 14 | amigennight | 407 | 日常 | 披萨电影夜，+1 |
| 15 | firsttimeamisroom | 439 | 剧情 | 初见早晨，NPC 导游宣言 |
| 16 | amisroom3to4 | 690 | 日常 | 韩剧早餐，+1 |
| 17 | amisroom5 | 714 | 剧情 | 餐厅约会，Kaori 登场 |
| 18 | amisroom10 | 714→1054 | 日常 | Smashmouth 翻唱乐队 |
| 19 | amisroom15 | 1121 | 日常/分岔 | 宅家日；fingered→通向初体验 |
| 20 | amisfirsttime | 1572 | 路由 | 初体验分发，设 ami_virgin=False |
| 21 | amisroom20 | 1599 | 剧情 | 商场+女仆打工提议+"名单" |
| 22 | amisroom25 | 1966 | 日常 | 家中试穿女仆装 |
| 23 | amiinvite1 | 2088 | 剧情 | hex albatross+断线文本+车祸爆料 |
| 24 | amiinvite2 | 2466 | lust 入口 | 解锁邀请 lust 选项 |
| 25 | amiinvite3 | 2531 | 剧情 | Ayane 过夜；Noriko 记忆空洞质疑 |
| 26 | amimaid30 | 2928 | 剧情 | 第一女仆之谜+泳装计划 |
| 27 | amidate35 | 3272 | 剧情 | 试衣间操纵；交往要求被拒 |
| 28 | amilust15 | 3782 | lust | 整事件是一首诗 |
| 29 | amidate50 | 3816 | 剧情 | 扫墓；亡母真实回应 |
| 30 | amidate50p2 | 4177 | 剧情 | 动漫店；与 Molly 丧母共鸣 |
| 31 | amidate50p3 | 4499 | 剧情 | 读诗→失忆→碎杯割手 |
| 32 | amidate50p4 | 4865 | 剧情/meta | 倒行巴士；USER1 登录 |
| 33 | aminew1 | 5183 | 日常 | 生日将被遗忘的预言 |
| 34 | aminew2 | 5482 | meta | warble 第四面墙；游戏自认知 |
| 35 | amilust35skip | 5995 | lust/警告 | 拒绝分支：系统错误警告+theend |
| 36 | amilust35intro | 6075 | 过渡 | 秘密泄露闪回串 |
| 37 | amilust35 | 6267 | lust/meta | 文本崩坏；god_love+1 |
| 38 | amimaid50 | 6447 | 剧情 | 更衣室；"stop suffocating me"→"No." |
| 39 | amiinvite4 | 6780 | 剧情/meta | timeloop 真相告知+打断演示 |
| 40 | amispecial50 | 7163 | 剧情/meta | Aki-kun；letmeout；仪式化宣誓 |
| 41 | amilust50intro | 7627 | 门控 | 卡拉OK；拒绝分支 Sana 冲突 |
| 42 | amilust50 | 7727 | lust/meta | Maya 人格扮演；"I did a bad thing" |
| 43 | amilust60intro | 8020 | 剧情 | 囚室日常；筛查访客；omurice |
| 44 | amilust60 | 8080 | lust/meta | caretaker 疯狂叙事；Xoanon 插叙 |
| 45 | amispring1 | 8281 | 剧情高潮 | 剪发崩坏；剪刀刺掌；BEDRIDDEN/DEPRESSED |
| 46 | amicamp1 | 8718 | 剧情 | 露营提议；父女誓约；阴森 coda |
| 47 | amicamp2 | 9013 | 剧情 | 剪发揭晓；"actual daughter" 炸弹 |
| 48 | halloweenami1 | 9481 | 剧情 | 安慰 Maya；偷听坦白；三人契约 |
| 49 | amispring2 | 9747 | 剧情 | 豪华车旅行；算计 Niki；向 Noriko 交底 |
| 50 | amispring3 | 10138 | 剧情高潮 | 对质爆发；母亲死因真相；离家 |
| 51 | amispring4 | 10594 | lust/meta | 文本完全崩坏；"Is this my daughter?" |
| 52 | amispring5 | 10918 | 剧情高潮 | 下药绑架 Karin；main heroine 宣言；反向捆绑 |

---

*文档生成于全文精读完成后。所有行号为近似定位（±5 行）。*


---

## 【二轮增补】Ami 线逐 label 详梳

> 摘自二轮核心角色组精读（R1）。行号=源文件行号。

## 二、Ami 线逐 label 详梳（AmiEvents.rpy，v0.60.0，约 11454 行 / 52 label）

### 2.0 调度与门控（事件依赖网）

- **amisroom 调度器 [2-15]**：amisroom5←love≥5；amisroom10←love≥10；amisroom15←love≥15+amidorm15；amisroom20←love≥20+**beachvacation16+mayadorm25**（Ami 房间事件居然依赖 Maya 宿舍线）；amisroom25←love≥25+**ami_virgin==False**+amidorm20 [12]。
- **amiinvite 调度器 [18-30]**：amiblock 期间全线封锁（"I don't think Ami wants to see me right now..." [19]）；amiinvite3 需 **shrine35==True**（Maya 神社线前置）[25]；amiinvite4 需 love≥50+**kaorispecial40+amimaid50** [27]。
- **amimaidhub [174-183]**：amimaid30←love≥30+**utadorm10+bar35**；amimaid50←love≥50+**treasureisland+makotodorm55p2+norikoinvite3** [176]。
- **callamiafternoon [199]**：amidate35←love≥35+amimaid30+**shrine35**——Ami 中期约会硬依赖 Maya 线两次。
- **lust 入口 [75-83]**：两 lust 选项均需 ami_virgin==False；第三项需 amiinvite2==True（好叔叔线永久 miss，见下）。

### 2.1 日常与 early love 线

- **firsttimeamisroom [439]**（+1）：初见晨。Ami 自嘲 "I'm starting to feel like one of those NPCs that guides the protagonist in the beginning of an RPG." [525]（NPC 导游是 Ami 自己的台词，非旁白评价）。名台词 "I'm all you'll ever have because I'm also all you'll ever need." [589]（我是你仅有的一切，因为我也是你所需的一切）；"如果你交女朋友我就烧了这栋房子" [603]。
- **amisroom3to4 [690]**（+1）：韩剧早餐，纯过渡。
- **amisroom5 [714]**（+1）：美式餐厅；Kaori Kadowaki 初登场（"Goddess of Gluttony" [934]、蜘蛛纹身 [964-967]、误认二人 "romantic pheromones" [865]、"Protect this tiny human" [884]）。结尾 Ami："I kind of like her, though... I just kind of...do." [1031-1034]（无理由好感，违和感伏笔——Kaori 与 Ami 的家族性亲近在后文 amicamp2 [9018] "[[REDACTED] with Kaori" 再现）。
- **amisroom10 [1054]**（+1）：非 bonus 版为 Smashmouth 翻唱乐队恶搞 [1104-1107]。
- **amisroom15 [1121]**（+1）：全天宅家日。三处要点：
  1. **最早的主角宣言**：Ami 嬉闹时自称 "That's right. And I, Ami Arakawa, am the true protagonist of this story." [1297]——比 amicamp2 的 "ultimate niece" 复诵 [7587-7590] 与 amispring5 的 "main heroine" [11253] 早数千行，且以"看家者=真主角"的玩笑形式出现。
  2. **血缘疑云措辞**：bonus 分支 Ami 抱怨 "Why did you have to go and be born like a million years earlier than me? And also be related to my dad?" [1306]（你干嘛比我早出生一百万年？还跟我爸是亲戚？）——若 Sensei 仅是叔叔，正常措辞应是"和我有亲戚关系"；"related to my dad" 是 Ami 以"女儿"自居的世界观泄漏（非 bonus 版同位句为棕发/旋转门玩笑 [1309]）。
  3. **单向门 [1536-1567]**：amifingered==False → 平凡入睡+炖牛肉温情收束；True → 浴室夜 → amisfirsttime。路障玩笑分岔 [1313-1358]：坏叔叔 "I kind of like you the way you are" [1314]；好叔叔 "all we are is [uncle] and [niece]... probably all we'll ever be." [1357-1358]。
- **amisfirsttime [1572]**：非 bonus 版"幽灵闯入被我击退"三行恶搞 [1579-1581]，随即 `$ ami_virgin = False` [1585]、`specialclassroom = True` [1587]——用荒诞文本遮盖事实推进（flag 落点与 05 对照一致）。
- **amisroom20 [1599]**（+1）：商场+打工提议。新细节：
  - Sensei 知道女仆咖啡厅的真正原因是 Maya，且主动隐瞒："What I can't tell Ami is that Maya {i}is{/i} the reason I know about it." [1826-1828]——**Ami 线第一章就埋下 Sensei–Maya 瞒线**，为 halloweenami1 的偷听揭发做对照。
  - 恐吓链 [1881-1884]：切指喂鸭→"I raised an army of carnivorous ducks and have been hiding them behind the dorms."
  - 结尾名单 [1936-1939]："Now I have to add another name to my list." / "Don't you worry about it, Sensei. Don't you worry at all..."——比一轮 md 记录多出第二句阴森收尾。
  - Ami 的"秘密收入"实为偷刷 Sensei 信用卡+低级身份盗用买漫画 [1704-1705]。
- **amisroom25 [1966]**（+3）：家中试穿女仆装；"You are forbidden from calling anyone else that name." [2022]（Master 称谓独占）；"I'd rather die than do something like that." [2035]。
- **amiinviteaff [85]**（+3）：并床夜。旁白："her relationship with me is much more than mine will ever be with her" [96]——Sensei 自认是"没继承记忆的替代品"，与 amiinvite1 [2338] "I {i}was{/i} a different person all of a sudden" 同一元层自白。

### 2.2 中期剧情事件（love 主干）

- **amiinvite1 [2088]**（+3）：全事件结构与 05 对照一致（"邀请 Ami 来她自己家"救护车喜剧 [2113-2117]、hex "61 6c 62 61 74 72 6f 73 73"=albatross [2315]、CONNECTION WEAK 断线文本块 [2317-2328]、父母车祸 "roadside sculpture of steel and shattered bones" [2340]）。新增两点：
  - bonus 分支的黑暗期补写 [2348]："maggots consume everything as your traumatized [niece] finds new ways to please herself on the opposite end of the house. Anything to distract from the pain."——旧 Sensei 崩坏期 Ami 在房子另一端自我麻醉的具体描写（与 amispring1 虫意象、halloweenami1 门后自慰互文）。
  - 好叔叔锁死机关 [2367-2419]：Ami 直问 "Then how come you won't finger me?... there's anyone else in the world who I'd rather have fuck me from dawn 'til dusk." [2369-2373]（非 bonus 版为"为何不抱我" [2376]）→ `$ amiinvite2miss = True` [2419]，系统嘲讽 "Imagine having morals in a place like this." [2417]。坏叔叔版以 "Stay with me forever... I'll make you happier than anyone has ever made anyone in the history of the universe." [2438-2439] 收尾。
- **amiinvite2 [2466]**（+1 lust）：坏叔叔专属；电话直球 "So you want to have sex?" [2481]。
- **amiinvite3 [2531]**（+1）：Ayane 过夜。Sensei Love Squad 成立 [2670-2713]；Ayane 记忆空洞 "I've known Ami since elementary[school] and I'd never even heard of that Noriko girl until she walked into class." [2731]；Ami 攻击 Niki 失踪逻辑 [2749-2751]；Ayane "You're pretty much the only family I have now." [2784]；深夜旁白 joy/sorrow 循环哲学 "Think nothing, but feel everything... Praise be." [2859-2862]（与 halloweenami1 的 "Praise be!" [5563-5564] 呼应——同一邪教式语汇）。结尾旁白好叔叔版更阴暗（"hopes that she dreams of what I do to Ayane" [2900]）。
- **amimaid30 [2928]**（+1）：女仆咖啡厅。第一女仆之谜 [3131-3134]（"she's never coming back anyway"）；新细节：①**amipatgasm 分支** [3143-3153]——若此前摸头触发过异常反应（amipatgasm==True），Ami 会惊慌 "We found out last time that weird things happen when you pat my head!"（摸头小游戏的世界内回响）；②**"Mega Ami"** [3187]："I spent years and years and years and years turning into Mega Ami so you wouldn't look at people like Uta-chan."（多年自我改造论）；③"walking trash receptacle for your love" [3184]（自我物化措辞）；④Osako 客串吐槽 "My appearance in this event is over now." [3059]（配角自觉元台词）。
- **amidate35 [3272]**（+1）：泳装商城。Molly 的 Sada Abe weebnote [3396-3401]；**cute girl magic** [3366-3375]：Ami 解释刘海变化 "The same way Maya can eat more than her body weight in food and **Ayane can materialize guns and giant bananas out of thin air**."（把游戏引擎级的荒诞设定当作"可爱女孩魔法"糊弄过去——世界内自洽话术）。试衣间操纵 Chika [3494-3509]（"This fucking demon."×2）。结局分岔 [3633-3777]：好叔叔止于商场+`amidorm40miss=True` [3649]；坏叔叔续摊逼婚 "Then make it official and start dating me for real." [3700]→拒绝→"And if anyone ever tries to ruin that, I will do horrible things to them." [3725]→旁白 "held together by Scotch tape and glue" [3748]。坏叔叔版 Ami 当场露骨自曝（"lets you cum on her face" [3727]，成人内容不展开）。
- **amilust15 [3782]**（+2 lust）：整事件是一首诗。开头四行引 Baudelaire《Les Fleurs du mal》"Au Lecteur"（"At my side the Demon writhes forever... an eternal guilty desire" [3783-3786]），随后接"人脂成光"的存在主义散文诗 [3787-3797]；非 bonus 版自嘲 "That's it. This entire event was a poem." [3802]。
- **amidate50 [3816]**（+3）：扫墓。开场**William Blake《Auguries of Innocence》**七行引诗 [3828-3834]（"To see a World in a Grain of Sand..."，一轮 md 未记出处）；te 角色（梦中介于神/教师之间的存在）："You need to wake up or God will cut your hands off and feed them to his angels. It's true because I said so." [3874]；床吞噬意象 [3835-3856]；旁白重置暗示："I wonder if these too are wiped clean each time I come down from the rooftop under a starlit sky." [3841]；母亲亡灵 **se 实际应答** [4018-4048]（"I'm always here, though. Even if you can't see me." [4026-4027]；"And your uncle too. He's helpless on his own." [4046]）；**Daisy Bell 是母亲哄睡歌** [3986-3987]："I still get that old song you'd sing to me in bed stuck in my head... Daisy...Daisy..."（amispring1 剪发夜再唱此曲即"亡母之歌"）；旁白直书循环困境 "even those are plagued by an unending misery in which she'll never be able to truly overcome them **for she can never grow old**" [3943]，以及 "She grows stronger by the day. I fade into the background." [3932-3933]。结局 good/bad 分岔 [4103-4129] 同 05 对照。
- **amidate50p2 [4177]**（+1）：动漫店。Molly 丧母共情 [4409-4411]；My Sweet Prince 叔侄漫画 [4333-4343]；**Niki 情报线**："Niki told me about how you two used to watch anime together" [4272]——Ami 对旧 Sensei 的知识部分来自 Niki。
- **amidate50p3 [4499]**：咖啡馆读诗。诗《My Life With You》全文 [4711-4719]（"A room full of sunshine- that's my life with you."）；**母亲诗歌在阁楼被发现** [4766]（"when I was going through some of Mom's stuff last night, I found a bunch of her old poetry"）——为 amispring3 的 "POEM AFTER POEM" 爆料 [10456] 预先埋点；碎杯失忆 [4785-4834]：Ami 对数十秒前的事完全无记忆、徒手捡玻璃割伤 [4849-4852]，旁白收束 "It reminds me of something." [4853]（戛然而止）。
- **amidate50p4 [4865]**（+1）：超现实回程。结构：倒行巴士 [4873]→舔舐伤口 [4880]→天空城堡问答 [4897-4900]→**呼吸密码 "One. Two. One. Four. Eight."** [4909]（"a secret language we devised when we weren't as tattered"——二人童年密语；abacus 旁白 [4911-4914]）→REAL HUMAN FEMALE（saki）四次重复路加福音问候 [5059-5063]→**"Sometimes, I wish you knew how to drive... Because it would give us something to do when everything else disappears."** [5079-5084]→**Ami 全盘否认说过** [5097]："Sensei, I haven't said anything this entire ride. You passed out the second we got on."（愿望台词被世界抹除的现场演示）→手伤次日照常痊愈 [5109-5115]（**连身体创伤也被重置**）→Uta 缺勤伏笔 [5124-5127]→**`USER1 HAS SUCCESSFULLY LOGGED IN`** [5170]→jump returntosummer1。
- **aminew1 [5183]**（+1）：四女咖啡店。"quadrouple" 梗 [5223]；Ami 当众宣言 "I consent to a romantic relationship with this man..." [5326]；后台 Maya/Ayane 对话 [5434-5458]："When do you think he'll remember it's her birthday?"→"He's not going to remember at all, is he?"→**"There's always next year."** [5458]（循环世界里的"明年"是黑色玩笑）。
- **aminew2 [5482]**（+1）：**全文件 meta 核心**。层次：
  1. 旁白彻底崩坏：被迫重复 "I am going to spend the morning with my niece because she is cute and I love her." [5494]；live studio audience（雇来的罐头笑声观众）[5524-5531]；marsh warbler 知识播报 ×2 [5582-5585]/[5797-5800]。
  2. 两个纯黑小人 a1/a2："Congratulations! You have made it to one of many landmarks in the fantastic journey that is **Lessons in Love**!" [5561]（**游戏名入台词**）。
  3. 会说话的盆栽 plant7 [5702-5738]（埋袜子梗："Stop thinking altogether. Erase your mind... Life goes on." [5736-5737]——与 amiinvite3 "Think nothing, but feel everything" 同一指令句式）。
  4. Sensei 游戏自认知："She is a character in a video game that I have somehow found myself inside of." [5554]；"A game with both limited and unlimited possibilities, that will never truly end until I have decided that I have either won or lost." [5808]；"No one ever cares that I am not the real me. **I am just a player in a game.**" [5806-5807]。
  5. "I want to feel it again." 连环重复（旁白 4 遍 [5819-5826] + Sensei 口中 5 遍 [5834-5838] + 密集串 [5860]）+"I want to fall in love." [5827]+济慈《夜莺颂》"Do I wake or sleep?" [5906]。
  6. **Ami 的知情护理** [5965-5980]："When you wake up, I'll be right here... The same way we've done so many times before. I'll cry...and you'll stand tall. **And when tomorrow comes, it will be like none of this ever happened.** We'll forget together. We'll survive together. We'll grow together."——Ami 不仅知道"明天会像没发生过一样"，还说"我们以前这样做过很多次"（**对重演的明确自觉**）。
- **amimaid50 [6447]**（+1）：更衣室。好/坏分岔 [6512-6556] 同 05 对照（好叔叔版 Ami 逼求、坏叔叔版安全感）；新细节：**Uta 主持的"Sensei love ranking"** [6611-6618]（"Ami's held the number one spot... ever since it was established"，Chika 排前五会买榜）；"stop suffocating me"→**"No."** [6747-6767]（十行静默对峙后一个字）；Ami 的敌我逻辑 [6699-6701]："Because she's a teenager." / "I'm different. I'm your niece. We live together."

### 2.3 第三章末–第四章（崩坏与重建主线）

- **amiinvite4 [6780]**（+1）：timeloop 告知事件。开场强迫重复 "I love my niece."×多段 [6793-6806]，其中插入 **"The Ami scene will begin now."** [6806]（场景切换的机器式报幕）；血咖喱玩笑 [6862-6868]（"It's full of my blood. I used it in place of salt."）；Sensei 当场失忆裸体 [6910-6913]；**Ami 的心理学解释** [6907-6909]："There's a disconnect between your mind and what's actually happening... It's a coping thingy."（她长期照护失忆者/解离者的经验之谈）；母亲话题 [6937-6985]："I was always more of a mama's girl"、"No one could ever look good next to her"、**"I know you loved her, Sensei... I know she was important to you in a way my dad never was."** [6977-6982]（Ami 亲口点破 Sensei 对母亲的爱超过对其"父亲"——"everybody loved her" 的万人迷设定）、"I know Mom never believed in God. She pretended to around me" [6966-6967]。timeloop 告知全文 [7104-7108]："Your first year of high school is never going to end. You and everyone else are caught in a timeloop that causes it to start over every few months. You retain most of your memories... **Also, everybody disappears, the sky turns red, and pregnancy is probably not the cause.**"→Ami 拒绝（"That is the dumbest thing I have ever heard." [7120]）→**同一句台词被强制重复三遍** [7132-7136]（"And stop believing everything Maya tells you..."）→场景硬切回 "Curry? You never make curry." [7143-7144]。泄密链：Makoto 短信告知 Ami "the end of the world... the world being a loopy thing" [7085-7090]。
- **amispecial50 [7163]**（+1→jump 主线版）：恐怖游乐园夜。开篇罐中自我独白 [7170-7195]："this jar I'm trapped inside reflects not the me that {i}I{/i} see but the one that {i}you{/i} do." [7173]（**罐=屏幕，你=玩家**）、"staring back at someone I can only view as **the protagonist of this story**" [7178]（直指玩家）、"Warble, warble, warble." [7195]。中段：Ami 深夜被困旧城区求救电话 [7209-7229]（"I was just doing what I was told!" [7226]——被谁指使未明）；worm-man/word-man 谐音崩坏 [7233-7239]；"Just take the fucking password!" [7252]（叙事者对密码/口令机制的暴躁自指）。**se 猫形现身** [7277-7352]："Not everybody gets regular chances to spend time with their **dead girlfriend**, you know." [7288]（明确 se=亡女友）；"I always knew Heaven was a joke, but it would have been really cool if there was at least {i}something{/i} after death." [7333]；"Here's the thing though, **Aki-kun**. You can't just ignore me forever." [7338]；"I think you already know that." [7352]。Ami 获救后的器官论 [7438-7446]（"An organ you can just give up? A body part you can just cut off?"）；背负独白 [7549-7579]："I tried to change things sometimes... But I was a stupid little girl... I didn't understand what you wanted at all. But now I do. Now, I know that all you really want is to feel safe. **So I built a world where you could.**" [7550-7570]（Ami 自称"建造了这个世界/家"）；"ultimate niece" 复诵仪式 [7587-7590]。
- **amilust50intro [7627]**：卡拉 OK 场；**叙事者直接报数值**："My lust level with Ami is high enough to trigger this event, so I take it upon myself to telepathically communicate to her that I am willing to proceed." [7639-7641]（把游戏机制说成心灵感应）；Sana 冲突支线（amilust50skip [7719]）。
- **amilust50 [7727]**（+1 lust）：扮演/真身混淆事件。"I can smell her on you... Sana." [7737-7742]；"Are you still confusing girls for {i}other{/i} girls?" [7749]；结尾旁白 "It's that Maya smells a lot like Ami today... And it happened again. **I did a bad thing.**" [8007 前段]。
- **amilust60intro [8020]**：chap4 闭锁期；Ami 筛查访客、提及 **Niki 和 Noriko 留了礼物** [8026]；喂食飞机梗；skip 分支 +10 love [8070]。
- **amilust60 [8080]**（+1 lust）：第三人称驱魔叙事 [8118-8128]（"she was determined to exorcise her uncle's demons"）；Xoanon 插叙与 "awaits the next reset"（一轮 md 已记，v0.60 文本未见变动）；"The carrots are left out to thaw." [8268]。
- **amispring1 [8281]**：大崩坏夜。Giles Corey 虫寓言全文 [8288-8304]（结尾 "We have all drunk from the water. Now, we all have worms inside of us. And every time we talk to God, we're only making them stronger." [8302-8304]，副标题 "- The true story of how we came to be" [8305]——**创世伪经**）；"I am house." [8312]；Daisy Bell（亡母之歌）[8314-8333]；剪发+《麦琪的礼物》戏仿 [8372-8386]（"It's the night before Christmas, boy... I sold it for you."）；课堂/教程现实闪烁 [8395-8410]（"Rule number one is keep your hands off all of your students! BUT YOU DIDN'T FOLLOW THE RULES, JIM!"）；日语拒绝 [8412-8414]（"やだ"×14）；核心控诉 [8421-8469]（含 "YOU'RE SUPPOSED TO TREAT THIS LIKE A GAME! YOU'RE SUPPOSED TO GET ME PREGNANT! YOU'RE SUPPOSED TO REACH THE EPILOGUE!" [8458-8459]）；**指控 Sensei 咀嚼亡母头发** [8429]（"You picked some off a piece of her scalp when it was all we had left. You tasted it... You wanted to feed your worm."——暗示 Sensei 曾守着遗体/遗物失控）；剪刀刺掌 [8517-8521]；事后否认 [8539-8540]；**旁白忆旧**："There was someone just like her who used to lick my wounds... in hindsight, I sometimes believe she only did this because **she liked the taste of blood**." [8543-8545]（指 se——Arakawa 家两代女性的镜像）；se 谴责 "What have you done to my darling little girl?" [8596]；"The worms need to be together." [8614]、scissor angel 与 Heaven's Web [8620]、"this world may have {i}already{/i} come to an end. And this is all that's left." [8621]；好/坏收束分岔 [8623-8657]（坏=候补新欢论；好="This is hell. But it's right where I belong." [8656-8657]）；clockwater 梦与盒子 [8677-8679]；结算：amiblock+senseisad [8683-8684]、`Ami Arakawa [[BEDRIDDEN]` [8686]、**`Akira Arakawa has obtained the status effect [[DEPRESSED]`** 及嘲讽式系统安慰 "All he has to do is get over it!... And the worm will feed once more." [8708-8714]。
- **amicamp1 [8718]**（+1）：门之诗 [8744-8751]；**车祸预告** [8731-8732]（"Or I am going to be hit by a car on the way home and Ami will be left with no one but **a girl who only wants her because she shares my blood**."——同时泄露 Niki 对 Ami 的执念源于"她流着我的血"）；**Ami 的自供清单** [8892]："I cut your hand! I threatened all of the other girls at school! **I went through your phone! I used it to blackmail people!**"（手机泄密+勒索——amiinvite4 的 Makoto 泄密、amispring1 的 "going through my phone" [8525] 三处连成一条"Ami 掌握信息渠道"暗线）；婚礼誓词对答 [8933-8937]；"I will build you a world where nothing can hurt you anymore." [8917]；Ami 的幽闭预言 [8815-8817]（"one day, we'll be in this same position again... We'll grow old and die inside of this house, and no one will find us until we're both decayed and covered in maggots."）；阴森 coda [8976-9003]（独白对象不明，失败预案 "I can chop it off."）。
- **amicamp2 [9013]**（+10）：露营修复。**[[TEMPLATE9] 泄漏梗** [9018]（"I've even [[REDACTED] with Kaori and [[TEMPLATE9]."——变量名直接裸露在旁白里）；Niki 的请求闪回 [9026]（"Let me move in with you. Let me be her mom."）；"this game would be so much easier if that family would just fuck off already." [9051]（游戏措辞）；Sara 剪发+8000 日元玩笑 [9129]；公开 "I love you, Ami." [9165]；日落散步：信仰问答（sky castle [9242-9243]）；**Sensei 的既视感** "Also, is it just me, or have we had this conversation before?" [9257]→Ami："there are probably {i}tons{/i} of conversations we've had before that we're going to forget about and then have again." [9263]（**双方对话级别的循环自觉**，一轮 md 未记 Sensei 侧 [9257]）；Dad 称谓获批 [9328-9333]；**"my first dad... I never really get a response"** [9334-9335]；actual daughter 炸弹 [9344-9357]；好/坏回应分岔 [9384-9396]；**alleged 生父玩笑** [9425-9427]：Ami 抱怨 Ayane 可能也叫 Dad，说 "I've never once complained that {i}her{/i} allegedly biological father is alive."，Sensei 纠正"Ayane 的父亲不只是'所谓的'吧"，Ami 答 **"I know that. But {i}mine{/i} is [alleged] and I'm trying to draw parallels here."**（我的生父才是"所谓的"——Ami 亲口自认生父身份存疑，血统暗线最直白一句之一）；结算 [9443-9449]（DEPRESSION/PARANOID 减弱；坏叔叔 "(ALLEGED) DAUGHTER-FUCKER" 称号）+系统尾刀 "If only you would stop looking down." [9457]。
- **halloweenami1 [9481]**：神社夜。skinwalker 措辞 [9487-9492]（"the tragic tale of Maya Makinami (or the one who wears her skin)"、"if only she knew the horrors she had already seen — and the others that have yet to befall her" [9492]）；Sakura Sunlight/七步半预知 [9499]；**旁白打油诗崩坏与玩家喊话** [9590-9598]（删除线 ABC 歌 "IT'S HOT DOWN HERE IN HELL"、"Lock eyes with screen, put dick in fist"、"The needle goes in to suck out the truth."）；Maya 的 Niki 焦虑 [9575-9581]（"did somebody put you up to this?"、"Just because she's moving in doesn't mean you don't need me anymore, does it?"）；Maya 自述关系起源 [9647-9649]："In the beginning, all we were doing was just...hiding our pain inside one another. And we worked because {i}that{/i} worked."；Ami 摊牌 [9618] + 门后偷听全招 [9695-9709]（含 "your {i}father{/i}" [9706] 与 "You and I have cum together so many times and you didn't even know it" [9709]，成人内容抽象）；皮带/三人契约 [9681-9733]（"It will never be only you again. Not for the rest of our lives."）→Maya "**I'm in.**" [9740]。
- **amispring2 [9747]**（+1，noriko_love+1）：豪华轿车行。新细节：
  - **Noriko 的时间职责预言** [9865-9874]："Just faith that she'd fulfill the role she needed to fill **to keep the wheels of time spinning while everything else has stopped**."＋格言 "A pencil in the hand of God is as good as a pen in the hand of the Pope. But when both of those tools are taken away, only one can write in blood. The other must simply watch."——把 Noriko 定位为"时间停摆世界的上链人"（与 Maya "I do the time thing" 构成双执行者结构，一轮 md 未记此段）。
  - Niki 的 ED 诅咒小字旁白 [9860]（诅咒童年好友"她不在场就勃起障碍"）；"pregante/pragent/pergenat" 拼写三连 [9847-9850]。
  - Ami 转向"不阻止"策略 [9944-9951]："I'm done trying to stop people from doing it. There's just no way for me to get what I want by interfering anymore."；她的"想要"= 反对 Niki 取代亡母 [9952-9981]（"My mom understood the strange, sometimes {i}carnal{/i} bonds two people who don't belong together can have. {i}She{/i} wouldn't think I'm broken." [9980]；"being 'broken' is just an Arakawa family trait" [9981]）。
  - Noriko 的困惑 [10025-10028]："I just feel like we're supposed to be closer than we are... maybe if we met each other more when we were little, things would be different now?"（同龄却陌生——记忆/循环异常）。
  - Ami 的面具自白 [10033]："I've just made too many mistakes to ever give away what I'm really feeling anymore."
  - 自我牺牲退场 [10122-10125]（"The time has come...for Ami Arakawa... To do something {i}good...{/i}"）。
- **amispring3 [10138]**：对质爆发夜。Niki 引退伏笔 [10150-10151]（"Graduating" I think they call it in the idol world）；对质链 [10309-10541]：承认带路 [10314-10319]、得知 Niki 留下后失控 [10367-10397]；**母亲死因真相** [10448-10465]："YOU SAW WHAT WAS HAPPENING TO HER AND YOU IGNORED IT! YOU WERE THE ONLY ONE SHE TRUSTED AND YOU DIDN'T FUCKING LISTEN! YOU LET IT CONSUME HER!" [10448]＋"POEM AFTER POEM AFTER POEM! VOICES, VOICES, VOICES! IT'S NO WONDER SHE COULDN'T BREATHE WITH A NOOSE LIKE THAT AROUND HER NECK!!" [10456]＋"she was {i}practically{/i} dead for a whole fucking year before that while her mind was being overrun by who the fuck {i}knows{/i} what! And {i}you{/i} could have done something! ... But you didn't understand them! You didn't believe them! No one did!" [10464-10465]——**且 Ami 将其与自身相连**："And I...how am I supposed to think you'll believe {i}me{/i} then?" [10471]；"七岁养两个大人" [10522]；"YOU happened to me!" [10515]；**死亡暗示** [10532-10538]："Despite all of that... I have never stopped living for {i}you{/i}... But sometimes?... I feel like you'd be happier if I died too. / And there's only one way to find out if that's true or not."（一轮 md 未记 [10538] 这句接续——离家即赴死暗示）；"Somewhere I won't be a fucking {i}burden{/i} anymore!" [10548]；Sensei 独白 "I miss my daughter. **I miss my childhood friend.**" [10565-10566]（AmiEvents 内直称 Niki 为青梅竹马）；衣柜笔记本 [10576-10579]；结算 amiblock+noriko_love+1+"Everyone else has abandoned you..." [10583-10587]。
- **amispring4 [10594]**（四值各+10）：lust 事件+文本崩坏极点。Noriko 介入三人局（成人内容抽象）；**血统再爆**：Noriko："You called Akira your uncle before he was your dad, right?" →Ami："**Yeah, but that doesn't mean I ever thought he really {i}was.{/i}**" [10652-10653]（Noriko 追问 "Wait, what? But that-" 被打断）——Ami 从未真正相信"叔叔"身份；Noriko 的时间感叹 "Time works in mysterious ways, doesn't it?" [10695]；Noriko 自述印照片贴抱枕 [10710]；文本退化为乱码 "Daddy" 六连段 [10838-10844]→"father." [10845]→"I sex." "I cum." [10847-10848]→"MORE." [10881]→五遍 "I love my daughter."→**"Is this my daughter?"** [10899]。
- **amispring5 [10918]**：父亲感谢日绑架事件（好/坏双版本结构同 05 对照 2.4 节，全部核对无出入）。v0.60 细读补充：
  - 开场诗化崩坏 [10926-10962]（"Lucy, I'm house."+Victrola+音节滚落）。
  - 好叔叔版威胁 [11143]："you're nothing but a man who will soon **pay the ultimate price for his insubordination** right when you least expect it."（一轮 md 未录此句）。
  - 好叔叔版 Reconciliation 逻辑链 [11065-11131]：自封"最无私"→被斥后爆发 "THAT'S THE WHOLE FUCKING POINT, YOU LIMP-DICKED BETA FUCK!" [11080]→"they're all going to do it anyway" [11086]→"this you doesn't understand love. But the next one?... They'll fuck me... they will be saved. But you? You will fucking suffer... until the credits roll." [11148-11151]。
  - 坏叔叔版"捷径论" [11191-11201] 与 "To complete the collection" [11245]→"Because walls don't work the same for me that they do for you. I'm special. **I'm the main heroine.**" [11253]。
  - 汇合段 [11262-11326]："Fuck me and I'll tell you." [11262]；**"You haven't even slept with {i}Rin{/i} yet"** [11279]（对 Sensei 关系网的全知清单）；"Just play the game already instead of letting it {i}play you.{/i}" [11280]；karaoke booth 指涉 [11282]（"better this than fearing for her life while some guy forces himself on top of her in a karaoke booth"——呼应主线/chap3 卡拉 OK 袭击事件）；反捆绑 [11313-11315]（ami_love-10）；Karin 苏醒与 Kirin 话题被搁置 [11357-11379]；对峙 "you'll no longer be my daughter." [11412]→"Acknowledge me." [11420]→"Can you say it back, please?"×2 [11422-11424]→"I love you too..." [11429]→"I'll untie Ami in the morning." [11432]。

### 2.4 Ami 线元叙事点汇总（二轮归纳）

1. **三层自觉的渐进**：NPC 自嘲（firsttimeamisroom [525]）→"true protagonist" 玩笑（amisroom15 [1297]）→"建造世界"自白（amispecial50 [7570]）→"游戏该有的玩法/epilogue"（amispring1 [8458-8459]）→"main heroine/polygons/credits roll/collection"（amispring5 [11146-11253]）。
2. **重置抹除的现场证据×4**：碎杯失忆（amidate50p3 [4812-4834]）、"wish you knew how to drive" 被否认+伤愈（amidate50p4 [5079-5115]）、timeloop 告知被三连打断（amiinvite4 [7132-7136]）、"Can you say it back, please?"×2（amispring5 [11422-11424]）。
3. **Ami 的信息渠道暗线**：贴门偷听（halloweenami1 [9695]）→翻手机+勒索（amicamp1 [8892]）→Makoto 短信（amiinvite4 [7089]）→"walls don't work the same for me"（amispring5 [11253]）——从物理偷听到"穿墙"全知。
4. **血统四连暗示**：amisroom15 [1306] "related to my dad"→amicamp2 [9351] "I already know you loved my mom"→amicamp2 [9427] "mine is [alleged]"→amispring4 [10653] "doesn't mean I ever thought he really was [my uncle]"。
5. **母亲暗线**：Daisy Bell 哄睡歌（amidate50 [3987]→amispring1 [8314]）；阁楼诗稿（amidate50p3 [4766]）→诗/声音吞噬她最后一年（amispring3 [10456-10465]）；亡灵三次现身且明确 "dead girlfriend/Aki-kun"（amispecial50 [7288]/[7338]）；Ami 转述母亲 "understood carnal bonds"（amispring2 [9980]）。

