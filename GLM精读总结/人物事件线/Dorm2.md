# Dorm2Events.rpy 精读摘要（宿舍二楼公共事件集，v0.55）

文件：`Dorm2Events.rpy`，约 13787 行。宿舍二楼住户（按房间分区）：Room 7 = Uta & Io，Room 8 = Nodoka & Otoha，Room 9 = Touka & Yasu，Room 10 = Kirin & Noriko；Molly、Tsuneyo 亦居住于此层（Molly 房在 Otoha隔壁）。

---

## 一、概貌：label 主题分组

1. **入口 hub**：`dorm2monday`（行 1 起）——二楼周一入口，按 `otohaspecial15p2` / `mollysad` / `day288` / `christmas7` 切换场景背景；菜单含 Knock on a door / Talk to Molly / Talk to Otoha 等。
2. **Molly 事件**（行 1500–3000 一带）：Molly 以游戏中的性癖好谈论作为逃避现实手段（"willing to do virtually anything in order to separate herself from the real world"）；自述 ADHD（"There's not a lot of space on my hard drive so I need to constantly delete things"）。
3. **Tsuneyo cosplay 线**：`tsuneyocos12–15`，Molly 帮 Tsuneyo 试穿服装的喜剧桥段。
4. **Room 7（Uta/Io）**：`utadorm` 路由器（行 4513，按 uta_love 5/10/15/30/40 跳 `utadorm5/10/15/30/40p1`）、`utadormgen`（4530）、Uta facetime 事件（兄弟入狱、亡祖父为古筝演奏者）、`iodorm15`（Io 药物过量的膝枕夜，行 7501–7717）。
5. **Room 8（Nodoka/Otoha）**：`nodokadorm` / `otohadorm` 路由（7723 / 7738）、走廊 gen/first 事件、`nodokadorm1`+`otohadorm1`（欢迎会连环事件）、`nodokadorm5`（Nodoka 狂躁发作）、`otohadorm5`（睡衣夜）。
6. **Room 9（Touka/Yasu）**：`toukadorm` / `yasudorm` 路由（9962 / 9983）、`toukadorm1`（吐槽 Yasu）、`yasufirsthall`（邀请去教堂，解锁 New Hope Cathedral）、`toukadorm5`（家族继承重负）、`yasudorm10`（Yasu 神学独白+meta 图像闪烁）。
7. **Room 10（Kirin/Noriko）**：`kirindorm` / `norikodorm` 路由（11742 / 11802）、`kirindorm10`（"契约"同居）、`kirindorm15`（被炉+诡异电影）、`kirindorm20`（未遂亲密）、`norikofirsthall`（旧识重逢+号码）、`norikodorm5`（世界重置对话）、`norikodorm25`（餐厅告白+**meta 崩坏事件**，文件压轴）。
8. **通用 gen 事件**：各角色 `*dormgen` / `*hallgen` 为低门槛刷好感模板（Nodoka 问"牛在搞什么鬼"、Yasu 传教、Touka 视频补课等）。

路由依赖跨角色咬合明显：`nodokadorm15` 需 `yasudorm20`；`nodokaspring1` 需 `makotospring5`+`yasuspring8`；`kirindorm10` 需 `utadorm5`+`iodorm5`+`day271`；`norikodorm25` 需 `convenience25`；`norikodorm30` 需 `norikodate30`+`otohadate20` 等。

---

## 二、逐事件脉络（重点事件详述）

### Room 7：Uta & Io

- **`utadorm`（4513）/`utadormgen`（4530）**：Uta 房间事件路由器+通用互动。Uta facetime 线透露家庭背景：兄弟入狱（"a person who has literally attempted murder on the other line"、"He didn't...try to murder you, did he?"）、亡祖父曾是古筝（koto）演奏者——Uta 的音乐性有家族渊源。
- **`iodorm15`（约 7460–7717，Io 好感 15 房间事件）**：Io 服用抗焦虑药后神志不清，爬上 Sensei 膝盖。关键台词：
  - "Because I have to." / "Because you're my last bastion of hope for adults in this world."（"因为你是我对成年人世界最后的希望堡垒。"）
  - "I would very likely be dead if I never met Uta."（"如果没遇到 Uta，我很可能已经死了。"）——Io 对 Uta 亦师亦友的救赎性依赖；"Uta's the perfect girl. I hate it so much. But I also love her so much."
  - 自嘲："I'm just a weightless, overmedicated cockroach with a grand total of two bras and four boxcutters."（四个美工刀细节暗示自伤倾向）
  - Uta 回家撞见，尴尬逃离："Don't...do anything crazy without...calling your aunt!"
  - 收尾旁白极暗："Io is practically dead already. / And there is no one who deserves rest quite like the dead."（"Io 其实已经死了。没有人比死者更该休息。"）

### Room 8：Nodoka & Otoha

- **`nodokafirsthall`（7896）**：Nodoka 走廊初遇。bonus 版她在读《Lolita》，直问 Sensei"能否爱上远比自己年轻的人"，并自称渴望禁忌（与 incest 设定呼应）；结尾"Remember that when the time comes for you to become my own Humbert Humbert."（"等你成为我的 Humbert Humbert 时记住这一点"）；normal 版换成《大红狗克利弗》喜剧化处理。另透露 Futaba 说 Sensei 曾经是作家。
- **`otohafirsthall`（8127）**：Otoha 初遇。核心信息：宿舍"没有规则"（Sensei 亦无法解释自己为何被雇用）；Otoha 说"Rin 对你和对别人不一样，包括对我"（Rin 线咬合）；"I had no idea that living with people similar to me could be so...exhilarating."
- **`nodokadorm1`+`otohadorm1`（8314 / 8695，搬入欢迎会）**：Nodoka 当众"测试"Sensei：逼问"你想要什么"，把好感度系统说破——"To max out your relationship with everyone around you would equate you to a king... Perhaps even a god. And who doesn't want to be a god?"（"把与身边所有人的关系都刷满，你就是王……甚至是神。谁不想当神呢？"）随后抛出纯 meta 台词："Perhaps this entire world is nothing like either of us perceive it to be?"（"也许这整个世界和我们感知的完全不同？"）。事后她自称这是"评估 Sensei 误伤女孩们概率的测试"。Otoha 借口搬东西把 Sensei 拉出门解围：判断 Nodoka"只是在看能把你逼到什么程度"；再向 Sensei 请教 Rin 的感情问题（"I'm just the flavor of the month"——Rin 移情速度的担忧）。本段旁白名句："Which smile do you think is harder to maintain? ... The correct answer is that both smiles are impossible to maintain. Because this world is miserable."
- **`nodokadorm5`（9075，Nodoka 狂躁发作）**：Otoha 逃出门后，Sensei 独对连续数日未眠、咖啡因过量的 Nodoka：反复念"It's wrong. It's so wrong."→"IT DOESN'T MAKE SENSE! IT IS INCOMPLETE!"。**此处演出强烈指向 meta/暗线**：插入静电音效+闪切图片 `ayhh6`，并播放 BGM `amiawake.mp3`（与 Ami 觉醒事件同曲）——暗示 Nodoka 的"过载"与 Ami 的觉醒机制同源。她展现天才式全知（梭罗遗言"Moose! Indian!"、丰臣秀吉卒年、锗电子排布脱口而出），声称"I see everything. I hear everything."；Sensei 偷看她的笔记本——**没有文字，只有稚拙的"房子"涂鸦**（与后文 Otoha 电视卡住的"奇怪的房子画面"、Kirin 房"倒立房子"电影构成贯穿性"房子"意象）。结尾低语："I see it... I see everything..."
- **`otohadorm5`（9540，睡衣夜）**：Otoha 吃甜甜圈看"香肠派对"面；电视卡在"一张奇怪的房子图片"（呼应上条）；妈妈来电时 Sensei 捣乱几乎害她被接回家——"One wrong move and that could all come to an end. My parents know the address of this place and they could come get me at any moment."（监护权/紧绷的 leash 隐喻）。隔壁 Molly 跑团喊话"SEVEN VIOLET FUNGUS APPEAR! ROLL FOR INITIATIVE!"（Molly 是跑团 DM，Rin 因怕丢脸不让 Otoha 参加）。

### Room 9：Touka & Yasu

- **`toukadorm1`（10162）**：Touka 首次房间访问，核心是吐槽室友 Yasu：Yasu 从回家起一动不动坐着不说话、凌晨 3 点对白板耳语、放弃关灯；Touka 问"Am I going to die tonight?"。喜剧点：她睡的是"情趣酒店同款床"却坚信是"快速睡眠模式科技"；提到 Makoto 私下给她做个性化讲义（Makoto 线咬合）；随口说可以让家人"几分钟内暗杀你"。结尾 Touka 派司机送 Sensei 回家。
- **`toukafirsthall`（10563）**：Touka 走廊初遇。伏笔：她说自己"已经气走 yet another teacher"随即慌忙改口；家有三间卧室、带 Sensei 参观需要"特殊准备"；Io 坐在走廊地上冷眼旁观（Io 与 Touka 互斥的暗示）。
- **`yasufirsthall`（10783，解锁教堂）**：Yasu 走廊初遇，本文件最重要暗线之一：
  - "Romance is out of the question until my wings grow in, Sensei."（"翅膀长出来之前免谈恋爱。"）
  - "Because soon, you'll finally be ready to see where I've been hiding all this time."；"The reckoning. The hole that swallowed everything."——Sensei 追问后确认她说的是**Kumon-mi Academy 天坑**；Yasu 只回一个词："{i}Slip.{/i}"（"说漏嘴了"）。
  - 邀请 Sensei 去"sanctuary"（实为教堂），"There is only me. It's a special place that only the chosen can enter... I'm choosing you right now."；解锁提示："Congratulations! You may now visit New Hope Cathedral!"
  - 从手套里取出一张旧报纸剪报塞给 Sensei（内容本文件未揭晓——伏笔）。"Then why do you reek of a {i}shrine?{/i}"（"那你为什么一股神社味？"——暗示 Sensei 与神社/旧线有牵连）。
- **`toukadorm5`（11046）**：Touka 睡衣夜，卸下大小姐外壳哭诉融入困难："I am a {i}real{/i} girl with {i}real{/i} feelings. And I would very much like {i}real{/i} friends"；家族设定：Tsukioka 家自古"每位男性家主只生两孩、长子继承"，父亲只有两个女儿，她作为长女被迫扛起继承人身份——"The disease of being born a woman to someone who, more than anything, wanted a male heir."；误会 Ayane 与 Sensei 有婚约（ dojo 线咬合）。
- **`yasudorm10`（11379，Yasu 房间首访）**：**本文件 meta 密度最高的事件之一**。开场旁白即玩图像把戏：bonus 版闪切 `realtoukaimage`，普通版闪切 `toukaolddis8`——同一"皱眉的 Touka"存在两个版本图像，配合旁白"If you pay close attention to the image in front of you..."，是给细心玩家的图像层 meta。Yasu 神学独白：
  - 灵魂论："If your body is the container that stores your thoughts now, what would happen if you switched containers?"（如果身体只是容器，把意识存进世界本身呢？）
  - "To die is to disappear. And since it's impossible to fully vanish, there is no death."（死亡=消失，但无法彻底消失，所以死亡不存在）——与游戏"重置/回收"设定同构。
  - 她能听见"以太中的低语"（voices trapped in the aether）。
  - 对 Sensei 的恐惧宣言（暗线核心）："You. Who is blessed and cursed at the same time. Who is both the purest entity I have ever seen and a person so tainted that it's a miracle you can still walk. ... But because I can not feel you."（她能感知所有人的"低语"，唯独感知不到 Sensei——Sensei 是异类/盲点）
  - 末世预告："Before long, the snow will melt. The seasons will change. And His slumber will come to its end."（雪融之时，祂的沉睡将结束——季节/重置伏笔）
  - "I am not crazy, though. I am chosen... I will give you myself and you will give me yours. And then we will give it all to him."

### Room 10：Kirin & Noriko

- **`norikodormgen`（11816）**：普通版温馨；**bonus 版旁白重磅 meta**："It's possible that's just this body's old memories banging against the bars of the prison I forced them into, but it could also be that Noriko's just...different."（"也许只是这具身体的旧记忆在撞我囚禁它们的牢笼栏杆"——直接坐实 Sensei 灵魂/记忆与身体分离、旧记忆被强行压制的设定）。
- **`kirinfirsthall`（11930）**：Kirin 吐槽 Noriko 放歌；解释为何拖到进班才搬宿舍；bonus 版直球问"Do you want to fuck Ami?"，若 `amifingered == True` 则 Sensei 装傻岔开（Kirin 怀疑 Ami 半夜偷听，建议装摄像头）。
- **`norikofirsthall`（12152，重逢+拿号码）**：Noriko 暗线核心事件：
  - 童年记忆佐证："I still remember how hard you had to work to get Niki to like you back in the day."；"There's no need to add 'apparent' to that, Sensei. It definitely happened... Even if you don't remember it right now, I'm sure you will in time."（她与 Niki 的旧关系确凿存在，Sensei 失忆中）
  - **Maya 旧识揭露**：Sensei 曾同时教 Noriko 和 Maya（"That's why Maya and I turned out so darn smart"），十岁就读《1984》；而 Sensei 完全不记得，只记得 Maya 警告"Noriko 是邪恶的、会毁掉一切"。
  - Noriko 提出可以养他："I could {i}probably{/i} support the two of us if you wanted to just quit teaching altogether."
  - 姐妹战争定调：Noriko 在 Sensei 手机里给自己名字加爱心、在 Maya 名字旁加呕吐 emoji。
- **`kirindorm10`（12349，Room 10 首访）**：Kirin 与 Noriko 的"契约"：bonus 版 Noriko 宣言"Kirin gets to have your dick and I get to have your heart. And also your dick."以及"I am going to shatter your harem and make you love me and only me."（我要粉碎你的后宫，让你只爱我）；契约条款：Kirin 只许有性无爱，违约"Noriko gets to dissect her"（"我要解剖她"——以冷幽默包装的支配条款）。Kirin 自我欺骗式独白："me actually 'liking' someone? That's just not possible."
- **`kirindorm15`（12731，被炉电影夜）**：三人挤被炉看 Noriko 的"艺术电影"：**一栋钉死窗户的房子里，五个女孩围着厨房桌沉默地吃灰色食物**——Noriko 说"我从来没看完过，每次看到一半总会有事发生，我不得不离开"（强烈的重置暗示：她可能在"上次循环"里看过结局）。bonus 版直接跳转 `kotatsux` 成人分支；普通版是 Bee Movie 欢乐结局。
- **`kirindorm20`（12950）**：Noriko 意外不在场，Kirin 独处未遂亲密事件（`kirinalmostx` 分支），围绕"契约不许动感情"的张力。
- **`norikodorm5`（13033，散步谈心）**：
  - bonus 版开场旁白再次点破重置："Especially one revolving around the sole creature in this universe that the girl responsible for resetting it hates."（"这个宇宙中唯一让**那个负责重置世界的女孩**讨厌的生物"——即 Noriko 是 Maya 所恨之人；直接指认 Maya 与重置的关联）
  - Sensei 向 Noriko 解释世界重置观："when someone fades away, the world stops existing... No one disappears. They just get recycled."；"Ami and Ayane would take it the worst. Maya would throw a party."
  - Noriko 的 meta 台词："Can you just like, hurry up and remember me already?"；"Don't lure me in like that! You know those memories are what my character arc is based around!"（"那些记忆可是我角色弧线的基础"——角色自知有"剧本"）
  - 插入静电闪切图片 `yumis2`（Yumi 记忆闪回），Sensei："I feel like I almost remembered something."
  - Noriko 坦言动机："I built myself around trying to catch your eye. But alas, I was never the favorite."
- **`norikodorm10`（13370）**：洗衣服日常（bonus 版跳 `norikounderx`）。
- **`norikodorm25`（13416，餐厅约会——**本文件压轴 meta 事件**）**：
  - Noriko 完整讲述"你消失之后"的过去：她曾把每周去旧补习班见 Sensei 视为"城堡"——"for a few hours every week, it was the most beautiful place in the whole wide world."；后来 Maya 出现，"the castle for two turned into a castle for three"；"every time I tried to move closer... you'd just move even further away in response. And then one day... you moved further away than I ever expected you to."（Sensei 突然消失）
  - 她全城寻人，终于在巴士车窗瞥见他——但此处文本被**逐字涂黑**（多处 `[[redacted]`），她看到的是 Sensei 与某人在一起的画面，内容被强制遮蔽。
  - **第四面墙崩坏**：文本直接输出大写——"{b}STOP PLAYING LESSONS IN LOVE{/b}"（"停止游玩《Lessons in Love》"），随后系统风格文本："///////////////////EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS / PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT AS A THANK YOU FOR YOUR CONTINUED SUPPORT AS WE ATTEMPT TO REPAIR YOUR CONNECTION"（"事件与预期失去同步……我们正在尝试修复您的连接"）——以"游戏系统故障"为名强行掐断 Noriko 的关键证词。
  - 结尾菜单"Would you like to phone?"：bonus 选 Phone 进入 `restofnorikorestx` 续篇；普通版选任何项均"EVENT FAILED"，+3 好感了事。**谁在阻止玩家听到这段往事，是本文件最大的未解之谜。**

---

## 三、与主线的咬合点汇总

1. **Kumon-mi Academy 天坑**：Yasu 的"the hole that swallowed everything / Slip"（yasufirsthall）与 Touka 的"everything the sinkhole claimed"（toukadorm5）互证——转学生们都是"被吞没前"旧校的幸存者/关联者。
2. **New Hope Cathedral 解锁**：yasufirsthall 是教堂场景的入口（Yasu 线主舞台）。
3. **Maya–Noriko 旧识**：norikofirsthall 揭示 Sensei 曾同时家教 Maya 与 Noriko；Maya 对 Noriko 的敌意（"evil / stalker"）与 norikodorm5 旁白"负责重置的女孩恨 Noriko"闭环。
4. **重置/循环设定**：norikodorm5（"recycled"）、norikodormgen bonus（"old memories...prison"）、kirindorm15（Noriko 从未看完的房子电影）、nodokadorm5（`amiawake.mp3`+`ayhh6` 与 Ami 觉醒同源演出）多点互证。
5. **Nodoka 的"神/玩家"发言**：nodokadorm1 的"max out relationship = god"几乎是在描述玩家的攻略行为，是全游戏 meta 层最直白的文本之一。
6. **Yasu 对 Sensei 的定位**：yasudorm10"我感知不到你 / 你是最纯净又最污秽的存在"——Sensei 在世界规则中的异常性。
7. **跨线依赖**：nodokadorm15←yasudorm20、kirindorm10←utadorm5+iodorm5、toukadorm25p1←toukaarchery20 等，宿舍事件是各角色线的中继站。
8. **Rin 线**：otohafirsthall（"Rin 对你不一样"）、otohadorm1（Otoha 的"flavor of the month"担忧、`rindorm45` 披萨梗）、otohadorm5（Rin 回避跑团）。
9. **Makoto 线**：toukadorm1 中 Makoto 私做讲义（助手身份的延伸）。
10. **Ami/Niki 线**：kirinfirsthall 的 Ami 质问、norikofirsthall 对 Niki 旧恋情的确认、otohadorm1 的"Ami is my niece"误会。

---

## 四、未解伏笔清单

1. **Yasu 手套里的旧报纸剪报**内容未揭晓（yasufirsthall，行 11017–11025）——"你所有烦恼的答案都在那张纸上"。
2. **Noriko 在巴士上看到的人是谁**——`[[redacted]` 涂黑 + "STOP PLAYING LESSONS IN LOVE"强制中断（norikodorm25）；续篇在 `restofnorikorestx`（本文件外）。
3. **"Would you like to phone?"的"电话"是什么、打给谁**——系统故障式演出暗示有"外部存在"在干预叙事。
4. **Nodoka 笔记本上的"房子"涂鸦**、Otoha 电视卡住的"房子画面"、Kirin 房"五女孩灰食之屋"电影——"房子"意象三连，指向未揭晓的同一原型。
5. **Nodoka 发作为何配 `amiawake.mp3`/`ayhh6`**——她与 Ami 觉醒机制的关系未明说。
6. **Yasu 的"祂的沉睡将随雪融而结束"**——末世/季节转换倒计时。
7. **Touka"气走 yet another teacher"的具体历史**（toukafirsthall，话头即断）。
8. **`realtoukaimage` vs `toukaolddis8`** 双图像 meta 的完整含义（yasudorm10 开场）。
9. **Io 的"四个美工刀"**与"Io is practically dead already"——自毁倾向的后续。
10. **Uta 兄弟（杀人未遂入狱）与亡祖父 koto**——家庭线尚未展开。
11. **Kirin"契约"违约条款"dissect her"**是否会在后续成真（黑色玩笑还是真flag）。
12. **Noriko 自述"角色弧线基于记忆恢复"**——她的"下一阶段"（向父母姐妹证明自己没疯）尚未发生。
