# Haruka 事件线全析

> 源文件：游戏文本/HarukaEvents.rpy（共 44 个 label）。
> 定位：Haruka Hamasaki 是本作成人侧的核心配角——Koi Cafe 老板娘、已婚却深陷不伦的孤独成年女性、Rin 的 "work mom"。她的线是全作中"成年角色如何被 Sensei 一步步拖入深渊"的最完整样本，也是元叙事介入最频繁的角色线之一。
> 阅读提示：love 线呈现"孤独→友情→自我重建→再度崩塌"的完整弧光；lust 线则是一部加速堕落的编年史，两线在 harukadate30 处汇合为"堕落契约"。文中以 label 名为锚点，可在 HarukaEvents.rpy 中检索核实。

## 一、角色基本盘

- **姓名与身份**：全名 Haruka Hamasaki，Kumon-mi 咖啡馆 Koi Cafe 的创办者兼老板（"Just a bunch of part timers at a cafe I own about a mile away from here"）。开店是她从小到大的梦想（"You've wanted that cafe since you were a kid?" / "It was practically my dream"）。
- **婚姻状态**：有丈夫，但丈夫长期不在场——叙事将其处理为"去了太空/外星人任务"，且 Sensei 内心独白怀疑这个世界根本不会让他回来（"despite her being fully aware that her husband is safe and sound"、"this world won't let him come back"、"Unless everyone in space is somehow exempt from these strange timeloops"）。
- **社交圈**：与 Maki、Sara 组成三人闺蜜团；是 Rin、Molly 等店员的 "work mom"（"I'm just as much of her work-mom as I am her boss"）；与 Sensei 从炮友逐渐演变为"主人/奴隶"关系。
- **性格底色**：话痨、戏剧女王式的过度敏感（"I'm kind of an overly sensitive piece of shit drama queen"）；极度害怕孤独（"Bold claim for someone who gets lonely the second no one's looking at her"）；自我认知清醒而残忍——她主动承认自己是坏人（"Do you think I'm a bad person?" / "I agree. I am a bad person"）。
- **核心创伤**：丈夫离岗后的空虚。她对 Chika 自陈："Being lonely is terrifying. And Sensei makes me feel a little less alone sometimes." 这句话是她整条线的钥匙。

## 二、love 线逐事件脉络

### 2.1 日常入口与店铺事件（call / harucafe / invite 系）
- `callharukamorning`、`callharukaafternoon`、`callharukanight`、`callharukanighthang` 构成按时段呼叫 Haruka 的入口组，是好感度系统的日常维护面。
- `harukacafe` 与 gen 系（`harukainvitegen`、`harukainviteaff`、`harukacafegen` 等）提供店铺场景的基础互动与好感分支。
- `harukareverse`、`harukanightgen2`、`harukamorninggen2`、`harukagennight` 为夜间/晨间通用桥段，负责把"老板娘"身份钉进玩家日常。

### 2.2 约会系列：从客套到交心（date1 → date20）
- `harukadate1`、`harukadate5`、`harukadate10` 为递进式约会事件，逐步建立两人"能说真话的朋友"关系。
- `harukadate15`：Sensei 受邀到 Haruka 家看电影，Sara 临阵放鸽子，Molly 留店看铺——这场"半成型的家庭夜晚"是 Haruka 第一次把私人空间向 Sensei 打开。
- `harukadate20`：以醉酒夜谈收束。Haruka 吐露真心："I feel less alone tonight than I have in a long time."，并以调侃提及 "the man who defeated Dr. Badguy"——她在 Sensei 面前第一次卸下表演。

### 2.3 sadgirls 系列：Maki 丧夫支线中的 Haruka
- `sadgirls2`、`sadgirls4`、`sadgirls5` 是挂在 Haruka 文件下的 Maki/Sara 群像支线：Maki 的丈夫 Masahiro 突然去世，最后一句话竟是 "Don't fuck too many aliens!"。
- 花店段落中，一名自称不常如此疯狂的陌生女人（源文以 q/"???" 指代）强行塞给 Haruka 一束蓝花，Narrator 以"森林倒下"的寓言预告了即将到来的痛哭。
- Maki 的总爆发直指 Haruka 的失职："Your husband is still alive and mine has been dead for two fucking months!"、"YOU CALLED ONE TIME!"。
- Haruka 的道歉是其 love 线少有的高光："I wasn't there for you when I should have been... because beneath the selfishness and inability to look forward, I love you." 和解落在细节上——蓝色恰好是 Maki 最爱的颜色（"Blue is my favorite color..."）。

### 2.4 makihornytrip：以"修复朋友"为名的自我重建
- `makihornytrip1`：Maki 丧夫后性欲全无，Haruka 组织度假村一日游试图"修好她"。车上她罕见地自我检讨："I have made out with you behind my husband's back... and then abandoned Maki when she needed me most. I've been kind of a bitch."
- `makihornytrip4`：旅行失败收场，但 Maki 反过来肯定了她："Stop putting yourself down. You've been great lately and I'm happy to have you by my side."——love 线给过她一次真实的救赎机会。

### 2.5 harukacamp1：露营夜谈与 Koi Cafe 的意义
- 篝火边 Haruka 与 Sensei 交换人生史：她坦白自己"标准 upbringing"之下的溃烂——"I'm insanely lonely. I'm a borderline nymphomaniac. I send naked pictures of myself to teenage girls and pretend I never meant to."。
- 她讲述 Koi Cafe 的诞生：小学商业计划书里的 "Rainbow Cafe"，以及锦鲤命名的原因——"they've always stood for accomplishment. Or courage. Strength, even... choosing a symbol for the qualities I lack seemed like a way for me to trick myself into believing I might actually have them"。
- Sensei 回以全作罕见的真诚："I'm really proud of you." Haruka 的反应揭示了她的软肋："It's different when it comes from someone else, obviously. Especially someone you look up to."（"But...it makes me really happy."）
- 星空下的并肩（"And we both close our eyes."）是 love 线的情感顶点——也是此后一切坠落的参照物。

### 2.6 harukaspring4：work-mom 的最后一职
- 深夜的 Koi Cafe，Rin 向 "第三位妈妈" 求助感情问题（"you're practically a third mom to me"）。Haruka 听完 Rin 在 Chika 与 Sensei 之间的摇摆后给出建议："You two are clearly compatible despite the age difference... So...love now...consequences later?"。
- 打烊后她深夜致电 Sensei："She's falling for you, Akira. And if you don't act quickly, you might lose your chance."——她把自己得不到的东西亲手推给别人。
- 结尾旁白撕开伪装："She thinks about how lonely she is. And how there is only one person she's met who would choose her over anyone else. He's so far away now." 注意：这里的"他"指向丈夫而非 Sensei，是她线上最冷的一刀。

## 三、lust 线概貌

lust 线是一条不可逆的下坡路：从初次欲望事件，到酒店三人行，再到"堕落契约"与其后的连环事故。截断段在本线中承担双重功能——既压缩露骨描写，又通过留白凸显场景的失控感与重复感（性事越来越频繁，情感含量越来越稀薄）。

### 3.1 起点与过渡
- `harukafirstlust`：lust 线的首次点火事件，确立两人越界关系的开端。
- `harukalust25intro` / `harukalust25`：班级旅店夜，Imani 被安排同房又识趣让位（"Looks like there's only one bed in here anyway"），随后 Sara 与 Haruka 联手的截断场景以 dorm war 积分结算——lust 线在此已带有"收集/竞赛"的游戏化色彩。

### 3.2 harukadate30：堕落契约（两线的分水岭）
- 开场即虚无："Part of me wants to feel bad that we're still doing this despite her being fully aware that her husband is safe and sound"。
- 事后床上，Haruka 提出双重请求：其一，"I want to give you full control over my body... Anything you ask me to do... I'll do it without a question."；其二，"I want you to help me fuck someone in your class." 理由是 "if I'm going to be bad...I want to be bad."（"I want to feel as free as you."）
- Sensei 承认厌恶却接受，Haruka 一语封喉："You'll agree because you're like me. You're fucking scum."
- 结算界面直接授予成就："Haruka has gained the 'Predator' trait!"——游戏系统亲自为她盖章。

### 3.3 契约之后：spring 系列的连环坠落
- `harukaspring1`：Haruka 受命把 Molli 引入浴室的企图失败（"based on the lack of perverted shrieking, I can only assume the mission ended in failure"）；转而以"惩罚"为名在柜台发生关系，被陌生顾客当场撞破（"What the fuck is going on in here?"），她甚至在围观中达到高潮并报出全名与婚姻状况。
- `harukaspring2`：BBB 投诉送达，Cafe 面临调查与停业。Rin 得知"完全控制权"协议。Haruka 的恐惧点不在羞耻而在店："I love this place. And without it, I wouldn't just be broke. I'd be lost."
- `harukaspring3`：复业电话；枕边情报交换中 Sensei 透露对 Sana 的所作所为（"Took her virginity on my couch the other day"），Haruka 则立誓要证明 "Sara 会和女儿上床" 的猜想——她的欲望已经全面转向学生群体。
- `harukachristmalloween1`：浴室里安慰哭泣的 Chika，却在共情铺垫后突然发出邀约（"if you need someone to cheer you up right now, the same way you cheered up Rin, I'd do it with no questions asked"），遭 Chika 怒斥 "Touch me again and I will fucking kill you!"，以哀求 "Don't tell anyone" 收场。
- `harukachristmalloween2`：转而猎取 Kirin，被 Sana 撞见；Sana 以 "I was never here...and I never saw anything." 完成一次意味深长的包庇。
- `harukaspring5`：Sana 主动摊牌与 Sara 的三人行，并点破 Haruka 与 Kirin 的事（"Did you have fun with Kirin at the party?"）——两个孩子互握把柄，Haruka 问出那句标志性的 "Can I watch next time?"。Narrator 以 golem/guilt 与 dragon/lust 的战斗作结："In the end, the dragon won because the dragon always wins."
- `harukaspring6`：全线的谷底。巴士站旁，Haruka 致电 Sensei 说 "I think I'm sad"、"I think I kind of want to, like...be dead tonight?"，甚至问 "Do you think there's any helping people like us?"——回应她的是 "Just shut the fuck up and take your tits out already."。事后她瘫在原地，被路过的 Karin 撞见（"What the- oh my god!"），只留下 "Leave...me...I don't deserve your help"。当夜 Sensei 回家被 Niki 逼问行踪。

## 四、与主线/元叙事咬合点

1. **重置循环层的窗口**：Sensei 关于丈夫的独白是玩家层世界观的直接泄露——"this world won't let him come back"、"strange timeloops"。Haruka 的婚姻悲剧因此不只是个人不幸，而是循环机制的产物。
2. **Narrator 的人格化登场**：`sadgirls5` 中 Narrator 两度直接向玩家喊话——先念出署名 "The girl who cannot breathe" 的诗，再借"森林中的树"寓言预告悲剧（"Does it happen? Does it not? You will never know!"）。
3. **Tebiso 事件**（`harukaspring3` 内）：Sensei 踩死又救活一只名为 Tebiso 的虫子，虫子质问 "You've been here for so long and have accomplished nothing"，并精准报出 "How many times did she call you last night? Six. You answered none of them."——超自然存在对循环内行为的监察。
4. **作者现身**：`harukaspring6` 的巴士站场景中段突然插入 "TRANSLATION NOTE: Hey guys, Selebus here."，随后 Narrator 又否认自己的存在，并以诗句自白 "It's your misery that lifts me up! I'm the key and you're the kite."——痛苦本身就是叙事者的燃料。
5. **路线警告**：`harukaspring5` 结尾系统提示明言 "But she doesn't make any character progress because this is the route where she only gets worse and everything ends horribly."——Haruka 线被官方标注为无救赎路线。
6. **世界观谜题**：Haruka 在酒吧发问 Kumon-mi 作为封闭城镇的物资来源，Sara 猜测 "helipad supply drops"——小镇封闭性与主线设定互文。
7. **玩家层自白**：Sensei 的小字独白 "This game is awesome... none of these characters are actually real people" 把 Haruka 的苦难明码标价为玩家的娱乐内容。

## 五、未解伏笔

1. **丈夫的命运**：他是真的在太空，还是循环机制抹除的存在？Sensei 自己也承认这只是假设（"That would sure be a trip."）。他若归来将直接引爆 Haruka 线（"Imagine he just comes back one day..."）。
2. **Nodoka 悬念**：Cafe 中 Haruka 突然变色后含糊地说 "Maybe we could talk about that the next time you come over?"——她与 Nodoka 之间有一段未揭开的对话。
3. **BBP 调查余波**：周边商铺的监控是否拍到当晚始终未结案；丑闻若扩散，Haruka 的反应令人不安地期待（"I'd never stop being wet again."）。
4. **Makoto 问题**：Maki 发现女儿与 Sensei 的关系后的谈话悬而未决，Haruka 已被卷入并为自己的钱包索赔。
5. **Sana 的 "favor"**：Sana 明言将来会要求回报（"I might call in a favor eventually... I don't know yet."）——这是悬在 Haruka 头上的勒索。
6. **Karin 目击**：`harukaspring6` 结尾 Karin 撞见瘫痪的 Haruka，此事是否会传开、由谁处理，均未落地。
7. **Kirin 秘密**：Christmalloween 浴室未遂事件是 Kirin 与 Haruka 之间的共同秘密，随时可能成为新的爆点。
8. **"everything ends horribly"**：官方路线警告预示 Haruka 线尚有一个灾难性的终点尚未到来。
9. **她的孤独终局**：结尾旁白提出的问题——那个"愿意选她的人"是否永远遥远——是全线的终极悬念。
