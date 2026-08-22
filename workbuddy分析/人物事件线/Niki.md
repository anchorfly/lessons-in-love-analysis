# Niki 事件线全析

> 源文件：`NikiEvents.rpy` ｜ digest：`_digest_Niki.txt` ｜ 共 31 个 label
> 定位：偶像角色，dating sim 养成丰满；元叙事价值集中在**记忆缺口、时间循环暗示、Akira 真名揭露、以及 [uncle]/[niece] 框架**（与 DormEvents `trinity1` 同构）。

## 一、角色基本盘
- 偶像（idol），因职业无法公开约会（[2654] "I can't *go* on actual dates. I'm an idol, remember?"）。
- 与 Sensei 有"童年玩伴→重逢"的漫长羁绊（[2541] 一起看《Friday the 13th》、[1096] 第一次去卡拉 OK），自述"把整个 20 岁都浪费在你身上"（[1008]）。
- 与 Kaori 被并列为"有自己生活、不围着我转"的两大范例（[1397]）。

## 二、love 线（dating sim 主线）脉络（condensed）
标准邀请→电话→约会→特殊事件链：
- 电话/邀请：`callnikimorning/afternoon/night`、`nikigen*`、`nikiinvite*`、`nikiinviteaff`
- 约会：`nikidate1` → `nikidate5` → `nikidate10` → `nikidate15`
- 表白/命名：`nikilovesyou1→3`、`nikifirstlust`、`nikinaming`、`restofnikifirstlust`
- 春季长线：`nikispring1→8`（含 [5053] 附近 beachfive8）
- 群像：`dormwarssixniki1`
- 反复出现的"假装失忆"喜剧框架（[474] "pretending to have amnesia"）是其恋爱线标志。

## 三、lust 线概貌
`nikifirstlust` / `nikinaming` / `restofnikifirstlust` 构成首次性支线；以偶像身份下的隐秘/偷情张力为卖点（[1771] "Does hand stuff not count anymore?"、[1654] bjreplay 等命名暗示）。

## 四、与主线/元叙事的咬合点
1. **Maya 对"无数人"的说法 + 质疑**（[861]–[863]）：
   > N: And not just me, but seemingly countless other people if we're going by what Maya says.
   > N: But what if Maya's wrong?
   明确引用 **Maya 的说法**（"数不清的其他人"= 被重置/被创造的个体），且叙述者首次质疑 Maya 是否错。
2. **记忆仅限"过去几个月"**（[879]）：
   > s: Because if that's true, it's going to be a lot harder to justify why I can't remember anything past the last several months.
   与全局"循环后记忆截断"母题一致。
3. **时间循环被角色口头点名**（[937]）：
   > s: That doesn't explain the time loops.
   角色在对话中直接说出 "time loops"——元叙事词汇渗入日常台词。
4. **Ami 的 [uncle] 框架**（[2170]–[2171]）：
   > a: Even if you did date my [uncle] in the past, I don't think I was really old enough to remember it.
   > ni: And I wouldn't expect you to. But since *I* remember you, that's really all that matters.
   与 DormEvents `trinity1` 的 [uncle]/[niece] 框架同构——Ami 称 Sensei 为 uncle，Niki 与 Ami 有此辈分关联，暗示 Sensei 与 Ami 的"拟亲属 + 跨循环记忆"关系。
5. **Akira 真名揭露**（[3547] / [3549]）：
   > ni: Akira?...  ／  o: Your name is Akira?
   Niki 与 Otoha 在同一段（酒店场景）得知 Sensei 真名 **Akira**，呼应 Ayane 未来线直呼 Akira。

## 五、未解伏笔
- **"Maya 的数不清的其他人"**：Niki 听到的 Maya 说法指向何种规模的存在？是否即被重置的历次迭代个体？
- **Niki 与 Ami 的 [uncle] 关系**：Ami 视 Sensei 为 uncle，Niki 又曾与"uncle 辈的 Sensei"交往——跨循环辈分如何成立？
- **Niki 是否循环感知者**：能说"time loops"、察觉记忆截断，但是否真正记得过往迭代（如 Makoto 那样）仍不明。

## 六、label 总表（31 个，节选关键）
callnikimorning[1] · callnikiafternoon[28] · callnikinight[77] · nikigenmorning[92] · nikigennight[156] · nikiinvite[169] · nikiinvitegen[180] · nikiinviteaff[223] · nikifingeranim[283] · nikidate1[304] · nikidate5[701] · nikidate10[1217] · nikidate15[1643] · nikiinvite1[1936] · nikiinvite2[2371] · nikilovesyou1[2603] · nikilovesyou2[2871] · nikilovesyou3[3273] · nikifirstlust[3752] · nikinaming[3897] · restofnikifirstlust[4053] · nikispring1[4284] · nikispring2[4700] · beachfive8[5064] · nikispring3[5391] · nikispring4[5793] · nikispring5[6085] · nikispring6[6400] · nikispring7[6764] · nikispring8[7050] · dormwarssixniki1[7373]


---

## 【二轮增补】Niki 线逐 label 详梳

> 摘自 R1（该 agent 于 Nodoka 节前中断，Nodoka 增补待后续）。

## 四、Niki 线逐 label 详梳（NikiEvents.rpy）

### 4.0 调度与门控

- **callnikimorning [5-12]**：nikidate10←love≥10+**secondbeach18**；nikilovesyou1←love≥20+**slumberreset5**+day==6；nikispring1←love≥40+**otohaspring2**+day>5（Niki 线与 Otoha 线强绑定）。
- **callnikinight [81-84]**：nikidate5←love≥5+**rindorm40**（依赖 Rin 宿舍线）；nikidate15←love≥15+day==6。
- nikiblock 封锁期 [2-4]。

### 4.1 日常与约会线（nikidate1/5/10/15）

- **nikidate1 [304]**：假名三选喜剧（Noodles the Bird/Paul/Barack Obama）[342-374]；Route 69 Diner"sausage-fest"；Kaori 不识 Niki [486-547]；道歉债结构 [624-635]。
- **nikidate5 [701]**：**全文件关键身份事件**：
  - Sensei 自白 "It's like I'm a different person occupying this body." [834]→Niki 否定："You're exactly the same way you've always been... if there is anyone out there who would be able to catch if you were magically a different person or whatever, it's me. **We grew up together. Shit, you basically lived at my house.**" [840-847]。
  - **Niki 的镜像解离史** [893-918]："Something similar happened to me before... there were a lot of days where I woke up and felt sorta...disconnected from the world. **Like I was also just a visitor in my own body.**... I lost sleep. I heard things. I'm pretty sure I even started hallucinating at some points... I thought about killing myself too. Not cause I wanted to die... I think I just wanted to teach you a lesson."——Niki 在 Sensei 失踪期同样经历"访客感/幻听/自杀念头"（与 Ami 失忆、Maya 时间跳跃并列为世界异常三症状）。
  - **年龄揭晓** [980-1000]：**Sensei 31 岁、Niki 29 岁**（"You're two years older than me."）——全作唯一具体年龄披露。
  - "That doesn't explain the time loops." [937]（一轮 md 引用无误）；"seemingly countless other people if we're going by what Maya says... But what if Maya's wrong?" [861-863]。
  - Niki 秘密地下教室教 Otoha 唱歌 [1129-1152]。
- **nikidate10 [1217]**：**Niki 仍是处女** [1494-1541]："Since we...you know. Never really did it... We just did...{i}hand{/i} stuff most of the time. It was hard since my parents and Noriko were always home..."——**与 Maya 线 mayachristmalloween2 [9245] "I was the first! Not counting fucking Niki and...Ami's mother" 存在张力**（Maya 所指或为夸述/或将手部亲密计为"fucking"）；"I'll just fill in the blanks with how I want things to be and force myself to believe they're true. / Is that really how you want to live?... / **Gee, wonder who I learned that from?**" [1546-1549]（Niki 指控 Sensei 教会她自我欺骗）。
- **nikidate15 [1643]**：演唱会+Grand Tsukioka 酒店夜（酒店为 Toriko Tsukioka 家产 [1713]）；"Nakayarakawayama" 合姓玩笑 [1786-1787]；初夜之邀 [1899-1909]。

### 4.2 邀请线与 nikilovesyou 三部曲（真名揭露线）

- **nikiinvite1 [1936]**：Niki 携 Noriko 为 Ami 而来（girls' night）[2069-2099]；"third Nakayama sister" 收编 [2220-2239]；[uncle] 框架对白 [2170-2171]（一轮 md 引用无误）。
- **nikiinvite2 [2371]**：电影夜；嗅觉怀旧与虚无 [2517-2526]（"I attempt to envision a younger version of Niki. But again- There's nothing there. And it's almost as if I never existed at all."）；**黑暗预演自白** [2490-2500]："Especially girls that spend their entire life waiting on you despite you being a heaping pile of shit **who takes advantage of girls while they sleep**. / Just kidding. / I didn't do anything. I'll never do anything. / ... / **Not until I'm supposed to.**"
- **nikilovesyou1 [2603]**：圣诞爽约对质 [2616-2634]；**系统级屏蔽词**——Niki 台词中反复出现 `[[REDACTED ~ NOT YET READY]`、`[[REDACTED ~ MORE UNNECESSARY INFORMATION]`、`[[REDACTED ~ UNIMPORTANT]`、`[[REDACTED ~ REPEATED USAGE OF PROHIBITED WORD]`、`[[REDACTED ~ FURTHER OFFENSES MAY RESULT IN UNEXPECTED SIDE EFFECTS. PROCEED WITH CAUTION.]` [2727-2845]——**被屏蔽的即 Sensei 真名**（提及过多触发世界级报错）；游乐场起源 [2749-2777]："Just...two kids who met by chance one day... This is where it all began. **And if you didn't show up today, it's where it would have ended.**"；城墙可见性 [2787-2788]；**复制体常识** [2790]："There are other Niki Nakayamas in other parts of the world. I'm sure they'll be fine."；Noriko 兄妹定位嘱托 [2810-2833]。
- **nikilovesyou2 [2871]**：无底洞哲学 [2892-2905]（"In the end, you either drag them down with you or let go..."）；"I love you so much." [2907]；**"You're not like this because you're a bad person, you're like this because you never learned how to be a good one. {i}It's not your fault.{/i}"** [2936-2937]；"I'll always be your home when you have nowhere else to go." [2943]；**记忆巡礼**：`[[REDACTED ~ REPEATED USAGE OF A PROHIBITED WORD HAS RESULTED IN A FATAL ERROR]`＋**"////////////////PLEASE NOTE THAT RESTARTING YOUR DEVICE BEFORE AN UPDATE IS COMPLETE MAY RESULT IN IRREPARABLE DAMAGE"** [2962-2967]；Wallace Stevens 引诗块 [2976-2995]（"The fire eye in the clouds survives the gods."）；**se 现身吃醋** [3090-3099]："how come {i}we{/i} never carved our names into a tree?... Are you two together again? **Does she {i}fuck{/i} you like I did? Who's better, me or her? Be honest.**"（se 与 Sensei 性关系再确认）；合掌造部落初吻地 [3062]；刻名树（她把他的名字划掉 [3063-3064]）；**"You jumped. Do you remember?"** [3163-3164]＋"**This is where your world was ripped away from you.**" [3210]——**该地=旧 Sensei 世界崩坏+跳落（自杀未遂）之处**（一轮 md 未记）；**真名揭露正点** [3254-3263]："**{i}Let's go home, Akira...{/i}** / Akira... That's...my name. My name is Akira. / ... / **I'm a good boy.**"
- **nikilovesyou3 [3273]**：Niki 旧居；**信件监狱** [3295]："This is where she must have written me those letters — **the prison I locked her in when I left her behind.**"；"Who {i}knows{/i} that name? Ami surely does, yet she's never said it to me. I'm sure Maya knows too...maybe even Ayane." [3299-3301]；**"The weight of five forbidden letters presses down on my neck"** [3305]（Akira=五字母禁词）；se 的罗密欧与朱丽叶戏仿 [3338-3348]（"Doff thy name!... You're such a Montague sometimes."）；初夜场景（抽象）；"**She gave me a name.**" [3717]；+10 love＋"Who is it you truly belong with?" [3735-3738]。

### 4.3 lust 支线（nikifirstlust/nikinaming/restofnikifirstlust）

- **nikifirstlust [3752]**：海边旅馆（Imani/Wakana 同室喜剧）； nikinaming [3897]：`$ nikimaster` 输入分支。**Selebus 分支** [4016-4039]："Hey, I know that guy. **He created Lessons in Love.**... I fucking hate him... it's {i}his{/i} fault that half of my life has been a living hell? Do you have any idea how much I've suffered because of my fucking backstory? **He's the asshole who came up with that.**... So fuck that guy. He can touch grass."＋Sensei："I still think it would be right to go support him on **SubscribeStar** as he develops this game entirely alone"——**作者实名+订阅平台+游戏名三重入戏**；其余分支：Akira/Sensei/Daddy/Onii-chan 接受，"Niki Nakayama"（拒，"identity theft"）与"Noriko"（拒）。
- **restofnikifirstlust [4053]**：Imani/Wakana 旁听吐槽；Wakana："No wonder he doesn't spend time **writing anymore** if {i}this{/i} is his new skillset of choice." [4086]（**Sensei 曾写作**——诗人设定旁证）；+5 lust。

### 4.4 nikispring1-8 与 beachfive8（第四章家庭剧主线）

- **nikispring1 [4284]**：地下教室粗暴 couch 场景（抽象）；"the looming desire to fall asleep and never wake up" [4472]；**Otoha 在场自慰并同步高潮**（抽象）[4623-4655]；"which could bring me one step closer to **another tally mark**" [4677]（收藏计数，与 Ami 线"collection"同源）；jump otohaspring3。
- **nikispring2 [4700]**：**Ami 初潮/卫生巾事件**（guardianship 失格自省 [4722-4737]）；**口袋照片** [4775-4781]："It's a picture from before this all started. **A girl with twintails in a field full of flowers**... She's smiling...laughing at something. I wasn't there for it, but I wish that I was. Because now- **I would kill for her.**"（双马尾=Ami 的"一切开始之前"旧照）；**se 内心之声全面爆发** [4894-4918]："{i}Liar! She wants her mother but her mother's dead!... You still hear her in the walls! See her reflection in the mirror! And you wish SO BADLY for her to tear down the barrier between life and death to RETURN TO FORM, but she never does!... **I taught you better than this, my lightning-bug.** Should I have nibbled on your ear more? Sliced your scrotum with my nails?{/i}"——**se 称 Sensei 为 lightning-bug（萤火虫）**；**"{i}Tell her! About the rooftop! About the girl with aquamarine eyes!{/i}"** [4966]（天台+碧绿眼女孩=Maya 的信息链）；**"Let me move in with you. Let me be her mom."** [4978]（amicamp2 [9026] 闪回同帧）；"Which side of the bed do you prefer to sleep on？" [5051]＋鸟巢诗 [5058-5060]。
- **beachfive8 [5064]**：Ami-Niki 居家夜；**se 全程在场并被 Ami 感知** [5276-5299]："the ghost mom! **The one who liked children in {i}every{/i} way possible.**... she stood there in all her ghostly envy — wishing {i}she{/i} could be the one providing a lap pillow right now."（"以各种方式喜欢孩子"——暗指含性）；**Ami 的母亲颂词** [5317-5354]："The closest a girl could ever come to perfection... She {i}understood{/i} things. Things about God... **Her words alone could change the way you see. They could change what you hear...what you {i}think.{/i}**... she took me to the top of a hill... put me up on her shoulders... sung to me... spun me around beneath her favorite tree... **read me some of her favorite poems**... **Sometimes, I wish I could rewrite the past. Figure out a way to put someone else in her place so that {i}they{/i} could die instead of her.**"；**se 呼唤被 Niki 听见** [5359-5379]（sekni "Ami..."→Niki："I just thought I...heard something."→旁白"It wasn't."）→结算 **"{i}Niki's sanity has decreased by 1!{/i}"** [5384]（理智值系统化）。
- **nikispring3 [5391]**："see me in the spring time" 红墨水字条 [5403]；Niki 搬入谈判：spoon 类比 [5658]（"Ami Arakawa, let me be your spoon."）；Ami 条件测试 [5705-5713]；成功 [5731-5737]。
- **nikispring4 [5793]**：开场诗 "{s}You kissed me after this one.{/s}" [5801]；Noriko 姐妹闹剧；**Nakayama Sister Law 19A-B-42L=恶魔献祭权** [5949-5952]；**NordVPN 广告打破第四墙** [6074-6075]；fanservice 元讨论 [5987-6000]。
- **nikispring5 [6085]**：混浴夜话；偶像缺陷论 [6159-6200]（"my flaws come out in droves when you actually listen to what I'm singing about... I'm clingy and obsessive and desperate and scared"）；**Ami 诛心三问** [6232-6270]："Having too much faith in someone... How do you think that happens to someone, Aunt Niki? If it's true that he's worse than you imagine...do you think he's {i}always{/i} been that way? **Or do you think someone made him into that?**"；
  - **核心闪回：少年 Akira 与"教师"** [6271-6330]：漫画共读→Niki 质问："you've been spending a suspicious amount of time with **your teacher** lately... She picks you up like every single day... **she spends more time with you than your {i}actual{/i} mom.**... **And she's engaged to my brother, so {i}she{/i}'s family too.**... / I just need extra tutoring. {i}That{/i}'s all. / You promise? / **Yes. {i}I promise.{/i}**"——**补习教师=兄长未婚妻=se，每日接送、独处"辅导"**；
  - Ami 判词 [6344-6389]："Not because my dad is evil... Because he's sad. And he'll take love in any form that he can get because it's the only way he can distract himself from the pain of **losing his {i}first{/i} true love.**"（first true love=se）；"If she did, would you think {i}she{/i} was evil?... Then would my dad be evil too if he did the same?"；Niki："I can't forgive anyone who would hurt Akira that way." [6369]；Ami："If he lied, it was only to protect you... I wish I could be as kind as him." [6386-6389]。
- **nikispring6 [6400]**：Noriko 五小时事件后夜（Niki 门外听了全程 [6433-6441]）；**Niki 崩溃审判**：
  - "The same things that were done to {i}you?...{/i} **That turned {i}your{/i} life into a living hell?!**" [6496]；
  - **"Not everything has to be some super deep and complex mental puzzle about you getting molested as a child! And yeah, that was horrible!"** [6530]——童年性侵直接文本；
  - "My parents should've called the cops on **that fucking tutor of yours** {i}long{/i} before she died. But {i}I{/i} told them everything was fine. Because I believed you." [6573]（tutor=se 实锤；Niki 当年的"I promise"使侵害延续）；
  - "while {i}I{/i} was in bed watching Pokemon and painting my nails, **you were in bed with a grown woman, learning everything about life except what's important.**" [6576]；Sensei 辩护："It wasn't like that... **She loved me. She {i}really{/i} loved me.**" [6577]；Niki："her being nicer to you than your mom or your brother doesn't mean she gave you {i}life.{/i}" [6584]；
  - se 死后"狩猎" [6587]（"Started {i}hunting?{/i} Because I wasn't good enough?"）；"I acted on instinct after she died. And my instinct was to leave you behind." [6593]；
  - **自缚请求** [6663-6667]："Chain me up or something, please?... I just can't stop myself, Niki...I cave every single time."（与体内之声 sportswars14、nikiinvite2 预演互证）；
  - 结算：nikiblock=True、niki_love-=50 [6754-6755]；**"This next album...is going to be my last."** [6699]（引退宣言）。
- **nikispring7 [6764]**：Morning Gold 广告第 57 take 失控；Noriko 四分钟谈判 [6858-6984]，其中 [6913-6917]："I'm not going anywhere so long as he lets me near his side... **It's because he needs me. He needs {i}us.{/i}** / He doesn't fucking need {i}us.{/i} That's why he {i}left{/i} us. / **He left us {i}because{/i} he needs us. And that's the single most selfless thing he's ever done.**"（失踪之谜的 Noriko 版最终解）；奴隶条款 [6981-6984]。
- **nikispring8 [7050]**：**Say Anything（1989）举录音机戏仿**（Peter Gabriel "In Your Eyes"）[7062-7090]；律师组 Truman Show 假说 [7082]；"In your eyes, I am complete." [7132]；**"Are you going to keep cheating on me, Akira?"→"...Yes. I am."** [7264-7269]；**催化剂预言** [7274-7275]："there's a catalyst somewhere out there... Constantly telling me that there's a life after this where things are {i}good.{/i} I can sense it somewhere in the depths of my dreams. I have...what feels like {i}memories{/i} of it in the middle of the day."（对循环外未来的类记忆——元层伏笔）；Niki 奴隶化条约+新壁纸自拍 [7303-7343]；chikablock=True [7369]。
- **dormwarssixniki1 [7373]**："Please, call me **Mrs. Arakawa** instead." [7494]；Chika 私谈激将法 [7641-7706]："**None of this would have ever happened if Akira didn't run away from me. Him shattering my heart into a million pieces gave me the spite and the fuel I needed to rebuild myself from the ground up.**" [7696]；"This world needs more idols." [7698]。

### 4.5 Niki 线元叙事点汇总（二轮归纳）

1. **真名系统**：真名 Akira=五禁字；`[[REDACTED~...]]` 屏蔽与 FATAL ERROR [2962-2967]；揭露正点在 nikilovesyou2 [3254-3263]（勘误一轮 md 的 [3547]/[3549]——后者只是 nikilovesyou3 的呼唤）。
2. **Niki 的异常症状**：解离/幻听/自杀念头（nikidate5）＋听见 se 呼唤（beachfive8，sanity-1）——学生外角色中唯一有"理智值"结算者。
3. **性侵真相链（全作核心创伤）**：补习教师=兄长未婚妻=se（nikispring5 [6315]/nikispring6 [6573]）；"molested as a child" 直文 [6530]；Ami"someone made him into that"+"first true love" [6270/6345]；se 死后 hunting→失踪（为救 Niki：dormwarssixmaya1 [9687]+nikispring7 [6917] 双版本互证）→归来。
4. **信件与监狱**：nikilovesyou3 [3295]——数百封信写于 Sensei 亲手造成的"囚禁"。
5. **自杀地点**：nikilovesyou2 [3163-3210] "You jumped... This is where your world was ripped away from you."
6. **作者层**：nikinaming [4016-4039] Selebus/SubscribeStar/游戏名；NordVPN 广告 [6074]。
7. **未来记忆**：nikispring8 [7274] catalyst 预言——Sensei 怀有"循环结束后好生活"的类记忆（与 USER/上层结构呼应）。

