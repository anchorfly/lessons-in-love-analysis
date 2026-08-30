# Molly 事件线全析

> 源文件：MollyEvents.rpy ｜ 共 31 个剧情 label
> 定位：宅系中二的外来者——爱尔兰转学生、咖啡店夜班店员、漫画社社长兼 D&D 主持人。她用游戏黑话包裹一切真实情感，把恋爱理解为「route」，把失恋理解为「debuff」，并反复把自己钉死在「NPC」这个位置上。她的 love 线是一条从「自我物化」走向「主动求偶」的缓慢升级之路，而每一次升级都被元叙事层的旁白标注为玩家的又一次堕落。
> 阅读提示：台词直引格式为 `> 前缀: 英文原文`；mo=Molly、s=Sensei/Akira、a=Ami、h=Haruka、t=Tsuneyo、ni=Niki、f=Futaba、r=Rin、sa=Sana、ay=Ayane、m=Maya、w=Wakana、os=Osako、tb=Tsubasa、mod=Molly 之父、emp=店员、N=旁白。全文以 label 名为唯一锚点。

## 一、角色基本盘

Molly MacCormack 的身份底色是「永恒的异乡人」。她是爱尔兰人，在 Kumon-mi 被店员反复用「Nihongo jouzu desu ne」提醒自己不属于这里；而在故乡爱尔兰，她同样是被围观、被嘲讽、被借五镑不还的局外人。母亲早逝，留给她的遗产是一柜子童话书与对 fae（妖精）的信仰；父亲独自把她养大，是「Are ya winning, son?」式的笨拙暖男。

她的一切性格机制都围绕三层防御展开：

- **游戏化翻译**：把熬夜说成「long rest 会变成 short rest」，把心碎说成「resurrection sickness」，把散步说成「side quest」，把性爱说成「power-leveling」。语言即护甲。
- **中二自设**：称 Sensei 为 Supreme Overlord / Herald of the Adolescents，自称 Emerald Guardian，给 Tsuneyo 起名 Kendo Princess，给 Haruka 起名 Magistrate of Mammaries，给 Futaba 起名 Sword-dancer of the Seven Suns。她甚至给脑内那个让她脱口失言的声音起了名字——Siobhan。
- **NPC 自我定位**：她坚信自己是别人故事里的背景板。在 mollycafe30p1 里她说得最完整：「What do you get for falling in love with an NPC? They never change.」／「Sir is the protagonist and I'm just a stepping stone.」／「Best chance I have is to wait for a fandisc that makes all the background girls like me more appealing to the masses.」这句自我认知既是笑点，也是全事件线的悲剧引擎。

同时她毫不掩饰自己的欲望属性：「I'm a pervert, Sir.」是她的自我宣判。她的插入式经验几乎全部来自玩具——「most of my penetrative experience comes in the form of toys」——这使她在 love 线中的每一次真实接触都具有「初体验」的重量。

## 二、love 线逐事件脉络

### 电话门控（callmollymorning / callmollyafternoon / callmollynight）

这三个入口都不是「打通电话聊天」，而是三种打不通：早上她还没醒，旁白判定「I guess she's still asleep」，把玩家踢回 callmorning；下午她接了，但一句「These are gaming hours」把 Sensei 挡在门外，还说要再刷二十次坐骑才可能腾出时间；晚上则分两种——咖啡店还没打烊时提示「Molly is working right now」，打烊后拨过去无人接听。此外三个入口都先检查 Sensei 自身状态：senseisad 为真且 saracamp2 未完成时直接放弃拨打，mollysad 为真时 Sensei 只回一个「No.」。chap4 生效期间，早晨入口改跳 mollyspringmorninggen（chap4generics.rpy）。

### 咖啡店阶段（mollycafe1 → mollycafe20）

**mollycafe1** 是 Sensei 第一次夜里进店。Molly 以「Greeting and salutations, Supreme Overlord!」开场，用「I can't be equipped until much later into the game.」把自己物化为未解锁的装备。她把 H-Scene 解释给 Sensei 听，被追问时脱口而出「REAL LIFE IS STUPID! THERE'S NO BACKGROUND MUSIC OR TSUNDERE CHARACTERS! JUST NTR AND PREGNANCY!」。她当场求收养、求当她的新父亲，并宣称 Ami 是「Cult of Molly」的忠实成员。她也承认自己「不常和活体男性建立联系」，并主动挑明年龄差（bonus 分支）：「Even if you are three times my age.」

**mollycafe5** 里她躲在柜台后玩音游，被抓包后喊出「I DIDN'T DO IT, I SWEAR!」。本段最要紧的是她的「扶梯人生哲学」：「And so I, Molly MacCormack, have vowed to live a life on the escalator.」——不爬楼梯，站着等一切经过。她同时给出逃避现实的机制性自白：「Real life is hard...The progression system is hidden...and you can't even check your affection scores with everyone.」她一边嚷着要当「lead heroine」，一边承认「I would be a horrible girlfriend if it actually came down to it.」

**mollycafe10** 中 Rin 与 Futaba 闯入，揭穿 Molly 其实是漫画社社长、Futaba 是副社长（她此前曾向 Sensei 装可怜说自己很难被社团接纳）。Rin 与她以「宿敌」互称，Rin 吐槽她「把所有点数都加在魅力上」。Molly 在此正式提出：假期要开一次 D&D one-shot，并邀请 Sensei 加入（他最终只答应旁观）。

**mollycafe15** 是冬夜店门外的长椅。她讲爱尔兰「见新月要祝福自己」的迷信，讲「在爱尔兰人眼里，我们就像矮人和哥布林一样被贴标签」，讲自己「进屋总忘了脱鞋」「不知道该怎么叫服务员」，结论是「If life's a game, I'm basically playing on the hardest difficulty right now.」。她直接问出「Am I on the Sensei route already?! Are you in love with me?!」，得到「I'm not in love with you.」，随即自嘲「F's in chat for the Irish girl.」。结尾她把 Sensei 定义为「一个差劲透顶、却让身边每个人过得稍好一点的老师」，并邀他「Onward to Valhalla」。

**mollycafe20** 是 D&D 团正式开场。六人角色对应为：Sana＝Zagull Throat Spear（断臂）、Rin＝Nithhala（tiefling）、Ami＝Arborea（法师）、Maya＝Urrheak（aarakocra，只会「Bacawk」）、Futaba＝Xessaxia（satyr，别称 Sword-dancer of the Seven Suns）、Ayane＝Lidearel（扒手）。Tsuneyo 在场但没有角色，她自称阵营是「noodle evil」，被 Molly 纠正为「Neutral evil」，后来又被她判定为「True noodle」，理由是「我还不能上场玩」。剧情推进到港口城市 Frostford，队伍进酒馆前撞见一名持金匕首的半精灵女子，她尖叫着「Thaum is coming」，随即当众变成蘑菇，Molly 宣布：「The woman suddenly turns into a mushroom. Go ahead and roll for initiative.」Sensei 与 Tsuneyo 有一段关于骰子的对话，Tsuneyo 说：「Perhaps there is a certain ingrained desire in all of us to allow chance to rule our lives?...So that we do not have ourselves to blame when things don't go our way.」随即自己推翻：「Or maybe they just like dice.」

Sensei 提前离场，理由是「This sort of thing just isn't for me.」。Molly 试图挽留：「There are plenty of things I never expected to like that I absolutely love now...And I never would have known that if I didn't give them a chance.」（bonus 分支里她补了一句：那些东西「全都是同人志的不同标签」。）即便如此，旁白照旧冷冷弹出「Molly's affection has increased」。

### Rin 心碎之夜（mollycafe25 / mollycafe25p2）

**mollycafe25** 开场，Molly 打烊后对着吧台同一块地方擦了十分钟。她先用游戏隐喻自我诊疗：「my long rest is going to turn into a short rest and I'm not even going to recover all of my hit points.」随后给出核心定义：「This whole thing with Rin is like a bout of resurrection sickness. For a little while, everything is going to hurt a lot more than normal.」她承认最难熬的不是 Rin 和别人在一起，而是尴尬——「It's the embarrassment of what happened.」她拒绝逃避情绪的劝告：「I {i}deserve{/i} to feel down right now.」最后她把 Sensei 留下摆椅子，并要求他送自己回家。临走前有一段中间名玩笑（bonus 分支）：她先反问「Is my name Molly Medb MacCormack?」，被猜中后纠正「Wrong! It is Molly Moyra MacCormack!」，Sensei 答「It wasn't in your character profile.」

**mollycafe25p2** 是步行回宿舍的一段。两人穿过 Otoha 常去的公园、路过她的长椅，Molly 在此举行了一场面向 fae 的祈祷：「Arise, spirits of the night! And to arms, my fae companions!」Sensei 问她既然不确定对方存在为何还要说话，她答：「I've spent most of my life talking to things that aren't really there in the hopes that...if they {i}are{/i}, they'll know I believed in them.」

本段的核心是母亲的记忆。她讲出 Tír na nÓg——「the Land of the Young」——一个无人死去、永葆青春的彼岸，并说：「One of those people was my mother.」她记得的不多，只记得母亲临终前念过的那一堆童话书，那是「her way of communicating」。紧接着是全线情感谷底，她把败因归为外貌与属性点分配：

> mo: If I was...prettier or...cooler like someone like Chika or Otoha, you and I wouldn't be on this bench right now.
> mo: I'd have won.
> mo: But I made the executive decision to put all of my stat points into categories that didn't matter as much as aesthetics to some people.

Sensei 安慰她「现在改还来得及」，她给出全书最锋利的元叙事回答之一：

> mo: But, Sir...you {i}have{/i} to say that.
> mo: You're the protagonist.
> mo: It's your job to make us feel loved or wanted.

她还拒绝承认圣诞节与 Rin 的吻是初吻：「as far as I'm concerned, I still haven't had my first.」——为将来把「第一次」留给 Sensei 埋下结构性伏笔。末尾她以一句爱尔兰语骂他收场（「Go dtachtfadh an diabhal thú!」），被他用胡乱发音学舌，两人笑场。

### Haruka 晚宴与客厅摊牌（mollycafe30p1 / mollycafe30p2）

**mollycafe30p1** 以一段赤裸的叙述者「鱼钩」独白开场。他自陈只给玩家看「最重要的部分」，并连珠质问观看者：「Do you like it when I strip myself of special text?」／「Do you like it when I make your screen flash?」／「Do you like it when I lead you into dark rooms with exchange students and award you affection points under the pretense that you will use them to get your dick wet?」，末句挑衅「If it doesn't, you can always jerk off into a sock.」，署名「- One of the narrators, or Sensei, or Selebus, or a bug, or something else, or all of those things, or you.」，最后问：「How does the hook feel nestled in your jaw?」

紧接着是一段闪白改口的黄色插曲：Molly 一句「that's the story of when I let fifteen dudes fuck me in one night!」被 Haruka 接上，画面闪白后同一句被替换成「solo'ed fifteen group-bosses in one night」。

Haruka 请客，名义上庆祝 Molly 独自撑过一个大夜班。席间她逼问 Molly：若现在要和谁谈恋爱会选谁。Molly 答「Probably...the Herald of the Adolescents...」，随即陷入 NPC 式自我否定（引文见第一节）。段末旁白点题：「she got my hook caught in her mandible.」／「her only options at this point are to either wait for me to free her- Or to be captured and consumed.」／「Because you're the same as her.」／「And I love the way you taste.」

**mollycafe30p2** 是送醉酒的 Haruka 回家。Haruka 在床上呓语「Just......like that.........Tsuneyo.....」，接着一句「It's okay...you can bite it, baby...it won't hurt me...」，Molly 落荒而逃并宣布「What happens in my boss's room stays in my boss's room」。

摊牌发生在 Haruka 家客厅。Molly 追问「到底是什么让我和别人不一样」，Sensei 说出那句关键台词：「But none of those people ever took advantage of you while you were unconscious in a dark room.」Molly 立刻截断：「{i}Stop going back to that.{/i} It's over.」，随后又软化：「Let what happened in the dark {i}stay{/i} there...It doesn't matter if it was the worst thing possible or nothing at all.」她说，如果今天再走进那样一个房间，「there is no one I would rather have follow me in than you. Or maybe Felicia Day.」然后发问：

> mo: Sir, answer me honestly-
> mo: If I were to make a move right now, how would you react?
> mo: Because I'm going to.
> mo: And this is the part where you make a decision that changes the rest of our relationship.

菜单只有一个选项「Rape her」，选中后画面闪白，而 Sensei 的实际反应是拒绝并逃走：「I think you should sleep here tonight. I can't walk you home.」／「You never got to say no.」留下 Molly 独白：「Can't you see this is exactly what I meant when I put you before everyone else?...As if any of the others would ever look that way for me...」以及「Why do humans have to be so hard?...」

之后 Sensei 在公园长椅上用一连串自我开脱说服自己：「She didn't mean that. She's confused. She doesn't know what she wants. She's just a hormonal teenage girl.」随即反问「But if that's true...What is it that makes the others different?」结尾：「The hook under my desk reels me back to safety and I don't have to run at all.」／「I end the night by jerking off into an orange sock.」本段还会推进一天，直接接 mollydate35p1。

### 试衣间与电车（mollydate35p1 / mollydate35p2）

**mollydate35p1** 次日清晨开场，Molly 用一通《魔兽世界》血精灵语电话强行重启关系：「Bal'a dash, malanore! Doral ana'diel?」／「Anar'alah, Sir!」／「Shorel'aran, Sir!」，把娱乐区称作「Silvermoon / Eversong Woods」。她要 Sensei 陪她去买 cosplay 服装，逻辑荒谬却自洽：「The fact that you are so wholly opposed to physical contact with me at this point makes you the {i}perfect{/i} dressing room partner, Sir!」她甚至预先豁免一切后果：「But, on the off chance you do, I consent to everything. Now, no one has to feel guilty if anything does happen.」

途中埋下 Haruka 衣橱伏笔：Sensei 追问 Haruka 昨晚对她说了什么，Molly 答「Nothing. But, if she happens to ask about anything missing from her closet, I was never there.」试衣渐入暧昧，她问「Would you mind maybe...helping me take this costume {i}off?{/i}」，被质问说好的纯柏拉图呢，她答「I'm a pervert, Sir. I tried.」Sensei 承认被吸引但请求时间：「I just need a little more time, Molly.」

**mollydate35p2** 在返程电车上。车厢拥挤，两人被挤成贴身姿势，Molly 低声说「Oh God...I'm in one of {i}those{/i} games.」，并下达指令「This is the part where you stay still and discreet or the game ends. I have experience. Trust me.」到站后她冲进厕所自救，解释道：「We just came way too close to fulfilling a lifelong fantasy of mine and I need several minutes to myself before we're both arrested for public indecency!」

菜单只有一项「Don't do sex (Now fully implemented!)」，Sensei 照例选择「I think I need a little more time.」。Molly 进厕所后撞上 Wakana 与 Osako 的私会现场，双方达成「Neither of us were ever here and we never speak about this again.」的默契。出厕后 Sensei 问起 Molly，Wakana 连续两次以同一句话替她圆场：「I have never met anyone who goes by that name before.」段末旁白承认：他离「再一个 dark room、再推一把」只差一步。

### 露营来电（mollycamp1）

Sensei 带 Ami 露营期间主动打电话给 Molly——他极少主动联络她，Molly 说「It's been so long that I was taken quite aback when I saw Arthas Menethil's name pop up on my screen just now.」（她把 Sensei 在手机里存成这个名字。）她一度以为自己产生了幻觉：「I believe my delusions of grandeur may have finally begun rewriting reality in a way that causes me to overwrite actual dialogue with what you'd say as a character in a dating sim.」

通话时她和 Tsuneyo 在游戏厅，Tsuneyo 配合她的「心灵感应」玩笑（「I must listen closely so the sounds are not muddled by various action games.」）。他说出那句：「I just wanted to hear your voice.」随后向这位「由单亲父亲养大的孩子」请教如何当父亲，得到答案：「It's to be mindful of her wants and needs...and to always keep her in your heart and mind.」挂断前她说「I miss you.」，旁白以粗体大字收尾（配 apollotheclown 画面）：**someone who will lend me everything**。

### 游戏厅约会（mollyspring1）

本段开头是全书最露骨的内心声音内战。Sensei 刚拨通电话就脱口而出「Good morning and get ready for the penis.」随即挂断，斜体旁白接管，声称「it was a joke about that time you raped her.」，两个声音就「谁在想谁的念头」争吵不休，旁白自陈「i'm not even real. OR AM I?」。Molly 给自己的内在声音命名为 Siobhan：「The entity commanding my every thought is named Siobhan. It is {i}her{/i} fault I am the way I am, not mine.」Sensei 则称自己的那个为 Pareidolia（他试图命令它「Teleport me home now, Pareidolia.」）。

约会地点是游戏厅——Molly 提醒他，这其实是「you said you wanted to do something nice for me since you've yet to pay much attention to any of my hobbies」。途中她讲了一段「hidden flags」的游戏术语，源文在此埋下变量 hiddenmollyflagwhatdoesitmean，注释写着「shhhhhdonttellakiralmao」。她也坦承：「years worth of dating sims don't prepare you for the nerves you experience when communicating with actual humans!」

段末她说出比任何告白都惊心的愿望：

> mo: It is nice to be cherished, yes.
> mo: But sometimes I wish that you'd just break me already.

她自己也点破了根源：「It's because of Halloween, isn't it?」／「Put it behind you, Sir.」最后一句是「Come back to the dorms with me. We can do something for {i}you{/i} next.」

### 魅魔之夜（mollyspring2）

目的地是 Molly 的宿舍——她解释 Touka 出资给她的房间做了隔音，因为她的尖叫影响对方睡眠。她让 Sensei 闭眼，换装后自报家门：「You see before you Yrelixis, Succubus of the Void — experienced satiator of ten thousand lusts.」（同一场里这个名字也写作 Yrlexis。）她把整场性爱包装成角色扮演，并在开演前刻意要求口头同意：「Also, please provide verbal consent so as to prevent any more misunderstandings.」——直接回应万圣节旧创。love 线的首次真实性接触由此完成（口交）。

事后旁白急转直下。Molly 问「How do I look? Like a degenerate?」，Sensei 嘴上答「I don't think you've ever been prettier, Molly.」，内心却承认那是一句谎话：「In the act, she was beautiful. But now...all I see is the inability to ever {i}truly{/i} abstain from anything.」并把病态审美推到极致：「How they're pretty when they're touching me- But prettier when they're locked inside of their rooms.」系统提示「You have also unlocked the dorms again!」，旁白补刀：「Now, you can go back to hurting little girls whenever you want.」Sensei 道晚安时依次向观众和内在人格道别：「Goodnight, audience.」／「Goodnight, Wilford Blackhole Hands.」——后者回以「Hi-yah.」并给了他一巴掌，他整晚都在挨打。

### 学 D&D 与「变回 loser」计划（mollyinvite1）

Sensei 主动邀请 Molly 来家里。动机当场被自己拆穿又否认：「Molly's cute and I want to put my penis inside of her.」→「Just kidding. I simply want her to be happy.」→ 斜体补刀「{i}I'm not kidding about wanting to put my penis inside of her, though.{/i}」。表面上的名目是「学 D&D」，Molly 从种族、职业讲起，Sensei 张口就要当「a bird-man warrior from Tokyo who kills the demon lord」，被她判为「你全都有答案，而且全都是错的」。

意外爆点来自 Niki。她端咖啡进来，顺口爆料：「he and I used to hang out in my room watching mech shows and playing Dragon Quest all day.」Molly 当场尖叫「THE SUPREME OVERLORD HAD AN OTAKU PHASE AND I NEVER KNEW ABOUT IT?!」，而 Sensei 对那段童年记忆一片模糊：「Everything from back then is...still kind of blurry to me.」Niki 补上一句「I might still even have one of our old save files on a memory card back at my parents' place.」Ami 追问「你和 Niki 阿姨小时候做了什么」，被双方同时叫停（「I'll tell you when you're older.」）。

Molly 因此爆发存在级震撼：「All this time, we had that thread in common...just obscured by the passage of time and the onset of shame.」她当场撕掉刚建好的角色卡（「Your character has been scrapped! ... YOU ARE NOT PREPARED!」），并宣布新使命。旁白记下：「She wants to turn me back into a loser.」

### 黄油双修（mollyinvite2）

Molly 带着一台装满黄油游戏的笔记本电脑上门：「In this bag, I possess a laptop with so many porn games from so many genres that Jesus Christ would cast me to Hell the moment he stepped within one hundred miles of it.」她提出 cum meter 理论——「The white bar in the bottom right hand corner of your screen that slowly fills up over time and needs to be emptied by a sexual partner or masturbation.」她随即澄清自己的动机不是「desperation」：「Because you stopped doing something that made you happy.」最终幻想成真：两人边玩黄油边互相解决，她的终身幻想被逐字说出——「I may or may not be exceedingly close to fulfilling my lifelong fantasy of playing porn games with someone I like while we...both masturbate and fully immerse ourselves in our delusional perversions?」

本段的另一核心价值在 Sensei 入户前的「龙巢」独白。他把每个来访的女孩都视为闯巢的冒险者：「She feels like it's her duty to conquer me. But she doesn't realize she's not strong enough yet, so it'll have to be a learning experience.」并收束于「But it's better me than someone who will pick her bones clean.」／「Dragons must eat too.」

事后系统提示连环轰炸：Molly 解锁为 Invite 角色；然后「That's right, Akira! You've once more fulfilled your only purpose on this planet and ejaculated all over some helpless girl! Great job!」；affection 与 lust 各 +1；最后「Upon reaching 500 headpats, Molly MacCormack will-」被 Sensei 一句「Oh, fuck it. Goodnight.」掐断。

### 森林与命名（beachsixmolly1 / mollysexnaming / endofmollysexnaming）

海滩篇中，Molly 把野外性爱设计成一场「Mystical Breeding Forest」的 NPC 循环台词剧——她的原话是「one of those NPCs you find in indie porn games that repeat the same phrase over and over as their bodies are used passionately and violently to sate the lust of a rampant hero」。她先交底：「most of my {i}penetrative experience{/i} comes in the form of toys that...don't quite measure up to your...{i}Skill level...{/i}」Sensei 则宣告：「I have had a very rough month. And I intend to make you feel every last bit of that before you exit these woods.」性爱被明确定义为「power-leveling」——她解释这个词的含义后，他答：「Oh, then yeah. That's exactly what I'm doing here. We're going to max out your sex level or whatever. Sound good? Good. Take your swimsuit off.」

**mollysexnaming** 是一个自由输入的小游戏：玩家输入什么，Molly 在性爱台词里就用什么称呼他（存进变量 [mollymaster]）。源文为几组特定输入写了专属分支：

- 输入 **Molly**——被她以「文化挪用」为由驳回，并举例「如果我和另一个欧洲人生了孩子、给他取名 Akira 不是很怪吗」，被 Sensei 反呛「I'd like to congratulate you on the birth of your fictional son.」，跳回重新输入。
- 输入 **Rin**——她当场慌乱，承认这个名字「对我的性癖有相当重要的意义」，并坦白「I have also imagined what it would be like for {i}girl{/i} Rin to have a penis as well!」
- 输入 **Tsuneyo**——她以「怕将来三人一起时会混淆」为由拒绝，跳回重新输入。
- 输入 **Haruka**——她先问是不是两人串通好来气她，随后承认「I'd be...lying if I said I hadn't...{i}thought{/i} about it before. Several...times.」
- 输入 **Sir**——最温柔的一支。她说「I always kind of worry that...you think I might be trying to be different {i}on purpose{/i} or something」，得知他喜欢「只有她这么叫」后说「I would very much like to have sex with you now if...that's okay.」
- 输入 **thunderfury, blessed blade of the windseeker**——她纠结「我一直想{i}握{/i}它，可如果你{i}就是{/i}它，这个愿望就成真了」。
- 输入 **daddy / papa / father / dad**——她先推说自己「不是 Chika 或 Kirin 那种类型」，怕被笑；被鼓励后叫出口，追问「So...you'll be my [mollymaster] for...the rest of our lives?」
- 其余任何输入走通用分支，Molly 机械登记：「Your entry has been recorded in the log. You will now be referred to as [mollymaster] during most sexual dialogue.」

**endofmollysexnaming** 里她先念完那段 NPC 台词（「This land is known as the Mystical Breeding Forest...」「The Land of Plenty is to the east...and the Dark Moors of Formalia are to the West.」「Be careful, Traveler. The wildlife here is rather {i}thirsty...{/i}」），随后被按在树上，一边被干一边努力维持角色，直到喊出「PIERCE MY FRAGILE WOMB WITH YOUR PLEASURE-SPEAR! I'M GONNA CUM!」内射之后 Sensei 不给喘息，连续再来——旁白用「Then a third.」「Then a fourth and a fifth and a sixth until her body has been adequately {i}power-leveled{/i}」计数。她昏过去，醒后他扶她站起来，旁白收尾：「Who shall I conquer next?」随后跳回 chap4.rpy 里的 beachsixsexmenu。

### 身世回溯与猫娘装扮（mollyspring3 / mollyspring4）

**mollyspring3** 前半段是与 Ami 逛内衣／情趣服饰店。店员对 Molly 实施系统性的种族微歧视：连说三次「Nihongo jouzu desu ne」，跳过她本人请 Ami「翻译给你的爱尔兰朋友听」，坚持问「她只是来探望你的吧」，最后问能不能拍照「We don't get many foreign customers here.」Ami 替她爆发，Molly 却安抚她：「This is just what happens as a foreigner sometimes. You just have to deal with it.」

随后大段闪回爱尔兰校园：同学围观她的便当并问「里面有生鱼吗」；她看漫画被指「又把卡通黄漫带来学校」；Aoife 与 Orla 一边说着「我想帮她变正常」一边向她借五镑；旁白总结「five-pound loans that would never be repaid」。回家推开空屋门，她喊出「Tadaima...」，无人回应。父亲进门前喊「Are ya winning, son?」，两人为晚餐拌嘴，父亲要去 Belfast 出差。她立誓「One day, I {i}will{/i} get to experience the real thing. And live out my days as a real Japanese high-schooler and the {i}true{/i} heroine of someone's life.」，父亲答：

> mod: You'll always be my heroine, Molly. No matter where the wind takes you.

而她的回答是一句预言：「I'm hoping for a route with a lot less consanguinity and a lot more catgirls.」回到现实，她感叹「Yet, somehow, I have ended up with both.」——此时站在她身边的 Ami 正穿着猫娘装（说话带「nyaa」），而 Ami 与 Sensei 的关系本身就是「血亲」那一类。Ami 说「You're just as Japanese as me as far as I'm concerned.」，Molly 纠正她：「I'm not Japanese. I'm Irish. And I'm {i}glad{/i} to be Irish.」，并补上一句「I can assure you I still feel more welcome here than I ever did at home.」

**mollyspring4** 按 amifingered 分成两条互斥支线：

- 若 **amifingered == False**（未与 Ami 发生性行为），本段是纯粹的惩罚性元叙事：旁白宣布「Also, Molly never dressed up as a sexy cat or pet her friend. Life is bad and we are all going to die miserable and alone.」，接着点名玩家——「Oh, and you missed another event for not having sex with Ami. Way to go, loser. Now you get less of the pervy gamer-girl too.」／「Why won't you let her be happy? She loves you so much.」并置 mollyspring4miss = True。
- 若 **amifingered == True**，走电车对话支线。Molly 起头：「it wasn't all that long ago that I almost fulfilled a lifelong fantasy of mine with your dad on this very train route.」随后借「开新档／练小号」倾吐倦怠：玩着玩着就想重来，「So you make an alt...or start a new save file...and do things a little differently than you did last time just to see what it's like.」Ami 回应：「It's still the same game at the end of the day, though.」并补一句「there are too many games out there to keep playing the same one. The hard part is actually {i}finding{/i} them.」旁白写下全文件最重要的伏笔之一：

> Is there {i}anything{/i} she can do at this point to change her fate? Or have the route and its ending already been written?
> There's no way to know but waiting it out.
> Or rather, there {i}is.{/i}
> She just doesn't know about it yet.

两人还谈到了彼此的「屏障」：Molly 说 Ami 是「a {i}niche{/i} pick in terms of a heroine. A fetish, even.」，而自己面对的是「a cultural barrier instead of a familial one」，并坦言「I don't feel entitled to see him as anything more than what he's been to me. But {i}you{/i} do.」Ami 安慰她「if someone like {i}me{/i} can win...of course someone like {i}you{/i} can win as well.」末尾 Ami 下车前当众宣称「My name is Ami Arakawa and I have {i}tons{/i} of sex with my dad!」，Molly 独自在车厢里念着「A date, huh?...Should I wear my dress again?」回到宿舍后，她借手机屏幕的光自慰入睡，画面里是那张猫娘照片。

## 三、lust 线概貌

lust 线由通用邀请系统与少量专属事件构成：

- **mollyinvitegen**：电话邀人上门后进入 mollyinvitehub 的三分支菜单——「Hang Out (Raise Affection)」、「Cunnilingus (Raise Lust)」、「Headpat」。这是 affection/lust 双轨的最小可见单元。
  - **mollyinviteaff**（affection 分支）：Molly 征用 Sensei 的 YouTube 账号在评论区跟人吵架（「I somehow am both proud and disappointed at the same time.」），之后挪到床上看电影，双方都没自慰，molly_love += 3。
  - **mollyinvitecun**（lust 分支，定义在 animatedscenes.rpy）与 **mollyheadpat**（定义在 headpatcentral.rpy）是本文件之外的两个跳转目标；headpat 支线连着「500 headpats 解锁某物」的长线钩子。
- **mollylust10**：圣诞派对（Tsukioka Manor）上的一场。Sensei 刚和 Futaba 在浴室里结束，Molly 敲门闯入，一进门就挑明「The fact that you are not wearing pants.」他明确说出这是当天的第四个（「It's not because she's the fourth girl today, is it?」），无法再勃起，改用手指。Futaba 被要求「旁白」，随即崩溃摔门而去。Molly 一边被做一边坦白自己的幻想清单：被哥布林群使用、当精灵王国的摄政女王、「How I want you to bend me over and fuck my little brains out」。Sensei 想说羞辱性台词时与脑内声音当场争执，把它称作 **Malvin**（「No, Malvin. I'm not going to say that.」），并拿 Pareidolia 作比较：「Pareidolia was an asshole, but at least he got things done.」结尾 Molly 两次用「Ahem」抢戏，随即 Tsubasa（tb）推门而入，以那句「in the words of that {i}very young{/i} white girl, may I just say — {i}ahem.{/i}」接管场面，本段 jump christmastsubasa1（TsubasaEvents.rpy）——lust 线在此充当向圣诞事件输送角色的管道。
- **mollyinvite2** 结尾也同时 molly_lust += 1，是 lust 与 love 同时记账的少数节点之一。
- **命名系统**（mollysexnaming）：把「她该怎么称呼我」的选择权交给玩家，使 lust 行为本身变成一次角色扮演配置，是 lust 线中最接近「meta 玩具」的设计。

## 四、与主线/元叙事咬合点

- **万圣节旧创**：Molly 与 Sensei 之间始终悬着一桩「dark room」事件。三方都只有碎片——Sensei 在 mollycafe30p2 说「none of those people ever took advantage of you while you were unconscious in a dark room.」；Molly 转述 Haruka 时提到「He's never been good at that to begin with, but ever since that Halloween it's just...」；Sensei 在 mollydate35p1 的版本是「the blissfully ignorant me who would have fucked her on Haruka's couch prior to our dramatic fallout two Halloweens ago.」；Molly 则反复要求「Put it behind you, Sir.」「Let what happened in the dark {i}stay{/i} there...」。这些证词拼出一个从未正面展示的原点创伤。
- **Rin 三角**：rinspring3 里 Rin 逐一点名 Sensei 的性伴侣，问到 Molly 时他承认「She may or may not have put my penis in her mouth recently.」，Rin 回「Good for you, Molly. You've finally made it.」。dormwarssix12（dorm wars 闭幕式）里 Rin 大发存在主义感慨，被 Molly 一语拆穿「You're reading existential manga again, aren't you?」，两人接着拿「H-Scene」「yuri 最不好卖」「会不会被腰斩」说笑，Molly 还抛出「It's a timeloop, I tell you. And the only way out is for the main character to complete all of the routes.」在本文件内，Rin 既是 Molly love 线的前置伤口（mollycafe25 全段），也是她反复用来衡量自己的参照系。
- **叙述者的自我暴露**：mollycafe30p1 开场的鱼钩独白，与 mollyinvite1 里「Molly's cute and I want to put my penis inside of her.」／「Just kidding.」／斜体补刀的三联句，是元叙事层最直白的两次现身：动机被说出、随即被否认或推翻，供玩家自行裁决哪句是真。
- **内在人格系统**：Molly 的 Siobhan（mollyspring1 命名）与 Sensei 的 Pareidolia（同段命名）、Wilford Blackhole Hands（mollyspring2 结尾命名，会扇他巴掌）、Malvin（mollylust10 中被点名）构成一组并置的「脑内声音」。源文只呈现它们各自被命名与被争辩的过程，并未说明它们的来源。
- **系统提示的武器化**：affection/lust 弹窗在关键情感节点被旁白挪用为讽刺——mollyspring2 的「Now, you can go back to hurting little girls whenever you want.」，mollyinvite2 的「That's right, Akira! You've once more fulfilled your only purpose on this planet...」，以及 mollyspring4 直接把「错过事件」的锅甩给玩家。
- **重置循环暗示**：mollyspring4 电车段里「新存档／已写好的结局／她还不知道方法」，与 mollycafe25p2 的 Tír na nÓg（无人死去的彼岸），形成一组关于「重来」的暗语。

## 五、未解伏笔

1. **万圣节真相**：「dark room」那晚到底发生了什么，三方均只有碎片，全文未正面回收。
2. **「改变命运的方法」**：mollyspring4 的电车段明言存在一条她尚不知晓的出路，指向后续章节或循环层操作。
3. **500 headpats**：「Upon reaching 500 headpats, Molly MacCormack will-」被掐断，解锁内容悬置。
4. **Niki 与 Sensei 的童年**：机甲番、勇者斗恶龙，以及那张可能仍在 Niki 父母家的存档记忆卡；「两人在 Niki 卧室里做过什么」被双方紧急叫停。
5. **Haruka 衣橱缺失物**：Molly 暗示从 Haruka 家拿走了东西（「if she happens to ask about anything missing from her closet, I was never there.」），配合 Haruka 醉后呓语 Tsuneyo，构成 Haruka 私生活的三角疑云。
6. **中间名**：Medb 还是 Moyra？玩笑背后是对「角色档案由谁书写」的一次小规模元质询。
7. **consanguinity 预言**：「less consanguinity and more catgirls」却「ended up with both」——她对 Sensei 的感情是否正在滑向父位替代，文本刻意不结案。

> 按源行号检索本角色 label，见 `索引/Molly索引.md`。
