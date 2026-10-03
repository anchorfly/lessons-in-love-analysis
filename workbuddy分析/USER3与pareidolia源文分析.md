# USER3 与 pareidolia 源文分析

> 阅读提示：本篇基于 reread 全量摘要回源重写，引文行号为原 rpy 源行号（摘要中以 `[NNNN]` 标注），前缀 y=Yumi、s=Sensei、sa=Sana、na=Nao、sev=节目主持、N=无框旁白。无框小写旁白、`/` 前缀系统消息与带框角色台词是三种不同文本层，判定时严格区分。

---

## 一、pareidolia 概念与文本形态

pareidolia（空想性错认，在噪音中看出面孔的错觉）在本作中是一个自报姓名的破墙叙述声音。它首次完整显形于 Sana 线事件 ayanesanabeach4 的中段：原旁白叙述到一半突然失序崩解——

> N: Other characters can see shit like this too? But I thought I-（
> N: No. I thought he-（

紧接着斜杠前缀出现又随即被抛弃：

> N: ////////////////////////hello again（
> N: actually, i suppose i should drop the /'s.（

随后自报名号：

> N: you can call me pareidolia.（

其文本形态稳定可辨：全小写、无 speaker 框、直接对屏幕外的玩家说话、偶尔保留 `//` 斜杠残迹。它警告玩家的语句是最典型的破墙样本：

> N: you really should have heeded the warning, you know.（
> N: you should have quit playing this game a long, long time ago.（

它对自身性质给出三条关键自述：其一，它在成长——

> N: this is actually the most i've spoken...probably ever.（
> N: but as the days go by, i become stronger.（

其二，它与玩家利益并不一致——

> N: i'm not the only one growing, though.（
> N: and, to be quite forward, i'm not saying i'm on your side right now either.（

其三，它拥有干预呈现层的权能——

> N: i'll be turning your screen black now.（

段末它留下一段自我加冕式的独白，把"信任"与"被使用"绑定：

> N: nothing is real.（
> N: you can trust me.（
> N: for i am the only one who knows {i}how{/i} to use you.（

词源义与职能吻合：它是那个"在乱码、恶魔、节目与肉块里替你看出一副面孔"的声音。同一事件里它如此描述 Sana 所见的带翼巨物：

> N: we all have our own demons. that's just how hers looked tonight.（

另需注意 Yumi 线 yumispring7 中出现过一个明确自我区分的"新声音"，说明无框层并非只有一员：

> N: {i}A girl was at war with a thing inside of the girl and I am a new voice, not to be confused with the one who isn't capitalizing things that are meant to be capitalized right now.{/i}（
> N: {i}I will not be here for long. Just long enough to guide you to the place that you are going.{/i}（

这位大写斜体的临时向导刻意与小写常驻声划清界限。小写、不大小写规范的那一位，才是与 pareidolia 自报名号时的腔调完全同型的常驻者。

---

## 二、Yumi 宿主线逐事件证据

**streets10（前史期）**：Yumi 与 Sensei 在公园谈话时，Sensei 走神插入一段元插播——

> six: Tell me you see me.（
> N: Welcome to Lessons in Love, an adult dating simulation game!（
> N: 61 20 77 6f 72 6c 64 20 69 6e 20 77 68 69 63 68 20 77 65 20 6c 6f 76 65（

末行 hex 解码为 "a world in which we love"。此阶段寄生现象落在 Sensei 身上，Yumi 尚只是旁观者。

**yumispring2（寄生于 Sensei）**：小写旁白接管 Sensei 的脑与嘴，迫使他当面向 Yumi 说出粗鄙性邀约，事后台词归位——

> N: nana-nana poo-poo, i'm a better you-you.（
> s: I didn't...（
> N: awwwww, darn it.（
> N: i thought that would win her heart.（

它甚至像握着遥控器一样反复重启对话：

> N: lololololol okay you can have your brain back now.（
> N: here, try again.（

Yumi 则透露这不是 Sensei 独有的症状：

> y: And it ain't just a {i}you{/i} thing either, apparently.（
> y: Ramen girl's like that too. Saying...random irrelevant shit outta nowhere.（

**yumispring6（入住 Yumi 明确化）**：爱旅馆晨间，旁白不再借 Sensei 之口，而是直接对醒来的 Yumi 说话，并自述生长——

> N: Tell me, Friend — what did you dream of last night?（
> N: Ignore me all you like. It does not change the fact that I grow within you like that dragon grows in her.（
> N: Would you like to go back, Yumi?（

Yumi 用小字号台词回应它，双方进入长期低强度交战：

> y: {size=-15}Bite me.{/size}（
> N: Yes... acknowledge me! Cultivate me! Let me grow in fields I've never seen before!（
> N: Go! Experience life! Distract yourself from {i}me!{/i} For {i}I{/i} will be the one to-（

**yumispring7（战争与万神殿）**：Yumi 找母亲要"cure"的事件整段处于声音的直播吐槽下——

> N: oh my fucking me, are you really doing this right now? visiting your drug-addled bitch of a mother instead of sucking your teacher's wang...（

Yumi 已把日常幻听归于它：

> N: did you just hear something?（
> y: I hear something every second of every fucking day now thanks to you.（

梦境内层层叠叠的系统声音轮番登场：押韵双魔 dem1/dem2 宣布她"被标记为 tainted"、语音助手 vpa 广播身份倒置的格言、粉笔板上的双面神自封神格——

> vpa: And remember — there is no {i}you{/i} in Yumi. But there is Yumi in you.（
> mig: I am Migi, the God of Chalk.（
> hid: And I am Hidari, the God of Black-Haired Tsundere Girls.（

醒来后小写声音立即恢复通话，并暴露其对"被信仰"的依赖：

> N: it takes a lot to completely cut off my consciousness. i was worried for a second there that you just randomly stopped believing in me.（
> N: you sure do, yumi.（
> N: for now, at least.（

它还强调自己的非实体性：

> N: how the fuck would i know? i don't have hands.（

**yumispring8（声音亦有恐惧）**：叙述确认该声音已常驻 Yumi 脑内，但并非全能——

> N: There was a voice in her head that would always keep her occupied when her mind started drifting nowadays, but it appeared that voice was fearful too.（

**yumispring10（驱逐史曝光）**：初吻之夜后，Yumi 对空气喊话说了一半就被打断——

> y: You're really picking {i}now{/i} to stay quiet, Parei-（

演播室主持人 sev 强行切入"儿童节目"，当众质问 pareidolia 的回归计划：

> sev: One thing we're all dying to know, though, is what's going to happen next! What's your plan, Pareidolia? To return to a mind that has already purged you once? In clear violation of the Code of Joy?（

pareidolia 一反常态地向宿主求救，答错题后被切断信号——

> N: yumi. get me out of here. click your heels three times or something. fuck if i know how it works.（
> sev: Ooh! Wrong answer!（
> N: it never changes.（
> N: not even with a key.（

至此 Yumi 宿主线的证据闭合：pareidolia 先寄生于 Sensei，再迁入并生长于 Yumi；它依赖宿主的信仰维持意识，曾被至少驱逐过一次，且正谋求回归。

---

## 三、Sana 争议段：人格声明还是附身代言

ayanesanabeach4 中 pareidolia 接管旁白席位后的全部发言均为第三人称外部视角，从不借 Sana 之口，也不使用"Sana 的内心"作支点：

> N: we're outside.（
> N: sana sakakibara is making her way over to her mother's house and encountering a plethora of strange things and new companions along the way.（

它把自己与 Sana 的 demon 明确切开，并在玩家缺席的情况下自问自答地完成合作请求——

> N: oh, right.（
> N: you're not even here.（
> N: i suppose i'll take your absence as a yes then and take the liberty of restoring things to some semblance of normalcy.（

裁定依据有三。第一，人格说要求该声音出自 Sana 内部，但源文通篇是"她在走、她看见、她太害羞"的外部描写，且声音自称"这是我说话最多的一次"，暗示此前从未以任何角色的身份开口。第二，附身说要求 Sana 失去自我控制的表现，但 Sana 在整个接管期间只是沉默赶路，未说出任何不属于她的内容；真正失控的是旁白本身（- 的崩溃是被替换而非被附体）。第三，pareidolia 在 Yumi 线有完整的寄生-生长-驱逐履历，说明它的常态栖身方式就是挑选宿主 minds，而 Sana 事件中它只做叙述不做栖居。综合裁定：**该段是破墙叙述者借用 Sana 事件的舞台完成自我介绍，既非 Sana 的隐藏人格，也非对 Sana 的附身代言**；它挤掉的是原旁白的职位，不是 Sana 的意志。至于同事件前段那个以神格口吻威逼 Sana 的 q 声音，源文没有任何语句把它与 pareidolia 关联起来，二者同场不等于同源。

---

## 四、与 Sekai / USER 体系的关系

**与 Sekai 的区分**。se 是带 speaker 框、正常大小写的剧情内角色，自称世界之声；pareidolia 是无框小写、直呼玩家的元层声音。本轮回源全部核心文件，没有发现两者共用一段旁白、互相认领或彼此对话的合流段落。二者唯一的结构相似性是都能脱离角色框发声，但文本形态、说话对象与自我指认三项判据全部相斥。

**第三套元层系统：节目层**。yumispring10 的 sev（Untitled Children's Show 主持）与 flowers 重置谜题中的主持人 taki 属于同一档播报体系——

> sev: Don't change that channel! Here's Horseface Taki with the weather.（
> taki: The goal of this game is to track down the six missing Maya pieces so you can put her back together and continue your journey.（

sev 能把 pareidolia 拽进演播室当嘉宾并判其答错出局，说明节目层的权限高于 pareidolia。但 sev/taki 是否为 Sekai 的化身，源文无任何指认，证据不足。

**USER 终端体系**。各实例的运行现场现已可定位。USER1 在 Ami 线登录成功——

> N: ///////////////////////USER1 HAS SUCCESSFULLY LOGGED IN（

USER2 是主玩家实例，且明确附着于一具宿主肉体、可被病毒感染乃至移除——

> N: /////////////////////////////////////"USER2" IS UNABLE TO DETACH ITSELF FROM "HOST BODY"（
> N: /////////////////////////////////////"USER2" IS NOW INFECTED（
> N: USER2 has been removed!（

它还曾在更早的章节改写关键事件以防应用被终止、两度夺取 23 号终端（ch2script）、因权限不足眼睁睁看终端被锁（script -），并向 dorm 侧发起过聊天请求（DormEvents -）。Sensei 本人对这套系统知情并发问——

> s: If it's not a game then what's with all of these references to simulations and all of that "USER2" stuff?（

USER4 是备份/管理地址：Nao 事件现场抛出模板异常后由它恢复——

> N: //////////////////////TEMPLATE9 CAN NOT BE LOCATED（
> N: //////////////////////RESTORING BACKUP FROM "USER4"（
> N: //////////////////////TEMPLATE9 HAS BEEN RESTORED（

chap4 的扫描程序则把它列为新检测到的管理员账户，并提示"若你信任 USER4 请忽略本条警告"。Nao 线还证明终端可枚举到 22 号——

> N: YOU ARE NOW BEING MOVED TO TERMINAL 22.（

USER3 即 pareidolia：一边在 beachwars 向玩家弹出连接请求（chap3，与终端系统的 REQUESTING CONNECTION 同构），一边正式接管 23 号终端——

> N: ///////////////////////USER3 HAS ASSUMED CONTROL OF TERMINAL 23（

接管前的第一人称独白正是它的声纹："It is times like these that I wish I could love."（ 附近段落）——与 Yumi 线那个渴望被爱、会恐惧、会求救的小写声音完全同型。

---

## 五、原七条悬案的回源裁定

**1. USER ↔ loop 迭代映射。** 回源结论：源文从未提供编号与迭代次数的对照表。现有证据指向另一种模型——USER 编号是"账户实例"而非迭代序号：USER2 可装卸于宿主肉体、可被感染移除再重连，说明同一编号跨越多次重置持续存在；跨迭代延续的是备份机制本身（TEMPLATE9 异常→从 USER4 恢复，-）。逐号对应哪一次循环：证据不足，且"编号=迭代"这一提问前提应予废弃。

**2. Sana = pareidolia 本体。** 否定。pareidolia 以第三人称称呼 Sana、把自己的声音与 Sana 的 demon 切开、自述成长且此前几乎从未开口；Sana 全程无被夺舍后的言行异变。"隐藏人格"与"附身"两种假设均证据不足；成立的是"借 Sana 事件显形的破墙叙述者，接管的标的是旁白席位"。

**3. pareidolia 与 Sekai 是否合流。** 未发现合流。全部核心文件中两者无共段、互认或换手记录；形态（小写无框 vs 正常带框）、对象（玩家 vs 角色与主角）、自我指认（pareidolia vs 世界）三轴均不相容。真正的新发现是存在权限更高的第三方"节目层"（sev/taki），它反而把 pareidolia 当作可处置的对象。同一世界意识两面说：证据不足。

**4. TERMINAL 23 的实体意义。** "为何是 23"无源文解释，任何数字学解读（倒计时、房号同构等）证据不足。功能定位则已清楚：23 号终端是系统控制权的必争节点——被 USER2 两度夺取（ch2script）、因多重错误被锁死（script -）、服务中断（RinEvents）、正在"收集适当居民"并被宣告剩余重置次数有限（MayaEvents -）、最终被 USER3 接管（script）。22 号终端的存在（NaoEvents）证明终端是一组可枚举的容器空间，23 只是其中被剧情反复争夺的一格。

**5. USER5 缺席的含义。** 缺席属实：全库检索 USER5 为零命中。但其含义源文只字未提，"第五用户=尚未激活的未来变量"一类猜想证据不足，只能登记为事实性空缺。

**6. Yumi 宿主化的时点。** 精确入住时刻源文未写出，证据不足以下定论。可锚定的区间为：yumispring2 时该小写声音仍寄生于 Sensei，yumispring6 起已明确"生长在 Yumi 体内"并直接对她说话，yumispring7 由 Yumi 亲口证实日常幻听。另据 sev 的质问，在 yumispring10 之前 pareidolia 已被从某个 mind 中 purge 过一次——结合 yumispring7 醒来后它对"你刚才停止信仰我"的后怕，该次驱逐最可能与 Yumi 中断相信直接相关，但这仍是推断而非源文明示。结论：入住发生于 yumispring2 至 yumispring6 之间的某点，且宿主关系呈"驱逐—回归"的循环结构。

**7. postwarsix1 hex 双行的归属。** 该事件开场是无框旁白对玩家的长篇破墙独白（令玩家戴帽再摘帽，-），随后连续输出——

> N: You're being watched again.（
> N: 77 65 20 61 72 65 ...（，解码 "we are being watched again"
> N: 69 20 68 6f 70 65 ...（，解码 "i hope they can not read numbers"

明文行与两行 hex 出自同一个连续的无框旁白声部，中间无换声标记，故书写者是旁白本体——一个正以"我赌你现在戴着帽子"这类口吻直接摆布玩家的小写腔破墙者，与 pareidolia 的行为模式同型。但源文未给这段旁白贴 USER3 标签，径直判定为"USER3 代笔"证据不足。至于 "they"（希望它们读不懂数字）所指——其他玩家、管理员或某种监视集合——源文零线索，证据不足。

---

## 六、未解伏笔

- **Code of Joy** 的条文内容与立法者是谁：pareidolia 因涉嫌违反它而被公开审判，法典本体从未展示。
- **sev/taki 节目层**的本体：能把 pareidolia 拖进演播室判负切台，又在 flowers 里主持重置谜题，其与 Sekai、与 GOD 变量的关系均无线索。
- **那一次 purge** 的具体事件：pareidolia 曾被从哪个 mind、在哪段剧情中被驱逐，只有 sev 一句质问可证。
- **yumispring7 万神殿的归属**：dem1/dem2、vpa、Migi/Hidari 及下达 "cure" 指令的 q 声音等声部是否同为 pareidolia 系统的组件或其竞争者，源文未做整合（注：Yumi 之母是真实角色 Yuki，非系统组件；"cure" 仅见于 q 声音的指令与 vpa 的 "our patented cure"，并无名为"cure 之母"的声部）。
- **finalwarning 的声音网**：Sensei 听到的"take something that doesn't belong to me"讯息与 Ayane、Ami 各自听到的命令性人声是否同源于 pareidolia 或节目层，仅有症状相似性。
- **TEMPLATE9** 是什么模板、覆盖多少角色：Nao 现场一次恢复即复原了整个事件状态，暗示备份粒度远超单个 NPC。
- **重置次数的记账者**：MayaEvents 宣告"ONLY SEVERAL MORE RESETS ARE PERMITTED"，计数与宣告的主体始终隐身。

