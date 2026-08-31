# Tsubasa 事件线全析

> 源文件：`游戏文本/TsubasaEvents.rpy`（全文件共 17 个 label，本文件已逐个通读核对）。
> Tsubasa Tsukioka 是 Kumon-mi 最有势力的女人、Tsukioka 家的主母、两个女儿（长女 Touka、次女 Tsukasa）的母亲。她的线由两部分构成：台前是对 Sensei、对女儿、对 Chika 的无死角操控，幕后是"只有极少数人能看到她卸下姿态"的片段。
> 阅读提示：label 名是唯一锚点。台词的归属一律以 `label <name>:` 定义行到下一个 `label` 定义行之间为准。人物缩写为源文变量名：tb=Tsubasa、s=Sensei（Akira / Arakawa）、to=Touka、tk=Tsukasa、yu=Yuki、ni=Niki、a=Ami、mo=Molly、sar=Sara、w=Wakana、limo=司机。
> 只取 bonus == True 分支作为事实依据；`if bonus:` 的非 bonus 一侧不作为剧情记录。

## 一、角色基本盘

- **权势定位**：她本人在多个场合自我定位为掌控者。在 `tsubasaspecial15` 她对 s 说 "I'm a very powerful woman, Sensei."。在 `tsubasaspring6` 她以 "This is my privilege as the most powerful woman in Kumon-mi." 确立头衔，并紧接着强调这是新近才成立的："now I can make it even {i}more{/i} difficult because I currently {i}am{/i} the most powerful woman in Kumon-mi."。此外，"wealthiest woman in all of Kumon-mi" 这一表述出自 `tsubasadate1` 开头 s 的旁白（不是她的自称）。
- **家族与婚姻**：Tsukioka 家 "dating back to the origins of Kumon-mi"（`tsubasadate1`）。她的婚姻是包办："Arranged marriages are still very common in our world"，她在见到 Tomonori 本人之前先爱上了这座宅邸（`tsubasadate1`）。夫妻如今不同房：她在 `tsubasaspring3` 说 "I see {i}you{/i} more than him at this point. He and I don't even sleep in the same room anymore."。丈夫 Tomonori 是名义家主，她在 `tsubasaspring4` 反问："Tomonori may be the family head, but do you really think {i}I'm{/i} the type to gleefully allow someone else to pull my strings?"
- **两个女儿**：长女 Touka 是继承人（`tsubasaspring4` 称其为 "the heir apparent"），次女 Tsukasa。她对 Touka 的判断是 "Touka's been just as invested in the history of our family as me ever since she was a little girl."（`tsubasadate1`）。
- **她的操控语法**：一句被她反复使用的自辩是"我只是随口说说"——`tsubasaspring7` 结尾她压低声音说 "sometimes I just have to {i}say{/i} things"。威胁同样明写在文本里：`tsubasaspring2` 中她说 "for every minute you take from here on out, I'll reveal one of your {i}deepest...{/i}darkest secrets..."。至于"交易"，Yuki 在 `tsubasaspring6` 直接点破："It's always gotta be a fuckin' trade with you."
- **情报能力**：她两次宣称 "I know everything that goes on in this house."（`christmastsubasa1`），并说 "If it's something you've written on paper and handed over to someone, chances are I have access to it."（`tsubasaspecial20`）。在 `tsubasaspring4` 她提到能直接看到 Tsukasa 的浏览记录："The poor girl doesn't realize I can see her browsing history right from my telephone."
- **与 Yuki 的关系**：Yuki 称她 "Nee-sama"，两人没有血缘——Yuki 在 `tsubasaspring4` 明说 "We ain't actually related, no. I've just always called her that."。她们相识极早，Tsubasa 在 `tsubasaspring8` 说 "Yuki and I have known each other for longer than you've been alive."。阶层落差由 Yuki 本人说出："You were born to eat from silver spoons and shit and I was born to polish 'em."（`tsubasaspring6`）。s 在 `tsubasaspring4` 观察到她跟 Yuki 说话时没有跟他说话时那种戒备（"There's no guard up when you talk to Yuki like there is when you talk to me."），但 Tsubasa 当场否认。
- **需要澄清的归属**：`tsubasaspecial20` 里被翻出的"写诗的过去"、被追问后自述的失忆，以及 `tsubasaspring8` 柜中关于"被锁进壁橱、数数、听门外尖叫与呻吟与床响"的独白，说话人都是 s，不是 Tsubasa。

## 二、love 线逐事件脉络

### tsubasadate1

首次正式约会，功能是立骨架：财富、家族史、仪式、以及她对"世界"的自我认证。她把 s 接到宅邸并亲自当导游。段落核心是枯山水庭院与"仪式之间的人生"——她说 Tsukioka 家 "dating back to the origins of Kumon-mi"，这座庭园自江户时代起基本未被改动，而她第一次见到它是在前来与 Tomonori 相亲的行程上。

随后的"ceremony room"是她对仪式性的正面陈述："It's where I married my husband and where my daughters will marry theirs." 她也在此处透露曾为 Touka 安排过多位求亲者，最终" rethink things"（重新考虑）。

收尾在室内植物园。园中只养一棵树——一株靠精确控温、进口土壤与"意志力"维持的常开樱花（"an everblooming sakura"）。她用一个词点题：**"Perseverance."**（坚韧），理由是它是昔日世界唯一残存的痕迹。她同时给出全段的自我定义："this is my world. It's one that I chose and one that I {i}would{/i} choose if the chance to do so repeated itself."

### tsubasadate1p2

第二段，场景从樱花树转入画廊与泳池。Touka 在池中被撞见，三人同场。

实质内容是她与 s 的单独摊牌。她先用"productive"自辩为何总在做事（带参观、带孩子、替家族生意巡视各地温泉旅馆），随后切入正题：

> tb: A young lady who I've grown rather fond of lately seems to believe that the two of you are involved in an exclusive relationship with one another.

bonus 分支里她把话说明：

> tb: You are a grown man sleeping with a girl in [high_school]. Sleeping with your {i}student.{/i}

这里的"young lady"是 Chika——s 的旁白明确说 "She's one of the only people Chika trusts enough to talk about our 'relationship' with"。她随后表示在意的不是行为本身，而是"你会不会伤到那个女孩"，并要求 s 作答：

> tb: Do you love her?
> s: Not the way I'm supposed to.

（这两句分别是 Tsubasa 的提问与 s 的回答。）s 给出的答案是会伤人、但不离开她："She doesn't have to be alone anymore." 她接下这个答案："As long as you're not just using the girl, I can accept the nature of your relationship."

段末是"游泳课"。她先问 s 觉得池子多深，再讲 Touka 小时候学不会游泳、雇遍名师无效，于是她照女友母亲的做法，把 Touka 直接推进池里：

> tb: And now you're her teacher.

——先制造困境、再解释困境的必要性，是她在本段给出的自我方法学："Sometimes, forcing people to do things they're not comfortable with is the best way to move them forward." 她也承认 "I've known from the beginning that you were the exact opposite of what Touka needs. / And I think that's exactly what makes her need you the most."

bonus 分支中 s 反呛："you have literally heard me have sex with a girl the same age as your daughter"，她平静回答 "Lots of it."

### tsubasaspecial15

车内—公寓的一段。她借"送 s 回家"之名把 Tsukasa 中途放下，独自进入 Touka 投资的那栋楼、也就是 s 的公寓。

对峙感由她自己给出："I think you {i}should{/i} look slightly more threatened right now. I'm a very powerful woman, Sensei." s 猜她想要性，她否认；她真正想要的是把 Chika 与她妹妹挪进更安全的地方。这里落下她的方法论自陈：

> tb: The type of person I {i}actually{/i} am would subtly convince her that what she wants isn't what she needs...all while slowly guiding her from the shadows into a safer, healthier life.

> tb: It's manipulation in the {i}good{/i} way.

> tb: I look out for my girls.

她把分工定死：她负责财务与"母亲式的陪伴"，s 负责维持"她靠自己做到了"的幻觉（"you can be the curtain maintaining the illusion that she's doing it all on her own"）。实施手段是把这套安排包装成"价格低到不会让她起疑的新公寓"。

顺带落下的伏笔是"slideshows"——Tsukasa 问起时她回 "Now, Tsukasa's curiosity is going to be piqued and we'll need to start her on 'those' slideshows even earlier than anticipated."

结尾她连抛三问，s 只接受了前两问后她又补最后一问：

> tb: Can you still love someone if they're always right beside you?

她不待 s 回答就离开。s 的旁白是："Tsubasa leaves before I can tell her I already have an answer to that last question."

### tsubasadate20

弓道场。本段的第一层信息是社交网：她与 Wakana 同为 Higashigaoka Girls' Academy 校友，并主动提出以名字相称（"a fellow alumna of Higashigaoka Girls' Academy"）；两人并不同届，"I'm much, much older than Wakana."。第二层是年龄：她拒答自己的年龄，s 自报 "I'm 31."

第二场景是搬迁计划的推进。她通报 Touka 已同意把楼里几间空房以远低于市价的租金挂出，目的从一开始就不是营利，而是 "to give her an understanding of how the system and property management work as a whole." 她把动作描述为"把钥匙放在地上让她自己捡"。

哲学核心是她对替他人做决定的辩护：

> tb: Most people aren't smart enough to make their own decisions.

> tb: What's wrong with playing God when the one we dreamt up never wants to come outside?

她自称 "the 'bad cop' who just-so-happens to have good intentions"，把 s 放在 "good cop" 的位置上。关于 Touka 的自治权，她的说法是她反复出现在学校本身就是提示："There are several mistakes I {i}want{/i} her to make- and she is well on her way to making them."

木偶师意象由 s 提出、她本人认下：

> s: You really are just a well-endowed puppeteer, aren't you?
> tb: Perhaps I am!

段末 s 的旁白承认自己是被牵线的人，但同时承认甘愿："I don't mind having her yank my strings a little longer if it changes that."

### tsubasaspecial20

向日葵田的梦作引子，随后是办公室会谈。

会谈的第一项成果是她的背景调查：她直接叫出 s 的名字 "Akira."，并说明依据——他学生时代的成绩优异，且"every single career assessment survey you ever filled out all had the same exact aspiration listed on them. {i}Teacher.{/i}"。她另外问了一句 "You were quite the poet as well. Do you still write?"，s 答 "No. I don't write anymore." 并拒绝谈原因。s 在此自述失忆："the past is a bit of a touchy subject for me as there's still a lot of it I don't remember" / "Just call it amnesia."

第二项是请求：她要 s 接手 Tsukasa 的家教（"Tsukasa, how would you feel about Arakawa-sensei taking over your lessons?"），并计划让两个女儿搬进 Touka 的那栋楼。Tsukasa 当场爆发："You're always working and Papa never wants to see me and I'm tired of you always trying to get rid of me!" 随后摔门离去。

s 点破 Tsukasa 的孤独，她两次承认 "You're right... / You're absolutely right."，并宣布："All other {i}things{/i} are now on hold — and that includes this meeting." 家教计划改为"等母女关系修复后再进行"。

离场前她把姿态放平：

> tb: Just because I'm powerful doesn't mean I don't make mistakes. I'm as flawed and vulnerable as everyone else.

> tb: I'm the same as you.

> tb: That's what I meant by {i}equal.{/i}

紧接着又以"女儿发育阶段论"划界：Touka 已进入发育的最后阶段，她对 Touka 的身体自主不设限制；"But if you believe for even a moment that I'd apply that same ideology to Tsukasa...we'd have a bit of a problem on our hands." 最后以一句悬空的收尾："All you need to do is let me know and...{i}arrangements{/i} can be made."（s 追问 "What the fuck are {i}arrangements?{/i}"，她未答。）

### tsubasaspring1

春季篇开场。s 的梦交 God of Torment 被电话打断，6:30 她来电把他叫到宅邸。

本段的第一记重音由 s 给出：他要求她"绝对不要插手"自己的侄女 Ami——"Do {i}not,{/i} under {i}any{/i} circumstances, get yourself involved with my niece." 她先模仿威胁口吻，随即笑场并正式承诺："if you do not want me to get involved, that I will keep my nose out of it."

她给出的新制度是定期汇报：

> tb: Status reports.

> tb: On all {i}four{/i} of my daughters since the Chosokabe girls are under my wing now as well.

她要的不是学业评估（"It's not their {i}education{/i} I'm interested in"），而是 s 对她们"正在成为什么样的女人"的判断。对话中 s 承认在 Touka 身上找到的是"comforting"、她追问为 "matriarchal?"；谈到 Tsukasa 时 s 说 "Tsukasa's a brat." 但也说她聪明、好教。

段末是手机没收。她以"报警"相胁拿走 s 的手机，还回去时里面已经多了一个号码——"You have obtained Tsukasa's phone number!" 她的解释是冲动行事能提升血清素，并把它称为一次"test"。摊牌句落在：

> tb: Who says I'm putting {i}any{/i} trust in you at all? Maybe I'm just...cutting off a few of your strings so you don't confuse yourself as my puppet anymore.

### tsubasaspring4

Chinami 传来的联姻风声促使 s 主动致电。她在电话里先自嘲自由的边界："the freedom I typically have is almost always inhibited by the constant possibility that I may need to stop what I'm doing to address some sort of conflict or trade."

"惊喜"是一段真人：她把 Yuki 安置在自己的办公室里，Yuki 已脱离濒死状态。她的定性是 "Yuki's health is no immediate concern and the Tsukioka Foundation is fully covering any and all treatment she may need." Yuki 本人的说法是 "I'd be dying without you, Nee-sama."

正题是联姻。她把决策权推给丈夫：

> tb: {i}I{/i} don't. My husband does. And this company is even more his child than the girls are. I imagine Touka would be in the same boat if she were not the heir apparent.

> tb: What I'm doing is mediating the facilitation of his desires as that is my role in both the company and this family.

同时她给出止损条件："I'd not hesitate to call this off should Tsukasa verbalize her hesitancy. Even mere {i}unease{/i} would do the trick."

随后她翻出 s 在 Tsukasa 房间里的事，拒绝接受"只是意外"的解释：

> tb: You dragged that woman to Tsukasa's room for one reason and one reason only. You wanted to plant a seed.

> tb: And no — I'm not talking about the type you planted in {i}her.{/i} I'm talking about the type that wakes a curious little girl up.

她以此为据要求 s 在给 Tsukasa 的家教里增加一门课，并留下双关的收束："us Tsukiokas are 'hands-on' learners." s 尚未答应，她已经按铃叫 Tsukasa 到办公室，并宣布自己要在场旁听第一节："You don't have a choice! And neither do I — so let's just make the most of this, shall we?"（本段结束跳转至 `tsukasaspring6`。）

### tsubasaspring5

Touka 与母亲的正面对峙，一小时后发生于浴室。

Touka 的指控有两层：一是她在自己家里替 s 与 Tsukasa 制造机会，二是这一切出于嫉妒——

> to: Love for someone that was not {i}chosen{/i} for me.

Tsubasa 的反击是把"联姻"重新定义成一场局：Tsukasa 已经自己查清了婚事却一句话没对她说；无理由取消会连累全家；于是——

> tb: But if a third party interferes...and she falls for someone outside of our direct sphere of influence, perhaps we won't need to call off a wedding at all?

Touka 逼问这是否等于"把 Tsukasa 给 Sensei 以免把她给别人"，她答：

> tb: Maybe. Or maybe it's just one more lie that's far easier for you to understand than an even harsher truth.

同一段里她也给出母位的条件句：

> tb: What if what I'm doing right now is the ultimate sign of love?

以及一句把所有人算进去的总纲：

> tb: There's only one way to save all of you. And I imagine we'll {i}all{/i} wind up sleeping with him eventually, so what's the point in holding back now?

关于 s 对她而言是什么，她拒绝回答：

> tb: Just a friend, of course. Any other connection is purely coincidental.

被 Touka 追问"你答应过要保护他"时，她不解释对象与时间，只反呛 Touka 对"她睡他"和对"Tsukasa 睡他"反应不同。末尾她抬出家族纳妾史施压："But we have a {i}long{/i} history of concubines in this family... / And if you don't hurry up, I might be tempted to take one."

旁白随后罕见地掀开她的状态：她裹着浴巾站了整整五分钟，手指按着眼皮，"came to terms with always being seen as the bad guy"，并短暂怀疑自己让 s 去教小女儿性知识是否是个坏主意。判词是：

> N: Tsubasa Tsukioka was an excellent babysitter — and an even better business partner.

> N: Her job just sucks.

### tsubasaspring6

与 Yuki 的私人日，是全线唯一让她把权力放下的一段。

开头是主线的钩子：Kumon-mi Mall 正在"renovations"，官方从不说明在改造什么，商场里有个巨大的深坑——"And something tells me that soon, I will." 而她有施工期进入权限："Because Tsubasa Tsukioka has special privileges and is allowed inside during the construction for some reason."

商场里是芭比裙的羞辱式玩闹。斗嘴中她递出一句悬置的说法：Yuki 那位"袖手旁观妻子被一伙人侵犯"的丈夫，"a group of cronies who I may or may not have had subsequently castrated"——她随即收回："Hm? I didn't say anything."（Yuki 追问时把这伙人称作 Yakuza。）她的特权宣言在此处落下："Only {i}I{/i} should be able to say mean things to you without being punished. This is my privilege as the most powerful woman in Kumon-mi."

她解释了为什么不把 Yuki 锁在身边——两句连着说：

> tb: The same reason as last time. A forest bird never wants a cage.

> tb: I'm just saying — it's your freedom that's always made you so beautiful.

夜里两人骑车去湖边。Tsubasa 想让 Yuki 改口直呼其名被拒，Yuki 用阶层落差回绝："You were born to eat from silver spoons and shit and I was born to polish 'em." 她答 "Va bene."。

段末旁白是全线对她的心理描写：

> N: ...for Tsubasa Tsukioka had a difficult time being herself in front of anyone else.

> N: It came with a tinge of guilt, though — for she'd opened the door of a cage she bought in hopes that a forest bird would fly into it on its own.

她是把笼子装满浆果与种子的那个人，因此这份收留仍显得勉强；"But perhaps if she kept waiting, it would one day land on her shoulder. / The thought of that alone was enough to keep her going when all else began to crumble."

段末 s 收到一条图片消息："You've received a picture message from Maya Makinami!"

### tsubasaspring7

s 家。Niki 与 Ami 在场，Tsubasa 已先一步登门并与 Niki 聊过 s 的过往。

Ami 拿出印有父女合照的定制马克杯，Niki 抗议时她给出全线最荒诞的一句辩护：

> tb: Frankly, I don't see the issue so long as both parties consent. Incest dates back longer than any of {i}us{/i} do and has been employed by nobility for thousands of years to keep bloodlines pure.

Niki 下逐客令后她立刻认错："I apologize. You are absolutely right and I was being inconsiderate after you went out of your way to extend a warm welcome to me." s 的错愕换来一句定位：

> tb: I enjoy playing with you. You're the only toy I have that I can use in public without being put on a registry.

车内是实质内容。她先清算 s 在住宅区小巷里对 Touka 的越轨："I offer up my entire home to you to essentially do as you please with Touka, and you claim her in a public alleyway?" 随即点破他的可操纵性："It makes me wonder if you've always been this easy to manipulate."

围绕 Tsukasa 的交锋落在"怪物"一词上：s 说 "I'm a monster now, Tsubasa."，她反问——

> tb: Maybe turning her into a "monster" is precisely what will save her? It saved {i}you,{/i} did it not?

s 否认后她抛出半句预言：

> tb: Then you've given up on achieving any sort of happy ending? Of reaching a future where everyone's dreams can come true?

画面切入她处闪回后，她封口："Nothing at all."，并在黑屏里落定——

> tb: I just have to {i}say{/i} things.

分支结构上，本段以 `if tsukasaspring6 == True and amifingered == True:` 分岔：条件成立则继续（跳转 `tsubasaspring8`）；条件不成立则进入另一支，s 拒绝配合，文本打出 "**EVENT CHAIN CANCELLED.**" 与 "Tsubasa's affection stagnates."，同时置位 `tsubasaspring8miss`、`tsukasaspring7miss`、`tsukasaspring8miss`、`tsukasaspring9miss`。这是本线唯一带硬取消节点的分支，触发条件是前置事件是否完成，而非玩家当场选择。

## 三、lust 线概貌

四个主要场景群，共同命题是：**她把欲望当作可操控的信息与可支配的场面**。

- **`tsubasaspring2`（酒吧）**：她推门进来时 Sara 正在吧台后为 s 口交。她识破后没有离开，反而坐下点酒、品评酒质、一边抚摸 Sara 的头一边指挥节奏，一句 "Deeper." 把场面彻底接管。她给出的理由是 "Leaving a job like this incomplete is unbecoming in numerous ways."。收尾是威胁式倒计时："for every minute you take from here on out, I'll reveal one of your {i}deepest...{/i}darkest secrets..."。事后她又以送 s 回家为由把他塞进自己的车——直接接入下一段。
- **`tsubasaspring3`（车内）**：她先讲述自己婚前与四名按摩师发生关系的"家族传统"（"The night before I was married. It's a family tradition."），又补上另一段四人群交，然后亲手拆台："wouldn't you say it's possible neither of those...what do you call them — orgies — happened at all"。她给出这一整套行为的目的：让 s 不再怕她——"All it took for you to change the way you look at me was a little bit of lust and some seductive whispers — tall tales of times that I've been vulnerable."，并以 "I'm as scary as I've always been. You're just easy to manipulate." 收口。同一段她也说到与丈夫分房的事实。光喻四连是本段的收束："It all changes with the light, Akira." / "Sometimes, the things you see aren't really there." / "you can never know what's real until you {i}experience{/i} it."
- **`christmastsubasa1`（圣诞宅邸）**：她把 Molly 赶出房间、重新锁门，然后就地接管局面。她逐层推进称谓体系——从 "little boy"、命令其自慰，到逼他说 "I'm sorry, Mother...I've been a very bad boy."，再把 Mother 换成 Mommy。中途她把 Touka 叫到门外，以"抓老鼠"为名制造暴露恐惧，并在 Touka 找钥匙的同时压低声音催促。高潮后落下核心禁令：

  > tb: Never...and I mean {i}never...{/i}cum for anyone other than a Tsukioka in this manor {i}ever{/i} again. Do you understand me?

  s 答 "Yes... Mother..."，旁白以两行盖章："O world- / Look what you have done to me." 本段的背景是那场被 s 打断的会议——她斥责他 "jeopardize a meeting ten years in the making"。
- **`tsubasaspring8`（塔楼浴室）**：她把这里称作 "my own personal Heaven. Tyranny is {i}so{/i} much easier in the bath with a nice merlot"。s 拒绝闭眼，她凭一股力气把他塞进更衣柜并反锁，理由由她自己给出："Have you never heard of hysterical strength before?"

  柜中的独白属于 s，不是她：那是他被锁进壁橱时的童年记忆——数数游戏、门外的尖叫与呻吟、床头撞击墙壁的声音，结束于 "A neglected animal with no one left to give me water. / This cage will not unlock again."（源文未点名门外的声音属于谁。）

  她把整场定性为演示："This is practically a sales pitch. So sit back and enjoy the presentation, would you?" Tsukasa 进来后她一边共浴一边诱导，先问"你想不想有人像那些女孩看 Akira 一样看你"，再把话题推向"如果他现在就在那个柜子里对着你自慰呢"，最后以贴耳一吻收尾（"Chu..."），Tsukasa 尖叫逃走。s 在柜中失控，她只回一句：

  > tb: Hysterical strength, Aki-kun.

  段末旁白宣告阶段结束："every worker bee is back outside of the hive... / And, in other news- / So has the charade."

## 四、与主线/元叙事咬合点

1. **"playing God" 一句的语境**（`tsubasadate20`）：她在为自己替 Chika 做决定辩护时说出 "What's wrong with playing God when the one we dreamt up never wants to come outside?"。句中的 "the one we dreamt up"（我们构想出来的那一位）在文本上明指被造者的存在，是全线最直接的元叙事措辞。
2. **商场 renovation**（`tsubasaspring6`）：Kumon-mi Mall 封闭施工、内部有巨大深坑，官方从不公布改造内容；Tsubasa 拥有施工期进入权限，且能带人进去。这是她与全镇尺度地下工程的直接接口。
3. **圣诞会议**（`christmastsubasa1`）：那场 "ten years in the making" 的会议被 s 打断，本段结束跳转主线标签 `christmasfive6`。议题在源文中始终没有揭晓。
4. **`tsubasaspring7` 的取消节点**：`EVENT CHAIN CANCELLED` 一支会同时置位 `tsubasaspring8miss`、`tsukasaspring7miss`、`tsukasaspring8miss`、`tsukasaspring9miss`，说明 Tsubasa 线与 Tsukasa 线在此共用同一道闸门。
5. **slideshows**（`tsubasaspecial15`）：她以"要提前给 Tsukasa 上那套幻灯片"的说法带过，Tsukasa 提到 Touka 看完后"整整一周没出自己那一翼"。内容与用途在本文件内没有再展开。
6. **Maya 图片消息**（`tsubasaspring6` 结尾）：s 收到 "a picture message from Maya Makinami"，本文件到此为止，未说明内容。
7. **旁白人称的异动**（`tsubasaspring5` 末尾）：旁白在描述 Tsubasa 的心理后突然转为第一人称复数——"Neither one of us can tell you what it is because neither one of us knows."，随后才回到第三人称判词。这是本文件内旁白唯一一次以"我们"自称。

## 五、未解伏笔

- **s 的失忆**：`tsubasaspecial20` 中 s 自述 "Just call it amnesia."，在 `tsubasaspring1` 又提到过去"still pretty hazy"；源头与内容始终没有交代。
- **圣诞会议**：那场"十年筹备"的会议议题未揭晓；s 推断它需要对某个女儿保密，Tsubasa 只回答 "Perhaps the {i}meeting{/i} concerns said daughter?"，未确认。
- **slideshows**：内容与用途悬置。
- **"protect him" 的承诺**：`tsubasaspring5` 中她对 Touka 说自己是"a mother who's already promised to protect {i}him{/i} as well"——向谁承诺、何时承诺，均没有交代。
- **"the harsher truth"**：比"让 Tsukasa 与 Sensei 产生牵连"更残酷的那句话从未说出。
- **Yuki 的笼子与她的治疗**：`tsubasaspring6` 结尾"等鸟自愿落到肩上"的等待，与 Yuki 的治疗进展（同段中 Yuki 说 Sara 还不知道癌症的事）共同构成本线的情感悬念。
- **Tomonori 的实体性**：名义上的家主、与妻子分房、几乎不在女儿们面前出现；s 在 `tsubasaspring7` 说 "I'm not even sure he's real, to be honest."，她顺势接 "Perhaps you'd like to meet him?"——这个承诺没有兑现。
- **视频的真伪**：`tsubasaspring4` 中她提到 s 在 Tsukasa 房间里的画面"音频几乎听不清、画面很糊"，s 追问是否真有录像，她回 "Either that or I'm lying. Which one is it, do you think?"，没有给出答案。
- **s 的柜中童年**：`tsubasaspring8` 的壁橱记忆（数数、门外的尖叫与呻吟与床响）属于 s，源文没有点名门外的人是谁。
- **"sometimes I just have to say things"**：这句话究竟是托辞还是陈述，全文件内没有判据；她说过的话里哪些属于"必须说的"也没有清单。

> 按源行号检索本角色 label，见 `索引/Tsubasa索引.md`。
