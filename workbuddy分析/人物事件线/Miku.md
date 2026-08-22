# Miku Maruyama 事件线深读（MikuEvents.rpy，v0.55，源约 9400 行 / 38 label）

> 基于 `_digest_Miku.txt`（4805 行）全量精读重写。台词直引格式：`> mi: 英文原文…（[源行号]`；成人内容仅做叙事功能概括；所有事实断言标注行号，存疑处标"待核"。缩写：s=Sensei、mi=Miku、mak=Makoto、ka=Karin、a=Ami、i=Io、u=Uta、maki=Maki、f=Futaba、sa=Sana、ay=Ayane、N=旁白。

---

## 一、角色基本盘

- **身份**：足球部出身的前运动少女（soccer 系列事件），后转入游泳部相关活动（[6262]）；与 Makoto 同宿舍、互为最亲密的室友兼"共享恋人"同盟。
- **家庭背景（本线最大解明）**：幼年家中遭两名窃贼入室抢劫，父母双亲被枪杀于她眼前，她躲在母亲身下/床下全程听见枪响——这是她"怕巨响、拔头发、解离"的创伤根源（[6074]–[6151]，详见 mikudorm55p2）。
- **精神状态**：PTSD + 拔发癖（trichotillomania）+ 解离倾向。长期服用 Io 私下提供的来路不明药物（"Dr. Io"是她的戏称 [5406]），药物过量事件后经 Makoto 介入转向正规治疗（[5972]、[6013]）。
- **表面性格**：精力过剩、口无遮拦、性知识贫乏但性欲觉醒极快；自称"Champion of Justice and Soccer"（[4978]）。对 Sensei 的感情定位长期是"friends with benefits"，直到 spring7 才请求"boyfriend"称号（[9363]）。
- **元层级位置**：她是全书少数**玩过《Lessons in Love》本体游戏**的角色——在 Maki 店里被要求试玩前半小时以熟悉商品（[8439]–[8453]）。这使她成为元叙事咬合最深的角色之一。
- **关键变量**：miku_love / miku_lust 多次系统级直显（[5120]、[5475]、[5835]、[6195]、[6985]、[7502 附近]、[8750]–[8751]、[9406]–[9407]）。

## 二、love 线逐事件脉络

### 入口桩
- **mikupool[1]**：泳池入口场景。
- **soccerfield[13]**：足球场初遇。
- **callmikumorning[42] / callmikuafternoon[58] / callmikunight[141]**：三段电话桩，随好感度分流。

### mikuinvite[231] / mikuinvitegen[242] / mikuinviteaff[286]
邀请上门的三分支桩（普通/好感线），后续 invite1/invite2 的前身。

### mikusoccergen2[323] → firsttimesoccer[354] → soccer2to4[619]
足球部初见与早期社团互动。firsttimesoccer 是 Miku 线正式起点：Sensei 被拖进足球部当"Coach"（该称呼后来进入 lust 线命名树，[8406]–[8433]）。

### soccer5[652] → soccer10[951] → soccer15[1355] → soccer20[1651] → soccer25[2067] → soccer30[2439]
以 love 值阶梯推进的社团约会系列：训练—独处—肢体接触升级的标准爬塔结构，同时铺设 Miku "怕巨响""过度活跃"的伏笔（具体触发点分布待核，前半 digest 为概读）。

### mikuwinterbeach1[2754]
冬季沙滩特别事件，soccer30 与 soccer35 之间的节令插入。

### soccer35[2804]
足球系列收官。此后足球部解散（后文 Sensei 提到 "since the soccer club disbanded" [8412]），社团线让位给宿舍养成线。

### mikudorm45[3145] / mikudorm45p2[3496]
宿舍线核心转折：**Makoto 得知 Miku 与 Sensei 的关系后的三角谈判**。Miku 亲吻 Sensei 被 Makoto 知晓，两人达成"不互相隐瞒"协议；Makoto 表示宁可 Miku 也参与也不愿她去找别人：
> mak: I'm more comfortable with the idea of you romantically pursuing Miku than any of the other girls.（[3276]–[3307] 区间，精确句行待核）
> mi: The whole reason I wanted to do somethin' like this is so we wouldn't hurt each other's feelings...（[3307]）
> mi: ...maybe just *consider* it when we're all doin' stuff together?（[3306]）

这确立了贯穿全线的"三人共同体"结构：Maku 先行、Miku 跟进、彼此透明。

### mikuspecial50[3899]
50 级特殊事件（内容为概读，细节待核）。

### mikudorm50[4260] → mikuinvite1[4306] → mikuinvite2[4649]
- invite1：首次手指爱抚节点（lust 首次解锁的前置）。
- invite2：**本线第一个成人事件**——Miku 主动跑到 Sensei 家要求"回礼"（"fair is fair and I'm the only one who's gotten some so far" [4745]）。事件后旁白罕见地打破第四墙直接向玩家忏悔：
> N: Right now, a high school freshman is on her way to my house because I am going to do things to her. And *she* is going to do things to me. This is happening because I let it. And there is no way you can word it that makes it okay. Please. Stop watching me.（[4692]–[4696]）
- 事件中埋下两条重要暗线：①万圣节失忆事件——Sensei 内心提到酒店房里发生过什么但"Miku doesn't seem to remember that"（[4748]，另见 [4849] "Valium"、[4857] 万圣节服装）；②Miku 泄密习惯——她把手指的事说给了 Kirin 听（[4874]–[4876]）。

### mikupool55[5132]：泳池药物过量事件（全线上半最重要节点）
- Miku 在泳池边意识涣散近乎昏迷，Karin 误判为疲劳（[5136]–[5143]）。
- Sensei 的内心独白完整展示其自利推理链：不送医务室是因为怕 Makoto 发现他早就知情（[5186]–[5192]），并反复自我催眠"I am making the right choice"（[5222]–[5249]），甚至预先把责任推给 Io（"It will be Io's fault." [5235]）。
- 背回宿舍后误拨电话给 Ami，随后说出全书罕见的自我暴露：
> s: That's my name. Just it isn't. My real name is Akira. Hello.（[5363]）
- 苏醒后的 Miku 处于药物残余状态，主动提出以初夜"回报"并被拒（[5395]–[5413]）；她随即暴露真实想法："Because they'll make me talk!"（医生会逼她开口，[5770] 呼应段）以及"You ain't got the first idea of what I'm dealin' with"（[5424]）。
- 事件以一段坠落意象诗收束（[5447]–[5456]），并给出系统级惩罚文本：
> {i}Miku's affection has increased to [miku_love] for the remainder of the night, but it goes back down the morning after when she has trouble remembering what happened.{/i}
> {i}You hurt yourself when you got home, but only you will know what that means.{/i}（[5475]–[5476]）

### mikudorm55p1[5481]：解离夜
- 开场即超现实化：Sensei 敲门"震碎现实"，进入西语的**萨尔瓦多·达利／圣安东尼的诱惑**幻境关卡（[5503]–[5553]）——达利指令中"看穿墙壁"引出旁白承认自己有"看见一切"的主角能力，却"看不进她的脑子"（[5545]–[5552]）。
- 门内 Miku 在解离循环："It isn't real. None of it's real."（[5558]–[5563]）。旁白借蠹鱼（silverfish）隐喻展开对玩家的第二次直接攻击：
> {i}But the craziest part of all is that there are people even worse than you. And you never know what those people are doing with doors.{/i}（[5577]–[5578]）
- 随后旁白本身崩坏（大小写错乱）："But I woN'T keep It THat WaY any LOnger... And why the month of July no longer exists for me."（[5587]–[5589]）——"七月消失"是未解伏笔。
- 旁白补叙 Miku 战前的温暖家庭记忆（微波炉晚餐、周末电视、睡在父母中间），并以一句惊人的措辞收尾：
> N: The following day would mark a reset — just not the kind you're familiar with.（[5617]）
- 现实层：Miku 归罪 Sensei 偷走她的药（实为 Makoto 收缴，[5734]），歇斯底里发作、撕扯头发，Makoto 回家后 Sensei 被请走。系统结算：affection -10（[5835]）。

### mikudorm55p2[5843]：道歉日与创伤解明（全线情感顶点）
- 清晨 Miku 主动上门道歉，坦白前一晚的真相：药没被偷，是她自己忘了放哪；Makoto 找到后冲掉剩余药物并联系 Maki 安排正规就诊（[5996]–[6013]）。
- Miku 决定第一次向 Sensei 讲述"为什么我是这样的人"（[6051]–[6068]），完整复述童年惨案：深夜起床喝水→撞见两个入室者（含两人的对话插叙 int1/int2 [6081]–[6104]）→叫醒父母→躲藏→两声枪响→呼喊渐弱→试图摇醒遗体（[6074]–[6151]）。
> mi: Was it my fault? If I never woke up...If I never got thirsty...If I was quieter...Then maybe...maybe they would...（[6142]–[6144]）
> s: There is no "because of" anyone. Some things just happen without a reason.（[6147]）
- 创伤机制点明：任何巨响都会把她拽回现场（[6158]–[6163]），"They'll make me talk"的真正含义是害怕向医生复述这段经历。
- 结算：affection +10（[6195]）。

### mikuspring1[6216]：抑郁期重逢（第四章开端）
- 时间点位于 Sensei 因 Ami 相关事件陷入"sadness-coma"闭门数月之后（[6256]、[6439]）；开场大段自毁性自言自语独白（[6219]–[6229]）。
- Miku 电话把他拉回社交圈：组织与 Io/Uta 的野餐（[6269]）。她自述近况：戒断药物成功、开始心理治疗、成绩回升（[6260]–[6261]）。
- 野餐上她逐一报告众人状态，其中 Ayane 每次游泳部后在淋浴间偷偷哭的观察（[6462]–[6463]）是为 Ayane 线埋线。
- **记忆异常时刻**：她说想回到"年初那样"，随即卡壳——
> mi: Wait...what? Weren't you absent at the start of the year? How does that...nah, I've gotta be...（[6483]）
  她隐约察觉 Sensei 年初根本不在学校，但念头被自己掐灭。这是 Miku 线最直接的"循环/时间线不一致"露头。

### mikuspring2[6512]：promised land（成人用品店）
- Miku 把 Sensei 带到 Miyamura 家的成人用品店"启蒙"（[6518]–[6521]）；Maki 出场，马件（horse cock）喜剧段（[6588]–[6627]），同时确认 Maki 已从 Sara 处得知 Sensei 回归（[6635]）。
- Miki 信息更新：Makoto 的"神秘男友"似乎已了结或转入地下（[6673]）。
- Miku 在店内看到不该看的东西当场社死逃离（[6681]–[6696]）（具体所见未明示，待核）。
- 夜路上 Miku 首次主动求牵手，被 Karin 撞破后慌乱圆谎（"That's just from all the porn." [6791]）。事件末解锁 karaoke 支线跳转（karinspring2，[6990]）。

### mikuspring3[6993]：Dorm Wars 动员与室友深谈
- 前半为运动会喜剧：Miku 给 Futaba/Sana/Ayane 排兵布阵（[6997]–[7150]）。
- 后半 Makoto×Miku 淋浴间对话是本章重心，信息量极大：
  - Makoto 自述反常的轻松感："Like all of the weight I've been carrying my whole life has somehow just *vanished.* And I can be me *now* without worrying about how I'll be in the *future.*"（[7266]）——结合世界观（无限时间、"no rush anymore" [7290]），这是死亡驱动/循环感知的强烈暗示。
  - Miku 试探竞争底线并获得承诺："If that person's me, we'll stay friends...won't we?" — mak: Of course.（[7293]–[7294]）
  - 本章收尾旁白只有两句，指向 Sensei 缺席的状态：*One more day without you passes by. The cogs continue to move.*（[7299]–[7300]）

### mikuspring4[7308]：跑步约会与告白铺垫
- Sensei 一反常态主动约 Miku 慢跑（"To make you happy." [7347]），恢复旧日活动。
- 膝枕段 Miku 脱口而出："Is this what havin' a boyfriend's like?"（[7485]）、"I like you *so* much, Sensei."（[7502]）。
- 两人就"排他性/嫉妒"长谈，Sensei 少见地袒露过去："I used to have feelings for someone who belonged to someone else."（[7575]–[7584]）。
- Miku 给出本线最重要的自我定义陈述：
> mi: I can't give ya brains like Makoto or boobs like Futaba. I ain't as creative as Nodoka, ain't as stylish as Chika, and I ain't even half as cute as Ami. I ain't got much, really. Don't even have a family anymore. All I have to give is myself.（[7604]–[7605]）
> s: You've really grown up, Miku. — mi: Not without help, I haven't.（[7611]–[7612]）
- 章末 Miku 正式提出初夜意愿（"I wanna do it with you..." [7630]），并补充 Makoto 教的安全套常识但自己不想用（[7639]–[7644]）。

### mikuspring5[7652]：初夜失败（全线下半最重要节点）
- 事前反复确认与怯场喜剧（倒数十秒协议 [7832]）之后急转直下：进入失败、剧痛、大出血，Miku 数次喊停（[7970]–[7978]）。
- 过程中旁白出现**第二种声音**——粗体小写的内心恶魔，用最粗鄙的话阻止他停手：
> hey man, it's not YOUR fault she's tight as shit... stop thinking, bitch boy. just savor the moment.（[7945]、[7957]）
  这是 Sensei 内在加害者人格的首次成文化显形，与 mikupool55 的自我合理化独白同构但更露骨。
- 恐慌处理段落里 Sensei 再次拨给 Makoto；Makoto 冷静接管（拒绝叫救护车以免暴露，"You doing that raises so many red flags" [8104]），并顺带回忆起自己初夜也被同样丢下（[8100]）。
- 本事件使 Miku 的阴道性交此后长期不可用，直接塑造 mikulust5/spring6/spring7 全部替代式性行为的叙事逻辑。

## 三、lust 线概貌（抽象概括）

Miku 线的成人内容有一条清晰的**身体承受力母题**：她的身体无法容纳常规性行为，于是所有 lust 场景都围绕"替代方案—练习—等待成长"展开，且每次都伴随权力/竞争话语（与 Makoto、Kirin、Sana 比较）。

1. **mikuinvite2（[4745]–[5124]）**：首次口交。"fair is fair"的互惠框架由 Miku 自己提出；她把性行为理解为与好友的"竞争得分"（"It just...feels kinda like I'm...winning right now" [4947]）。事件解锁 lust 变量与随时邀约权限（[5120]–[5121]）。
2. **初夜失败（spring5）**：唯一一次尝试阴道性交，以伤害与恐慌告终（详见上文）。叙事功能：把"性=竞赛"的 Miku 式认知撞碎一次，也让她此后对 Sensei 的信任反而加深。
3. **mikulust5 → mikunaming/mikupostnaming（[8123]–[8537]）**：店后室场景引入"naizuri"类体位替代方案（[8266]），核心是命名选择树——Sensei 让 Miku 选一个称呼（详见第四节 meta 分析）。此段确立 Miku 性格中的开关特质："the sexual stuff is essentially activated by a toggle switch"（[8726]）。
4. **mikuspring6（[8848]–[9027]）**：秘密公寓的豆芽菜晚饭+轻度亲密。成人内容退居背景，主体是道德辩护对话（见第四节第 6 条）。
5. **mikuspring7（[9132]–[9330]）**：指尖+仅顶端进入的边缘行为，Miku 主动配合并自慰；Sensei 在最后关头的出体外射决定中闪过一个"whale"念头（[9322]–[9323]，含义未解）。事后 Miku 提出 boyfriend 称号请求（[9363]）。

## 四、与主线/元叙事咬合点

1. **Sensei 自报真名 Akira（[5363]）**：药物过量事件中意识混乱时说出 "My real name is Akira. Hello."——与 Ami 线系统文本、Maki 等人直呼同构，是"真名"母题在 Miku 线的落点。另见命名树的 Akira 分支（[8511]–[8522]）："What's more romantic than being called by your regular name during the most intimate moments of your life?"

2. **Miku 玩过游戏本体——全书最直白的元叙事对话（[8438]–[8466]）**：命名树 Selebus 分支中，Miku 脱口接上 "Lessons in Love. I know."（[8440]），解释是 Maki 让她试玩前半小时熟悉商品，还提到游戏里的 Ami 对她说 breed her（[8445]–[8446]）。随后两人共同推演套层悖论：
> s: I just feel like this creates some sort of meta paradox thing where we all exist inside of a game that simulates exactly what we're going through right now.（[8453]）
> mi: So you're sayin' that what's happenin' now could be happenin' in the game version too?（[8454]–[8455]）
Sensei 为避免悖论主动放弃该选项（"let's just say you *shouldn't* call me Selebus" [8463]）。这是全项目对"游戏套游戏"最露骨的一次正面讨论。

3. **reset 措辞（[5617]）**：旁白描述 Miku 战前日常时写道 "The following day would mark a reset — just not the kind you're familiar with."——用玩家熟悉的 "reset" 一词指代普通生活的日复一日，与循环层术语形成刻意互文。

4. **记忆不一致的自觉（[6483]）**：Miku 是少数自己察觉"年初你不在学校却说要回到年初"这一矛盾的角色，虽当场自我否认。配合 spring3 中 Makoto 的 "life is a constantly repeating-" 被打断（[7186]，Makoto 线），构成宿舍组对循环层的渐进感知。

5. **旁白对玩家的两次直接攻击**：①mikuinvite2 后的忏悔独白 "Please. Stop watching me."（[4696]）；②mikudorm55p1 的蠹鱼段落——"there are people even worse than you. And you never know what those people are doing with doors."（[5577]–[5578]）。两处都把玩家的观看行为本身定为共犯结构。

6. **道德辩护与 groomed 一词（[8962]–[9013]）**：spring6 晚餐上 Miku 以"社会多数派"逻辑为关系正当化（"In a world where everybody's crazy, it's the normal person who's insane" [9001]、"[if] we can't make each other happy because of a number...that's kinda lame, ain't it?" [8973]）。Sensei 的回应罕见地不闪避：
> s: ...that's exactly what any girl who has been groomed would likely say.（[8970]）
> s: I do this because I'm addicted, selfish, careless, and self-destructive. It's the worst combination possible.（[8991]）
而 Miku 的回答是本线情感核心："You're one of the very few things out there I'm not afraid of, Sensei."（[8994]）、"if you wanted to hurt me, you'd have done it already."（[9011]）

7. **内心恶魔声音成文化（[7945]–[7957]、[8028]）**：初夜失败段出现的粗体第二人称声音，以及恐慌顶点 Sensei 内心吼出的 "EVERYTHING WILL BE FINE"（[8028]），把 mikupool55 中"I am making the right choice"的自我催眠机制升级为人格化的加害者声部。

8. **Makoto 的异常化（[7253]–[7268]、[7290]）**：室友观察视角记录了 Makoto 的剧变——"you've felt a lot...different. Happier, maybe?"→mak: "I am. Happier now... Or...at least, more *free.*...all of the weight I've been carrying my whole life has somehow just *vanished.*"——与 Makoto 主线的死亡驱动线索互证；Miku 作为最近距离的观察者是这条暗线的重要证人。

9. **万圣节失忆事件（[4748]、[4849]）**：Sensei 内心两次提及酒店房里发生过的事"Miku doesn't seem to remember"，且以 "Valium." 一词点出可能原因——暗示存在被药物抹除的共同经历，属跨线伏笔。

10. **命名权自指玩笑（mikunaming 全分支 [8286]–[8534]）**：让角色为玩家角色命名的分支树本身就是对视觉小说命名输入机制的戏仿；其中 Makoto 分支（"every time I close my eyes, I also just imagine I'm Makoto" [8368]）与 Kirin 分支、Coach 分支（足球部回忆杀 [8406]–[8433]）各自回收本作其他人物线。

11. **affection/lust 变量直显常态化**：本线 8 处以上系统文本直接以变量名结算（[5120]、[5475]–[5476] 含条件回退、[5835]、[6195]、[6985]、[8750]–[8751]、[9406]–[9407]），其中 [5475]–[5476] 的"次日回落+你回家后伤害了自己"两条是系统文本直接向玩家施压的罕见案例。

12. **Moby Dick 双引文（spring7 [9117]–[9128]、[9389]–[9395]）**：madness/forbidden seas 引文对应 Sensei 自我认知的恶化（"I bypassed a chrysalis entirely and evolved discreetly before your very eyes" [9127]），温暖/寒冷对照引文则用于收束 boyfriend 请求后的夜晚——文学引用承担了旁白的自我诊断功能，与 Yuki 线的诗歌引用同构。

## 五、未解伏笔

按可信度排序：

1. **"七月消失"**：旁白崩坏段自称 "the month of July no longer exists for me"（[5589]）——指向 Sensei 经历中的某个被删除/不可面对的时间段，与循环层的重置节点可能相关。（高可信为有意伏笔）
2. **whale 念头**：spring7 射出前一刻 "It's a whale."（[9323]）——无上下文，或与 Moby Dick 引文体系、或与世界观某意象相关，待核。
3. **万圣节失忆**：Valium + 酒店房（[4748]、[4849]）——那晚实际发生了什么、谁下的药、为何只有 Sensei 记得。
4. **Miku 拔发复发**：spring6 提到新发型是因为 "the thing happened again and Makoto had to...clean stuff up"，且 Miku 自己"完全不记得那一晚"（[8866]–[8868]）——解离性发作在治疗开始后反而复发，且伴随记忆缺失。
5. **Io 的药物来源与动机**：Miku 坚持不在 Makoto 面前提及 Io（"I didn't wanna throw Io under the bus" [6009]）；Io 的"药剂师"行为链未见源头交代。
6. **Chika 的 boyfriend 崩坏**：Sensei 向 Miku 承认 Chika 因称号问题"kind of snapped"并担忧她会杀人（[7550]–[7556]）——跨线炸弹。
7. **Makoto 的 vanished weight**：室友视角确认其反常轻松感（[7266]），与主线死亡暗示的最终关联待后续章节验证。

## 六、label 总表（38 个）

mikupool[1] · soccerfield[13] · callmikumorning[42] · callmikuafternoon[58] · callmikunight[141] · mikuinvite[231] · mikuinvitegen[242] · mikuinviteaff[286] · mikusoccergen2[323] · firsttimesoccer[354] · soccer2to4[619] · soccer5[652] · soccer10[951] · soccer15[1355] · soccer20[1651] · soccer25[2067] · soccer30[2439] · mikuwinterbeach1[2754] · soccer35[2804] · mikudorm45[3145] · mikudorm45p2[3496] · mikuspecial50[3899] · mikudorm50[4260] · mikuinvite1[4306] · mikuinvite2[4649] · mikupool55[5132] · mikudorm55p1[5481] · mikudorm55p2[5843] · mikuspring1[6216] · mikuspring2[6512] · mikuspring3[6993] · mikuspring4[7308] · mikuspring5[7652] · mikulust5[8123] · mikunaming[8286] · mikupostnaming[8537] · mikuspring6[8762] · mikuspring7[9041]

---

## 二轮增补

（原浅版文档不含二轮/三轮增补小节，此处保留占位。若后续有增补内容，请追加于本节之下。）

