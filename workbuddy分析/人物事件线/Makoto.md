# Makoto Miyamura 事件线深读版（MakotoEvents.rpy，约 11600 行 / 53 label）

> 基于 `_digest_Makoto.txt`（5984 行）分块全量精读，无跳读。所有结论标注 label 名与源行号；无法确认处标注"待核"。Makoto 是全书**觉醒弧线最完整的角色**：从普通优等生 → 隐性跨循环记忆者 → 第四位 loop-aware 觉醒者 → 启示录小队军师 → 主动测试世界规则的"实验者"。她同时是 sadgirls 群像的核心悲剧承担者。

---

## 一、角色基本盘

- **身份**：Kumon-mi 学园一年级生，班级实际运转者（工作表、测验、留言板全由她制作——见 sadgirls8 返校演讲自述 [5947]-[5948]）；家族经营成人用品店，与母亲 **Maki**、父亲 **Masahiro** 同住店铺楼上（pornshop 系列）；挚友兼邻居 Miku。注意：旧版文档误作 "MacCormack"，正确姓氏为 **Miyamura**（[5902] 自报家门）。
- **表面性格**：毒舌完美主义、"霸凌 Sensei"担当（[6465] "I'm the one who is supposed to be bullying him now"）；强迫性努力的内驱力是"让爸爸骄傲"（[5948] "something inside of me made me feel like I had to make my daddy proud one day"）。
- **深层状态**：长期抑郁伴自杀意念史——遗书早已写好多封（写给 Sensei、母亲、Miku、甚至 Ami，[6304]-[6306]）；反复出现的跳楼梦与跳楼冲动（winterbeach4 [3047]-[3083]、sadgirls7 [5138]-[5142]）。父亲之死（sadgirls1）是全角色线最大悲剧节点，直接催生"新 Makoto"人格。
- **loop-aware 轨迹**：winterbeach2 已有残缺的重置记忆（记得 IP 地址那次重置前的卧室事件 [2547]-[2562]）；makotodorm55p1 被 Sensei 测试出"谈重置不打断话题"（[6877]）；makotodorm55p2 正式入队，成为继 Maya、Ayane 之后第四位觉醒者。
- **关键变量**：makoto_love / makoto_lust 双轨（结算文本多次出现）；makoto_virgin（script.rpy 定义，待核具体门控）；witch costume（万圣节道具，被 Sensei 反复提及）；**sanity 变量在 makotospring2 中 +1**（[8923]，全 digest 唯一一次 sanity 结算）；"code red" 通讯暗语体系（spring4 起）。

---

## 二、love 线逐事件脉络

### 第一章～第二章（色情店日常与邀请系列）

- **pornshop / makotoinvite / postbluejaycall / postbluejay**（[1]-[74]）：事件路由器。postbluejay 过渡段承接 Bluejay 线后续。
- **callmakotomorning**（[75]）：Koi Cafe 早电话。穿插 Sensei 的黑暗独白（[141]-[147]），叙述基调异常沉重。
- **callmakotoafternoon**（[166]）：图书馆。Makoto 读宗教书，Sensei 内心独白 "**There are no gods**"（[235]）——叙述层的虚无主义宣言，与她后线的"神明不存在但观测者存在"体验形成反讽对照。
- **callmakotonight**（[257]）：夜电话路由。
- **makotoporngen2**（[272]）：钓鱼小游戏日常。
- **makotoinvitegen**（[312]）：邀请菜单入口。
- **firsttimepornshop**（[360]）：初遇核心场景——发现优等生 Makoto 在家族色情店打工的反差确立。
- **pornshop5 / 10 / 15**（[763]/[970]/[1025]）：店内递进。pornshop15 出现 Hero's Harem Guild 海报梗；**获得 Maki 的电话号码**（[1078]），为后期家长线埋点。
- **makotoinvite1**（[1141]）：家中邀请。Ami 宣战式登场（[1444]）；Makoto 即兴南北战争讲座（[1471]）——"未来教师"人设的第一次完整展示。
- **makotoinvite2**（[1497]）：支开 Ami 后的二人时间。拥抱与同意的讨论中，旁白抛出全书级台词：**"I console her because I am a little nicer in this version of the game."**（[1622]）——首次把当前循环称为"这个版本的游戏"。
- **makotoinviteaff / grind / finger**（[1641]/[1681]/[1864]）：亲密分支三连，finger 分支为 lust 入口。

### 第三章（冬季海滩四部曲＝记忆觉醒前奏）

- **makotolust5 / makotolust10**（[1090]/[1885]）：lust 节点，meta 密度极高（详见第三节）。
- **makotowinterbeach1**（[1935]）：冬季海滩。禁欲周末约定（沙里藏避孕套的喜剧）；结尾 Sensei 的 "**Hope**" 独白（[2219]-[2227]）——以希望为名的自我欺骗，为四部曲定调。
- **makotowinterbeach2**（[2266]）：Miku 同行日。Miku 崩溃史补完（[2432]-[2434]）；Makoto 质问自己是否只是 Sensei 的工具（[2458]-[2487]）。**全文件最重的伏笔场景**：Makoto 突然说出——
  > mak: We've been here before, haven't we?（[2547]）
  
  她记得"某次重置之前"在卧室发生过的事、记得一个 **IP 地址**（[2549]/[2552]），却说不清发生在何时——偏头痛随即打断对话（机制层面的"记忆检索被拦截"）。这是 Makoto 跨循环记忆的第一手证据，且比她正式觉醒早整整一个章节。
- **makotowinterbeach3**（[2599]）：末日感夜空；储物柜记忆矛盾（[2672]-[2688]）。**HO / A1 / A2 三个神秘实体登场并留下时钟三针谜语**（[2782]-[2823]）——Makoto 以近乎出神的状态接收信息。随后出现地震体感（[2851]-[2858]）、对"Yasu Yasui"的调查（[2860]-[2866]），以及**她对 Maya 展开的人肉侦查：Maya 所有电话号码均为空号**（[2882]-[2892]）。Niki 恋情在本段确认。
- **makotowinterbeach4**（[2944]）：跳楼重复梦的告白（[3047]-[3083]——同一个梦做了很多轮？措辞暗示重复）；正面承认抑郁（[3150]）；要求 Sensei 坦白其他女孩，得到 "**There are others**"（[3230]-[3231]）。love 线在此完成"互相暴露深渊"的结构。

### 第三章节点（new 三部曲）

- **makotonew1**（[3287]）：泳池清扫。Chika 生活状况的侧面暗示（[3443]-[3465]）；真诚夸奖戏；旁白出现 "**the previous iteration of me**" 措辞（[3544]）——叙述者对 past-loop 自我的直认；落水身体接触喜剧收尾。
- **makotonew2**（[3649]）：秘密房间撞见→相互爱抚（成人内容抽象处理）。收尾句 "**first seeds of corruption**"（[4112]）——把这段关系明确定性为"堕落的种子"。
- **makotonew3**（[4125]）：噩梦式开场 "SOMETHING IS SPROUTING"（[4144]）＋worm 寄生虫独白（[4151]-[4170]，与 Ami 线 amispring1 的虫神学同源）；午夜都市漫步、趴在父亲肩上的童年回忆（[4381]-[4392]）；关系定性问答 "**What are we?**"（[4405]）→ "**Maybe one day**"（[4417]）；装睡回避（[4439]-[4447]）；结尾连续弹出 **ERROR ADVANCING TO SATURDAY / ERROR ADVANCING TO SUNDAY**（[4482]/[4491]）——系统层错误直接写在恋爱事件结尾。

### 第三章末大悲剧（sadgirls 群像）

- **sadgirls1**（[4494]）：Yasu 开场预言 "**I'm sorry for what comes next**"（[4517]）；广播点名；Maki 冲进教室（[4621]）；**父亲死讯送达，Makoto 在浴室彻底崩溃**（[4701]-[4723]）；Miku 加入哀悼。
- **sadgirls7**（[4826]）：向日葵起源独白——"**that flower was me**"（[4832]-[4868]，向日葵=她自己的人格图腾）；对母亲的恶意玩笑（[5010]-[5024]）；**自杀意念直球**："Shouldn't I just die too?"（[5138]-[5142]）。
- **makotolust30skip**（[5231]）：拒绝分支。碰倒相框——渔夫帽小女孩与亡父的合影（[5242]-[5245]），无声的刀。
- **sadgirls8**（[5699]）：一周后的返校。开场 "I am one of those bad things"（[5727]）；Miku 向 Sensei 转述 "Makoto loves ya"（[5780]）。随后是**全文件最长的一幕公开崩溃**：Makoto 逃家返校，当全班的面宣布——
  > mak: Guess who's back, bitches.（[5811]）
  > mak: My name is Makoto Miyamura and my dad is fucking dead.（[5902]）
  > mak: BZZZZZZZZZZZZT! THE ANSWER IS THERE IS NO FUCKING POINT.（[5922]）
  
  控诉同学冷漠、否定努力的意义，最后自我贬低为 "Just like my mother."（[5966]）。Ayane 远距离听见全部内容（[5876]-[5883]）。N 旁白罕见地解释自己的纵容："Ami is a girl I have cherished and loved... And Makoto? Makoto will become one of those too."（[6000]-[6008]）——**把 Makoto 预编入"被珍视的女孩"名单**。Ami 以丧父过来人身份完成救援（[6029]-[6055]）。结算：affection 上涨，jump advancetosat。

### 高阶节点（special50～dorm55）

- **makotospecial50**（[6105]）：红鸟诗开场（"Redbirds bleed and blue ones die — that's the nature of this world of mine." [6110]-[6121]，第二段在天台收束时变为 "I could tell you why the cardinals fly." [6391]——同一首诗的治愈版回环）。签试卷日常后上天台，Makoto 完整交代遗书史：
  > mak: I went as far as writing notes. To you. To my mom. To Miku. I even wrote one to Ami once — but even that was mostly about you.（[6304]-[6306]）
  
  新人生目标："**Not writing any more notes.** And learning how to smile from the bottom of my heart instead of the pit of my stomach."（[6329]-[6330]）。affection +5（[6402]）。
- **makotopool55**（[6410]）：泳池边谈 Miku 与 Io；核心意象——两人是"太固执而不肯自己倒空瓶子"的人，约定互相倒空（[6633]-[6635]）；"secretary slash assistant slash friend slash girlfriend slash fuck buddy slash porno clerk... Just Makoto."（[6643]-[6645]）的身份清单自白。
- **makotodorm55p1**（[6671]）：空调故障裸读日常。Sensei 试探性谈论世界循环（[6858]-[6868]），发现 **Makoto 是唯一不切换话题的人**：
  > s: ...and yet here {i}you{/i} are, perfectly navigating the talk as if it's something you've known all along.（[6877]）
- **makotodorm55p2**（[6965]）：觉醒确认事件。先演示 Miku 对照组——每次提到重置都被逐字相同的台词打断（bra shopping 台词原样重复，[6882]-[6931]；Sensei 点名 "It's everyone except you and the two girls I mentioned earlier. And, for a brief moment in time, Yumi and Tsuneyo as well." [6929]-[6930]）。随后启示录小队（Maya/Ayane）在色情店集合：Maya 给出官方设定——每几个月世界重置一次、城市正常流动而人被送回、**Sensei 是所有人记忆延续的锚**（[7037]-[7045]）；Yumi/Tsuneyo 先例存疑（[7025]）。Ayane 正式命名 "Rooftop Apocalypse Squad"（[7060]-[7065]）；假结婚证勒索喜剧（[7183]-[7214]）；Makoto 以"反正没有可失去的了"接受新世界观并主动求欢（[7246]-[7254]）。

### 第四章（军师期）

- **sportswars19 / makotovsmolly**（[7279]/[7539]）：Dorm Wars 收官（详见第三节）。Makoto 弃权又被迫参赛、最终夺冠。
- **makotospring1**（[7942]）：电话邀约→"无限之夜"（[7994]）；Makoto 正面承认已放弃"赢到最后"的幻想、选择做合作的 harem 公主（[8009]-[8013]）；情报交换：Yumi 又开始缺勤（[8056]-[8059]）。本事件后半衔接一段**somnophilia 场景**（安眠药、Sensei 趁睡侵犯、"I have permanent consent" [8195]、睡中呓语 "**Daddy?**" [8279]-[8283]）；中途开发者乱入吐槽（[8313]）与 Akira/dev 对话（[8437]-[8447]，详见第四节）。该段的 label 归属待核（可能仍属 makotospring1 或独立子 label）。
- **endofmakspring1**（[8502]）：晨起怀疑自己说梦话（[8527]-[8561]）；Niki 搬入进行中（[8570]-[8571]）。
- **makotospring2**（[8591]）：偷猎者/羚羊隐喻开场；Miku 受伤送医；公园谈话是**Makoto 时间观哲学的集中爆发**：
  > mak: ...restore the flow of time.（[8845]）
  > mak: We're all dogs chained to poles.（[8860]）
  > mak: Make a new world.（[8886]）
  > mak: I love you so much.（[8888]）
  
  大理石眼猫意象（[8869]）。结算 **sanity +1**（[8923]）。
- **halloweenmakoto1**（[8944]）：Ayane 内心音开场；与 Yumi 谈论重置后的 Makoto："New Makoto just wants to relax and get laid"（[9002]）；**在 Yumi 面前公开承认师生性关系**（[9050]-[9065]）；Yumi 罕见释放善意；Makoto 承认此前的狠话全是自我说服（[9109]-[9111]）。
- **halloweenmakoto2**（[9186]）：**Sekai 平行时间线事件**。两人发现自己坠入"Sekai 未死"的世界线：Sekai 与 "Aki-kun" 结婚、Ami 是他们的女儿、京都鸭川求婚（[9203]-[9213]）。Sensei 对"不劳而获的幸福"感到愤怒而非喜悦：
  > s: But instead of being happy, I'm just...fucking {i}mad.{/i} Mad that somewhere else, I get to live the life I've always wanted while the {i}real{/i} me...has to suffer endlessly.（[9237]-[9238]）
  
  Sekai 强行发起三人性行为（幽灵设定，成人内容抽象），期间持续羞辱 Makoto——"Aki-kun won't ever love you...or anyone else so long as I'm around."（[9415]）；Ami 在门口围观，Makoto 反击 "Who's...unwanted...now...huh?!"（[9469]-[9472]）。Sekai 结尾留下元叙事级台词 "**You just have to believe.**"（[9523]）。
- **halloweenmakoto3**（[9531]）：余波。Makoto 吐槽 Sensei 对 Sekai 有斯德哥尔摩综合征（[9567]）；醉 Molly/Tsubasa 乱入（[9579]-[9597]）。给母亲打电话说出 "I...love you...and stuff..."（[9632]）后惊觉**这条时间线上父亲还活着**（[9640] "He's not in space?! Or...dead?!"）。随后 Maki 报告店里进来"眼睛很美的小女孩"→念出 "symposium" 一词后电话变成群交杂音（[9646]-[9670]，抽象处理）。插入童年闪回：小 Makoto 把母亲的群交当白噪音、95% 自动过滤（[9679]-[9691]），并许愿"生在别的世界"——旁白应答 "**Her wish is granted.**"（[9692]）。Makoto 醒来变回小孩、孤身处于异世界的家中（[9699]-[9716]）；遭遇"影子妹妹"实体（脸被 "giuseppe" 取走放进戏法袋，双重说话体 [9719]-[9756]）；VPA 广播强制通知她参加 **Transpacific Sadness Symposium**（[9769]-[9786]，提及 Terminal 23、"willful participation in necrophilia"、Eastern Branch Office 代表接见）；小丑神 **Giuseppe, God of Clowns** 登场（[9858]+），把她拖进一档儿童节目的"再教育"环节：Sensei（化作 AXELROD ADAMSON）被绑在椅子上"放气"，兔子合唱团只说 "Confess. Repent. Die."（[9896]-[9933]）；Giuseppe 自辩 "I am not THEM. ... I have SPECIAL ACCESS as a WRITER and ENTERTAINER."（[9949]）；Makoto 反抗失败被吹成气球戳爆（[9974]-[10002]），结尾冷冰冰两句："And it didn't. / Makoto went home."（[10009]-[10010]）。
- **makotospring3**（[10018]）：与影子散步的开场诗；咖啡约会。Makoto 提出派系构想与**牺牲实验**：把 Maya 引回小队、在下一次重置时故意让她留在天台之外——若记忆保留则改写一切规则，若失败"We just get a new one"（[10081]-[10138]）；Sensei 以"你是在牺牲她吗"质询，Makoto 答 "Not {i}exactly.{/i} I'm just willing to {i}risk{/i} it."（[10131]-[10136]）。Rin 咖啡厅争风吃醋喜剧（[10163]-[10216]）；讨论"让妈妈撞破我们"以测试记忆清除规则（[10229]-[10267]，"testing the sandbox"）；压轴的**蚂蚁农场理论**：
  > mak: I had a dream recently, Sensei. That this world was alive and we were its entertainment. Little ants rummaging through a thin, plastic rectangle in the room of some god or something.（[10269]-[10270]）
  > mak: It'd mean acting...{i}differently,{/i} though. Deviating from what's expected from us so there's never a reason to shake up our home at all.（[10276]）
  
  ——把"DEVIATION"概念提升为主动生存策略。
- **beachsixmakoto1**（[10325]）：温泉回。与 Miku、Io 谈 Io 在下水道发现的"通向虚无的无底洞"（[10490]-[10508]）；大段心理侧写：恐惧已退化为"偶尔的路坑"，但困惑成了新的恐惧来源（[10413]-[10427]，结尾删除线大字 "AT LEAST FOR NOW" [10427]）。深夜独自记录**异常清单**：朋友们忘记她记得的事、墙上陌生的画、角落里抽动的盒子、无人敲门、无人来电、床下的笑声（[10639]-[10646]）；笔记本贴在耳边能听到海声（[10662]-[10663]）。打电话要求 Sensei 重视无底洞未果（[10543]-[10625]）。
- **beachsixmakoto2**（[10677]）：开头是一整段**身份不明的女性声音旁白**，对着"你"倾诉永恒陪伴与隐藏的真相（[10681]-[10706]，疑似 Sekai 或亡故恋人，待核）。正片：Makoto 以"修复世界需要你"为由招募 Maya 参加睡衣派对（[10724]-[10760]，"abuse my status as Sensei's dream girl" [10741]）；Ami 与 Maya 的紧张对峙插曲（[10765]-[10806]）；彩色灯光 meta 旁白 "Which gods do the gods worship?"（[10829]-[10838]）；与 Yumi 的海滩夜谈——"Lots of sad girls 'round here nowadays. And they've all got the same fuckin' thing in common."（[10919]）/ "I didn't do that because I'm dumb. I did it because I'm sad."（[10918]）。
- **makotospring4**（[10952]）：色情店星战玩具大战→**Maki 情绪爆发解雇两个女孩**（[11001]-[11032]，自责"是我让你们在这种地方长大" [11024]）。Makoto 孤注一掷：**故意在关于重置的陈述里夹带性告白，赌母亲会像普通人一样"遗忘涉时信息"**（[11111]-[11130]，"TIME IS UNLIMITED AND I AM IMMORTAL" 连呼）——结果 Maki 完整听进去了："Have you gone fucking insane?"（[11137]）；Makoto 失控大喊 "Why aren't you repeating your last line of dialogue?!"（[11144]）——**用 NPC 逻辑要求真人，证明她的世界观已经系统化**。code red 电话求援（[11166]-[11217]），中间竟提议 "So, how are we going to kill her?"（[11188]）；对照组 Miku 对 "time paradox" 台词毫无反应照旧要去麦当劳（[11199]-[11200]）。Sensei 判定：**Maki 成为首个成年 outlier**（[11177]）。
- **makotospring5**（[11256]）：PowerPoint 家庭会议。"code red" 把 Sensei 骗到宿舍，实为 Makoto 准备好的正式宣讲（[11304]）：道德相对主义开篇（[11365]-[11373]）、年龄同意制度批判（[11386]-[11392]）、slide two "The world is broken, everything is fucked"（[11398]）、"我心理上早已成年因为时间根本不流动"论证（[11404]-[11408]）；传唤 Ayane、Yumi 出庭作证世界破碎（[11442]-[11476]，"You're the first adult we've ever had apart from Sensei!" [11455]）。Maki 不为所动："Keep your hands off my fucking daughter."（[11503]）。结尾 Sensei 的**花瓶独白**：等待 Maki 的精神裂痕碎裂、"I'll mix her with the rest. And with those fragments, I will make something beautiful. A vase. A vessel to hold my flowers."（[11565]-[11568]）——碎片收集者叙事再次现身。

---

## 三、lust 线概貌（抽象概括，不复述露骨细节）

lust 节点：makotolust5（[1090]）、makotolust10（[1885]）、makotoinvitefinger（[1864]）、makotonew2 后半（[3649]-[4112]）、makotolust30skip/lust30（[5231]/[5278]）、makotospring1 后半 somnophilia 段（约 [8100]-[8450]）、sportswars19（[7279]）、makotovsmolly（[7539]）、halloweenmakoto2 三人行段（[9326]-[9510]）。特征：

1. **meta 元素与性场景强绑定**。makotolust5 里 Sensei 吐槽 "**Patreon doesn't want this scene in the game.**"（[1107]/[1108]）；Makoto 玩的游戏与《LiL》互为镜像（"she hasn't even shown up in the game yet" [1121]-[1122]）。makotolust10 中她高喊 "**I am the protagonist!**"（[1911]）并被回应 "**that's what the script says**"（[1916]）——剧本（script）一词直接入场。
2. **性作为创伤应对机制**。makotolust30 是悲恸性爱：父亲死后数日，Makoto 主动要求以性麻痹痛苦（[5305]-[5321]）；正文 TRIMMED 约 186 行；事后结算 Maki affection 与 Makoto lust 双涨（[5684]-[5685]）——数值系统亲自记录这场悲剧的"收益"。她自己对成长环境的总结是获奖感言式的："thank...my mother — for creating an environment where I became desensitized to casual sex at such an early age..."（[7916]）。
3. **比赛化/表演化的公共性爱**。Nodokathon 决赛 "The Pit of Despair"（仿 Harry Harlow 抑郁猴装置命名，[7418]-[7421]）：Makoto 先弃权（"I can't say I find the idea of riding a sex toy in front of a bunch of people I'm not sexually attracted to very fun." [7485]）后被拉回，最终夺冠（[7906]）。sportswars19 则是她与 Maya 的恨爱场景（抽象），全程互骂结构。
4. **somnophilia 段的特殊性**：这是全 digest 中唯一一处**系统性剥夺同意**的场景（服药后进行），且被开发者乱入打断两次（[8313] "bro can you just be normal and enjoy the goddamn somnophilia scene"；[8437]-[8447] Akira/dev 对话）——meta 干预恰恰出现在道德最低点，形成结构性反讽。
5. **halloweenmakoto2 幽灵三人行**：性场景同时是 Sekai 对 Makoto 的支配仪式与"爱情宣判"（"in MY world, I'm the only one whose love ever reaches him" [9414]），情欲书写完全服务于平行世界线的权力结构展示。

---

## 四、与主线／元叙事咬合点

1. **最深的重置记忆个体案例**（winterbeach2 [2547]-[2562]）：Makoto 记得"IP 地址那次"重置前的卧室事件——记忆残片的具体程度超过任何其他非锚角色，且出现在她"官方觉醒"之前。
2. **第四觉醒者与锚理论**（dorm55p2 [7037]-[7045]）：Maya 亲口给出 Sensei=记忆之锚的模型，并把 Makoto/Yumi/Tsuneyo 的例外归为"公式变更"（[7040]-[7045]）。
3. **记忆清除规则的三组对照实验**：Miku 对照组（逐字重复打断 [6882]-[6931]）；Maki 夹带告白实验失败（spring4 [11111]-[11144]，成年 outlier 诞生 [11177]）；Makoto 自己提出的"撞破实验"与"牺牲 Maya 实验"（spring3 [10131]-[10138]、[10253]-[10258]）——她是全 cast 中唯一把重置规则当作可测试科学假设的角色。
4. **HO/A1/A2 与时钟三针谜语**（winterbeach3 [2782]-[2823]）：三个神秘实体通过出神状态的 Makoto 传达信息，谜语内容指向主线时钟母题。
5. **Maya 电话空号**（[2882]-[2892]）：Makoto 独立侦查发现 Maya 的所有联系方式无效——与"旧 Maya 已死/被替换"的主线暗线直接对口。
6. **Sekai 平行时间线**（halloweenmakoto2 [9203]-[9528]）：文本内首次完整呈现"另一条世界线"的实际样貌（Sekai 活着、家庭完整、Ami 是亲生女儿），并以 Sensei 的"替代品愤怒"（[9237]-[9238]）和 Sekai 的 "You just have to believe."（[9523]）双向锚定元叙事。
7. **Sadness Symposium 机构层**（halloweenmakoto3 [9769]-[9786]）：Transpacific Sadness Symposium、Terminal 23、Eastern Branch Office——官僚化元叙事机构首次具名；Giuseppe 自称 "WRITER and ENTERTAINER" 且 "I have SPECIAL ACCESS...But I AM NOT them"（[9949]）——作者层内部也有派系。
8. **蚂蚁农场理论**（spring3 [10269]-[10276]）：玩家层的完整民间表述（世界=塑料盒里的蚂蚁农场，重置=摇盒子），并与 DEVIATION 概念焊接成生存策略。
9. **"this version of the game"/"previous iteration" 措辞链**：[1622]（this version of the game）、[3544]（previous iteration of me）、[11144]（Why aren't you repeating your last line of dialogue?!）——三层措辞分别对应游戏版本、迭代自我、NPC 循环，构成递进的元语言。
10. **系统错误直接入文**：ERROR ADVANCING TO SATURDAY/SUNDAY（makotonew3 [4482]/[4491]）。
11. **开发者乱入与 Akira/dev 对话**（spring1 段 [8313]、[8437]-[8447]）：开发者在场景内自我讨论，且对话对象直呼 Akira——真名在最不设防的场景泄露。
12. **异常清单**（beachsixmakoto1 [10639]-[10646]）：以清单形式集中罗列世界故障（遗忘差、陌生画、抽动盒、空敲门、空来电、床下笑声），可视为全游戏 anomaly 母题的索引页。
13. **花瓶独白**（spring5 [11565]-[11568]）：叙事者的"收集碎片制成花瓶"宣言，与 Ami 线的 "collection"（amispring5 [11245]）呼应——存在一个跨角色的收藏者结构。
14. **sanity 变量唯一结算**（spring2 [8923]）：Makoto 的精神状态被单独计量，暗示她在系统层面有独立的理智轨道。
15. **N 旁白的名单预告**（sadgirls8 [6000]-[6008]）：叙述者在悲剧现场预先宣告 "Makoto will become one of those too"——她进入"被珍视者"序列是被安排的。

---

## 五、未解伏笔（按可信度排序）

1. **影子妹妹实体的身份**（halloweenmakoto3 [9719]-[9756]）：脸被 "giuseppe" 取走、"born from innocence and the guilt"、与真身共乘救生筏——是异世界的妹妹、某个被囚存在还是 Makoto 人格投影，未解。（可信度高：多次铺垫）
2. **Sadness Symposium 的 Eastern Branch Office 代表**（[9778] "a meeting with a special representative"）：始终未现身；Giuseppe 是否即该代表亦未明。
3. **时钟三针谜语的答案**（winterbeach3 [2782]-[2823]）：HO/A1/A2 留下的谜语全文已录，解读悬置。
4. **beachsixmakoto2 开头的女声旁白**（[10681]-[10706]）："Which one am I this time, do you think?"——Sekai？某条线的亡故恋人？还是叙事者的又一面具？（待核）
5. **Maya 电话为何全部空号**（[2882]-[2892]）：与旧 Maya 死亡/替换说的关键物证，文本未回收。
6. **父亲之死的机制**（sadgirls1 [4701]-[4723]）：死因、"gift from the sky"（[6087] 天空之声）与太空死亡玩笑（[5869]、[11074]）之间的关系未明。
7. **异常清单诸现象**（[10639]-[10646]）：抽动的盒子、床下笑声等均无后续回收。
8. **Makoto 的记忆保留边界**：她能记多少轮、IP 地址那次是第几轮，文本拒绝量化（"I don't know how old I even am" [11404]）。
9. **大理石眼猫**（spring2 [8869]）：单次意象，无回收。
10. **somnophilia 段的 label 归属**：该段是否独立 label 还是 makotospring1 子段，待核对源 .rpy。

---

## 六、label 总表（53 个）

| # | label | 行号 | 类型 | 一句话概括 |
|---|-------|------|------|-----------|
| 1 | pornshop | 1 | 路由 | 店内事件分发器 |
| 2 | makotoinvite | 36 | 路由 | 邀请事件入口 |
| 3 | postbluejaycall | 49 | 过渡 | Bluejay 后续电话 |
| 4 | postbluejay | 61 | 过渡 | Bluejay 后续 |
| 5 | callmakotomorning | 75 | 日常/电话 | Koi Cafe；Sensei 黑暗独白 |
| 6 | callmakotoafternoon | 166 | 日常/电话 | 图书馆；"There are no gods" |
| 7 | callmakotonight | 257 | 日常/电话 | 夜间电话 |
| 8 | makotoporngen2 | 272 | 日常 | 钓鱼小游戏 |
| 9 | makotoinvitegen | 312 | 菜单 | 邀请选项菜单 |
| 10 | firsttimepornshop | 360 | 剧情 | 初遇：优等生在色情店打工 |
| 11 | porn3to4 | 735 | 过渡 | 店内过渡 |
| 12 | pornshop5 | 763 | 日常 | 店内递进 1 |
| 13 | pornshop10 | 970 | 日常 | 店内递进 2 |
| 14 | pornshop15 | 1025 | 剧情 | HHG 海报；获 Maki 电话 |
| 15 | makotolust5 | 1090 | lust/meta | Patreon 玩笑；游戏镜像 |
| 16 | makotoinvite1 | 1141 | 剧情 | Ami 宣战；南北战争讲座 |
| 17 | makotoinvite2 | 1497 | 剧情 | 支开 Ami；"this version of the game" |
| 18 | makotoinviteaff | 1641 | 日常 | 亲密日常分支 |
| 19 | makotoinvitegrind | 1681 | lust | 亲密分支 |
| 20 | pornshop20 | 1702 | 日常 | 店内递进 3 |
| 21 | pornshop25 | 1818 | 日常 | 店内递进 4 |
| 22 | makotoinvitefinger | 1864 | lust | 手指分支；lust 入口 |
| 23 | makotolust10 | 1885 | lust/meta | "I am the protagonist!"/"script" |
| 24 | makotowinterbeach1 | 1935 | 剧情 | 冬海滩；禁欲约定；Hope 独白 |
| 25 | makotowinterbeach2 | 2266 | 剧情/伏笔 | 重置记忆泄漏（IP 地址） |
| 26 | makotowinterbeach3 | 2599 | 剧情/meta | HO/A1/A2；时钟谜语；Maya 空号 |
| 27 | makotowinterbeach4 | 2944 | 剧情高潮 | 跳楼梦告白；"There are others" |
| 28 | makotonew1 | 3287 | 剧情 | 泳池清扫；"previous iteration of me" |
| 29 | makotonew2 | 3649 | 剧情/lust | 秘密房间；"first seeds of corruption" |
| 30 | makotonew3 | 4125 | 剧情/meta | worm 独白；"What are we?"；ERROR 文本 |
| 31 | sadgirls1 | 4494 | 剧情高潮 | Yasu 预言；父亲死讯；浴室崩溃 |
| 32 | sadgirls7 | 4826 | 剧情高潮 | 向日葵起源；自杀意念 |
| 33 | makotolust30skip | 5231 | lust/拒绝 | 相框：与亡父合影 |
| 34 | makotolust30 | 5278 | lust | 悲恸性爱；双数值上涨 |
| 35 | sadgirls8 | 5699 | 剧情高潮 | 返校演讲崩溃；Ami 救援；N 名单预告 |
| 36 | makotospecial50 | 6105 | 剧情高潮 | 红鸟诗；遗书史交代 |
| 37 | makotopool55 | 6410 | 剧情 | 瓶子互倒论；身份清单自白 |
| 38 | makotodorm55p1 | 6671 | 剧情/测试 | 裸读日常；重置话题测试通过 |
| 39 | makotodorm55p2 | 6965 | 剧情/meta | 觉醒确认；入队；假结婚证 |
| 40 | sportswars19 | 7279 | lust/群像 | 与 Maya 恨爱；Nodokathon 决赛前夜 |
| 41 | makotovsmolly | 7539 | lust/群像 | Pit of Despair 夺冠；获奖感言 |
| 42 | makotospring1 | 7942 | 剧情/lust | 无限之夜；somnophilia 段；dev 乱入 |
| 43 | endofmakspring1 | 8502 | 日常 | 说梦话疑云；Niki 搬入 |
| 44 | makotospring2 | 8591 | 剧情 | 时间循环道德论；sanity+1 |
| 45 | halloweenmakoto1 | 8944 | 剧情 | 公开承认师生关系；自我说服拆穿 |
| 46 | halloweenmakoto2 | 9186 | 剧情/meta | Sekai 平行时间线；幽灵三人行 |
| 47 | halloweenmakoto3 | 9531 | 剧情/meta | 异世界童年；Symposium；Giuseppe |
| 48 | makotospring3 | 10018 | 剧情/meta | 牺牲实验；蚂蚁农场理论 |
| 49 | beachsixmakoto1 | 10325 | 剧情 | 温泉；异常清单；无底洞 |
| 50 | beachsixmakoto2 | 10677 | 剧情/meta | 神秘女声；招募 Maya；Yumi 夜谈 |
| 51 | makotospring4 | 10952 | 剧情高潮 | Maki 解雇；夹带告白实验失败 |
| 52 | makotospring5 | 11256 | 剧情高潮 | PowerPoint 家庭会议；花瓶独白 |

*另：somnophilia 段若为独立 label 则总数 54，待核。*

---

*文档生成于 `_digest_Makoto.txt` 全量精读完成后（分块覆盖工具行 1–5984，含 3 个持久化块补读）。所有行号为源 .rpy 近似定位（±5 行）。*
