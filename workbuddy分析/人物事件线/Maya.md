# Maya 事件线全析

> 源文件：MayaEvents.rpy ｜ 共 36 个剧情 label（含 shrine 跳转枢纽与 callmayamorning／callmayaafternoon／callmayanight 三个电话入口）
> 定位：她是全作中唯一从一开始就知道"世界在循环"的女孩，也是这条循环的机制执行者；她的线完整记录了一个"旧 Maya"在万圣节重置后消失、被一个没有背景故事的"新 Maya"顶替，以及新 Maya 在旁人的比对目光下重新争取 Sensei 的过程。
> 阅读提示：正文以 label 名为唯一锚点；台词直引以 `>` 起头，m=Maya、s=Sensei、a=Ami、ay=Ayane、ni=Niki、k=Kaori、mak=Makoto、u=Uta、no=Nodoka、y=Yumi、se=Sekai、wil=Wilford、q=未具名说话者。

## 一、角色基本盘

- **身份**：神社巫女。mayanoongen2 中，全镇被雪覆盖而神社一带却"不知何故未被雪触及"，Sensei 就此事追问时，她只给了一句"有些地方无论你何时造访都不会改变"的隐晦回答。她的日常职责是扫地与照看捐钱箱（shrine2to4、shrine5）。mayafestival3 里她交代了自己入行的时间与理由：大约中学前后、小学末尾，在升入高中之前；表面理由是"喜欢这身衣服"，真正理由是"万一正是巫女这个身份让我能挺过每一次重置，我不想冒险切断它"，并明确说过"I'm only a shrine maiden out of necessity"。
- **表面性格**：冷淡、毒舌、不停赶人走。shrine20 里被追问来历时的自我介绍是 "Maya Makinami. Age, [[redacted]. My hobbies include watermelons and the violin. My past is of none of your concern."。她的口头禅是反复强调 "I am a normal [teenage]girl."（shrine5、shrine10、mayafestival1 等）。
- **知情范围**：shrine10 中她给出全知的自我描述："I see everything that you see. The past. The present. The future."，并断言一切都是螺旋式循环，"every single one will be wiped clean after a set amount of time"。同一节的旁白（Sensei 的理解）写道：有人活在当下，有人活在过去或未来，"But Maya has somehow found a way to live in all three at once"——即三种时间状态同时并存，而非三个世界层级。
- **权限边界**：shrine20 里她明确否认自己拥有完整控制权："this world isn't something I have complete control over. I just know how to manipulate certain parts of it to make things easier."，同一节也说 "I need you to fail to a certain degree."
- **双 Maya 结构**：shrine25 里旧 Maya 亲口提出替换假设——"What if, after the next reset, there was a brand new Maya Makinami? One who didn't know too much about the world. One who didn't know too much about you."；mayaspring2 中 Sensei 说得明白："Everything Ayane and I told you should have been purged after Halloween."，即替换发生在万圣节那次重置；halloweenmaya3 里由 Ami 向新 Maya 说明这段替换史——"this sort of thing has happened to you tons of times now"，而这一次"you're the only one who was forced to start over"。新 Maya 的身世在 mayachristmalloween3 里补完：她最早的记忆是在雨中醒来，看见一个刚哭过的男人向她伸出手，随后被带到一间废弃公寓。
- **关键关系**：与 Sensei 长达数年的关系（sportswars10："It's been months! And we've been together for years!"）；与 Ami 的"最好的朋友"关系（sportswars5 的旁白写明 "Ami Arakawa would always be her number two"，且两人互相索取"秘密"作为信任凭证）；与 Niki 的正面冲突与和解（dormwarssixmaya1）；与 Ayane 从巫女学徒到互相承认的朋友（shrine40、mayaspring5）。
- **职能**：季节切换的执行者（shrine25："I'll be finalizing the switch during the next reset."，并说明众人"对时间的感知会随世界一起重置"）；搬箱流水线的运输端（mayafestival4 里她把一个打不开的箱子交给 Sensei，mayaspring1 里新 Maya 说这些箱子是 Ami 留在宿舍里的，自己一直在替她扔掉，而 Sensei 本能地坚持"它们得送去学校"）；以及靠重复台词计数循环的人——shrine20 里她说 "I'm really, really tired of hearing that line. It was cute the first time, but now it's just getting annoying."，Sensei 问听过多少次，她答"差不多和下一句、再下一句一样多"。

## 二、love 线逐事件脉络

### 神社授课序列（firsttimeshrine → shrine40）

shrine 只是跳转枢纽：它按 maya_love 与各前置旗标把玩家分派到 firsttimeshrine、shrine5、shrine10、shrine15、shrine20、shrine25、shrine30、shrine35、shrine40，未满足条件时落到 shrine2to4。

firsttimeshrine 里，开场两句署名 q（未具名说话者），"Oh...wonderful." 与 "Getting started early this time, I see."——"this time" 一词已表明她按周期计数；第三句起改署 m，说话者即 Maya。她当场戳穿 Sensei 的顶替身份："We both know you're not who you say you are."，并用 Ami 的生日做验证题（提示"在八月"，Sensei 答"七日"后猜错）。随后她给出无限世界论：

> m: There is an infinite amount of worlds out there...and an infinite amount of possibilities within each and every one of them.

> m: They spin together, but in different directions. Sometimes, they spin so fast that parts of them combine.

她随即把这番话全部推翻——"That none of that matters at all."，重要的是他来了之后要做什么——然后下达禁令，并给出全作最重的警告：

> m: The reason I was willing to help you out to the extent I have today is that my existence is heavily dependent on yours.

> m: And that existence is in grave danger if you do not heed this warning.

> m: getting close to you is the actual worst thing that could possibly happen. For {i}both{/i} of us. Not just me.

shrine5 中她把 Ami、Ayane 对 Sensei 的好感解释为被"残缺（mutilated）的感知"蒙蔽，并说只有自己看得清他是什么、想在这里得到什么；她用拼图比喻他的格格不入——"You're like a...3D puzzle piece trying to blend in with 2D ones atop the coffee table of...some old person who likes puzzles."，并点破"他起步就比别人高，因为所有人都已经爱他了"。

shrine10 是世界观宣言最集中的一节。她说"睡着与醒着没有区别"，抛出"感知即答案"的论断："The key to uncovering this world...or any world for that matter...is perception."，接着是：

> m: Nothing is real. Well...at least not in the traditional sense. Technically, everything is real. But only because that is the way we have decided things to be.

> m: What I am saying is that this has all happened before...and it will happen again. Over and over and over.

她把两人的关系也纳入循环描述："You will meet me and I will meet you... It will continuously spiral, much like life itself...circling the drain before disappearing, only to return once things have been purified."，并给出 wipe clean 的断言与"最好不去思考地活着"的结论。

shrine15 中 Sensei 在神社后方发现一处被大树和废弃捐钱箱遮住的隐秘角落，Maya 在那里午睡。禁果独白把两名对手并排列出：

> "More forbidden than the one with my blood."（紧随其后闪现 amiclass 画面——指 Ami）

> "More forbidden than the one who {i}wishes{/i} for that blood."（紧随其后闪现 ayaneclass 画面——指 Ayane）

她警告接近真相会让 Sensei 落到"从未见过的地方"、"回到一切的起点"，并在被说成"目标"时真正动怒："Stop... Treating this... Like a fucking game."，"those girls are people. And as much as I hate to admit it, so are you."。Sensei 随口问起"命运"，她回答 "Fate exists. It's all around us."，并因这个偏离惯例的提问而说出 "You're changing."，随即又收回。本篇结算时置下 `$ connect = True`。

shrine20 抛出复制体论："If all of the buildings and structures stay the same, but the people filling them are all replaced with identical copies equipped with altered minds, can we still call it the same world?"，紧接着是 credits roll 三连问——"But what happens after the credits roll? What becomes of everyone inside of that game? And what happens if they don't reset along with the others the next time you press 'Start?'"。她也再次亮出立场："You succeeding only makes things harder for me. I need you to fail to a certain degree."，并在结尾预告"近期可能还要请你再搬几个箱子"。

shrine25 里她自白季节切换的职责，说众人"对时间的感知会随世界一起重置"，这是她自己也尚未弄懂的一环；随后她拒绝回答"如果我消失会怎样"，反抛出替换预言（"What if, after the next reset, there was a brand new Maya Makinami?"）。Sensei 的内心回应是：即便新 Maya 兴趣完全相同——西瓜和小提琴——"those dead eyes are what I expect to see each and every time we meet"。本节 Maya 也说出了自己的恐惧："I'm finally starting to feel something again. I don't want that to go away."，并在被问"你害怕吗"时答 "Yes."。

shrine30 给出"记忆＝硬盘重格式化"理论：

> m: What you were experiencing in watching those girls adapt to you was a type of reformatting...that will be how they remain until a new user comes along.

她冷眼描述众女"Falling for version after version of the same [high_school] teacher but failing to truly capture him each and every time"，并挑明自己早就知道 Sensei 与 Ami 的事——"I really wish you didn't go all the way with Ami, though. I hate watching her get hurt after everything that she's been through."。她解释迟说的理由仍是同一句："I needed you to fail to a certain extent. And you failed wonderfully."

shrine35 发生在一个雪夜：Sensei 失神游荡数小时、浑身湿透地走到神社，撞见 Ami 与 Ayane。三人散去后，Maya 为前一晚的失控道歉（"I was desperate and angry and said some things that should never have been said."），Sensei 说他拒绝是因为不愿她出于绝望而那样做，她说 "Which is why I'm glad you didn't let me follow through with it."。她的知识开始衰减："everything I know about the world has been slowly fading away since winter began."，并罕见地自我推翻：

> m: I have told you in the past that you are "changing." I was wrong. I have told you in the past that everything is part of a cycle. I was wrong about that as well.

> m: there is clearly no cycle at all. And if there is, it's a really fucking stupid one without any rules.

身份问题逼近揭晓："The reason I don't want you to learn any more about 'your' past is precisely because it is your past. Probably."，并把两人的绑定说成 "Because the second you fall off- I fall as well."

shrine40 里 Ayane 穿上了巫女服。Maya 给出的理由是：既然她要整天赖在神社，不如让她干活；Ayane 自己的说法是"这样就能多聊 reset-stuff"。两人定下的本轮计划是"再测一次其他人能否也获得某种觉醒"——上一轮已经发现"别人获得某种察觉并非完全不可能"；Ayane 还吐槽旧 Maya 上次的做派是"拿出一整套理论，然后用整整一个周期去验证它"。Ayane 提议拉 Ami 入伙，被 Maya 直接否决，理由在此揭开：

> m: I'd be describing probably decades or...centuries of trying that exact thing to no avail as I thought the same thing as you. And not only did it never work, it made her...mad.

她把 Yumi 视为当前最佳人选，并说 Tsuneyo 她已单独试过、对方什么也不记得。收尾旁白是伊卡洛斯意象："This cycle will melt the wax of my wings. I'm flying too close to the sun."

### mayafestival 四部曲（第二章收束）

mayafestival1 是 Maya 的生日。清晨她溜进 Sensei 卧室（Ami 上班去了），Sensei 的祝词是 "Happy anniversary, Maya. Here's to a million more years or however long you've been wandering around inside of the bubble."。她在门边墙上发现一张署名为 MM 的留言条，字迹像自己的，"But I don't recall ever writing this."，并补了一句 "Remembering is kind of my thing."；她随后又写了一张贴上去，叮嘱别碰。天台话题落到 Ayane：Maya 的推断是 Ayane 上次能登上屋顶是因为怀了 Sensei 的孩子、"she was a temporary extension of you"，而重置连身体属性也会回滚——"she was rewritten to be the same exact person, just...without a parasite growing inside of her."（她自陈这是推测："This, like everything else, is all conjecture."）随后是情感突破："I'm finally starting to feel something again. I don't want that to go away."——被问"你害怕吗"，她答 "Yes."，并补一句 "Because I think that it might."

mayafestival2 中两人去了"库门美境内能到的最远处"的祭典：先坐巴士再步行约半小时，周边因学校停用而基本关门。Sensei 明确察觉"这里既不像旧区，也不像新区"。`amifingered` 为真时会出现一个卖瓜的无名摊主 q：她叫卖普通／方形／三角形甜瓜，说今天是第一天上班，拒报姓名（"it's just that nobody's ever asked me before"），并在 Sensei 未曾说明的情况下知道他是老师，随即岔开话题。Maya 听说有瓜摊时反问 "Was there really a booth like that here?... I had no idea."

mayafestival3 开场是一段无署名第一人称独白（文中未标明说话者），其中出现：

> "I'm scared. But no one can ever know that. No one in the middle, at least."

两人夜行时 Maya 说明自己为何只在生日见他，并否认"这是约会"；途中误入一座挂着"故障停用"牌子的神社，她猜里面供的是"某种兔子"。本节也交代了巫女身份的由来与她不肯脱下这身衣服的原因（见"一、角色基本盘"），她还说 "I've toyed with the idea of leaving before. Especially when I was getting a new {i}you{/i} every four months or so."，以及 "I draw the same one every time."（指抽签）。

mayafestival4 是超现实段落。烟花高潮处插入系统文本 "////////////////ADD HAND" 与 "////////////////HAND SUCCESSFULLY ADDED"，随后 Maya 讲了一个梦：

> m: I had a dream that I was flying. You were there, but it wasn't actually you. We were on the roof. The same room. At different times. The same place.

她随即拿出一个箱子当"礼物"——"I don't have it with me. In fact, it's not really a present at all. I just need your help carrying it."，Sensei 问能否知道里面是什么，她答 "Only if you can open it."。此处 Sensei 发生断片：Ami、Ayane、Uta、Makoto 等人的声音错位插入，回神后 Maya 问他是不是又在"断片／做梦"。收尾是系统文本 "////////////////MAYA EVENT COMPLETE" 与 "////////////////THERE ARE NO MORE MAYA EVENTS IN CHAPTER 2"，本节结算 maya_love +25。

### mayadate45 / mayaspecial45（第三章感情正线）

mayadate45 由夜间打电话触发（callmayanight：需 `shrine40 == True`、`norikodorm30 == True`、`mayadate45 == False`），结算 maya_love +100。电话里 Sensei 要求："Call me by my real name."，Maya 直接挂断；见面后她说真名是 Niki 告诉他的，并警告这件事本身险些要了他的命——"It's an actual miracle you're still here to talk about this when you could have been wiped right then and there."。她解释自己为什么不肯谈两人：

> s: And talking about us has?

> m: ...{i}Yes.{/i} Things have spiraled into chaos {i}every other time{/i} I have done that.

随后是历史性自白：她承认自己曾在数次失控与孤独中与历代"假 Sensei"发生过关系并弄坏了他们——"I may have caved into some of my carnal desires and...broken several Senseis... I've seen it firsthand."，"I can't imagine how breaking the {i}real{/i} you would feel"。她把这里称为 "chronoprison"，并说 "The world won't allow it."（指两人相爱）。阳台一段里，旁白写"困住我们的高墙正一天比一天不像比喻"（"less and less metaphorical by the day"），两人还发现看到的月亮大小不同——Sensei 觉得比平时大，Maya 说 "It looks the same as always to me."。临别她说："I don't...not...feel the same way you said you did before or... Yeah. Goodnight."

mayaspecial45 是雨天同行。Ayane 有两把伞，Maya 与 Sensei 被迫共撑一把，路中撞见站在马路中央淋雨的 Kaori。众人把 Kaori 送回她打工的"水果与奶油"咖啡店后，Maya 两次开口向 Kaori 要菜单都被完全无视，Kaori 只对 Sensei 回应；Maya 转而问 Sensei：

> m: But...I've never been ignored in my life. I'm adorable. Can you see me?

最后由 Sensei 替她点了"菜单上每样一份"。本节结算 maya_love +1、kaori_love +1，末尾的系统文本只有一句："{i}it is waking up{/i}"。

### sportswars 三部曲（旧 Maya 时代终结）

sportswars5 是 Ami 卧床期的探房。开场是数节无署名诗，其中含删除线的一句 "I hear things, Boy. {s}I'm scared.{/s} I'm yours!"。Maya 进屋时先注意到草莓气味的消失，旁白写明 "Ami Arakawa would always be her number two — regardless of who or what would have her rethink that."。两人谈 Ayane 的异常、谈 Ami 在教室里的"摘器官"发言，Ami 反将一军要求 Maya 交出一个秘密，最终以"如果我查出你说谎，我可以对你做任何事"的承诺收束：

> m: Anything anything.

Ami 这才吐露情报："Sensei's probably at the shrine."，并说 "You've never hurt someone before."。本节收尾的系统提示是 "{i}Maya Makinami has gained that status effect [[PARANOID]!{/i}"。

sportswars10 开场诗署名为 "- Girl"（诗中提到 "I hear things, Boy"），随后是 Wilford Blackhole Hands 的荒诞审判戏：他因 Sensei"影响了他的度假行程"而反复掌掴，黑洞胃里的"半透明流产儿"被取名 `[whatyousaid]`。画面一转，Maya 追上来质问他数月不露面，逼到极致时他抛出：

> s: You're not Maya...

> s: You're a meat puppet.

她的爆发与关系的自我定义都在这一节：

> m: No! It's been {i}months!{/i} And we've been together for {i}years!{/i}

> m: We don't fight. We fuck and we cuddle and we kiss and we part. That's how it's always been. And that's how it {i}should{/i} be because that's what we {i}want.{/i}

本节结算 maya_love −1。结尾诗同样以 "Girl" 的声音对 "Boy" 说话："We're closer than you know, Boy. This house is not your home."

sportswars14 是追逐与摊牌。她定义两人的系统："You break, I fix. I break, you fix. Then, we fill the radio silence with sex and our shitty idea of what 'affection' means..."，并说出全作最著名的自我宣言：

> m: {i}I{/i} am Maya Makinami. {i}I{/i} am the best and worst secret you have ever kept. And {i}I{/i} am the type of girl who will chase you down if I have to because not even a million time-loops could stop me from doing that.

她也亮出自己的阴暗面："In {i}here,{/i} I'm just as bad as you... I'm explosive. Sensitive... I'm probably even emotionally abusive at times."。结尾 Sensei 的内心独白承认后脑有个声音，说若顺从它"也许会有别的女孩免遭我的怒火"，并问 "Maybe there's someone it's {i}okay{/i} for me to hurt?" / "Maybe that someone is her?"；随后他答应送她回家，却改口 "I'm taking you to a different one."

### halloweenmaya 三部曲（新 Maya 诞生）

halloweenmaya1 中 Maya 开始在时间线之间不受控地跳跃。她在走廊里失神停下——此前已把几个箱子塞进 Sensei 怀里，却记不清里面装了什么——随后向 Sensei 说明 "how about being in like three different timelines at once?"。跳进教室里的一段亲热中，她脱口叫出真名 "A...Akira?..."，被纠正"在学校要叫我 Sensei"。场景切回真实层时，她正把舌头伸进 Ami 嘴里——转瓶游戏本该只是轻吻，Molly、Rin、Ayane 等人当场围观。收尾诗是 "the girl the girl the girl... it's me"（原文重复二十余次后以 "it's me" 收束）。

halloweenmaya2 里跳跃症状公开化：她向 Ami 与 Ayane 辩解无效，坚持"世界正在崩溃，每五分钟我就被丢到另一个时间点"。众人劝她再亲一次以触发跳跃，她转而强吻"Sensei"；画面崩坏后出现一段署名不明的诗，末尾插入 Ami 的意识入侵文本：

> {b}THIS IS SUPPOSED TO BE MY STORY{/b}

> The girl with the me who is me who is Ami I am Ami {b}CAN YOU HEAR ME?{/b}

随后"Sensei"中断亲热、拒绝说出"我爱你"，并承认自己不是本人：

> s: I'm not Akira. I'm not even here.

Maya 反问 "My conscience? The devil on my shoulder? Is this supposed to be some kind of 'trial?' Am I {i}dead?{/i}"，对方以响指作答："{b}YOUR WISH IS MY COMMAND.{/b}"。她的结论是：

> m: I get it now.

> m: I'm in Hell.

halloweenmaya3 是全文件元叙事密度最高的一节。新 Maya 醒来后发现自己被铐在椅子上、Ami 手持按摩棒并架了摄像机。Ami 说她昏倒在去派对的路上，是自己把她背来的；Maya 认出这个房间"堆满与我有关的东西"，却认不出是哪里。Ami 确认了 Ayane 与 Sensei 口中"另一个 Maya"的说法，并纠正数量：

> a: this sort of thing has happened to you {i}tons{/i} of times now!... this time... you're the {i}only{/i} one who was forced to start over.

> a: That's right. {i}Every single one of you.{/i} This is {i}my{/i} world. {i}I'm{/i} real. You and all of those other girls are tools. But {i}you're{/i} a good tool.

> a: Now, I just {i}take{/i} what I want. And if I'm unlucky enough to end up in a world where that doesn't work out- I take the {i}world{/i} away instead.

她逼 Maya 表态忠诚（"Do you think you can be loyal, Maya? To {i}me?{/i}"），遭拒后转而施暴，并当着她的面演示杀人：一边讲解人的颈部能承受上千磅力、压迫颈静脉约十秒即可致人昏迷，一边从十倒数到二。收束旁白抹除一切：

> And so does Ami. Neither one of them ever existed. Nothing has ever existed...

> {b}I am the ghost of better days.{/b}

系统随后解锁 Alexis："She exists in a different place at a different time... Just she is trapped. And you float freely, like a frog on a lily pad."；末帧倒计时："{b}CURRENTLY GATHERING: APPROPRIATE DENIZENS OF THE TWENTY-THIRD TERMINAL...{/b}" / "{b}THIS PLACE IS BECOMING INCREASINGLY LESS STABLE.{/b}" / "{b}ONLY SEVERAL MORE RESETS ARE PERMITTED{/b}"。文本自身也把"Ami 为何能同时出现在两个时间与／或地点"列为未答之问。

### 第四章：新 Maya 重建线（mayaspring1–5 与 christmalloween）

mayaspring1 的定调是："She was always the constant. She was always the one."，黑屏三秒后接 "Until she wasn't."，随后是一段充满敌意的无署名独白，质问"这个冒牌货凭什么穿她的衣服、碰她的东西"。夜里两人在宿舍外相遇，Sensei 问 "Which Maya? Old Maya? Or...{i}new{/i} Maya?"，她答 "Maya Maya. The only Maya there is."。箱子链在此揭秘：新 Maya 也在替 Ami 运箱子，而且一直把它们扔进垃圾桶；Sensei 本能地阻止——"No! Those aren't supposed to go in there! They need to go to the school!"，却说不出理由。两人抬箱到学校、塞进隔壁空教室后，她把他领回自己当年的课桌前，自封这项工程为"Maya Raising Project"，逼他说清想要把她养成什么样；她先提议"模仿你上一位真爱？背她的台词？"，再提到"比你还聪明的那个人——你失去的第一个女孩"，并顺带声明 "I fucking {i}hate{/i} Niki and I fucking {i}hate{/i} her annoying bitch of a sister."。她说自己真正的动机只有一句——"Because I {i}miss{/i} you."；Sensei 不肯直说爱，只报出一个名字："Natsume Sōseki."（借夏目漱石的名句代替告白），她回 "I'll take it..."。

mayaspring2 是"第二次初次约会"，地点是章鱼烧摊。开场旁白里 Sensei 自曝秘密研究："the secret resurrection studies I've been partaking in behind your back"，目标是"until I become one of them"，并直接点名 Sekai："I doubt Maya and Sekai would get along very well."。摊前对话中，新 Maya 展现出不该拥有的记忆，Sensei 当场点破：

> s: You shouldn't have retained any of that, Maya. Everything Ayane and I told you should have been purged after Halloween.

她把感情比作箱子："{i}You{/i} are the box I've stored all of my feelings in."，并说自己害怕"不再恒久（permanent）"。两人随后谈起"去过别处／别的时间"的体验，Sensei 承认 "Probably...yeah... It's kind of...hard to remember, though."，并说 "I often wish I didn't have to remember Sekai."。结尾他主动握住她的手——旁白写 "And it's the most unfaithful I have ever felt."（不忠的对象是 Niki）。

mayaspring3 里两人约在宿舍，却被 Ami 撞破：她说自己受不了每晚听 Sensei 与 Niki 做爱，所以搬回宿舍住。Ami 自曝利用帮他更新手机时开启了"查找我的手机"并绑定到自己手机上——"Now I can see where he is at all times"，还暗示"往他食物里放了东西"。争吵中 Sekai 的声音（se）插入，只被 Sensei 听见。Maya 威胁要把 Ami 的秘密全盘告知 Sensei，Ami 反制：

> a: Words like "kill" are too heavy and dramatic to be wasted on those who have never been alive to begin with.

> a: I don't have powers... And while I can't reset you myself, I can sure find a way to make you {i}wish{/i} I could.

Ami 最后说 "I'm not a bad person, Maya. I just do a lot of bad things."，并以驯化哲学收尾："Just want fewer things."。本节结算 maya_love +1、ami_love +100，系统还加了一句 "{i}She clearly loves you more!{/i}"。

mayachristmalloween 三部曲发生在情侣酒店。第一部以寄居蟹隐喻开场——"a hermit crab who found a pretty shell and crawled inside, not realizing that shell belonged to me"；成因对质中 Maya 否认自己是世界的成因：

> m: I didn't create this world, Sensei... Literally {i}none{/i} of this is what I want.

第二部揭开"辅导室初夜"的回忆（她反复提到 tutoring room／study room，并说 "You caved pretty quickly once I started begging to be broken"），并在性事中喊出第一顺位宣言：

> m: Because you're {i}my{/i} man! ...{i}I{/i} was the first! Not counting fucking Niki and...Ami's mother! And {i}I'll{/i} be the last too!

> m: Ami's mom has been dead for {i}years{/i} now...

第三部是身世完整版：她最早的记忆是在雨中醒来，看见一个手很大、眼镜起了雾、像是刚哭过的男人向她伸出手，阳光正从云里透出来；他带她去的是一间"看似废弃、其实有家具和电"的公寓，只有一张床，于是他当天出去买了张蒲团。他供她吃穿，教她"文学与诗歌"，却从不说自己的痛。醋意的源头是"另一个常来、与他相识更久的女孩"，加上他从不留宿、每次回来都带着草莓味——由此引出的答案是"你家里还有个侄女要照顾"。她承认是自己在冬天先告白的："I started it. I confessed to you in winter."，理由是"想保护收留我的人、也想成为他的出口"。她的存在被一句话定性：

> m: {i}Your{/i} Maya Makinami. The girl who would not exist at all if it were not for you.

本节结算 maya_love +200、maya_lust +200（前两部无数值结算）。

dormwarssixmaya1 是 Niki 与 Maya 在天台外的对峙。Niki 转述 Sensei 的警告："He told me {i}not{/i} to talk to you, actually. Something about you being 'different,' whatever that means."。两人承认彼此都在怕对方。Maya 亮出定位：

> m: I'm ground zero. And you can look at me as the catalyst to all of this if you want.

> m: He ran away to {i}save{/i} you! From {i}this!{/i} ... Of course they suck! They were always going to suck the moment Ami's mom died!

Niki 道出自己真正的目的不是让众人难堪，而是想确认"他还有没有救"；最后她说 "There's a konbini around the corner. How about I buy you a drink?"，并坦言也想从 Maya 这里打听 Ami 的事。收尾旁白说今晚只结束了一场战争，"Maya Makinami still feels insignificant — for she would never offer up an olive branch like this."

mayaspring4 是猫装性爱马拉松，开篇即写 "I have been having sex with this creature for roughly six consecutive hours now."。她带了一整袋道具（其中不少是她自己买的，还有一根可拆装钢管），并说明不同道具对应不同"Maya"。中途 Sensei 想起旧 Maya：

> "I wonder what it felt like back then. I wonder what noises she made. I wonder what she looked like after."

事后是那段著名对话："Let's get married." → "No." → "Good. That was just a test anyway."，她补一句 "I'd do it because {i}you{/i} want to. Not because I want it."。结尾诗节后只剩两句自我定义："I am nothing." / "I am seen."。本节结算 maya_love +1、maya_lust +1。

mayaspring5 以千禧时钟开篇——"the hands of The Millennium Clock ticked incessantly back and forth between The Martyr and The Old Clown"。Ayane 带着 Uta、Nodoka、Yumi、Makoto 穿着从唐吉诃德买来的巫女服列队突袭神社，说是要实现当年"全班都当巫女"的玩笑。等待期间 Makoto 向 Uta 与 Nodoka 科普重置机制：无限循环的高一里仍可能丢掉循环期间累积的记忆、被打回学年伊始的"起点"，Uta 追问"这发生在谁身上"，Makoto 答 "That happened to Maya."。单独相处时 Ayane 说她不知道"我认识的那个 Maya 在哪儿结束、你从哪儿开始"，只说想念以前两人一起聊"世界末日"的日子；Maya 反问自己算不算重要，Ayane 答：

> ay: I'd trade all of them for you. Just please don't tell any one of them I said that.

> m: I've never been that important to...anyone but Sensei before.

谈到 Niki 时 Maya 崩溃："Why did it have to be her?..."，并问出 "Is there somewhere out there for girls like us?..."。Ayane 答 "I believe that one day, there will be a place for everyone."。结尾诗是职能的自白："'Tis the hands, you see. In lifting them, I change the present nightly."

## 三、lust 线概貌

Maya 线没有以 lust 命名的独立 label；欲望内容全部内嵌于 love 线的亲密场景，且多数同时承担叙事功能：mayachristmalloween2 的性爱场景里塞进了"辅导室初夜"回忆与第一顺位宣言，并第一次把"Niki 与 Ami 之母"摆到 Maya 之前的性史序列上；halloweenmaya1 的教室亲热是时间跳跃症状的发作现场，真名脱口即症状顶点；halloweenmaya3 的折磨戏是世界所有权宣言的舞台；mayaspring4 的猫装场景包裹着"结婚测试"与"我是无物"的自我定义。全文件只有两处直接结算 maya_lust：mayachristmalloween3（+200）与 mayaspring4（+1）。

## 四、与主线/元叙事咬合点

1. **时间状态的活体样本**：shrine10 里她说自己看见过去、现在、未来，旁白据此写下"她同时活在三种状态之中"；mayanoongen2 里神社在全城覆雪中无雪，她给出的解释是"有些地方不随时间改变"。她是世界观机制本身的人形注脚。
2. **循环的执行者而非单纯的受害者**：shrine25 的季节切换、shrine20 的"我需要你失败到一定程度"与搬箱流水线，都说明她在处理这套机制；直到 shrine35 她承认"关于世界的一切知识从入冬起就在慢慢褪色"，并在万圣节重置后被这套机制碾过。
3. **Ami 的世界所有权**：halloweenmaya3 中 Ami 宣告 "This is my world. I'm real." 与"若不如意就把世界收走"，配合收束旁白 "I am the ghost of better days"、Alexis 解锁与第二十三终点站的剩余重置倒计时，构成全作元叙事层浓度最高的文本。
4. **记忆机制失效的先兆**：mayaspring2 中新 Maya 保留了本该在万圣节后被清除的记忆；mayafestival1 里 MM 字条笔迹像她却非她所写；mayadate45 里两人看到的月亮大小不同；shrine35 中 Sensei 毫无察觉地丢失了数小时。系统正在漏液。
5. **Ami 之母与"第一个失去的女孩"**：mayachristmalloween2 的第一顺位宣言把 "Niki" 与 "Ami's mother" 排在 Maya 之前，并说 Ami 之母"已死多年"——源文此处只写 "Ami's mother"，未点名；按已核验的家族事实，Ami 的母亲是 Sekai。mayaspring2 里 Sensei 另有一句 "I often wish I didn't have to remember Sekai."，Maya 答 "That's basically the only reason we're together."
6. **Sekai 与 ground zero**：mayaspring2 中 Sensei 自曝"背着你进行的秘密复活研究"，目标是"直到我成为他们之一"；dormwarssixmaya1 中 Maya 自认 "I'm ground zero." 与 "the catalyst to all of this"，并把一切变糟的时点定位在 "the moment Ami's mom died"。
7. **Kaori 的单向回应**：mayaspecial45 里 Kaori 对 Maya 的两次点单毫无反应，只对 Sensei 应答，Maya 因此问出 "Can you see me?"，最终由 Sensei 代她下单收场。

## 五、未解伏笔

- 涂黑的年龄栏与"雨中被捡回、无背景故事"的身世如何统一？她究竟是被造物、囚徒，还是世界的前一任"用户"？
- mayaspring1 中提到的"你失去的第一个女孩"未点名；她与 "Ami's mother"（按已核验事实即 Sekai）是否为同一人，本文件内没有给出确认。
- 巫女服是否真是她挺过重置的存续条件？mayafestival3 里这只是她的"万一"假设；若属实，新 Maya 继承巫女服意味着什么？
- 第二十三终点站在收集谁？"ONLY SEVERAL MORE RESETS ARE PERMITTED" 的倒计时归零后会发生什么？
- Alexis 是谁？"被困于别处、不同时间"的存在与 "I am the ghost of better days" 的发声者是否同源？
- MM 字条的真正作者：是旧 Maya 的残留，还是另一个 Maya？
- sportswars10 与 sportswars14 中的诗自称 "Girl"、对 "Boy" 说话；sportswars14 里 Sensei 又自述"后脑有个声音"。这个声音的来源与目的尚无答案。

> 本角色 label 的检索索引，见 `索引/Maya索引.md`。
