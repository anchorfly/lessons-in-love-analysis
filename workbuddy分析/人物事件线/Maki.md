# Maki Miyamura 事件线全析

> 源文件：`MakiEvents.rpy` ｜ 共 38 个剧情 label（含 3 个电话门控、4 个日常 gen、1 个店铺枢纽）
> 定位：成人用品店店主、Makoto 的母亲、Miku 的照管者，亡夫 Masahiro。她的线是全作对"成人世界的性"最去浪漫化的书写——欲望是货架上的商品、是养家糊口的营生——同时也是母职焦虑、丧亲之痛与元叙事崩塌交汇最深的一条线：从性玩笑起步，经丧夫通知、录像带摊牌与母女决裂，终于"Maki is gone"的放逐判决。她是源文中唯一用 "Are you or are you not attracted to teenagers? Yes or no?" 正面逼问 Sensei 的成年角色（该问句在 `游戏文本/` 全库仅见于本文件），并为此付出了切断整段关系的代价。
> 阅读提示：台词直引为源文英文原文，按所属 label 归属，不标行号。前缀约定：maki=Maki、s=Sensei(Akira)、mak=Makoto、mi=Miku、se=Sekai（Sensei 脑内的亡者之声）、a=Ami、sar=Sara、h=Haruka、os=Osako、r=Rin、mo=Molly、N=旁白。

---

## 一、角色基本盘

Maki Miyamura 在 Kumon-mi 经营一家成人用品店，自嘲 "I make a living selling rubber penises"（makispring2）。她的家庭结构全部可以在源文中逐条坐实：

- **女儿 Makoto**：亲生女儿，Makoto 是她反复强调的"天才"（"I've got a genius daughter to take care of"，sadgirls3）。
- **Miku**：由她照管。sadgirls3 中她说 "There's a reason I call her my second daughter, you know."；makispring1 中她说 "she's been under our wing for a while"（此前 "There was a little back and forth at first"），并明确表态 "I do see her as my daughter too." 源文未使用"收养"一词，但 makispring1 里 Sensei 用 "you *have* been her guardian this whole time, technically" 概括，Maki 未否认。
- **丈夫 Masahiro Miyamura**：sadgirls3 中由防卫队自动语音送达死讯。在此之前，全家一直以"他在外太空"的说法谈他（makidate1 的 "out there in space impregnating an alien-girl"、makiday351 的 "until mine stops fucking aliens"），死讯抵达后 makicamp2 里 Maki 仍在猜他生前是否曾因自己而 "miserable"。

三层世界观中的位置：

- **恋爱表层**：成熟、主动、"The MILF of the Month club"（makispring3）式的戏谑伴侣，约会线充满性玩具、glory hole、spanking 玩笑。
- **重置循环层**：她不掌握循环机制，但两次使用了循环层的词汇——makispring2 里她说 "maybe you just need a reset?"，Sensei 冷答 "Heh...yeah. Because those fix everything."；makispring2 结尾的系统提示则直接宣判："{i}You can't hide the truth from her much longer.{/i}"。她是离真相最近、也被真相摧毁得最彻底的角色。
- **元叙事层**：makinaming 中她直呼 "That's the Lessons in Love guy!"，并宣称 "I'm not real. I'm made of polygons and pixels. Just like you and just like everyone else you know."——恋爱表层角色对玩家层最完整的一次揭穿。

核心矛盾一句话概括：她是全作道德感最强的成年角色，却活在一个人人默许越界的城市里——"Literally no one I know is against this but me."（makispring5）

---

## 二、love 线逐事件脉络

### 2.1 call 三门控与日常生成（callmakimorning / callmakiafternoon / callmakinight / 四个 gen label）

三个电话 label 都以 `makiblock == True` 时拒接开头（"I don't really think I should call Maki right now..."），这条开关在 makispring5 结尾被置为真，是整条线的总闸。

- **callmakimorning**：第四章激活时跳 `makispringmorninggen`，第三章激活时跳 `makisummer2morninggen`，否则无人接听（"Nothing. I guess she's still sleeping."）。
- **callmakiafternoon**：`makidate1` 未发生时才真正接通。Sensei 自报家门 "Hey, Maki. It's your daughter's teacher."，被她反问后约在 Koi Cafe；挂断后 Sensei 盘算要找一个深夜去处，"that isn't filled with porn?"——两句话立住了这段关系的底色：他借"家长身份"接近她，她借"色情业者身份"消解严肃。之后第三章激活则无人接听，圣诞节后走 `makinoongen2`，否则走 `makigenafternoon`。
- **callmakinight**：`maki_love >= 0` 且 `mollycafe1` 已发生且 `makidate1` 未发生时跳 `makidate1`；否则只提示 "Maki should be at work right now. I can probably see her if I head over to the porn shop."

四个日常 gen label 各加 1 点 affection，维持她在商店与家庭间的存在感：`makinoongen2`（咖啡馆午餐，她"撑了整整十分钟才讲出当天第一个黄色笑话"，Haruka 过来训人）、`makinightgen2`（到店里撞见她摸海报，随后带 Sensei 参观 bukkake 区）、`makigenafternoon`（Koi Cafe 喝咖啡，她讲自己高中时的样子，与 Makoto 形成对照）、`makigennight`（店里 Makoto 休息，她推荐 DVD）。

### 2.2 pornshopmaki：整条线的门控枢纽

`pornshopmaki` 不是一场戏，而是 Maki 线的调度中心：它按 `maki_love` / `maki_lust` 与主线进度依次放行 `makidate5`、`makidate10`、`makidate15`、`makihornyquestintro`、`makilust5`、`makispring1`、`makispring3`（以及跨线的 `osakodate20`、`mikulust5`）；无事件可推时，第四章走 `makispringporngen`、第三章走 `makisummer2porngen`、圣诞节后走 `makinightgen2`，其余走 `makigennight`。`makiblock == True` 时它直接拒客。

成人用品店是这条线的入口与主要舞台，但第一次正式约会发生在 Koi Cafe（`makidate1`）。这个错位本身就是声明：这段关系从一开始就跨在"柜台"与"客厅"之间。

### 2.3 makidate1 / makidate5 / makidate10 / makidate15：笑闹中的边界测试

- **makidate1**：Sensei 打电话约她，她反问 "Sensei, are you asking a married woman out on a date right now?"，Sensei 答 "Yes, I suppose I am."。Koi Cafe 里 Molly 误认她是 succubus 并搅局；她自述与丈夫是 open relationship、"he's out there in space"。结尾她岔开话题问 "do you think the red-haired girl is doing okay?"，Sensei 的收束旁白是 "I just need to make sure Makoto doesn't find out about it."
- **makidate5**：Sensei 到店里，她说 Makoto 最近 "seemed really...out of it lately"，并抱怨自己无人可倾诉——"Sara...kind of sucks when it comes to talking about real-life stuff"（一遇到正事就跑），"Haruka...dives headfirst into problems...but she normally spins things to be more about her"。她讲起与 Masahiro 高中同校、后来重逢的经过，并甩出 "Well as long as you're not screwing my daughter, you're free to do whatever you want."，Sensei 还嘴 "Not even with your supervision?"。结尾她决定 "sit down with her soon"，喊出 "It's time for Maki Miyamura's Mom-Mode Mission!"——这条线的母职主线由此确立，并在 makidate10 被回收。
- **makidate10**：她记得上次那场谈话（"you provided some bad advice that made me realize what I *actually* had to do"），Makoto 却对 Sensei 表示毫不知情。Sensei 因此警觉："There's definitely something fishy going on, but I can't tell how much of that is due to the weird reset rules and how much of it is coming from Makoto directly." 这是循环层词汇第一次出现在本线。她还提到 Makoto 退还了她送的圣诞礼物。报酬菜单里可选 blowjob（`makibjx`，设 `makibj`）、可选 "Your daughter's hand in marriage"（被她以 "I'm not going to let you marry my daughter...especially while her father is still away" 挡回）、可选 "An 'upgrade' for the store"——由此提出 "I think you should install a glory hole."
- **makiday351**（购物中心）：信息密度最高的一节。她说 Makoto "seems truly happy for the first time since her father left"。Sensei 说 "Please don't love me. There is not a single person we know who would approve of this relationship."，她回 "Miku might."，Sensei 答 "Miku is on Team Makoto now."。随后是一段玩笑式的自陈：spanking 玩笑引出 "That's what my actual husband thought at first."，再到 "Oh please. She's such a daddy's girl..." 与 "But to everyone's surprise, I'm actually an innocent and pure sub at heart."；紧接一句 "Okay, fine. I was lying."，她自陈缺少实践臣服幻想的机会（"because of my husband's love for spanking and petplay"），再以 "Oh, no. He was the pet." / "We had a leash and everything." 收束。后半段她追问 "You don't actually think I'm a bad mother, do you?"，两人就 open relationship 与 Makoto 的成长环境交锋；她随后坦白 "But...I don't really want to wind up waiting forever."、"I miss my husband. I really do."，并说 "I'm not like Sara or Haruka."，最后以 "Even if my husband does wind up coming back, I hope you'll stick around." 收束。
- **makidate15**：她在店里玩钓鱼小游戏，吐槽 "everyone knows that putting mini games into a porn game is the quickest way to get people to drop it."；Makoto 中途出现打断，随后跳 `makihhgx`。
- **makibjanim / makidoggyanim**：插入约会之间的动画入口，分别跳 `makibjanimx` / `makidoggyanimx`。

### 2.4 makiinvite 系列与 sadgirls3 / sadgirls6：从店铺到客厅

- **makiinvite / makiinvitegen / makiinviteaff**：门控组。`makiinvitegen` 里她自称 "Porn Woman"，坚持 Sensei 得当 "Porn Guy"；到访后菜单给出 Hang Out（`makiinviteaff`）、Doggystyle/Huggystyle（`makidoggyanim`）、Headpat（`makiheadpat`）。`makiinviteaff` 里两人看 porn bloopers 并给演员打分，旁白在此刻把她的开放重新读成创伤——"if you start to view Maki's outlook on all things sexual as more of a desensitization thing rather than a quirky personality trait, it's kind of sad"；结尾 Sensei 承认 "she's a lot more than just...Makoto's mom."（+3 affection）。
- **makiinvite1**：她提着行李箱假扮上门推销的"lotion 销售员"，被 Ami 当场拆穿。她说 "Because I sell fucking porn, not security devices."；Ami 骂 "Get out of my house, you harlot!"，她回 "Harlot? Is this the renaissance? Have some dignity and call me a whore like a normal girl."。Sensei 第一次以家长口吻把 Ami 赶回房间（"Because starting right now, you are grounded."），并把它当作新获得的能力记下。
- **makiinvite2**：她盛装登门，坦白 "Was I...trying to impress you?"。两人差点越线又收住，理由始终是 Makoto（"I'm sure it's just a[school]girl crush...But like...it would break her heart if she found out about it."）。若玩家选择 "I can't do that to Makoto"，结尾系统在照常 +1 affection 的同时给出一条罕见的评语："{i}A string snaps- but Maki's affection still increases to [maki_love]!{/i}" / "{i}Who do you think you're helping?{/i}"。
- **sadgirls3**（丈夫死讯）：全线的第一个转折。她在咖啡馆复述那通自动语音——"Masahiro Miyamura." / "Status: deceased." / "Cause of death: asphyxiation." / "Date and time of death: June 19th, 21:13." / "Remember to smile." / "Transmission over."，并补上 "They waited two months to tell me." / "For two fucking months, my husband has been dead."。她拒绝 Sensei "你也需要哀悼" 的提议，理由是 "I'm the only parent Makoto has left...I can cry when that's done."。Haruka 匆匆赶来道歉时，她说 "I'm really happy for you." / "You had no way of knowing."。同场她解释为什么会照管 Miku："There's a reason I call her my second daughter, you know."。
- **sadgirls6**（清晨造访与驾车）：她不请自来，喝了 Ami 给 Sensei 煮的咖啡。Ami 问 "Would you like me to add a little something to it that will help you sleep better tonight? {i}Much{/i} better?"，她面不改色接梗 "I roofied myself once just to see what it was like."。随后一句 "Want to go for a drive?" 把整条线推上车——这句在 makispring1 结尾会原样重演。车里她坦白 Makoto "hasn't left her room since I took her home on Friday"、Miku 陪住，并说 "Makoto can't see {i}me{/i} without also seeing her father."；谈到 Miku 的过去时她主动切断话题（"That girl's been through enough."）。她以 "free porn forever" 为报酬，把开导 Makoto 的任务交给 Sensei。结尾旁白："Maki leads me up a dark staircase, but it's not dark enough to conceal the array of framed photos hanging on her wall. They've all been turned backwards."
- **makiinv3**：她借"送 Makoto 去做 therapy session"之名上门，实际是让 Makoto 找 Ami 谈。两人谈单亲与失去："your family's been really good at bailing me out lately"；"Knowing that Masahiro is dead completely changes everything even when we've been 'alone' all this time."；"How your worries become amplified the moment you're all someone has left?"；以及那段关于过马路的比喻——"Before my husband died, I'd only look to the left when crossing since that's where all of the cars come from. But now...I look to the right as well. Just to be sure." 结尾 Makoto 与 Ami 红着眼睛出来，Maki 揉了揉女儿的头发。

### 2.5 温泉旅行夜：罪恶感的封顶（makihornyquestintro 区）

- **makihornyquestintro**：起因不是欲望，而是欲望的消失。Haruka 说出 "She's not horny anymore."，Maki 自嘲 "It's dryer than a desert down there."；Haruka 买了三张度假村票（"a bunch of cougars can go silently ogle at younger fit guys and girls"），Sara 因要守酒吧缺席。
- **makihornyquestintrop2**（`makisex`/`harukasex` 均已成立时）：店里后间的三人闹剧。Maki 全程用黑色电影旁白解构场面，最后一句 "Ahh, fuck it. I'm still not feeling anything. Just stop." 把笑闹按停。
- **makihornytrip2 / harumakihornytrip**：度假村。她借 strap-on 把 Haruka 当对象，Sensei 只能旁观；她坦承 "I'm having a blast"，但被追问是否真的被唤起时答 "My nipples are a little hard, I guess. But that's probably just because the AC is cranked up. I'm definitely not wet, if that's what you're asking."
- **makihornytrip3**：love 线最重要的独白在此。她给出真正的理由——Makoto 最近 "genuinely enjoying herself"，加上 "the huge box of condoms I found in her room"，她判断女儿已经在发生性关系；"Now, any time I think about sex at all, I just start thinking about her."。她担心对方是 "some older dude who swooped in to take advantage of her in a time of weakness"。Sensei 的内心在此刻彻底转向："{i}I'm{/i} the man preying upon her daughter in a time of weakness." 与 "This couldn't stay hidden forever. Maki was destined to find out the moment she was forced into a more active role in Makoto's life."。她半开玩笑抛出 "Don't tell me {i}you're{/i} the one Makoto's sleeping with, are you?"，随即笑着收回。她追问 Sensei 是否会想要更认真的关系，Sensei 答 "Ask me again when Makoto's out of high school."，她回 "But if we wait that long, you might start liking her instead! I only have so many years of youthful beauty left!"。收束旁白是全线的判决书：

> My sins will go on to create the longest highlight reel one could imagine...
> And for Maki, it's trusting the wrong people.
> She should have never let me into her home.
> And I know that she'll regret it one day...
> Because, if she doesn't-
> This was all for nothing.

最后一行："And I pause the highlight reel in a room with a deep pink glow."

### 2.6 makicamp1 / makicamp2：露营与 "Love is in the air"

- **makicamp1**：开场独白把 "Love is in the air." 读成空气传播的病毒（"why is {i}this{/i} virus one that we all seem so determined to host?"）。店里，Maki 与 Haruka 劝他别只靠色情麻痹自己；她说 "now that I'm a widow, you can even marry me if you want to take advantage of my health benefits"；她认出 Makoto 当年用推荐信骗她签名的把戏（"She just asked to see my signature and then printed a whole ass form on top of it."）。她提出让 Sensei 带 Ami 去露营；面对 Sensei "I don't know how to be a {i}parent.{/i}"，她答 "That just sounds like parenting, to be honest."，并自嘲 "My parental genius knows no bounds! So long as it involves other people's children and not my own."。结尾 Sensei 在店外撞见 Makoto，把"陪着 Ami"的任务转交给她（"Help her out, okay?"）。
- **makicamp2**：湖边钓鱼。她说 "Masahiro liked fishing. He'd take Makoto out with him from time to time."，并总结 "it's less about being 'one with nature' and more about being 'one with dead husband.'"。两人交换"失去之后如何往前走"的经验："It's going to hurt for the rest of your life. But there are {i}other{/i} things that can keep you grounded."；"No matter what you tell me, I'll never understand the way you saw the person you're referring to. Just like how you'll never understand what I had with Masahiro."。Sensei 说 "I don't deserve to be called a parent."，她立刻驳回："And I {i}do?!{/i} I didn't take up the mantle of 'Mom' until my husband passed away."。她随后表白："It means you can lean on me because I like you. Okay? There. I said it."。结尾旁白："I'm ashamed because I doubt I could ever love her. But I'm regretful to have ever loved at all."

### 2.7 makispring1：dynamite 问题

开篇是店里的闹剧——Miku 把店名改成 "Miku's Cock Emporium" 招揽生意，Maki 解释让 Miku 帮忙是为了 "so she can feel better about taking money from me"。随后她把 Sensei 拉进后间，展示新买的二手"便携式 glory hole"：来自她和 Masahiro 去过的市区性俱乐部，"This thing's been operational for over thirty years now."；她说 "I knew this little sex box before I even knew {i}Makoto.{/i}"，并期待女儿将来也能 "learn that the memory of her father clings to {i}this{/i} as well"。

气氛从这里转暗。她说 Miku 最近让她担心，"Actually had to take her to the hospital recently because-"，被 Sensei 以"学校接到医院通知"打断。她随即给出自己的母职自评："Makoto doesn't need me. She was born smart and had her dad to look up to for most of her life. Miku had me."；"she's been under our wing for a while"；"I do see her as my daughter too. And I've talked to her about sex, but...it's hard to make Miku...{i}understand{/i} things at times." 然后开始自责："Do you think it's {i}my{/i} fault? For...putting them in a situation where sex is so...normalized?"；"The world a child is brought up in...does a lot to determine who they are and...how they wind up."

脑内 Sekai 在此插入："I've watched what you've done to {i}both{/i} of her little girls. Maybe even {i}felt{/i} it."

引爆点是她随口一问："How old were you when you had your first time, Akira?"。Sekai 煽风点火："{i}Booooom{/i} goes the dynamite. You {i}love{/i} opening up about this, don't you?"，并补上 "Finding out you were such an early bloomer might lessen the blow when she finds out you're porking her little girl."。Sensei 语塞，她察觉不对，抛出救命稻草 "Why don't we go for a drive?"，并称他为 "passenger princess"。Sekai 抱怨 "Nooooo, I hate cars! I have such bad luck with them!"，为下一节埋下伏笔。

### 2.8 makispring2：驾车课、Sekai 与崩溃自白

本节是 Maki 线的文学巅峰，也是 Sekai 身份的关键证据链。

- 开场独白 "{i}Hello alone.{/i}"，叙述者自嘲被朋友们不断从内心挣扎中打捞（"How lucky I am to be pulled away from my inner struggles constantly whenever they're around."）。
- 驾车课式的迂回质问：她说不会看不起学得早的人，"I'd think less of the person who taught them."——矛头直指当年"教" Sensei 的人；被点破后立刻退回字面义 "It's just driving, Akira. We're talking about driving."，随即道歉（"I'm sorry. I thought that would make it easier."）。
- 停车场的记忆闪回：她提到一个 "she" 常停车的位置，就在童年住所与 "the one {i}she{/i} made with {i}him{/i}" 之间；"She was larger than life. She was {i}Sekai.{/i}"；"Something didn't {i}always{/i} happen when she pulled into that spot... But many days, something did."；以及那句骇人的总结 "She taught me everything I know." 与 "Now, every single vehicle I lay my eyes on reminds me of her."
- 高墙与逃逸："Guess she figured it out in the end, though. Now, even death can't keep her in one place."
- 界墙下的闲谈从"有没有人在界墙边做过爱"滑向深渊，Sensei 忽然失语："I should have gone..." / "It doesn't matter anymore..." / "None of us are ever leaving this place again."
- 半揭底：Sensei 说 "I still see her, Maki. She follows me. She speaks to me."。Maki 问 "Can she hear me?"，脑内 Sekai 应答 "Loud and clear!"，并替他说出不可说之事："Fucked your daughter like a gazillion times! {i}Both{/i} daughters, actually!"。Maki 的第一反应是 "can I have a minute to think of something really horrible to say to whoever did this to you?"
- 她的回应近乎圣徒："Your past doesn't make you a monster, Akira."；当她试图定性 "That wasn't {i}love,{/i} Akira...That was-" 时被激烈打断；崩溃顶点她喊出 "Whatever you are...whatever you've {i}done...{/i}it's okay...We all make mistakes."
- 收束于循环层暗语：她建议 "maybe you just need a reset?"，他冷答 "Heh...yeah. Because those fix everything."；结尾旁白三连问 "Is this willful ignorance? Is it pity? Or have I effortlessly warped {i}her{/i} definition of 'love' now too?"，最终定格 "It's that I fucking hate driving."。affection 结算之后追加一句判决式预告："{i}You can't hide the truth from her much longer.{/i}"

### 2.9 makispring3：MILF 俱乐部与录像带摊牌

前半是荤段子聚会。开场旁白 "O, mothers and the desire to fuck them."，并交代 "The MILF of the Month club, that is, and all three members of it"——店主本人、"my cool lesbian friend"（Osako），以及 Sensei 这个被拉来凑数的人；Osako 中途退场（"{i}You{/i} guys can have sex since you're actually attracted to each other."）。她还拿刚买的 glory hole 开玩笑："it's been cleaned by a team of professionals too since I know you're afraid of germs."

后半急转直下。她放入一张旧 DVD，片名由 Sensei 念出："After School Service...Student Council Punishment Games..."。她全程用"严肃镜片"看片，并逐步收紧：

- 背景交代："a great deal of them {i}were{/i} in high school. Using fake names and fake IDs to shoot porn and help pay off their parents' debt."；"One of the girls couldn't handle the shame and wound up jumping off of a skyscraper after posting online about it."；"The company that produced the series couldn't come back from that and dissolved shortly after."；"everything that {i}was{/i} made is still out there — marketed as completely legitimate and not at all exploitative."
- 质询："It just feels so {i}weird{/i} to me that some people could consume something that caused someone so much pain and feel so much {i}pleasure{/i} from it."；"no one ever talks about it. Not even those it happens {i}to.{/i} Right, Akira?"；"What I {i}really{/i} want to understand, though, is if you look at my daughter the same way."
- 摊牌："Are you or are you {i}not{/i} having sex with her? Because if {i}you're{/i} not, someone else {i}is.{/i}"；"Especially since {i}you{/i} have been preyed upon. You should {i}know{/i} how big this is. You should know {i}better.{/i}"——她把他的受害者经历与加害嫌疑焊在一起。Sensei 只挤出一句 "What could be {i}worse{/i} than that?..."
- 她也承认自己先前的判断反复过："If it makes you feel any better, I decided you {i}didn't{/i} well before that. That's on me, though. And I will have to live with that forever."

### 2.10 makispring4：母女决裂与 Miku 替罪

摊牌被撞破。Miku 先以旁观者口吻点破现场："Maki broke out the Makoto doppelganger sex tape and is now watching it alone in a room with Sensei. This is probably weird, but I don't know why." 随后是全作最长也最狠的母女对骂：

- Makoto 控诉："You're watching fucking {i}porn{/i} with my teacher! {i}That's{/i} your best?!"；"Which makes {i}you{/i} the most abusive person I know now! And you didn't even have to fucking touch anybody to get there!"；"Don't fucking blame it on {i}teaching{/i} when it's thanks to {i}you{/i} that I learned what fucking sixty-nining was before I could even {i}count{/i} that high!"
- Maki 彻底崩溃："AAAHHHHAHHHHHH!!!! WHAAAHAHAHHAHHHH!!!!!!!" / "I'M...S...SORRYYYYY!!!!!! I'M...A BAD...MOM!!!!!!!!!!!"
- Miku 打圆场："You're just as much my mom as you are Makoto's."；"There ain't nothin' he coulda done that you can't, Maki." 而 Maki 哭着说出："I know I...try to be open and...teach you girls about all this stuff...I don't want you...to be like me..."
- Makoto 试图自白，只开口一次就被 Miku 打断：mak "Mom, I..." / "Well, Sensei and I..." / "We..." → mi "I have an older boyfriend!"。Miku 编造了一个网上认识的年上男友，把"broken vagina"的责任揽到自己头上："He ain't a bad guy, but...he probably shouldn't be porkin' a high schooler."
- 姐妹私下复盘：mak "Miku, what the fuck was that?" / mi "Lyin's friggin' hard."；mak "She'll see through all of the holes in your story soon if she doesn't already." Miku 则催她 "go apologize to your mom"。
- 本节结尾是全作最著名的 meta 文本之一：先是 Sensei 的 "she know She Knows she Knows {b}she KNows{/b} ... {b}SHE KNOWS{/b}."，随后四行——

> N: I cry. / I sleep. / I dream. / You watch.

"You watch." 是对玩家的直接点名——你在观看这场崩塌。系统同时给出一条反讽式结算："{i}Miku's affection has increased to [miku_love] as she was the only one not really negatively impacted by where you were and what you did last night!{/i}" / "{i}Congratulations! At least it's something!{/i}"

### 2.11 makispring5：审判与放逐

开场忏悔室式独白是叙述者写给玩家的遗书式文本："And the same thing I hope you feel when you feel the way I feel."；"Red dresses to match each sentence, or her eyes, or the color of the sky when the reckoning rolls in and you are forced to confront not your demons but mine."；并以一个问题收尾："If you were me, and you knew you were wrong, and someone else knew you were wrong, would you tell them you are wrong? Or would you ask why they asked at all?"

随后 Maki 带 Sara 上门做最后的对质（Ami 见到她的第一句是 "Oh, I know. I just don't like you."）：

- 直接定罪成立："You're attracted to teenagers. Aren't you, Akira?" → "Just answer the fucking question. Are you or are you not attracted to teenagers? Yes or no?" → Sensei："...Fine. Yes. Yes, I am."
- 孤立无援的世界观：Sara 听后的反应是 "Well, duh. He's a boy."，追问的是 "How does Makoto feel about it?"；Haruka 的反应被她评为 "somehow even worse"，于是有了那句核心台词 "Literally no one I know is against this but me."
- 她早已识破 Miku 的谎言："And then {i}Miku{/i} started going off on some ridiculous made-up tangent about a secret online boyfriend she's been having sex with"；"Because I already know you're the 'secret online boyfriend.' And I'm hoping you have the balls to come clean about this too."
- 她预先演练了两种结局：要么长篇控诉后永不宽恕、"ask that you stay away from both of my girls for as long as you live"；要么 "I sit here while my eyes swell up with tears and my jaw drops as my heart tears into a million tiny pieces."——"I can't tell you which one will happen either."
- Sensei 拒绝回答，把皮球踢回 Makoto，只留下一句 "Please don't hurt her..." 与最诛心的比较："So how did {i}you{/i} come out on top? Why are {i}you{/i} the one she looks up to when {i}you{/i} don't even try?... You're even weaker than me...I don't understand it."
- 她自陈："I've cried more in the last twenty four hours than I did after Masahiro died..."
- 判决下达："I'd appreciate it if you'd stay away from my store, my daughter, and me until I can figure that out." / "Goodbye, Akira."
- 而他转身拨通 Makoto 的电话："Are you free right now? Ami just left." → "I'll be right over."。旁白以斜体收束："{i}Someone I will not be kept from.{/i}" / "{i}Someone you can not hide from me.{/i}"，Makoto 的 affection 与 lust 同时上涨，最后一行只有四个词："{i}Maki is gone.{/i}"。同一时刻 `$ makiblock = True` 生效，此前所有"打电话/上门"入口全部锁死。

---

## 三、lust 线概貌

Maki 的 lust 入口分两路：一是 `pornshopmaki` 在 `maki_lust >= 5` 且 `yasuspring3` 已发生时放行 `makilust5`，其后紧接 `makinaming` 的命名流程与 `endofmakinaming`；二是 `makiinvitegen` 菜单里的 Doggystyle（`makidoggyanim`，跳转 `makidoggyanimx`）与 Headpat（`makiheadpat`），另有 `makibjanim`（跳转 `makibjanimx`）。

**makilust5 / makinaming / endofmakinaming：命名游戏与那句"我有个女儿叫 Makoto"。**
Sensei 只想买一部"正常"的片子，Maki 一路用 watersports、"mindless rimming"、"Totally Anal Volume 19" 搅局，最后以"教学"为名在店里发生肛交（endofmakinaming）。中途她让 Sensei 自选床上称呼，输入不同名字会触发不同分支：

- 输入 "makoto"：maki "Akira — you might not know this about me, but I actually have a daughter named Makoto." → "Which would make calling you her name during sex very uncomfortable for me."（这段常被误读为"刻意嵌套"，其实是源文写死的一个拒绝分支。）
- 输入 "masahiro"：她拒绝，"I'd kind of like to keep that name tied to my husband for a few reasons."——第一条是"I don't want my memories of my husband to fade"，第二条是"Makoto 若听见会如何"。
- 输入 "selebus"：她认出 "That's the Lessons in Love guy!"、"the hit dating sim with way too many words and way too few lizards!"，并在 Sensei 坚持后说 "Yes, but {i}I'm{/i} not real. I'm made of polygons and pixels. Just like you and just like everyone else you know."，系统随即以全屏大字 "PICK A NEW NAMEEEEEEEEEEEEEEE" 强制玩家重选——这是全作对"命名权"最直白的一次元叙事玩笑。
- 事后她说："You know I'm like...{i}actually{/i} into you, right? That this isn't just a sexual thing?"

**职业喜剧素材。** 性被处理成可谈论、可消费、可玩笑的日常：makidate10 里 Sensei 提议装的 glory hole；makispring1 里她买下的二手便携 glory hole（"operational for over thirty years now"）；makispring2 里她随口问 "I wonder if anybody's ever had sex up against the barrier?"，并邀 Sensei 去市区性俱乐部（"You'll get in for free if I bring you along."）；makispring3 里那句 "it's been cleaned by a team of professionals too since I know you're afraid of germs"。这些场景共同维持"性与金钱、母职共存于同一间屋子"的设定压力——从而让 spring 系列里同一个"性"字的另一副面孔（JK 产业、真实高中生、跳楼的女孩、解散的公司）显得更加刺目。

**lust 线的另一功能是掩护。** `makihornyquestintro` / `p2` 与 `makihornytrip2` / `harumakihornytrip` / `makihornytrip3` 把大量篇幅花在"如何让她重新想要"的性冒险上，使玩家与 Sensei 一样习惯性地低估 Maki——直到 makispring3 的录像带亮起，才揭示此前所有 lust 场景都与她此刻的指控同源：她卖了一辈子的东西，正是她最害怕落在女儿身上的东西。

---

## 四、与主线/元叙事咬合点

1. **Sekai 实名**：makispring2 的停车场闪回明确写出 "She was larger than life. She was {i}Sekai.{/i}"，紧接 "She taught me everything I know."；同节脑内之声 se 具备应答能力（"Present!"、"Loud and clear!"），Sensei 自己也承认 "There's all sorts of weird supernatural shit happening here every single day."——幻觉与超自然的边界被刻意模糊。
2. **reset 暗语**：makidate10 里 Sensei 把 Makoto 的记忆缺口归因于 "the weird reset rules"；makispring2 里 Maki 无意识地说出 "maybe you just need a reset?"，Sensei 的 "Because those fix everything." 是只有玩家侧才听得懂的黑色幽默。同一节结尾系统追加 "{i}You can't hide the truth from her much longer.{/i}"。
3. **polygons and pixels**：makinaming 中她指认 "That's the Lessons in Love guy!" 并宣称 "I'm not real. I'm made of polygons and pixels. Just like you and just like everyone else you know."，随后系统强制玩家重选名字——恋爱表层角色对玩家层最完整的一次揭穿。
4. **"You watch."**：makispring4 结尾的四行把镜头责任交还给玩家，与 USER 层的窥视结构直接对接。
5. **数值系统的恶意**：绝交判决的同一瞬间，系统弹出 Makoto 的 affection/lust 上涨公告，并把 `$ makiblock` 置真——引擎用 dating sim 的奖赏语法为主角的背叛颁奖，随后一句 "{i}Maki is gone.{/i}" 完成对整套机制的嘲讽。
6. **名字的互相驳回**：makispring2 中 Sekai 喊出 "Fucked your daughter like a gazillion times! {i}Both{/i} daughters, actually!"，把 Makoto 与 Miku 一并点名；而 makinaming 中 Sensei 想让 Maki 在性行为中叫他 "Makoto" 时，被她以 "I actually have a daughter named Makoto" 驳回。两个"女儿"的名字在同一条线上被反复调用，母职焦虑因此成为整条线伦理张力的支点。

---

## 五、未解伏笔

1. **Masahiro 之死的细节**：源文给出的只有那四行自动语音（asphyxiation；June 19th, 21:13）与"他们等了两个月才通知"；他如何死、死于何处，正文始终不提。死讯到来前全家一直以"他在外太空"的玩笑谈论他，makicamp2 里 Maki 仍在猜他生前是否因自己而 "miserable"。
2. **"She should have never let me into her home."**：makihornytrip3 的叙述者已预写 Maki 的结局——"I know that she'll regret it one day"。但"上一次"发生了什么，正文不提。
3. **Miku 的"网恋男友"谎言能撑多久**：makispring4 里 Makoto 预言 "She'll see through all of the holes in your story soon"；makispring5 里 Maki 明说 "And then {i}Miku{/i} started going off on some ridiculous made-up tangent"——她已经识破，但对 Miku 的清算悬置在线外。
4. **Makoto 那句没说完的自白**：makispring4 中 Makoto 只开口一次（"Mom, I..." / "Well, Sensei and I..." / "We..."）就被 Miku 打断——母亲至终没有得到女儿的亲口承认。
5. **界墙之外**：makispring2 里她说自己只去过一次京都（"Kyoto for a field trip once."），并提出 "for all {i}we{/i} know, everything else could be gone already."——世界尽头的设定在她口中说得比任何恋爱表层角色都明白，却无人验证。
6. **"until I can figure that out"**：放逐是有期限的判决。她保留了一个未定义的"然后呢"，这是 Maki 线唯一的活扣。

---
> 按源行号检索本角色 label，见 `索引/Maki索引.md`。
