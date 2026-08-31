# Wakana 事件线全析

> 源文件：`游戏文本/WakanaEvents.rpy`（共 4925 行，20 个 label）。
> 覆盖 label：3 个电话桩件（callwakanamorning / callwakanaafternoon / callwakananight）+ `wakananightgen` + `wakanadive` + date1/5/15 + `wakanaspecial15` + date25p1/p2/p3 + spring1–8。
> 定位：Wakana Watabe 是 Kumon-mi 高中的成年教师，也是这条线里把"活得清醒"这件事讲得最不掩饰的人——她的厌世不是姿态，而是有背书的：早产与脊椎畸形、长年服药、一段从大学延续到现在的同居关系。她的 love 线表面是毒舌与诗歌，实际推进方式是两个人轮流交出最不体面的那一部分：date15 她看见 s 崩溃，spring3 她在他怀里哭，spring5 他讲出童年的性经历，spring7 她讲出求婚被拒。
> 阅读提示：本文以 label 名为唯一锚点，可在 `WakanaEvents.rpy` 中直接检索核实；英文台词为源文直引，不做翻译性润饰。凡跨文件核实的内容（如 Twi 语台词、Karin Kanda 的身份）均在句中注明出处文件。

## 一、角色基本盘

- **身份**：Kumon-mi 高中教师，负责批改考卷、诗歌教学与弓道部指导；与 Osako 是同居恋人；与 Imani、Rika 同属一个小圈子——`wakanadive` 写的是四人每周一次、被她们自己称为"传统"的酒吧聚会。
- **表层人格**：厌世毒舌，开场即用口头禅 "I want to fucking die."。这句台词在 `callwakanaafternoon`、`wakananightgen`、`wakanadate1`、`wakanadate5`、`wakanaspring6` 中依次出现，是她最稳定的情绪基线；`wakanadate1` 里 s 问她是不是对所有人都这样接电话，间接确认了这是她的默认开场。
- **文学性思维**：一切体验先经过文本中介。最爱的诗人是 Poe，最爱的诗是 Byron 的 "She walks in beauty"——两者的区分由她本人在 `wakanadate1` 里说清；对 Frost 的厌恶是明确的立场宣示："Frost was a hack."；`wakanaspring7` 以 "my death-grip on life is loosening even quicker than Kafka's battle with tuberculosis" 自况；`wakanadate25p3` 以 "Are you familiar with Ecclesiastes 3:1-8?" 收束全章。
- **隐藏层一（身体）**：`wakanadate25p2` 披露她早产，由此带来"一系列健康问题，其中一些比另一些严重"；其中之一是脊椎畸形，富裕的家庭付得起矫正手术，但"即使是最负盛名医院里最有经验的外科医生也难免出错"，脊椎一处闪失即可终身瘫痪。她的自我评价是"在所有体力事情上都轻度无用"。同一 label 里她承认自己对止痛药"很不负责任"，因此出门不带药，并在走不动时求 s 背她；label 的最后一个词则是她回应 s 那句"Osako 要是看见我们这样会怎么说"时的 "Don't."
- **隐藏层二（关系）**：与 Osako 自大学时代交往——`wakanadate25p3` 里的紫色餐厅是她们第一次约会的地方。两人约定不靠她父母、只靠自己的收入过活，理由是"依赖别人到那个程度，意味着对方一抽走地毯你就可能被彻底毁掉；而如果我要被谁彻底毁掉，我宁愿是我的伴侣而不是我父母"。裂缝自 `wakanaspring1` 起进入前台（新药与性生活），到 `wakanaspring7` 引爆：她求婚被拒，分歧点是孩子。
- **自我呈现**：`wakanaspring4` 里她说自己发在社交账号上的每一张照片都是花，"谁想看我的脸，现实里随便看"。
- **元叙事位置**：`wakanadate15` 中恶意旁白在她面前接管叙事，她是唯一从头看到尾的目击者；`wakanadate1` 中 s 关于"时间扭曲"的独白完全围绕她的职业困境展开；`wakanaspring6` 是她直接介入 Ami 的归家线，并以系统判词 "{i}Ami is now {b}PENDING{/b}!{/i}" 收尾。

## 二、love 线逐事件脉络

### callwakanamorning / callwakanaafternoon / callwakananight

三个电话桩件，主要作用是分流。`callwakanamorning` 在 `wakanadate1` 未完成时直接跳入该事件，并在 `wakana_love >= 15`、`yumiyukispecial1` 完成且 `wakanadate15` 未完成时跳入 `wakanadate15`；进入 ch3 / ch4 后改为跳向对应的 gen 事件。`callwakananight` 在 `wakana_love >= 5`、`wakanadate1` 完成且 `kaoridate15p3` 完成后跳入 `wakanadate5`；其余时段（含 ch4）只是一句 "I guess she's busy tonight."。

三个桩件共有的前置条件：只要 `secondbeach18 == True` 且 `christmastwo20 == False`，三个时段一律改为 "I should probably give Wakana a little space for now."；`senseisad == True` 时则拒绝拨号。

真正有对白的只有两段：上午她一句 "What do you want?"、听说 s 只是想聊天就回 "Nothing? Okay. Goodbye."，全程只有"在忙"；下午她先答应 "Sure."，发现 s 是要求现在出门才改口 "You meant now. Yeah, I can't do that."，最后以 "I want to fucking die." 挂断。

### wakananightgen

无剧情推进时段的默认相处。她开口的 "I want to-" 被 s 抢断，条件式地答应去"我们第一次互留号码的那家咖啡馆"喝茶——条件是 s 说任何一句哪怕稍微惹恼她的话她就走。结果是她整晚瞪着他、一次也没威胁离开，喝掉的茶多到 s 数不清；旁白估算她最后付了约六千日元的茶钱。接到伴侣叫她回家吃饭的电话后，她撑开一把"不知从哪儿变出来的"伞走人。旁白补了一句关键信息：Osako 过去已经确认过，Wakana 确实在某种程度上享受 s 的陪伴。结算 `wakana_love += 1`。

### wakanadive

酒吧聚会的通用件，也是她与 Imani、Rika 同属一圈的直接证据。四人的相处被 s 描述成"在和 Imani、Rika 聊天的迷宫里导航"——"她们居然真的享受社交，这点跟我们很不一样"。两人挤出的空档聊的是诗歌，以及 s 不遗余力想套出的"她给女友做了什么"。散场后按"不让任何人独自走夜路"分成两组，s 与 Wakana 拼出租车回家，全程一言不发却并不尴尬——s 的说法是"我们已经耗尽了最后一点力气，选择只是'在'一起而不必'回应'彼此"。结算 `wakana_love += 3`、`imani_love += 1`、`rika_love += 1`。

### wakanadate1 —— 办公室改卷与文学沙龙开幕

首次正式独处，由早晨电话直接触发。她在周末清早就待在学校办公室改卷，把 s 叫来当免费劳动力。开场即确立她的口头禅，也确立她与 s 的说话方式：s 夸她漂亮，她先回 "Thank you. I appreciate that."，再补一句"再多就不专业、也不该有了，何况我的另一半能在不到十秒内把你的胳膊像牙签一样折断"。

中段有两处固定的立场展示：一是她对 Makoto（Miyamura）的偏爱——s 指出这位"最 pure as the whitest snow"的学生其实在色情店打工，她的回应是"在色情店打工的那个同龄女生不戴眼镜，完全是两个人"；二是 Frost——s 用 "the road less traveled by" 接她的话，换来 "Don't try to appeal to me through overrated literary references. Frost was a hack."（bonus 分支里她的措辞是"一个只要有机会就会去操树的人"，s 问她是不是对此特别上心）。她还顺手解释了办公室比 s 小是"日本职场更重视男性雇员"（bonus 分支追加"哪怕这些男性整天在走廊里游荡、用眼睛鸡奸学生"）。

本 label 的核心是她讲出的职业困境，以及 s 由此展开的时间扭曲独白。她说自己并非不喜欢这份工作，而是"仿佛不再有真正的回报了"——这份工作最满足的部分是"看着自己栽培的花终于被摘下、插进全日本的花瓶里"，而那种回报感"比以往任何时候都远"。s 随即顺着推演：如果她的记忆像其他人一样跨重置延续，而她的职业满足感全押在学年结束那一刻的释放上，她就会被困在 limbo 里——"无止境地追一个拿不到的目标，却仍然相信它就在拐角处"。

诗歌部分分两段。她先背出 Poe 的 "But when within thy wave she looks- / Which glistens then, and trembles- / Why, then, the prettiest of brooks / Her worshipper resembles; / For in his heart, as in thy stream, / Her image deeply lies- / His heart which trembles at the beam / Of her soul-searching eyes."，s 认出是 Poe；她再从书架上抽出拜伦，念出 "She walks in beauty, like the night / Of cloudless climes and starry skies;"，并明确区分："你问我最爱的诗人，答案是 Poe；但如果是最爱的一首诗，是这首。"理由是"相当难为情，我不想说"。

（按：这段 Poe 引文在 `wakanaspring4` 的大学闪回里被 Osako 当堂朗读，标题由教授点明为 "To the River"——两段是同一首诗，本线前後呼应。）结尾她把书插回去继续改卷，s 只改了三份就走人，并承认自己胡乱打分。结算 `wakana_love += 1`。

### wakanadate5 —— 周年纪念、厨房灾难与 Jell-O 真相

由夜间电话触发。她开口要帮忙，s 以为又是改卷，结果是做饭——这天是她与 Osako 的周年纪念，"因为她才是那个包办一切的人"。s 到门前先在楼下遭遇 John：那只鸡独自站在灯下念《约翰福音》15:13-15（"Greater love has no one than this: to lay down one's life for one's friends."），念完还跟 s 打招呼 "Sup."。这一幕与烹饪本身无关，是本 label 的荒诞插曲。

厨房里她连"汤要用锅"都不知道，被 s 问住后改口"……蛋糕？"，再被追问"……在煎锅里？"就炸了。下锅的东西包括：s 从柜子里翻出的盐、鸡高汤和一包"红色的东西"，她自己找来的整根胡萝卜、泡面、半瓶蛋黄酱和几包外带酱油。汤最后开始凝固。她给出的动机很朴素："我一年可以有三百六十四天躲着厨具，但这一天我必须至少试一次。"她的自我评价则是 "I was not designed for love."

Osako 推门回家，先问 "What is he doing here?"，弄清状况后立刻软化，并自己承认 "I...get jealous a little too easy, I guess."。红色粉末的真相由 Osako 揭晓——是夹在蓝色和黄色粉末之间的 Jell-O，汤因此变成了甜点。Osako 拉着 s 一起去便利店补货（顺路有事要谈），事件转入 `osakodate1`。临别前她对 Osako 说 "I bought a new rope that should be a little easier on-"，被对方红着脸打断（bonus 分支内容）。结算 `wakana_love += 1`。

### wakanadate15 —— 图书馆诗歌大赛与恶意旁白接管

由早晨电话在 `wakana_love >= 15` 且 `yumiyukispecial1` 完成后触发。她不在学校，而在市立图书馆——她自揽了新工作：为学校女生办一年一度的诗歌比赛，主题是 Kumon-mi，为此还要"补一补自己忘了的基本功"。她把 s 拉来当共同评审。

收到的投稿里，Nodoka 那首借"火龙果"写"渴望剥光我的衣服、尝遍我每一寸"的作品被取消资格（Wakana 承认"我其实挺佩服的，只是被题材吓到了"，并指出它跟 Kumon-mi 毫无关系）；Fukuyama 的诗把 love 押 love——"有可能是有意为之，但我几乎可以肯定那是失误，而规则规定一旦提交就不能收回"；Noriko 的那首她认出写的是 Hamori River 沿岸的花，因为她和 Osako 走过那条路，如今"听说那一带几乎荒废了"；她称 Noriko 这首是到目前为止她最喜欢的。最后是 Ami 的 "Summer. Winter. Paradox. No autumn, nor a spring; / At night, I watch the sakura peel themselves off thick, red strings. / Why can I see what isn't there? Why can't I feel the sting? / Of the town that took the world away and the evil song it sings."

她说这首诗让她想起年轻时追过的一位笔名诗人，一位据说同样出生并成长于此地的诗人，并说出那句 "The girl who cannot breathe..."。话音未落，恶意旁白接管：{i}Uh-oh!{/i} → {i}It looks like you might have remembered something!{/i} → {i}Remembering things is bad! Remember to remember that!{/i} → {i}This is all just a game! It's all part of a game!{/i} → {i}It's not real at all! Nothing is real!{/i}，黑屏后只剩一行 "but if that's true, why is everything so much bigger than you?"。

s 失态，把她按在图书馆墙上要求"离开这里、去做点更大的事"。她先用 "Just a minor lover's quarrel." 替他挡下图书管理员，然后连续逼问 "Do you want to have sex with me, Arakawa? / Is {i}that{/i} why you're cornering me like this?"，并要他复述她在他动手前说的最后一句话。s 说不出来，她只回 "Your eyes say otherwise."。她允许他靠着她待到平静下来，条件是别把舌头伸进来，也提醒他"我女朋友大概也不会喜欢这一幕"。最后一句是 "You're a lot uglier up close."

结算是本作最锋利的一次判词：{i}Wakana's affection does not rise.{/i} / {i}But she saw who you really are today.{/i}。结尾旁白："The rest of the day disappears once you let her go...along with the three poems and the words uttered thereafter."

### wakanaspecial15 —— 酒吧夜、当众接吻与洗手间场景

酒吧聚会，玩的是真心话大冒险（Imani 提到"我们俩完成她的 dare"，Rika 则抱怨"没人 dare 她们就自己亲起来了，这不合规矩，我要退款"）。Osako 加班迟到，一进门就被 Wakana 按着长吻；Imani 打趣"要么是新药的副作用真的上头，要么就是被我们完成她的 dare 给撩着了"。

随后 Wakana 宣布要"把这个人带走一会儿——我们在洗手间会更有隐私"，临走前对 s 丢下一句 "best of luck, Arakawa. I can only imagine how hard it must be for you right now."

洗手间场景在本文件内是完整写出的，不是压缩：Master/kitten 框架，Wakana 全程主导并掌握命名权——她给 Osako 的称号是 "my kitten"，Osako 对她的称呼是 Master。具体的权力语法包括她抱怨手铐忘在家里、提到床头柜里的黑色振动棒"因为你的缘故近来额外加班"、点数这个月已扯坏的第三条内裤、以"我会直接走出去、让你永远到不了"作为停止指令，最后命令 "cum for me, my kitten...That is an order." 并在公共洗手间完成。

回到桌边后，Rika 自曝 "I'm 42."，Imani 崩溃于"我和一个四十二岁的人亲过"，并翻出自己被 Rika 打过 6 分的旧账；Wakana 让刚回神的 Osako 给自己的吻打分，Osako 答 "A million..."，她当场换算成"大约比 Imani 好 166,665 倍，恰巧也就是我教得比她好的倍数"。

结尾是容易被忽略的一拍：Wakana 回到桌边后整晚再没理会 s。旁白原句是 "It feels different all of a sudden. And it distracts me for the rest of the night."。结算 `wakana_love += 1`、`imani_love += 1`。（注意：本 label 展示的是这段关系最牢固的样子，`wakanaspring1` 起才是裂缝。）

### wakanadate25p1 —— 书店、二十首诗与 "Nothing anymore."

开场是办公室喜剧：s 对自己的桌子说 "I love you, desk."，被推门进来的 Wakana 撞个正着，从此一路拿"你想和你的桌子做爱"开涮。她邀请 s 去"城里"，被追问理由时给出的是罕见的直白——"因为你是我朋友，我把你当一个人看"——同时开出条件："别再把我按到墙上演硬汉了，上次我可一点也不享受"（直指 `wakanadate15`）。目的地是 s 曾与 Futaba 去过的那家书店的第三家分店。

真正的请求在书店里抛出：她在独立调查 The Girl Who Cannot Breathe。她给出的理由链是——海滩上得到过一句提示；Ami 要么天赋异禀，要么抄袭，必须查清；而 Ami 一共投了二十首诗，"每一首都能赢"。她的立场是：如果 Ami 真有天赋，那她可能正走向"一个比你我更早迷失在黑暗里的人"的老路；"你是她的监护人，难道不正是你的责任吗？……我们是教师，我们必须帮她。"s 顶回 "It's just a poem, Wakana."，换来的是 "You know damn well that nothing is 'just a poem,' Arakawa!"——她当场承认自己前几天说《The Road Not Taken》"只是首诗"是出于偏见和装腔，并改口。

s 全程回避，最后她问 "What {i}are{/i} you to her?..."，s 只答一句 "Nothing anymore."，随后走出书店，把她一个人留在店里。结算 `wakana_love += 1`，直接接 `wakanadate25p2`。

### wakanadate25p2 —— 道歉、背人与身体史披露

街上的对话是两条线的交叉：她为越界道歉，s 反呛"我从没为把你按在墙上道过正式的歉"；s 要求她停止调查，她回 "If you want to refuse to divulge information to me, fine. But don't just outright lie to me. That's rude."

同一段里她交代了自己为什么非要 s 参赛写诗——"我每天都得看着你那张恶心又毫无表情的脸，同时清楚地知道你在压抑着什么、把自己弄得更丑"，并给出她反复给出的建议："写。不为给别人看，写作能把情绪在不拖累任何人的前提下放出来。"她对自己的厌世也给了界定："I despise every fiber of {i}every{/i} person's being...But I am glad you are a part of my life."，并说她一直对 s 严厉，是因为"我知道你能比现在好得多，而你就是不肯，这让我火大"。

随后她绕了极大的弯子求 s 背她——先问"背你会不会让你好受些"、连问三遍"你确定吗"，最后才承认："我的腿开始发抖了……我实在走不动了。"她解释自己出门不带药，是因为"我证明过自己对那些药很不负责任"。

被背着的路上她披露身体史：早产 → 一系列健康问题 → 其中之一是脊椎畸形；家里有钱支付矫正手术，但外科医生也会犯错，"脊椎是脆弱的东西，一处闪失或损伤就可能让你终身瘫痪，所以我很庆幸只落得这样"。她也说了自己仍然做得到的事：在 Higashigaoka 时代练过弓道，医生建议她换项目，她退让到"不能参加比赛，但一周能射两天"，如今则成了一群"毫无经验的公立学校女生外加一个不知为何很强的 Ushibori"的弓道指导。她还提到自己的伴侣能"背着她横穿全日本而不出一滴汗"。

结尾 s 问 "I wonder what Osako would say if she saw us like this."，她只答一个词："Don't."。结算 `wakana_love += 1`，直接接 `wakanadate25p3`。

### wakanadate25p3 —— 紫色餐厅与十年之爱的考古

她带 s 去的是那家"紫得不像话"的餐厅：她大学时代起的最爱，与 Osako 的第一次约会也在这里，而 s 是除 Osako 之外她带过的第一个人（她要求他别把这件事告诉 Osako，"否则她大概会以为我们在上床"）。两人因此拌嘴，牵出 Myspace 的 "top eight"——s 是 31 岁、从没玩过社交网络，被她评为"地球历史上最无趣的人"。

经济立场在这一段讲清：她出身优渥，却与 Osako 约定只靠两人的钱过活，"因为那样活着更充实；也因为依赖别人到那个程度，意味着对方一抽走地毯你就可能被彻底毁掉——而如果我要被谁彻底毁掉，我宁愿是我的伴侣而不是我父母"。

她以"你在恋爱这件事上认识的人里最成功的那个"自居，逼 s 处理 Imani。s 给出的理由是他会毁掉她——"等她发现我不是她以为的那个人，她会开始恨我，然后开始怪自己当初没看出来"。她的回应是当场"从 Imani 的红娘职位上退休"。s 说出不追 Imani 的真正原因，用的是本作最平的一句："I'm just in love with her."（指青梅竹马 Niki）。她顺带承认自己对男人也有欲望——"You {i}do{/i} know I'm attracted to men as well, correct?"——并承认若能和一个"格外有魅力的名人"三人行她本人并不介意，但"Osako 不是这么想的，她的想法和感受至少和我同样重要"，因此作罢。

阴影在这一段的尾部：她提起"那次我服药过量进了医院，而你完全无视我的存在"，s 说"那是好几年前的事了，该翻篇了"，她立刻反驳 "It's not been {i}years,{/i} Arakawa. Years would imply that-"——话被静电切断。此后她沉默良久，问出 "Are you familiar with Ecclesiastes 3:1-8?"，画面直接黑屏（答案不在本文件内）。结算 `wakana_love += 1`。

### wakanaspring1 —— "拿下他"、海滩旅行与淋浴间对峙

开场是绑架式喜剧：Wakana 与 Imani 闯进 s 家，命令 "Imani. Seize him."。Ami 的 "Dad" 梗在此被 Wakana 正面驳回："这男人不是你父亲，多半是给你洗脑了"，并要 Imani "在他继续洗脑之前拿下他"。目的地是海滩：只限教职员加 Osako（她的 plus-one）的一夜旅行，Ami 的班级旅行还要几周；s 想带 Ami 被拒，理由是"她会毁掉一切"，Ami 自己也认："It's sad because it's true."

旅店里 Imani 说破了真正目的：Wakana 和 Osako 最近在吵架，这趟是 Osako 攒的局，想就此止住；Wakana 一路撮合 s 与 Imani，只是"为了让气氛轻松、转移注意力"。她说 Wakana 近来"off"，"不只是工作上的那种拼命"。

真正的裂痕在淋浴间，s 与 Imani 隔墙听见。Osako 说从"一天好几次"到"几乎没有"很怪；Wakana 先以玩笑岔开（提出"要不要你去睡 Imani"），被 Osako 顶回后给出实情：新药"大概正在鸡奸我的性欲"，但性欲缺失好过"背疼得要死的同时还发情"。Osako 承认那次提议的来由是 "Babe! You {i}never{/i} cum! Like, {i}ever!{/i} And that seriously {i}fucks{/i} with me."，并说自己并不是真的想要那样。Wakana 的回应先软后硬——她承认自己近来心思被"一位挚友的安危"占着，随即爆发："那么也许需要别人的是你？"（"Maybe {i}you're{/i} the one who needs someone else?"）同一段里还交代了她们过去每周在 Wakana 办公室做爱（"我的办公室我能锁门，外面的世界我锁不了"）。本 label 无好感度变动，直接接 `wakanaspring2`。

### wakanaspring2 —— 篝火夜、King's Game 与被打断的半句话

沙滩篝火夜。她自己解释状态："我不是醉了，我是'上头'——酒精对我没用，但它跟新药一起就有用。"Osako 补一句 "I {i}did{/i} tell you not to do that."。她趁机翻旧账："要是我又进医院，也许这次 Arakawa 真会来看我了，你这个混蛋。"席间众人交换高中毕业年鉴式的"最有可能"头衔：Osako 拿过"最可能拿奥运奖牌""最可能环游世界"和"最佳笑容"，Imani 是 class clown，Wakana 则"什么也没拿到，因为我上的那所名校只收最拔尖的"。

游戏环节：Imani 想玩 King's Game，并为了抗议自己"明明有一半日本血统却从没玩过日本饮酒游戏"而大讲美式游戏 Stump（树桩、钉子、锤子，翻转锤子砸别人的钉子，砸中就罚酒，失手也罚酒）。Wakana 打断，改玩真心话大冒险：先"敢" s 去亲 Imani，被 Osako 劝住后改成 "Then I dare {i}Osako{/i} to kiss {i}me!{/i}"。两人在沙滩上当众长吻；Osako 问"你还生气吗"，她答 "For tonight, we shall live in the moment — lest the troubles of the daytime grind these weathered bones to dust."

转折在她转回撮合 s 与 Imani 时：她说到 "Hahah! It's funny you mention that, because earlier-"，被 Osako 一声 "Wakana!" 厉声切断，两人随即离席去散步。旁白的判断是不确定的："I think I saw tears in her eyes, but I can't be sure. She was gone too quickly."

本 label 的收束是 s 的独白，不是她的台词："I let my friend get lost at sea. The current reeled her in."。同一段里 Imani 在两人接吻时忽然用一句 "Medɔ wo." 换了语言，s 说听不懂，Imani 只回 "Look it up...jerk..."（按 `ImaniEvents.rpy`，这句话是 Twi 语，s 后来在圣诞事件中查过，追问 "Is it true, Imani?"，Imani 慌忙抵赖，含义始终未由角色明说）。本 label 无好感度变动，接 `imanispring1`。

### wakanaspring3 —— 寄生虫独白、清洁指令与 "That never happened."

开场独白是 s 的第一人称，不是 Wakana 的：他自称"人见人爱的半实体寄生虫"，今天要找个宿主钻进去，"靠他们的血而不是我自己的血活着，因为我自己的血有时会吓到我"；随后依次点名云、光、风。

紧接着是 Wakana 第一次主动打来电话请他过去——"我可以只是需要有人陪"，而 s 立刻点破她"平时打电话都是有求于我"。到了之后她先用一串荒唐指令压场：清淋浴间、洗地板、"要是你能钻进烤箱里就更好了"（指的是清洁），s 全部应下；她看穿了动机："能重新有点权力，感觉不错吧。"

实质内容紧随其后：她说和 Osako 之间"不完美"已经好几个月，是海滩那趟之后才真正开始变；她习惯了两人一直以来的样子，因此"看到她努力变好，反而让我脑子里有个声音说这一切都不对"。她解释为什么找 s 而不是 Imani："Imani 有她的长处，她在数不清的方面都比你强。但我跟你在一起更自在。"——s 误读为"我把你当兄弟/表亲"，她纠正：那只是玩笑，"我不觉得'什么都没有'，我觉得安全"，并说 "You're extremely special to me."

随后是哭泣拥抱：她要求他抱紧她、让她哭一场，条件是他闭上眼睛以保全她在他心里的形象。s 每看她滴一滴泪就替她许一个愿——愿她幸福、愿她的爱能活下来、愿有一天他们能走出这个地方、最后愿她别再哭了。约三十分钟后她抽身，只留一句 "That never happened."，然后"变回 Wakana"。

余下的群像段牵出四人行：她说 "I can't believe I allowed you to see my naked body — even in the throes of a foursome."，s 说不敢相信的是 Osako 允许；她接 "Yeah, that was...{i}odd.{/i} But I suppose it...might have been her first step?"，话说到一半自己掐断——"不，去他的，别再说这些丧气事了。"她要食物和酒，s 说有地方要去，转入 `wakanaspring4`。结算 `wakana_love += 1`。

### wakanaspring4 —— 重回紫色餐厅、生日、最后通牒与那次课堂朗读

s 主动把她带回 `wakanadate25p3` 的那家餐厅，坐的是"第一次来时的同一张桌子"。闲聊里她说出自己的生日是 10 月 10 日（s 猜万圣节，她评"够接近了"），并发现 s 记不起自己的生日、也不随身带证件。

中段是最后通牒：学年结束前不回学校，"我就把你宰了埋在你家后院"。s 心里想的是"学年永远不会结束"，于是爽快答应——"许下一个我没有打算兑现的承诺"，并自我安慰"对某人隐瞒真相，和撒谎不是一回事"。

s 反问她的童年。她说自己从小就很"gloomy"，因此没人在意；因为穿着、读的东西和写的东西被取笑过，但对方发现她不在乎就放弃了。她给自己的定性是"怪女孩"，"一半原因是几乎对一切都不感兴趣，另一半是我在身体上做不到同龄人能做的事"。她也给出一段明确的文学观：那些"什么都不用努力就一拍即合"的关系根本不存在，"都是些想靠浪漫题材赚钱的蹩脚作家编出来的"——"至少我以前是这么想的"。

闪回随之而来（大学课堂）：教授点名 "Next — Osako Osaka, reading 'To the River' by Edgar Allan Poe."，Osako 紧张到要抱着笔记本才敢念，念完后一直站在原地望着某个方向，同学窃语 "Watabe, probably. She's always looking at her."。她念的正是 `wakanadate1` 里 Wakana 背给 s 听的那一段。回到现在，Wakana 改口："也许'立刻就知道会不会合拍'这件事确实有几分真。"并说从那一刻起她的人生"充满了颜色，都是因为一个害羞又敏感的体育生"；"他们想把我切开多少次都行，我会一直期待下去，因为我知道前面有什么。"

她对 s 说的是祝福而非安慰：希望有一天你也能遇到那样的一刻，看见某个人、某样东西，心想"这就是我在这里的理由"；"我现在可能没有够两个人分的幸福……但如果哪天有了，希望你能分走一些。"

结尾：她翻出自己发过的所有照片，每一张都是花，s 要了一张；回程最后一段路 s 又背了她一次（"其实大概不必"）；到家门口他"行使了一项新到手的权利"——`wakanaspring3` 里她给过的拥抱许可——并说"我想这事还会再发生"。结算 `wakana_love += 1`。

### wakanaspring5 —— "I AM VERY SAD"、童年性经历与 "I just want Ami to come home."

开场是四行诗（s 的旁白口吻）："I can't show you what I look like. I can't mimic how she speaks. / But I'll hold your hand and weep with you when tragedy repeats. / Because time is sure to take me next — and when it does, don't fret. / Just leave my ashes on display somewhere you won't forget."，随后屏幕打出特大号 {b}I AM VERY SAD{/b}，紧接一句旁白自述：自己一直都很悲伤，也经历过几段比平常更重的时期，"Like when I raped Molly or killed Maya."，下一句立刻自我消解 "Okay, I'm good now."——（这句"我"是 s 的旁白声音，不是 Wakana 的供述；它把主线两大悬案以一句黑色玩笑扔进本线开头，随即被回收，没有任何确认。）

房间里 Niki 留下的外卖单、烘干机里 Ami 的一只袜子，他一样也挪不动。他打电话给 Wakana，她说 "We can be miserable together then."，并索要"我也要一个拥抱"作为回报。

她一到就说要"报答"他此前为她做的一切，边扎头发边说"我要为你做点更好的事"，s 误会，她抄着刀澄清："我是要给你做饭，不是那个。"两人随后都承认她并不会做饭。s 改提看电影吃垃圾食品——"这是 Ami 和 Niki 还不恨我的时候我们常做的事"。她追问 Ami 怎么会恨他（"你们俩一直腻歪得让人反胃"），s 说出 Ami 离家、Niki 分手。

写作线再次被推：她说 "Writers {i}need{/i} to write."，s 答 "Writing {i}is{/i} suffering though, Wakana. How am I supposed to do that when all it does is remind me of what I've lost?"。她随后承认自己读 The Girl Who Cannot Breathe 比他认识的大多数人都要多，理由是"这是你什么都不肯告诉我的时候，我唯一能了解你的方式"。

s 于是第一次正面讲出童年：他曾经崇拜"她"，以为她是某种天使，所以她想多花时间陪他，他就乐意奉陪；"关系变得性化之后，我从来没有真正试着阻止她，至少没有认真过——尤其知道那样做会在我唯一一段好的关系里撕开裂缝。"他说的理由是"我只是不想失去她"。他还说现在有时仍能看见她、闻到她，"每次我拿起笔，几乎能感觉到她悬在我肩头，纠正我、给我建议"。

她的判断被 s 逼出："You concede that it was romance, then?"——她的回答分两层：道德上不承认；但"没有第三方能真正理解另外两个人之间的感情"，结合她的诗作与她对 s 的影响，"不承认那里存在某种形式的爱，是愚蠢的"。她说读到的那个 "Boy" 在她诗里总是"无助而天真，像是不完全明白发生了什么"。

结尾回到当下：她问"现在这一刻，什么能让你好受些（口交除外）"，s 答："I just want Ami to come home."。她说那是她听他说过最像人的一句话，并提出自己可以去和 Ami 谈；s 给的口信是"就告诉她我很抱歉"，又承认自己其实并不觉得抱歉。两人互问是否说谎，答案都是"一直都在说谎——让日子好过些"，她补一句 "Don't look {i}too{/i} hard. You might not like what you see."。最后她推荐 Dead Poets Society 被赶出门。结算 `wakana_love += 10`——本线单次数值最高的一次。

### wakanaspring6 —— 办公室会谈、死亡必然性与 PENDING

午休时的学校。Wakana 主动拦下 Ami 带进办公室，一路以"我用办公室里的秘密抽屉把你绑起来"之类的玩笑维持喜剧密度，直到她一句点破："那不是恶心的原因。我想，我们之间的年龄差在你脑子里根本不算什么——毕竟你妈妈就是那个 The Girl Who Cannot Breathe。"

她说自己不是来辩论她母亲行为的道德问题，只说"不管她做过什么，她都极有才华，并把这份才华传给了你'丈夫'和你"。Ami 反弹：赢比赛是侥幸，她写了一百万首，"Noriko 的每一首都更好"，选她只是因为 Wakana 想多了解她妈妈。Wakana 承认这可能占了一部分，并说她原以为 Ami 连谈都不肯谈——"更别说 Arakawa Sr. 还叫我别多管闲事"。

她的核心劝说是：你是你母亲留下的唯一一块；你每离开"父亲"一秒，就等于她再离开一次。Ami 的回答是本作关于死亡最完整的一段：一切随时可以结束（陨石、动脉瘤、被谋杀），"你把醒着的每一刻都用来难过，就是在从一份非常有限的幸福里扣时间"；"人死了不会重来一次，就这么完了"——她母亲就是这样，"在她有机会向所有人而不只是见过她的人证明自己有多好之前"。她反驳"她想挑战世俗"的说法："那不是她想做的事，那就是她这个人。"她给自己的定性是：继承的不是才华，而是"对一个不想要她的世界的怨恨、随之而来的无限自责，以及一双我永远填不满的鞋"；回家"只会是更多的演戏，是血流不止的伤口上的一块创可贴"。

Wakana 的回应有两处值得记：她指出 s 把同样的话（先别管）也说给过她听，"只是他没像你这样写下来"；她说 s 若不是真的需要帮助，不会开口求她去找 Ami，"而我愿意帮他，是因为他帮过我"。

结尾是 Ami 的两句评价与一次更正。Ami 说 "you'd make a good mom, Miss Watabe."，并说她是"我爸能得到的最接近我亲妈的人——至少在他这个年纪里是"；又说"要不是你已经是 lesbian，你们俩会是很甜的一对"。Wakana 更正的是自己的性向，不是 Ami 的："I'm...bisexual, technically."（与 `wakanadate25p3` 里"你也知道我对男人同样有欲望吧"一致。）Ami 丢下一句"也许吧！回头见，Watabe 老师！这次谈得还挺有收获的！"夺门而出。

独自留下的 Wakana 说了两句——"Fucking Arakawas...Ending every single conversation by just making me more confused..."和 "I want to fucking die."——系统随即弹出 {i}Ami is now {b}PENDING{/b}!{/i}。结算 `wakana_love += 1`；事件以收到 Karin Kanda 的图片消息收尾。

### wakanaspring7 —— 酒吧、求婚被拒与本线的终点

夜里她打电话来："It's time to get drunk."，并把地点从常去的那家改到"我不愿说出名字的那家"——她在电话里报的名字是 Sakaki-bar-a，旁白则一律记作 [[REDACTED]。

Sara 先出场，抱着一箱给她女儿 Sana 的哥特服装来找她，为拖延道歉。Wakana 以 "Be gone, barmaid." 逐客；Sara 问她要不要再找一份工作（"上一个酷而神秘的女士坏掉了"），她答："不。但如果哪天我放弃这份职业、决定用余生专门气我父母，我会通知你的。"Sara 临走前点酒，Wakana 说 "Ten. And ten for my partner here as well."——s 追问 "{i}Partner?{/i}"，她只确认 "Partner."（一句喜剧误会，为后文的"种子"铺垫。）

Sara 走后正戏开始。她先说药物与酒精冲突、"你大概要赢我一回了"，并给出药效的准确描述："This medication just winds up turning me on and then making me tired."（`wakanaspring8` 里她会否认自己说过这句。）随后她罕见地反问 s："Arakawa, may I ask exactly what you see in me?"——因为她知道 s 的调情不是只看脸。s 想岔开，她直接掀牌：

> w: I asked her to marry me.
> w: Because she turned me down, obviously.

原因冷酷而具体："I don't want children, Akira."——而 "Osako {i}does.{/i}"。她反复强调的是"我竟然从来不知道"："一半应该了解它的另一半，而我就是不知道。"s 试探"也许这是她新冒出来的念头"，并说"也许某件事或某个人让她意识到，看似不可能的事其实并非不可能"，她立刻接住：

> w: So it was {i}you{/i} who planted the seed.

s 辩解自己只是"聊到 Ayane，然后一句接一句"。她的态度是不追究，反而庆幸："If anything, I should be thankful this happened now instead of another decade down the line."——她说这不是一时冲动，"这类事不会凭空冒出来"，她也不希望 Osako 为了迁就她而"将就一段不够完美的人生"。结论已写好：

> w: I think this is the end, Akira.
> w: I think the dream is finally over.

她的自审是五个形容词："someone as selfish, obsessive, cynical, hostile, and overwhelmingly unpleasant as me"，以及"我所挣得的，全是我给出去的东西：怨恨、疲惫、痛苦"。s 的反驳先照单收下再往回推："you're also creative, hot, artistic, hot, eccentric, and really fucking hot"，随后许下本线最重要的一句承诺："You deserve at least one constant while everything else is changing."她的回应罕见地柔软："You're really impressive in a lot of really unpredictable ways sometimes."——理由是"你已经失去过对你意义重大的人，而且不止一次，却还站着劝我继续走下去，而你自己连走下去都费劲"。

s 用玩笑卸压："我也想要孩子。"她回 "Hilarious." / "Too soon."。随后她靠着他的肩睡去，醒来前旁白写下本线最诡异的收束句——"There is no more narration."。结算 `wakana_love += 1`；事件以收到 Rika Rokuhara 的图片消息收尾。

### wakanaspring8 —— 被占领的办公室与 Operation: Cathy Simms

开场旁白（本 label 用第三人称写 Wakana）："Another sunny morning, another reason to pull the curtain closed."——这句晨间咒语如今她在 s 的办公室里默念，因为原来那间屋子"满是她的痕迹：午后的幽会、随手存放的个人物品"。他们仍同睡一张床，但"没有深夜长谈，也没有谁先醒时随手乱摸；只是一张睡得下两个人的床——宽到她们除了梦里之外永远不必相触"。

Rika 与 Imani 闯入，带来两条信息。其一，Rika 已经开始给 s 发裸照，并主动坦白："I promise it's only until someone other than Akira is willing to have sex with me."其二，Wakana 一句顺口的话点破了 s 的处境："这不是你的办公室，Imani，是 Arakawa 的；除非你有胆子去教务处承认他再也不会出现了，它就一直是他的。"

喜剧密度由三条线维持：Rika 设想"教师是否像将军那样，把 Akira 赶下台会引发继承危机"；Imani 找订书机翻出手铐（并把那副手铐放进了 Wakana 此刻正坐着的桌子里）；Rika 提议跟 Wakana 上床，"朋友不就是干这个的吗"。

冲突在 Rika 提议"你也去睡 Akira 解解闷"时爆发。Wakana 的论点有两个层次：一是"他不是玩具"、"在他经历过这一切之后，利用他是最后一件我们该做的事"；二是本作对整条 harem 结构最清醒的一句判词：

> w: Having sex with Arakawa will not fix anything, Rika. In fact, sex as a {i}whole{/i} can not fix anything. It's just a bandage for a bullet hole.

Rika 断言她与 s 之间有 "some {i}crazy{/i} sexual tension"，Imani 以"我把你当成头号情敌"的身份作证（"你在那场疯狂的海滩性爱之夜眼睛一直黏在他身上"），Wakana 的暴怒一路升级到 "OUT!"。Rika 最后抛出方案：设计成她和 Osako 在两间房里分别面对"被诱惑"的局面——她自称灵感来自《The Office》第八季，Jim 在商务旅行中与临时工 Cathy 同住一室却对 Pam 保持忠诚，"如果你们俩都能抵抗诱惑，就会加固彼此的爱；或者一方失败，那就说明不该在一起"。Wakana 的答复是简短的 "No!"，并声明自己要的不是帮忙而是清静。

结尾旁白复沓开场句，并补上一刀："On more than just the light this time."。Rika 临走前留话："Let me know if you change your mind about Operation: Cathy Simms!"结算 `wakana_love += 1`。

## 三、lust 线概貌

本角色只有一条数值线 `wakana_love`，`WakanaEvents.rpy` 内不存在独立的 lust 分支或专属 lust label。按本文件内实际写出的亲密内容，可归为三组：

1. **`wakanaspecial15` 的洗手间场景**：这是本文件内唯一完整写出的性场景，Master/kitten 框架，Wakana 全程主导并掌握命名权（她给 Osako 的称号是 "my kitten"，Osako 称她 Master）。关键道具与规则由她口述：手铐忘在家里、床头柜里的黑色振动棒"因为你的缘故近来额外加班"、这个月已扯坏的第三条内裤、以"我会直接走出去、让你到不了"作为停止指令。功能是把这段关系内部的权力语法摆到台面上，与她在职场、社交里的退让形成对照。
2. **`wakanaspring3` 的四人行回顾**：以对话形式回顾，参与者在本 label 内未被点名。功能有二：她把它解读为"也许是她的（Osako 的）第一步"，即两人关系松动的前兆；她话说到一半自己掐断，与同一 label 里 "That never happened." 的否认机制形成呼应——先借来温度，再销毁证据。
3. **`wakanaspring8` 的语言性欲群像**：Rika 与 Imani 关于 s 身体的露骨对话（"dick-wizard"、制服、三人行时长）本身构成一种替代场景——当事人不在场，欲望由旁观者代述。这恰好坐实了 Wakana 的判词：所有人的性话题都是弹孔上的创可贴。

另需澄清两点：`wakanaspring7` 虽然写到了药效（"先让人兴奋、再让人困"），但该 label 内没有任何亲密场景，收束于她靠在他肩上睡着与 "There is no more narration."；`wakanadate5` 结尾那句被 Osako 打断的"新绳子"属 bonus 分支内容，是两人私下 BDSM 实践的直接证据，但本文件未展开。

## 四、与主线/元叙事咬合点

1. **`wakanadate1` 的时间扭曲独白**：这是循环世界观第一次落到 NPC 身上——s 推演若 Wakana 的记忆跨重置延续，而她的职业回报全押在学年结束那一刻，她就会陷入 limbo：无止境地追一个拿不到的目标，却仍相信它就在拐角。她本人只给出"回报比以往任何时候都远"的直觉。
2. **`wakanadate15` 的恶意旁白接管**：{i}Remembering things is bad! Remember to remember that!{/i} 与 {i}It's all just a game!{/i} 之后，黑屏抛出 "but if that's true, why is everything so bigger than you?"——元叙事实体不止观察 love 线，还会主动攻击可能唤醒记忆的节点。而这次攻击恰好发生在她面前，使她成为唯一目睹全程的人，并以 "You're a lot uglier up close." 完成反打。
3. **"affection does not rise...But she saw who you really are today."**：游戏系统亲自承认数值无法度量这次关系的改变；本 label 也是全作极少数"好感度不动却推进关系"的事件。
4. **`wakanaspring5` 的开场旁白 "when I raped Molly or killed Maya"**：主线两大悬案以一句旁白自述被丢进本线开头，但立刻被 "Okay, I'm good now." 自我消解，全篇没有任何确认或追认。这句话的说话人是 s 的旁白，不是 Wakana。
5. **`wakanaspring4` 的明知虚假承诺**：s 在"学年永远不会结束"的前提下许下返校承诺，并以"对某人隐瞒真相，和撒谎不是一回事"自我开脱——本线因此成为"重置者的谎言伦理"的检验场。
6. **`wakanaspring6` 的 PENDING**：Wakana 线直接推动学生角色的系统状态变更（Ami 由离家状态转为 PENDING），证明她不只是恋爱对象，也是 Ami 归家线的功能性支点。
7. **`wakanaspring8` 的两句判断**：一是她顺口说出的"除非你有胆子去教务处承认他再也不会出现了"——成年同事视角对 s 长期缺席状态最直白的确认；二是 "sex as a {i}whole{/i} can not fix anything. It's just a bandage for a bullet hole."——对本作 harem 结构的作者级判词（Ami 在 `wakanaspring6` 里用几乎相同的比喻形容自己回家："a bandage on a wound that's bleeding out"）。
8. **`wakanaspring7` 的 "There is no more narration."**：叙述者在关键情感节点主动弃权，本线此后再无任何旁白注释。
9. **药物与时间感的不可靠**：`wakanadate25p3` 里 s 说那次服药过量住院"是好几年前的事了"，Wakana 立刻反驳 "It's not been years"——话被静电切断。这是本作时间线不可靠的一处直接证据，也与"循环"母题咬合。

## 五、未解伏笔

1. **The Girl Who Cannot Breathe 的完整真相**：本名未在本线出现，只以笔名流传（"she always used a pseudonym"）。Wakana 在 `wakanaspring6` 中点破 Ami 的母亲就是她——结合已核验的家族事实（Ami 的母亲是 Sekai），二者指向同一人。s 为何对这条线只剩 "Nothing anymore."，本线未解释。
2. **Ami 投了二十首、首首能赢**：`wakanadate25p1` 给出的"天赋 vs 抄袭"二选一，在 `wakanaspring6` 里被 Ami 自己解释成"写了一百万首"，仍未给出定论。
3. **"过量服药住院"的旧账**：具体时间、诱因，以及"你从来没来看我"这句指责的本事，本线均未交代；且两人对"过了几年"的说法直接冲突。
4. **"Boy" 是否即 s**：Wakana 读出的是"无助而天真，像不完全明白发生了什么"，s 承认 "It was true at first."，但本线未作身份确认。
5. **s 的生日之谜**：她有明确日期（10 月 10 日），他连自己的生日都答不出，也不随身带证件。
6. **"one constant" 的承诺**：s 承诺在万物变化时做她的常量，这个承诺本身尚未被检验。
7. **Karin Kanda 的图片消息**：Karin 是全作另有专属事件线的角色（`KarinEvents.rpy`，Kirin 的姐姐），但她与 Wakana 线的关联在本文件内仅止于这条提示，未展开。
8. **Rika 的图片消息与裸照线**：Rika 自陈"只是等到有 Akira 以外的人愿意和我上床为止"，动机指向她自身的崩塌弧线，与 Wakana 线擦肩而过。
9. **Operation: Cathy Simms 是否会被执行**：Rika 临走时说"改变了主意就告诉我"，方案悬置在提议阶段，Wakana 当场拒绝。
10. **`wakanaspring8` 结尾的床头状态**：两人仍同床、尚未正式分开（她本人说法是"正站在那不可避免的命运边缘，而且这次更严重"），分居是否落地留到 Osako 线。

> 按 label 检索本角色全部事件与行号，见 `索引/Wakana索引.md`。
