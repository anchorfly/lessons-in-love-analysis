# Imani 事件线精读笔记（ImaniEvents.rpy，v0.55，共 5170 行 / 19 label）

## 一、角色基本盘

- **Imani Imai**：31 岁实习教师（Sensei 的 kouhai/后辈），加纳裔（圣诞约会提到"飞去加纳见父母"行2773；imanispring4 中 Rika 被附体时喊 "Kwesi? That you in there?" 行4940）。身材高挑（接近 Senpai 身高，行3909），全身有伤疤。
- **伤疤与身体羞耻**：从不穿泳衣、遮盖身体；知情者仅限好友团（浴场同行的 Wakana/Osako/Rika）+ Futaba、Yumi、Ayane（`imanispring2` 行2196-2202）。她自述已向 Senpai 解释过"我为什么是这副样子"，且那是她唯一主动隐瞒的事（`imanispring4` 行5060）。
- **性格**：外向聒噪、黄段子手、"medium-sized bitch"自评（行222）；实为全班最护犊子的成年人——把学生们视作家人（"they really do feel more like family than students to me" 行5099）。
- **关系网**：Wakana（挚友）、Osako、Rika（后发展为情敌+一夜之缘）、Yuki（隔壁邻居）、Senpai（best friend→恋人方向）。
- **调度结构**：`callimanimorning`(1)/`callimaniafternoon`(19)/`callimaninight`(37)；夜间入口需 `wakanaspecial15 == True` 且按 `imani_love` 阈值分发（>0→date1、>=5→date5）；未解锁时表现为"她不接电话"。`imanidive`(59) 为第六届宿舍战争潜水入口（按 `chap4active` 分发）。

## 二、love 线逐事件脉络

### imanidate1（行105）
首次单独约。电话里互相试探："Is this a booty call?"（行125）→ "Daddy?" 梗（行141）。她的破旧公寓首秀："Congrats on being my first ever visitor."（行173）；6/10 接吻评分旧梗（行175）；谎称养猫养鹦鹉然后自己拆穿（行195-200）。批改学生作业摸清全班性癖的桥段（行229），Senpai 确认彼此信任："you're not out to hurt anybody"（行234）。

### imanidate5（行410）
Imani 以"快死了"为由杀到 Senpai 家——实际是空调坏了要借宿（行476）。租金谈判名场面："I will let you choose between the 50,000 yen I'm paying for my current place or one sexual favor per week. No mouth." ——"No mouth, no deal. I'll take the money."（行494-495）。Ami 回家撞见"入侵者"（行529）。

### imanidate15p1（行792）
放学同走去酒吧。大段 meta 独白（"Why does everything have to be an event?" 行815）。Knock-knock 冷笑话连环（行818-826）。Rika 来电让气氛突变（"Wait, really?... Like...not at {i}all?{/i}" 行903-905），为 p2 的独处铺垫。

### imanidate15p2（行1151）
全员放鸽子后的二人酒吧→送她回家。Imani 自卑于"你不是在和明星约会吗"（行1175）。摊牌：Imani 先说 "Do you want to come inside?" 又收回（行1187-1193）；正式告白 "The jig is up. I like you. We both know it."（行1216）；Senpai 承认喜欢但选择 friend-zone："It's not about {i}gaining{/i} anything. It's about not losing something... there aren't many people I can have as friends."（行1244-1246）。Imani："This is just the first time I've ever been friend-zoned."（行1253）。

### imanispecial15（行1485）（即 imaniwakarin 系列）
与 Wakana、Karin 买万圣节服装。Wakana 名言："My quota for human contact today caps out at one person and Imani already counts as at least four."（行1501）；"I actually like your scars. They add personality."（行1507）。Karin 被介绍为"I know Imani is a monster underneath her clothes 俱乐部"成员（行1506）。Imani 对 Niki 海报喊话宣战（行1554 "Get bent!"）。Wakana 的 goth 店有"成人专用 back room"（给 Osako 拍私密照买道具用，行1602）。Imani 吐露感情困境："There's a guy I like, but the guy doesn't like me. Or...{i}does{/i} like me, but also likes someone else."（行1539）。

### imanispring1（行1831）
海滩夜话（四人聚会中 Wakana 与 Osako 单谈后）。两人担心 Wakana 的脆弱（"How...{i}fragile{/i} she seemed?" 行1875）。Imani 对 Senpai 的核心承诺："I'm your loyal kouhai and best friend who can be anything you need her to be. Just say the word and I'll do it."（行1913）。Senpai 反问 "Why don't you ever wear a swimsuit?"（行1920），逼出她"embarrassed/shamed"的心结（行1941-1942）。

### imanispring2（行2128）
别墅换装：Imani 克服心结展示泳衣/伤疤。叙述者独白："I want to see with my own two eyes what haunts her more than anything."（行2159）。她列出知情者名单并谈到与 Futaba 的"裸体互相治愈"经历和宿舍战争寻宝卡"something beautiful"选了她（行2211-2212）。Wakana/Osako 归来打断（行2246）。

### christmasimani1（行2668）
圣诞约会（市区，避开"其他女生"）。开场 meta 独白交代信息差：Osako 早就知道 Ayane 与 Senpai 的事却瞒着 Wakana（行2679）；Senpai 决定继续瞒 Imani，"She's cuter when she lives in whatever world allows her to believe I'm not even half as terrible as I am."（行2678）。约会本体大量黄腔互怼（boner time、水果梗、"Racism." 行2781）。结尾表白式台词："it might not be love-love yet... I'd be really happy if the rest of my Christmases were just like this one."（约行3000-3040），随后 `$ christmasimani1 = True; $ imani_love += 1; jump christmasimani2`。

### christmasimani2（行3047）
圣诞树场景（延续上一事件，装饰/礼物互动；本事件以温馨收束为主，末尾 end_replay 行3041 前）。

### christmasimani3（行3308）
圣诞派对（Tsukioka 宅，Touka 出场抓包："Miss Imai? Sensei? Where are you-" 行3416）。开场超长 meta 独白：修士们（the monks）与 Malvin——"Malvin was never {i}raped.{/i} He was just a kid. And so was I."（行3336-3338）；对 "[[REDACTED]" 说 "You'd probably think I'm just some predator trying to look cool."（行3335）。Senpai 因回忆失控要求 Imani 说话分散注意力（行3344），随后以"去浴室"为借口离场开房（行3408-3417）。

### imanispring3（行4512）（gethimdrunk 系列）
Rika 与 Imani 合谋灌醉 Senpai，逼问"你是否在睡学生"。全程醉话灾难喜剧：Truth or Truth 变成互揭老底（Rika："We're supposed to be finding out if he wants to fuck my daughter, not you!" 行4631）；Imani 醉中真言："Attention's {i}nice.{/i} Bein' wanted is {i}nice.{/i} But'cha gotta draw the line where a line needs to go"（行4700）；"God {i}always{/i} forgives. So us regular people should too, right?"（行4715）。Osako 站 Senpai 方但盼他招供（行4723）。计划彻底失败，Imani 吐在 Senpai 裤子上（行4763-4770）——但当晚烂账：Rika 与 Senpai 发生了关系（p4 揭晓）。

### imanispring4（行4788）（rikaimanigym 系列）
次日清晨 Rika 在 Imani 床上醒来发现真相（Rika 醉酒短信："Sorry sex Akira. So dizzy. Huge dick. Good sex." 行4878）。健身房三人行：Rika 提议再灌一次并录像被 Imani 否决（行4908-4911）；Yuki 出场——Tsubasa 为监视她直接买下了健身房（行4997），Rika 与 Yuki 结成"gym buddies"。核心是 Imani 与 Senpai 的清醒对峙：
- "Don't play dumb, Senpai. I know you had sex with Rika."（行5035）
- "Be straight with me, Senpai. How far has it gone?"（行5068）
- 护崽宣言："I'm thinking of them like little kids at a zoo and {i}you{/i} as a lion who escaped its cage."（行5102）
- 动因："if Rika is starting to worry about her {i}actual{/i} daughter as a result of it, I shouldn't just ignore it any longer."（行5110）
- Senpai 的 meta 式反问："Imagine time stopped moving... Would you just keep looking at everyone younger than you as children for the rest of eternity?"（行5120-5121）
- 收尾温柔一笔："I think it's okay to stop covering up so much... You'll overheat working out in that." ——"Different conversation, Senpai. But thank you. I'll think about it."（行5153-5155）

## 三、lust 线概貌（抽象表述）

- **imanilust5（行3813）**：雨夜例行幽会。功能性对话（Wakana/Rika/Osako 情绪连锁、Yuki 隔壁砸墙梗 行3863）后发生关系；系统彩蛋：Senpai 发给她 "[[1 FREE SEX COUPON]"（行3890）。结尾共伞，叙述者承认让她"暂时占据权力上位"（行3911）。
- **imaninaming（行3988）+ endofimaninaming（行4242）**：玩家输入 Imani 对自己的称呼，多分支彩蛋——senpai（改回原称）、imani/wakana/osako/rika（互换身份恶搞，其中 rika 分支涉及"模仿她妈以接近 Rin"的危险玩笑 行4095-4099）、selebus（开发者梗）等。正片：Imani 换上学生制服 roleplay（"All of the student, none of the shame." 行4275），"extra credit" 师生扮演框架；文本自我点评为 fantasy 并反复强调"这只是幻想"（行4324-4325）。此处仅记录框架，不复述细节。
- **christmasimani3 尾部**：派对中途借口开房（成年人间，属 love/lust 混合）。
- **imanispring3→4 的暗线**：醉酒之夜 Rika×Senpai 得逞，构成 Imani 线最大的 lust 类剧情装置——它同时是喜剧素材、三角关系催化剂与主线秘密的扩散事件。

## 四、与主线的咬合点

1. **第六届宿舍战争**：`imanidive` 入口 + spring2 中 Im ani 主持的 scavenger hunt 回忆（Futaba 选她当"something beautiful"，行2212）；背景设定即她主持该届战争、平局分支中被录音勒索"分享 Senpai"（外部背景，本文件内未直接展开）。
2. **Rika 母女线深度绑定**：spring3/4 整段由 Rika 驱动——Rika 因 Rin 的怀疑而发起"灌醉审问"、酒后与 Senpai 发生关系、又怕 Rin 知道（"She's already had her heart broken a million times!" 行4922）。每场 spring 事件结尾都 jump 到 rikaspring6/7（行4786、5170），两线互为前后章。
3. **Wakana/Osako 线**：special15 是 wakanaspecial15 的联动前置；christmasimani1 独白揭示 Osako 长期知情（Ayane×Senpai）却瞒着 Wakana——主线的定时炸弹之一。
4. **Yuki 线**：lust5 中 Yuki 已是暴躁邻居；spring4 中 Tsubasa 买健身房监视 Yuki（行4997），Yuki 让 Senpai "drop by more often...easier to give you updates"（行5005）——Yuki 康复支线的进行时记录。
5. **Niki 偶像线**：special15 海报喊话、lust5 中"hot idol girlfriend" jealousy 梗（行3842）。
6. **meta 系统**：christmasimani3 的 monks/Malvin/"[[REDACTED]" 独白是全作最直白的第四面墙段落之一；FREE SEX COUPON 的系统级玩笑；14 处 `renpy.end_replay()`。
7. **教师身份主题**：Imani 是"唯一真正在教书的人"（替 Senpai 上课、批改、护学生），spring4 的狮子/时间静止辩论正面处理了主线最核心的道德命题。

## 五、未解伏笔清单

1. **伤疤来源**：仅以 "traumatic physical abuse"（行4934）一语带过；具体成因、是否与加纳童年/Kwesi 有关，均未揭示。
2. **Kwesi 之名**：Rika 灵光一现时 Imani 回 "Kwesi? That you in there? Get out of my friend's head."（行4940）——像是熟人/亲人的名字，无后续解释。
3. **Osako 的知情范围**：她"早知道 Ayane 的事"（行2679）且希望 Senpai 向 Imani 摊牌（行4642 "Then {i}I{/i} won't feel like I'm harboring a fugitive either."）——她在下一盘什么棋未明。
4. **Imani 知道多少/何时爆发**：christmasimani1 独白明言红旗堆积；spring4 结尾她仍处于"还没听到答案"状态（"until I find out how fucked up you really are" 行5146）——摊牌被持续悬置。
5. **校服请求的循环**：Senpai 多次提"schoolgirl outfit"（行4624、5147），endofimaninaming 中 Imani 自认"从穿上那一刻就想到了"（行4290）——这条欲望线如何反噬主线未展开。
6. **Yuki 的 updates**：spring4 中 Yuki 有话要对 Senpai"当面说"，内容悬置。
7. **"time stopped moving" 反问**：Senpai 给出的 meta 级辩解（行5120）未被剧情回收，疑似指向重置/停滞的世界观核心。

## 六、label 总表

| label | 行号 | 一句话内容 |
|---|---|---|
| callimanimorning | 1 | 晨间调度入口（未解锁=不接电话） |
| callimaniafternoon | 19 | 午后调度入口 |
| callimaninight | 37 | 夜间调度入口（需 wakanaspecial15，按 imani_love 分发） |
| imanidive | 59 | 宿舍战争潜水入口（按 chap4active 分发） |
| imanidate1 | 105 | 首次单独上门：公寓、6/10 梗、猫鹦鹉谎言 |
| imanidate5 | 410 | 空调坏了来借宿：租金谈判名场面 |
| imanidate15p1 | 792 | 同走去酒吧：meta 独白与冷笑话 |
| imanidate15p2 | 1151 | 独处摊牌：她告白，他 friend-zone |
| imanispecial15 | 1485 | 与 Wakana/Karin 买万圣节装：scars 与 Niki 宣战 |
| imanispring1 | 1831 | 海滩夜话：承诺一切，被问为何不穿泳衣 |
| imanispring2 | 2128 | 别墅换装：伤疤首次向 Senpai 展示 |
| christmasimani1 | 2668 | 圣诞约会：黄腔互怼与 love-love 表白 |
| christmasimani2 | 3047 | 圣诞树场景：温馨收束 |
| christmasimani3 | 3308 | 圣诞派对：monks/Malvin meta 独白+浴室借口 |
| imanilust5 | 3813 | 雨夜幽会：FREE SEX COUPON 与共伞 |
| imaninaming | 3988 | 称呼输入分支（senpai/imani/wakana/osako/rika/selebus…） |
| endofimaninaming | 4242 | 学生制服 roleplay 正片（fantasy 框架） |
| imanispring3 | 4512 | gethimdrunk：灌醉审问惨败+吐裤子 |
| imanispring4 | 4788 | 健身房清算：Rika 事发、狮子演说、时间静止反问 |
