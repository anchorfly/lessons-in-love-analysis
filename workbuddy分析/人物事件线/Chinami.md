# Chinami 事件线精读笔记（ChinamiEvents.rpy，v0.55，共 5889 行 / 22 label）

## 一、角色基本盘

- **Chinami Chosokabe**：Chika 的妹妹，小学生体型。自称"5000 岁巫师"（wizard），游戏内多处用 `if bonus == True` 分支区分"巫师设定"与普通解读（如 `chinamidate1` 行 332："even if she is a 5,000 year old wizard"）。
- **身体状况**：免疫缺陷 + 严重花生过敏（`chinamidate10` 行 1030 "peanut incident"，Yumi 曾喂她花生险出事）；出门须戴手套、口罩/头盔，除 Chika 外不被允许外出（Yumi 因花生事件被禁带她出门）。
- **语言习惯**：第三人称自称；经营虚构企业 "Chinami-Corp"（主营长颈鹿），热衷股票/GME/商业术语梗；口头禅后期变为 "Bad News Bears"（`chinamidate30` 行 2400 起）。
- **对 Senpai 的称呼**：从 "Sensei" 逐步过渡到 "future dad"（`chinamidate10` 行 931）→ "Papa"（`chinamidate20` 行 1618 起）。
- **调度结构**：`callchinamimorning`(行1)/`callchinamiafternoon`(22)/`callchinaminight`(39)，按 `chinami_love` 阈值（0→date1、10→date10、15→date15、25→date25 等）与章节标志分发；夜间通话曾因"Chika 在场不好解释"被拒。

## 二、love 线逐事件脉络

### chinamidate1（行200）
电话开场：Chika 请 Sensei 去"看妹妹"（dog-sitting 梗："You want me to dog-sit again." 行228）。首次独处：Chinami 假装看电视（电视其实没开），最爱节目是《权力的游戏》（行346 "Game of Thrones."），自测属于兰尼斯特家（"They have a lot of money and like each other more than they're supposed to" 行368）。梦想："one day, Chinami is going to be rich. And then she's going to buy a big house for her and big sis."（行375-376）

### chinamidate5（行545）
"Chinami hotline! This is the CEO, Chinami speaking!"（行559）。黑暗面一闪："Chinami never does anything. She just sits in a room and cries."（行569）。居家读 Yumi 藏的血腥漫画、玩杀猪手游（"The pig game is also the only thing she's better than her sister at" 行611）。提出想学"大姐姐们的课程"，为将来能上学做准备（行620）——旁白点出 "{i}If{/i} she's ever allowed to go to school."（行622）

### chinamidate10（行918）
接电话即喊 "Good morning, future dad!"（行931）。bonus 分支：Chinami 相信"牵手=怀孕"、催 Senpai 让 Chika 怀孕给她换小妹妹（行935-958）。阳台场景：Chinami-Corp 完成"收购"、想买大象、抱怨 Chika 不让她投 GME（行1046）。约定以后一起做 Jell-O（行1057）。

### chinamidate15（行1232）
冬季泳池派对（充气儿童泳池）。Chika 电话骚扰："Come get wet with my sister and me."（bonus，行1255）。Yumi 泡在 kiddie pool 里给 Chinami 上经商课（行1321-1323）。本段后部（约行1500）出现关键台词："Chinami has no future." / "Or at least not the kind of future her sisters and their future husband do."——Chika/Yumi 与 Senpai 结婚的玩笑语境，随后 Chika 回家撞见。

### chinamidate20（行1589）
商场约会。Chinami 戴狗面具喝不了草莓牛奶（"Doggies can't drink strawberry milk. They'll get a tummy ache." 行1639）。偶遇学生 Otoha 与 Rin，名场面："Please tell me you're not going to pretend she's a real puppy."（Otoha，行1706）/ Rin："If we just accept and agree that it {i}is{/i} a puppy, we can all move on"（行1708）。Otoha 翻旧账"你曾计划绑架我"（行1717）。

### chinamidate25（行2033）
Chinami 的"商业伙伴" Tsukasa 与其姐 Touka 来访。互称 "Papa!" / "Jeeves!"（行2098-2099，Touka 全名梗 "Philip Jeeves Tsukioka the Fourteenth"）。Touka 对贫民公寓的真实反应："It is an utter crime that people are allowed to live in such places."（行2132）。楼下的电视天线没人敢拆，"Chinami doesn't want to be homeless!"（行2147-2148）。

### chinamidate30（行2307）
强 meta 开场：blood1-4 场景 + "{s}I GO TO MALL{/s}"（划掉重写，行2321），旁白直白粗俗化（"time to fuck my fake girlfriend" 行2324）。商场陪 Chika 给 Chinami 买衣；"thick meatloaf" 双关梗连环翻车（行2383-2388）；Chinami 从 Tsukasa 处学来"affair"一词并爆料 "Tsukasa's big sister is having an affair with everyone in town!"（行2410）。

### chinamispring1（行2643）
Chika 出门打工后 Sensei 留守。大段自我厌恶独白：设想自己成为 Chinami 父亲 figure，"And I would break her like the china doll she is"（行2686）；担心自己像伤害 Yumi/Molly 那样伤害她（行2692）。鬼魂问答（行2706 "Do you believe in ghosts, Papa?" → static 闪切后答 "Yes."）。核心对话："Does Papa love Chinami?" ——"No."（行2754-2755）；"Is it wrong for you to love big sis Chika?" ——"It's extremely wrong. Because I'm thirty-one."（行2766-2771）。

### chinamispring2（行3001）
Senpai 敲门拜访，Tsukasa 以"商业伙伴"身份出场（"Jeeves"称呼延续）。两人大人式互动让 Senpai 不适；本事件铺垫 Tsukasa 对成人话题的好奇被点燃（在 spring5 被 Chinami 点破："She never talked about any of that adult stuff until she saw you do it" 行4372）。

### chinamispring3（行3421）
高烧看护事件。开场为整段颠倒世界意识流诗（"The sky was upside down when I stepped outside today." 行3426；"I will never get to where I'm going." 行3439）。此前插入 "mall Chika" meta 电话：低俗小写文风、"don't have sex with her either"（行3463）、"i love you bye"（行3475-3476）。正文中 Senpai 自我催眠："Hello. My name is Akira Arakawa. I have a wife named Chika and a daughter named Chinami. These are not delusions."（行3491-3492）。直面 Chinami 可能早死的恐惧（行3519-3520）。

### chinamispring4（行3957）
浴室场景。开场又一首自物化诗（"Today, my bones will be the soup..." 行3963-3967）。Senpai 全程背对、拒绝入浴（"this is already a step further than I planned on going today" 行3985）。Chinami 连环危险提问：Chika 说梦话泄露"你爱不止一个人"（行4014）、"Has Papa been doing naughty things with big sis Yumi?"（行4023）、最后压轴 "Or maybe {i}I'm{/i} your type and that's why you're afraid to get in the bath with me."（行4075）。Senpai 三选一回答："Chika would come out on top."（行4076）。

### chinamispring5（行4293）（即 chinamiconfronts 系列）
Chinami 回家质问：她听到了隔墙声音、且在 Tsukasa 家时 Senpai 与某女孩在其房间做事（行4342 "Papa {i}made{/i} this hole when he did it with a girl in Tsukasa's room!"）。核心控诉："She just doesn't understand why everyone starts going crazy once they meet {i}you.{/i} You're just a normal boy."（行4381）；"Big sis Chika too! She {i}never{/i} lied to Chinami before she met you!"（行4379）。Chinami 承认自己开始感到说不清的悲伤（行4397-4398），结尾 "Chinami doesn't know if that's possible anymore, Papa..."（行4408）。

### chinamispring6（行4636）
Chika 归家发现两人相拥睡着，幸福感独白（"Look at what I have..." 行4679）与叙述者冷峻插叙（"harm befell the man below her before he'd even reached Chinami's age" 行4674）。深夜 Chika 在熟睡的 Chinami 身旁对半醒的 Senpai 主动身体亲密（行4713-4743，含 "You'll wake up our daughter..." 行4729）——详见 lust 概貌。

### chinamispring7（行5106）
承接主线：偶像 Niki 向全世界公开与 Senpai 的恋情，Chika 崩溃失语并持刀（"she has a knife" 行5143）。Chinami 漂了金发（新立绘，行5181）并组织营救：用花生威胁失败（差点害死自己）、拖 Chika 到椅子上坐好。Senpai 用"Niki 后台通行证"试图唤醒，无效后开玩笑 "I'm going to run away with your little sister and marry her."（行5227）。观察到 Chika 仍下意识举刀护妹（"she's still {i}subconsciously{/i} trying to protect you" 行5244）。

### chinamispring8（行5371）
Chika 走出崩溃的方式是疯狂扫荡 Niki 周边（"WE NEED MORE MONEY!" 行5414）。Chinami 邀 Nao-chan（全程只发 "!" 的无口角色）一起买 boba；两人遭遇 mall 里两个"传送门"（Death / Life）的纯 meta 寓言段落（行5437-5464），Chinami 选择 Life 门："Because life is objectively better than death."（行5460）。收尾诗句："One step, two steps, three steps, jump. What fun we will have once the tree is a stump."（行5469-5470）。

## 三、lust 线概貌（抽象表述）

- 本文件**没有以 Chinami 本人为对象的独立 lust label**（对比 Imani 文件有 imanilust5 等）；Chinami 相关的成人内容全部以"在场者/旁听者"框架出现在 love 线事件中，且叙事上刻意强调 Senpai 的自我厌恶与克制。
- `chinamispring3`：fever watch 期间穿插 meta 化的粗俗旁白（把 Chika 称作妻子、把自己称作父亲的催眠式独白），以及"差点起意又压下"的心理描写。
- `chinamispring4`：浴室共处一室（背身），文本重心是 Chinami 的越界提问而非描写本身。
- `chinamispring5` 开头：以 Chinami 视角复述此前发生在 Chika 与 Senpai 之间、以及 Tsukasa 家房间里的成人行为（她只是听到者）。
- `chinamispring6`：Chika 在熟睡的 Chinami 身旁主动发起亲密行为——未成年人同床在场的框架，属全作最争议桥段之一，此处仅记录存在与位置（约行4713-4760），不复述细节。
- 结论：Chinami 线的功能是"欲望叙事的道德镜面"——她是 Senpai 用于自我证明"我还有底线"的对象，而文本不断暗示这面镜子正在碎裂。

## 四、与主线的咬合点

1. **meta/重置系统**：`chinamidate30` 的 blood 开场与划掉重写文本、`chinamispring3` 的 "mall Chika" 平行场景与意识流诗、大量 `_in_replay` / `renpy.end_replay()` 结构（17 处 end_replay）——Chinami 线是全作 meta 实验密度最高的线之一。
2. **家庭线（Chika 线）**：Chinami 是 Chika 线的常驻副舞台——从 dog-sitting 起点直到 Niki 公开恋情→Chika 崩溃持刀（spring7）→周边扫店疗愈（spring8），完全嵌在 Chika 弧线的每个节点上。
3. **Yumi 线**：花生过敏事件解释 Yumi 缺席；spring1 中 "big sis Yumi is...actually, Chinami doesn't know what big sis Yumi has been doing"（行2741）呼应 Yumi 主线失踪期。
4. **Niki 偶像线**：spring7-8 直接消费主线 Niki 事件；Chinami 对 Niki 海报的态度（Imani 线里也有喊话梗）形成跨线呼应。
5. **其他角色交叉**：Tsukasa/Touka（date25、spring2、spring5）、Otoha/Rin（date20）、Nao-chan（spring8，无口设定首次大篇幅展示）。
6. **Senpai 黑深残内核**：spring1/spring4 的诗与独白持续供给他"童年受害→加害焦虑"的主线心理逻辑（"someone lit my hands on fire a long, long time ago" 行3995）。

## 五、未解伏笔清单

1. **Chinami 的寿命**：多处暗示她可能活不长（spring1 行2695 "she's probably going to die before any one of us"；spring3 整场高烧恐慌），病因与结局未揭。
2. **"5000 岁巫师"真伪**：bonus 分支反复横跳，官方从未盖章；spring8 的传送门寓言进一步模糊现实边界。
3. **Chika 持刀崩溃**的完整后续与心理修复在 Chinami 线内未闭合（移交 Chika/Niki 主线）。
4. **Nao-chan 的"两个传送门"**：spring8 结尾诗句（"once the tree is a stump"）指向不明，疑似大型 meta 伏笔。
5. **Chinami 的早熟知识来源**：她自称"从 K-drama 学的""GoT 学的"，但对成人话题的精准追问（spring4/spring5）超出解释框架；"Chinami will do that so long as Papa promises to keep it a secret"（行4063）暗示她有交换筹码式的目的性。
6. **"everyone goes crazy once they meet you"**：Chinami 在 spring5 提出的指控是全作核心命题的角色版表述，尚未在文本内被正面回应。

## 六、label 总表

| label | 行号 | 一句话内容 |
|---|---|---|
| callchinamimorning | 1 | 晨间调度入口，按 chinami_love 阈值分发 |
| callchinamiafternoon | 22 | 午后调度入口 |
| callchinaminight | 39 | 夜间调度入口（通话被拒梗） |
| chinamimorninggen2 | 47 | 与 Chika 的晨间日常（通用填充） |
| chinaminoongen2 | 79 | 正午通用填充 |
| chinamigenmorning | 112 | 通用晨间片段 |
| chinamigenafternoon | 155 | 通用午后片段 |
| chinamidate1 | 200 | 首次看娃：GoT、买房梦想 |
| chinamidate5 | 545 | CEO 热线与讲故事：哭泣一闪、血腥漫画 |
| chinamidate10 | 918 | future dad 来电：收购、GME、Jell-O 之约 |
| chinamidate15 | 1232 | 冬季泳池派对："Chinami has no future" |
| chinamidate20 | 1589 | 商场狗面具约会：偶遇 Otoha/Rin |
| chinamidate25 | 2033 | Tsukasa/Touka 来访：Papa & Jeeves |
| chinamidate30 | 2307 | meta 商场行：meatloaf 梗、affair 八卦 |
| chinamispring1 | 2643 | 独守：鬼魂问答、"Does Papa love Chinami? No." |
| chinamispring2 | 3001 | 拜访：Tsukasa 商业伙伴登场 |
| chinamispring3 | 3421 | 高烧看护：意识流诗 + mall Chika meta |
| chinamispring4 | 3957 | 浴室拷问：naughty stuff 与三选一 |
| chinamispring5 | 4293 | Chinami 质问：为什么遇见你大家都疯了 |
| chinamispring6 | 4636 | Chika 归家：三人同榻之夜（敏感） |
| chinamispring7 | 5106 | Niki 公开恋情余波：持刀的 Chika |
| chinamispring8 | 5371 | 周边扫店：Nao-chan 与生死传送门 |
