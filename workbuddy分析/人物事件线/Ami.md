# Ami 事件线分析

> 源文件：`游戏文本/AmiEvents.rpy`（真实 label 数：52）｜按 label 名回源。
>   
> 定位：USER1 线实例、已故母亲 Sekai 之女；love/lust 双轨最长的角色线之一。源文在 amidate50p4 收束处出现系统提示 "USER1 HAS SUCCESSFULLY LOGGED IN"，印证其作为 USER1 观察样本的设定。
>   
> 阅读提示：台词直引为源文英文原文；a=Ami、se=Sensei（内心声部，0.60.0 起可证其自述已死，见「四」）、ya=Yasu、to=Touka、ri=Rika、tk=Tsukasa。label 名是唯一的回源锚点。

## 一、角色基本盘

Ami 是 love 线中与"真实/虚构"命题绑定最深的女主角。她是已故母亲 Sekai 的女儿，由 Sensei 以半监护者、半恋人的模糊关系照看（firsttimeamisroom 中 Sensei 称她为 "slightly-official niece"）。表层设定是活泼的漫画宅少女：住校生、maid 咖啡店打工（amimaid30 / amimaid50）、manga club 成员（amidate50 墓前独白提到 "the manga club is going well"），对 Sensei 的感情混合依恋与早熟的占有欲。文本在她身上留下"非人"裂缝——amispecial50 的内心独白把自身比作"困在罐中的主角"，amiinvite4 的咖喱以血代盐玩笑，amimaid50 写她"唯一能让血液沸腾的是同类的血"，都对"血"表现出异样亲近。作为 USER1 线实例，她既是攻略对象，也是元叙事层拷问"虚构角色能否被爱"的载体。0.60.0 的 Yasu 教会三连首次从他人感知侧坐实了"非人"裂缝：Yasu 触其手所见是 "this was Ami. Ami and...and something else..."（YasuEvents.rpy:7113）——把她吓得反锁进教堂的不是恶魔，而是"过量的存在"；Yasu 事后对 Ami 的定性是 "She is far more than just {i}Ami.{/i}"（7176）。墓前独白（amidate50）揭示其情感内核：孤独、把 Sensei 当作 "my new dad" 的自我说服，以及被 Sensei 以 "my sweet girl" 回应却仍隔着生死与不可见距离的隔阂。

## 二、love 线逐事件脉络

### 1. amisroom 路由桩与邀请系统

amisroom 是纯路由桩：按 ami_love 与前置 flag，依次跳转 firsttimeamisroom、amisroom5/10/15/20/25，否则跳 amisroom3to4。amiinvitegen 中 Sensei 打电话邀请 Ami，Ami 吐槽："Gonna invite me to my own house again?"——两人日常已互相渗透。邀请菜单提供 Hang Out、Headpat 等选项；在 bonus==False 模式下，Hug 跳 amiinvitethighjob、Hold Hands 跳 amiinvitereverse，选项文案与跳转目标存在系统性错位，使好感度菜单实际通向 lust 内容（amiinvitethighjob / amiinvitereverse）。

### 2. firsttimeamisroom：初次同处一室

amisroom 在首次进入（firsttimeamisroom==False）时跳转此处，是 Sensei 第一次正式进入 Ami 房间、两人关系越界叙事的起点。开场 Sensei 自述身处 "the early stages of a harem"，敲 Ami 的门并被迎入，奠定"半监护、半恋人"的暧昧基调。

### 3. amisroom3to4 / 5 / 10 / 15 / 20 / 25：好感度递进的同居化阶梯

amisroom 按 ami_love（5/10/15/20/25）配合相应前置 flag 逐段跳转，构成两人关系从相遇到同居生活的进阶。其中 amisroom25 要求 ami_virgin==False 且 amidorm20==True，是亲密同居生活的深层节点，为后续事件提供情感基线。

### 4. amisroom15：看动漫的日常

Ami 追番时剧透："Oh. Wait. I remember who wins now. It's the protagonist." Sensei 反问："Are you just going to spoil everything today?" 随后两人讨论作品里的审查设定："They got rid of censorship laws here years ago...as long as it's not a penis"。这段以玩笑完成的审查制度吐槽，同时是世界观自指——游戏世界对禁忌的容忍度被规则明文规定，正如角色行为被 label 结构规定。

### 5. amiinvite1–4：四次登门

- amiinvite1 / 2 / 3：邀约型日常事件，维持关系温度，把"房间"这一封闭空间逐步扩展到校园外的日常场景。
- amiinvite4：全 love 线重要转折之一。Ami 暂时离场后，Sensei 独白："She reminds me a lot of someone else I used to know... It's someone I try not to think about because it hurts when I do."——他主动掐断的思绪。Ami 回来端出咖喱，宣布 "It's full of my blood. I used it in place of salt"，Sensei 回应 "I love your blood"，Ami 补一句 "I was just kidding... This is normal curry without any Ami in it." 血的真实性与玩笑的收回性并置：读者无法判定哪句是真，这正是 Ami 角色"非现实"状态的具象化。

### 6. amimaid30 / amidate35：打工与约会的日常节点

- amimaid30：Sensei 到 maid 咖啡店探班，Ami 提到为他做了早餐、两人聊到账单与她的新工作，是"女仆"社会身份的展示。
- amidate35：Sensei 打电话约 Ami 去商场挑新泳衣的约会事件，巩固两人日常亲密。

### 7. amidate50：扫墓（墓前独白的情感顶点）

amidate50 是 date50 事件，包含 Sensei 被"吞没"的梦境（q 低语 "I can't sleep."、te 身影），以及 Ami 穿上亡母旧衣（"I remember that dress"）后于墓前的独白——这是 love 线情感浓度最高的段落：

> a: I miss you, Mom...Sensei misses you too, but he's too afraid of looking weak around me to admit it.

她报告 maid 咖啡店与 manga club 近况，又说："Daddy, too. Can you tell him that? Sensei's been doing an okay job as my new dad." 随后出现异常声部——Sensei 的内心回应："I miss you too, my sweet girl...I'm sorry you feel so alone. I do too. I'm always here, though. Even if you can't see me." "Even if you can't see me" 字面是活人对死者说话，但在重置／元叙事读法里，也可读作一个无法被角色感知的系统声部。亡母"回应"究竟是心理描写还是元叙事泄漏，文本拒绝裁决。

### 8. aminew1 / aminew2：新年事件

- aminew1：新年框架，Ami、Ayane、Maya 等结伴（源文称 "three girls who could pass for my daughters"）去咖啡店蹭情侣折扣，Ayane 以富家姐姿态宣称 "I am rich and can get you out of trouble if I have to"。多女主同框被处理成替代性家庭结构的展演。
- aminew2：新年次日清晨，Sensei 与这位"侄女"的亲密场景，明确以"即便我们 related，也不妨碍彼此贴近"的乱伦框架推进关系确认。

### 9. amilust35skip / amilust35intro / amilust35：love 线内置的中段欲望分支

amilust35skip 以 sauna 场景提供跳过入口（"No one can see us" 后 Ami 直言愿当下发生关系），说明该欲望分支的可选择性；amilust35intro / amilust35 为其中段 lust 内容。

### 10. amimaid50 → amispecial50：打工线与特殊事件的收束

amimaid50 是 maid 咖啡店更衣室场景（Ami 近乎全裸把 Sensei 拽进 locker room）；amispecial50 则是高度元叙事的内心独白（"the jar I'm trapped inside reflects not the me that I see but the one that you do"），把 Ami 的社会身份（女仆、社团成员）与私人身份（恋人、Sekai 之女）在文本层完成一次合流。

### 11. amilust50intro / amilust50：高好感度欲望场景

amilust50intro / amilust50 是 ami_love>=50 阶段的高好感度 lust 内容。

### 12. amispring1–5：春季篇章五连

时间线在春季明显加速，事件从"约会／打工"转向存在论与集体活动。amispring1 以"worm／Giles Corey"的元叙事引子与 Ami 反复吟唱 "Daisy Bell" 开场，把身体与文本、被书写与重生主题抛向台前；amispring2–5 延续这一季章节。全作中"reset"母题在 Ami 线确有落点：Ami 曾把某种打击比作 "pressing a reset button"，叙述者亦言 "awaits the next reset"，与"如果一切都会重置，此刻意义何在"的追问彼此呼应。

### 13. amicamp1 / amicamp2：归家与门廊的元叙事

amicamp1 写 Sensei 离开 Makoto 后回家找 Ami，在敲门时浮现 "The hallway of life is door upon door... Each door has a doorknob. Each opens to secrets" 的诗句，把日常归家升格为关于"选择／重生"的元叙事段落；amicamp2 延续 camp 章节。Ami 在此被重新定位在与其他女主的关系网中。

### 14. halloweenami1：万圣节特别事件

halloweenami1 以 Maya（"skinwalker"）走失、Ami 扮 "Sakura Sunlight" 寻友的万圣节戏谑开场；其后接入 Niki（ni）与经纪人 Patrice 的豪车情节——叙述者写 Niki "faith that she'd fulfill the role she needed to fill to keep the wheels of time spinning while everything else has stopped"，并以 "A pencil in the hand of God is as good as a pen in the hand of the Pope. But when both of those tools are taken away, only one can write in blood" 收束 pencil／pen／blood 的书写工具隐喻；Patrice 与 Niki 关于行李（"you only brought one bag"）的对话则把情节推向转移／离开。Ami 线的欢乐日常由此直接接入主线的时间停滞母题：车轮仍在转，而故事内的一切已被冻结。

### 15. 0.60.0：Yasu 教会三连中的 Ami（yasuspring6 / 7 / 8）

0.60.0 没有新增 AmiEvents 的 label；Ami 在本版本的全部剧情都发生在 Yasu 的教会线里（yasuspring6 "Child of Light"／yasuspring7 "Ichigo Daifuku"／yasuspring8 "Heretic"，场景 CG 前缀即作 yasuamichurch）。三个事件构成一个完整的"触碰—崩溃—审问"结构，是全作第一次让第三方角色直接感知 Ami 的内部。

**yasuspring6（教会初访，Ami 主动上门）**。Ami 自己找上门："I found a flier near the market by my house"，并解释动机——亡母遗物箱里有"很像你的广告的东西"："There were things in a box of her belongings that looked a lot like your ads. So I figured I...might as well come down and see what this is all about."（YasuEvents.rpy:6481）。她此行的目的在结尾说破：如果教会就是母亲生前信的东西，"I want to at least know what she {i}saw{/i}"（6720）。途中 Ami 把教义问得毫不遮掩——确认"救赎=内射"的教义后直问乱伦政策，再自己得出结论："Meaning...that my dad is special and your god will let me have a bunch of sex with him?"（6511）；Yasu 惊喜于她的"特殊"，称赞她是 "child of light"（6459）、"I knew you would be special, Ami!"（6517）。amifingered==True 分支里 Yasu 断言 "His scent clings to you like sin does to the dark"（6545）、"surely your role in this story is far greater than even mine"（6552）、"The black sheep is the most beautiful of them all"（6553），说到 "You're full of colors that no one else has. Colors that would surely spill from you when cut open! Yet you've selfishly imprisoned them and-"（6555）时突然僵住——尚未触碰，仅靠接近就已开始"看见"。色彩问答环节双方的颜色都以 hex code 交付：Yasu 自报 74d9e9（6617），Ami 的结果是 ff4dd2（6653）。母亲话题是本事件情感核心：Ami 记得母亲的声音 "so sweet that I can still hear it in my dreams after all this time"（6677）；母亲在她出生后 "found God"，随后 "started to lose herself. Started hearing things. {i}Seeing{/i} things. Things no one else believed, but things that were {i}very{/i} real."（6683）——Ami 直接把 Yasu 的感知障碍与母亲的幻听幻视并置："Living in what's essentially a different plane of existence from everyone else?"（6684），又替她顶住外部压力："People wanted my mom to change too. Heck, there's a girl living in my house right now that tells {i}me{/i} I need to change every single day. But who we are is up to us, isn't it?"（6696）。事件以触碰收束：Yasu 伸手前说了半句 "you're your mother's daughter. Just like your father is-"（6736，被掐断），随后看到的东西令她当场崩溃、连续嘶吼 GET OUT（6749-6774）。Ami 的离场异常从容："You must have seen something terrible. I really didn't mean to scare you."（6772-6773），临走留话 "You don't need to send me my color. But I'd love if you could send me yours. I have a feeling it's beautiful."（6780-6782）——她清楚自己吓坏了对方，却全程平静，甚至欣赏对方的恐惧。

**yasuspring7（牢房审问，Ami 不在场）**。整场 Ami 缺席，剧情全部围绕"她做了什么"展开：Touka 深夜电召 Sensei，报告 Yasu 把自己锁进教堂牢房数日、不停念叨 Ami，在校内两人一照面就几乎落泪（6872/6878）；Touka 给不出解释——"either Ami did something to her...{i}said{/i} something to her...or, equally as probable, Yasu dreamt something up"（6886）；Sensei 的反应是 "I don't think I've ever even heard her {i}talk{/i} about Yasu before"（6888）。牢内 Yasu 转述教会初访真相：Ami 来教会是 "To {i}learn.{/i}"，讲的都是亡母临终前"听到和看到的东西"（7075-7076）；然后 "And then I touched her... Hands can be so strange...can't they?"（7085-7086，插入的闪回 CG 全是 Ami 事件画面：amibus12／handsareweird2／amihair19，7089-7094）。她看到的不是亡母："No...I've never seen anyone like that before. This was...this was Ami. Ami and...and something else..."（7113），再追问后是 "E...Everything... It wasn't just {i}one{/i} something. It was so many of them! Each more perplexing than the rest! And the deeper it went, the darker they were! I could feel them inside of me. {i}Fighting{/i} for me."（7120-7122）。Sensei 先怀疑是 Sekai 的亡灵显形："Ami's mother didn't appear to you, did she? An older woman who looks just like her?"（7106），被 Yasu 否认；此时内心声部 se 插入全书最直接的判词："She's lying. Ami's not involved in any of this. I died before the curse could reach her."（7126）——说话者自述"已死"且以死护住了 Ami，并抛出"the curse"一词；Sensei 怒问 "What {i}curse?!{/i}"（7131）即被切换进下一事件。另有一处关系定性：Sensei 纠正 Touka 的称呼——"She is my {i}daughter,{/i} Touka. Please stop calling her my niece. {i}Please.{/i}"（6948）——"女儿"二字由他本人当面确认。

**yasuspring8（Heretic，情报交易）**。Yasu 以身体为代价请求 Sensei"救"她，Sensei 反向开价："I just need you to tell me, in the simplest way you can, what makes Ami different from everyone else."（7226）。Yasu 给出的画像是他处从未出现过的："She is far more than just {i}Ami.{/i} She's peeled the skin off of arbiters and fashioned it all into pretty dresses that can bend light — adorned with the eyes of the angels themselves. She is heresy itself. A souvenir stolen from the gift shop where the sidewalk ends."（7176-7177）；并断言 Ami 对她的处境知情且主动："She knew that this would happen. That's why she infected me."（7174）。Yasu 还反问 Sensei 一个他答不出的问题："How do you touch her without breaking? How have you slept with so many shadows sodomizing her so close by? Do you ignore them on purpose? Or are her walls simply that soundproof?"（7179-7181）——Ami 周身常年环绕"影子"，只有 Sensei 看不见。本场 Sensei 同时处于活动性幻觉中（看见角落里的女人并询问 Yasu 是否可见，对方答 "There is nothing... Not even me."，7203-7205），仍完整复述教会事件经过并推进调查；结尾他预约下一步实验——让 Yasu 用同样的方式触碰 Maya："I just need you to do whatever you did with Ami to Maya."（7231），理由是 "There's something I need to know. Something that affects {i}everyone.{/i}"（7233）。

### 16. 0.60.0 其余 spring 事件中的客串

- **ayanespring4 / utaspring9**（两事件共用同一段教室开场）：Ami 把空白笔记本叫作 "naked"，被 Makoto 纠正 "Please just call it {i}blank,{/i} Ami. We gain literally nothing from personifying inanimate objects like that."（AyaneEvents.rpy:14210-14211，UtaEvents.rpy:8487-8488 逐字复用）——她对无生命物的拟人化是习惯性感知错位；同一场景里她自曝用 ChatGPT 给未来的自己写信（14231-14232），并指出 Ayane 课桌裂缝里"卡着一根卫生棉条"——用词是 "popping out of a rift in your desk"（14254）。utaspring9 中 Ayane 说"我又像刚从另一个次元回来"，Ami 接 "Again? Is that something you do often?"，Ayane 反问后她答 "Whatever do you mean, best friend?"（UtaEvents.rpy:8508-8511）。
- **harukaspring6**：Haruka 自杀倾向独白（"It's not like I've done anything lately that would make me {i}want{/i} to be dead. I just {i}do{/i} want to be dead."，HarukaEvents.rpy:9723）的收束动作，是把话题抛向 Ami："You go! Tell me about your day. How's, uhh...how's Ami?"（9727）——全书最年长的角色在对最"非人"的角色表示关心时选择了借力逃避。
- **mayaspring5**：Maya 与 Ayane 修复友情的对话里出现记忆错位。Maya 只记得 "we're both always with Ami. And we probably met that way or something. But I can't specifically remember where-"（MayaEvents.rpy:10406）；Ayane 给出的却是另一版历史："Ami was barely even a part of it before you {i}left.{/i} If anything, {i}she{/i} was the one who started drifting away. It was always you and me until it just...wasn't anymore."（10407）。Maya 随后自白："the only {i}good{/i} friend I've ever had is Ami and I literally just trashed her behind her back."（10467）。重置改写了 Ayane 与 Maya 的关系史，而 Ami 在两人记忆中的位置被重新分配——她本人对此无一字解释。

## 三、lust 线概貌

Ami 的 lust 轨道由 amiinvitethighjob、amiinvitereverse、amigenafternoon、amigennight(2)、amilust15/35/50/60 等 label 构成，多数经由 amisroom 路由桩或 amiinvite 菜单错位进入。各段落功能高度一致：将 Ami 的身体作为可重复调用的场景资源，与 love 线的情感积累并行供给。值得注意的是 lust 内容从不质疑关系本身——质疑只发生在 love 线（如 amiinvite4 的 "someone else I used to know" 独白、amidate50 墓前对"看不见的存在"的困惑），欲望场景因此成为元叙事层之外的"安全区"，其空洞的重复性恰恰反衬 love 线每一次情感推进的不可复制性。

## 四、与主线／元叙事咬合点

1. **USER1 实例**：Ami 线含系统提示 "USER1 HAS SUCCESSFULLY LOGGED IN"（amidate50p4 收束处），她被明确置于 USER1 观察之下；三层世界观（恋爱表层／重置循环层／元叙事层 USER1-4）中，她位于最底层却被上层持续注视。
2. **"不真实者"命题**：咖喱以血代盐的真假并置（amiinvite4）、amispecial50 中"罐中主角／你眼中的我"的独白，把恋爱故事升格为本作"虚构角色能否被爱"的题眼；类似质询散见于其他觉醒角色线，Ami 是被说破最直白的一例。
3. **Sekai 遗产**：作为 Sekai 之女，Ami 承接 Sensei 对亡者的移情；amidate50 墓前"看不见的存在"双关使她同时成为哀悼者与被哀悼结构的继承者。
4. **血 motif**：血咖喱（amiinvite4）与 pencil／pen／blood 书写隐喻（halloweenami1："only one can write in blood"）共享同一符号链——血液既是生命真实性证明，又是剧本（用笔写就之物）的原料；角色的血进入叙事，等于承认自己被书写。
5. **时间停滞**：halloweenami1 中 Niki 相关的 "everything else has stopped" 表明 Ami 线的欢乐日常发生在被冻结的世界里，她的每一次微笑都是循环内的表演。
6. **"附着之物"的他者证词**：specialbonusamiscene 里 Ami 本体自述 "These hands... These smiles... Those aren't me. Those will never be me."；0.60.0 中 Yasu 的触碰感知从外部对上了同一判断——"Ami and...and something else..."、"It was so many of them!"（YasuEvents.rpy:7113/7121）。本体自白与第三方感知互为印证，"Ami"是容器、内里为多体的设定由单源升级为双源。
7. **内心声部＝Sekai 的最硬证据**：se 在 Yasu 报告后插话 "She's lying. Ami's not involved in any of this. I died before the curse could reach her."（YasuEvents.rpy:7126）——自述死亡、且以"我先死，诅咒才没碰到她"的口吻护女，只有亡母 Sekai 全部吻合。该声部同时替 Sensei 保管着关于 Ami 的关键信息（诅咒的存在），即他的"内心"里住着一个比他知道得多的记忆托管者。
8. **hex 编码的感知侧呼应**：Ami 的"颜色"以 hex code 交付（ff4dd2，YasuEvents.rpy:6653），Yasu 自身是 74d9e9（6617）——教会把人的存在直接写成十六进制，与全作"真相以 hex／乱码出现、谎言以台词出现"的形式学标记（babyfinches 车祸记忆、day220 遗言）同构。Ami 连"被他人看见的样子"都是编码过的。旁证：definitions.rpy:2334 定义了一个名为 "Pink" 的说话声部（第四章末彩装四人组 red/blue/green/pink 之一，ch2script.rpy:48101 "I'm the pink one!"），其专用色值正是 #ff4dd2——与 Ami 的"颜色"完全一致；是否即同一存在的两个显形位，文本未表态。
9. **父女正名**：Sensei 对 Touka 当面纠正："She is my {i}daughter,{/i} Touka. Please stop calling her my niece. {i}Please.{/i}"（YasuEvents.rpy:6948）——"侄女"是登记关系，"女儿"是他第一次在他人面前主动认领的名分；结合 rainking 的 "I am your little girl. And you are my—"（finalwarning.rpy）与 chap4.rpy:42287 的 "Dad?" 口误，父女论在 0.60.0 获得正面文本支撑。
10. **邪神侧的目标锁定**：教会传单集中出现在 Ami 家附近（YasuEvents.rpy:6537），Yasu 转述神意 "He wants you. {i}Both{/i} of you."（6554）——与 USER 层的持续注视平行，"超自然侧"同样把这对父女当作共同目标。Ami 的特殊性不是Sensei 的主观判断，而是多方势力的公论。

## 五、未解伏笔

- Ami 的血咖喱到底是玩笑还是真实？若是真实，她的生理构造指向非人设定。
- amidate50 墓前 Sensei 回应声部是内心独白还是系统级插话？"Even if you can't see me" 的主语究竟是谁。
- Sensei 说 Ami "reminds me a lot of someone else"——那个"别人"是否就是 Sekai（她已故的母亲），还是更早循环中的某个 Ami；源文只说 "It's someone I try not to think about because it hurts"。
- amiinvite 菜单选项与跳转目标的系统性错位是有意设计还是残留缺陷；若是有意，谁在改写菜单。
- halloweenami1 尾部 Niki／Patrice 的行李对话指向离开／转移，Ami 是否会在下一阶段被"打包"进新的循环。
- pencil／pen／blood 隐喻的具体机制从未被正面解释。
- Yasu 在 Ami 手中看到的"许多东西"（"so many of them! Each more perplexing than the rest"）究竟是什么；由此引出的 "the curse"（YasuEvents.rpy:7126/7131）内容与来源，全书尚未解释。
- Yasu 断言 "She knew that this would happen. That's why she infected me."（7174）——Ami 若真在"散播"什么，其目的与机制都是空白。
- Ami 提到的 "a girl living in my house right now that tells {i}me{/i} I need to change every single day"（6696）指谁——Sensei 家中同住者的身份在该时间线内未经说明。
- Yasu 触碰 Maya 的预约（7231-7233）结果未揭晓；Sensei 说 "There's something I need to know. Something that affects {i}everyone.{/i}"——他要借 Yasu 之眼验证的正是"Ami 的异常是否普遍"。
- "arbiters"（7176）是谁：Ami 身上穿着"仲裁者剥下的皮"，这一存在层级从未在任何角色线正面登场。
- 教会传单为何集中投放于 Ami 家附近（6537）；邪神侧对这对父女的"点名"与 USER 层注视是否同一来源。
- mayaspring5 的记忆改写：Ayane 断言 Ami "was barely even a part of it before you left"（MayaEvents.rpy:10407），与 Maya 的记忆（"we're both always with Ami"）冲突——Ami 在他人关系史中的位置被谁、为了什么而重排。
- Ami 用 ChatGPT"给未来的自己写信"（AyaneEvents.rpy:14231）：在会重置的世界里写给未来自己的信，落点是谁的手里。

> 按源 label 名回源见 `游戏文本/`：Ami 专属事件在 `AmiEvents.rpy`；0.60.0 交叉内容在 `YasuEvents.rpy`（yasuspring6/7/8）、`MayaEvents.rpy`（mayaspring5）、`AyaneEvents.rpy`（ayanespring4）、`UtaEvents.rpy`（utaspring9）、`HarukaEvents.rpy`（harukaspring6）。
