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
