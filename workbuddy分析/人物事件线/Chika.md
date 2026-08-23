# Chika 事件线全析

> 源文件：`_tmp_digest/reread/_reread_ChikaEvents.txt`（内部脚本行号约 [1]–[11357]，共 49 个 label）。本文件基于该 reread digest 整体重写，正文断言均附 digest 行号。Chika（Chosokabe Chika）是 Sensei 维持时间最长、情感浓度最高的学生恋人之一，也是全作中唯一被游戏系统显式改写精神状态的恋爱对象。阅读提示：她的 love 线不是"攻略成功史"，而是一部逐步崩解的 monogamy 幻想毁灭记录——从商场打工的元气 gyaru，到 maid cafe 的 yandere 服务员，再到对 Rin 告白后主动自我放逐。引用格式为 `> 前缀: 英文原文（[行号]`；c=Chika，s=Sensei，N=旁白，ch=Chinami，u=Uta，r=Rin，y=Yumi。

## 一、角色基本盘

- **家庭结构**：母亲已故，Chika 自少女时代起独自抚养非血缘妹妹 Chinami——旁白明确她"adapted quite seamlessly to being the caretaker of a child when her mother died"（[10757]）。父亲是抛弃者："I have cried more tears for you at this point than I did for my fucking father when he walked out on me"（c, [9824]）。
- **经济状况**：长期打工养家——先在 Great [[REDACTED]] Mall 服装店（mallgen2），后转职粉红 maid cafe；自认"limited disposable income"（c, [11167]），连内衣都要算作投资（[10546]）。公寓位于 Tsukioka 家产业、"technically for women only"的女性专属 complex（c, [9377]、[9431]）。
- **性格底色**：高能量、粘人、把恋爱神圣化为一夫一妻制；自我价值感极低——梦中自白"Why would God...give *me* a gift? I've never been special at all. I've done nothing to deserve this"（c, [10090]-[10092]）。她对"特别"的渴求是后续所有崩坏的心理引擎。
- **核心关系**：Sensei（男友，同时被 Chinami 当作"Papa"，[10364]、[9358]）；Yumi（前室友、如家人般的挚友，后期因误会决裂又部分和解）；Rin（多年密友，后被 Chika 拖入性/爱关系并成为告白的对象）；Uta（maid cafe 前辈）；Touka（房东阶层、破例允许 Sensei 进入女性 complex，[9431]）。
- **叙事定位**：她是 Sensei polyamory 生活方式的第一个、也是最惨烈的"代价展示品"。当其他角色还在用玩笑消化共享恋人时，Chika 线负责演示这套体制如何碾碎一个把爱等同于排他性的普通女孩。

## 二、love 线逐事件脉络

### 1. 商场约会期（mall 系列与早期 invite）
- `mall`/`chikamaid`/`chikainvite` 为入口路由；周末约会主场景是 Great [[REDACTED]] Mall，Chika 在服装店打工（mallgen2）。
- mall2to4 → mall5 → mall10 → mall15 → mall20 → mall40/40p2 → mall45 构成好感度阶梯式约会链，每级对应一次更深的私人交流，属于典型 Ren'Py 数值化恋爱推进骨架。
- `callchikamorning`/`callchikaafternoon`/`callchikanight` 与 `chikanightgen2` 是电话邀约的通用桩件，未接通时回落到"She doesn't pick up"（N, [13] 同构文本）。

### 2. 邀请上门与家庭暴露（chikainvite1/2 及分支）
- Chika 把 Sensei 带入自己与 Chinami 的小家，首次完整呈现"姐姐即家长"的家庭结构；同期段落里埋着两条重要支线：
  - Ami 与 Sensei 关系的冲突场景（[2137]–[2182]），让 Chika 第一次直面"男友与学生们的另一面"；
  - Yumi 以"类似妹妹的存在"进入家庭语境（[2160]–[2172]），为她日后搬离后留下的空洞做铺垫。
- `chikainviteaff`/`chikainvitelicking`/`chikainvitehandjob`/`chikainvitemissionary` 是 invite 事件的性行为分支树（详见第三节）。
- `day272` 与 `restofchinamibr` 属日程胶水层，标记 Chinami 相关日常节点。

### 3. 温泉合宿（chikaonsen1–4）
- onsenbegin 为公共入口，chikaonsen1–4 是 Chika 视角的温泉活动四段推进：从集体场景中的占有欲表现，到二人独处的亲密升级。该章确立了她在半公开场合对 Sensei 的强烈领地意识，为后续 yandere 化提供行为先例。

### 4. 转职 maid cafe（chikaspecial40/45、chikadorm45）
- chikaspecial40 铺垫经济压力与职业焦虑；chikaspecial45 中 Uta 正式招募 Chika 加入粉红 maid cafe。此事件被赋予元叙事权重——Maya 明言 Ami 出现在 maid cafe 是"世界第一个 major divergence"（[6548]），随后 Chika 作出转职决定（[6571] 起）。也就是说，Chika 的求职选择在世界观层面被登记为一条分岔线的起点。
- chikadorm45 处理宿舍侧的后续影响。

### 5. Spring 章：崩解五部曲（chikaspring1–8）
- **spring1–3**（[7542]–[8700]）：修罗场前的暗流。Chika 目击 Sensei 与 Yumi 的亲密（海滩夜），同时她与 Rin 之间已越过友谊界限——后文回溯确认"her tongue departed her good friend's clitoris"（N, [9937]）。她还经历了一段被 Sensei 称为"the whole sadness coma thing"的情绪休克期（s, [8860]）。
- **spring4 对峙**（[8701]–[9158]）：全 love 线的爆点。Chika 逼问 Sensei 与 Yumi 的关系，历数自己的付出——搬家、换手机套餐、停止索求性爱（c, [8856]）。Sensei 承认与 Yumi 的吻，并坦白 polyamory 本质："there are *so many* of you that I want to spend the rest of my life with"（s, [8924]）。Chika 当场完成一次可观测的人格重写：把"我是被伤害最轻的一个"曲解为"我最特别"——
  > c: That means if...you had to make a choice...it'd be me...it would definitely be me...（[8941]）
  > c: Yes it is. And I'm winning it.（[8968]）
  旁白以系统公告形式盖章这场精神事故：
  > N: {i}Chika has contracted [[RABIES]!{/i}（[9143]）
  > N: {i}Her sanity has decreased by 10!{/i}（[9144]）
  > N: {i}Her affection has increased by 1,000!{/i}（[9152]）
  事后她单方面宣布"The threesome is back on"（c, [9120]），用虚假的痊愈掩盖崩溃。
- **spring5**（[9161]–[9484]）：与 Rin 共浴长谈。Rin 直指要害——"you're just changing your definition of that to adapt and...protect yourself?"（r, [9249]），并承认自己早已知情 Sensei 的多线关系却保持沉默（[9261]–[9268]）。Chika 以"I'm keeping you with me forever"（c, [9285]）回应，把依恋转向 Rin。本章还坐实：Chinami 称 Sensei 为 Papa 且"he's the closest thing to a dad she's ever had"（c, [9358]）；Futaba 的父母长期失联（r, [9415]）。
- **spring6**（[9487]–[9927]）：Sensei 探班 maid cafe。Chika 已发展出完整的 yandere 服务人设——对想换人的客人施压"You want Chika-chan to die?!"（c, [9686]），收尾一句"Die, you fucking pigs"（c, [9701]）；Uta 透露这种风格反而使她成为人气第二（[9714]、[9668]）。深夜长谈给出她的核心诉求：
  > c: I need you...to *need* me.（[9828]）
  > c: Hurting with you beats hurting alone.（[9813]）
  并以"Leave the changing to me, Sensei...I'm young. I still *can*"（c, [9911]）宣告由自己承担改变的全部成本。Sensei 的旁观独白承认责任在自己："I'm the one who cracked her in the first place"（N, [9771]）。
- **spring7**（[9930]–[10312]）：Chika POV 的现实溶解。她自觉"too coherent for any of it to feel real"（N, [9951]），怀疑记忆真实性（[9952]）；归因于"the worm of Giles Corey began to eat away at her brain"（N, [9944]）。回家后 Chinami 开始 NPC 式循环复读"Welcome home, big sis Chika!"（[9958]–[9996]），旁白同步退化为无意义拼贴"She used her hand to shoulder. An act of reassurance. The kind that Mom would bake."（N, [9987]）——模拟层出现裂缝。随后的梦境序列是全 digest 最超现实段落：神秘角色"six"以十六进制串说话（[10012]）；语音助理 vpa 精确播报"Transpacific Sadness Symposium in nineteen years, eleven days..."（[10030]）并邀请她参加 Spacy's Summer Blast Savings event；知识之"cube"（[10142]–[10146]）把她吸入场内，那里是一场无尽群交的讽刺景观，Q 型无脸怪物反复劝诱"EVERYBODY'S DOING IT... WHY MATTER IF NOT LOVE?"（q, [10227]-[10228]）。当 Chika 发现 Chinami 也在场"帮助 ojii-sans"（ch, [10244]、[10257]）时，她选择代妹献身：
  > c: I will do whatever it takes to protect my sister.（[10268]）
  > c: Everybody's doing it.（[10272]）
  > c: This is Heaven.（[10280]）
- **spring8**（[10315]–[10687]）：回到 Sensei 视角。Chika 主动来电索求"all of the sex"（c, [10331]），以 maid 装束角色扮演填补空虚；Sensei 发现"I love you"三个字能像开关一样中断她的狂气自动驾驶（[10481]–[10494]）——这句话从此成为他操控她的复位键。旁白交代背景恶化："she's taking my forced polyamory a little harder than everyone else"（N, [10451]）。

### 6. Christmalloween 章：告白与自断（chikachristmalloween1/2）
- **christmas­halloween1**（[10690]–[11010]）：Chika 身穿 Jirai Kei 盛装赴会，开场旁白即宣判："Rabies had turned to cannibalism"——她对朋友的越界从被动染病升级为主动捕食（N, [10698]-[10699]）。她下意识设局把 Rin 引离派对，却在场外撞见 Yumi，被迫坦白："I...may have cheated on him. With a girl. Who I am now pretty sure I have a *major* crush on."（c, [10866]）Yumi 点破死局："That girl liked you *forever* and you turned her down."（y, [10879]）谈话尾声 Yumi 轻描淡写抛出母亲患癌的消息（[10917]-[10926]），Chika 意识到自己已自私到从未过问他人，当场崩溃质问"What's happened to me?...Is this really who I am now?..."（c, [10946]-[10947]），随后在洗手间自残式痛哭（[10986]-[11008]）。
- **christmalloween2**（[11013]–[11357]）：Otoha 向 Futaba 预言 Chika 将向 Rin 告白（[11074]-[11091]）。派对外，Chika 完成一场结构上自相矛盾的告白——先是全情袒露"But I think I'm in love with you and if I didn't admit that tonight, I'd probably just die."（c, [11184]-[11195]），紧接着宣判绝交"I don't think we should hang out anymore."（c, [11225]）。理由是她必须先修复自己："I've fucked things up with Yumi. My relationship with Sensei is going up in flames...I even fell into the yandere archetype at work"（c, [11251]）。Rin 拒绝放手，甚至以"Smother me. Smother me if that will keep you from leaving. I love you, Chika."（r, [11325]）挽留，Chika 仍微笑离开。系统以罕见措辞收束本段：
  > N: {i}Chika's affection has forcibly increased to [chika_love]!{/i}（[11353]）

## 三、lust 线概貌

- **invite 分支树**（chikainviteaff → chikainvitelicking / chikainvitehandjob / chikainvitemissionary）：早期 lust 内容以玩家选择性爱方式的形式组织在同一场景框架内，功能上是把 Chika 定型为"顺从型初恋情人"——她的每次配合都同步加深情感依赖，使性与忠诫在她身上不可拆分。
- **酒店事件（chikalust15skip / chikalust15）**：skip 桩件内嵌著名的"ERROR ADVANCING DAYS"异常文本（[4204]–[4211]），是日期推进系统报错的直接展示，暗示时间层被外力干预；正篇 chikalust15 为旅馆过夜事件，前后文涉及 Sensei 出钱购买 morning after pill（[4165]-[4166]），确立这条 lust 线的后果真实性与 Chika 承担风险的不对等位置。
- **chikalust25skip / chikalust25**：中期 lust 里程碑，延续酒店模式并进一步把"被需要"作为她的兴奋源——与她后来"all of the sex"式的补偿性索求（[10331]）一脉相承。
- **spring8 的选择分支**：性行为存在结局分歧，其中一条为"Neither of you collapse and Chika winds up going to work with your seed still lingering inside her. It somehow makes her service better."（N, [10666]-[10667]）——lust 直接反馈为 maid cafe 服务质量，完成性、工作、人格异化的三点闭环。
- **[TRIMMED] 段落的叙事功能**：digest 中被裁剪的显性描写段（如 imanilust 类似结构在本文件中体现为各分支中段）共同服务于同一功能：以不断升级的服从性表演外化 Chika 用身体换取"被选中"感的心理机制，而非单纯的感官内容。

## 四、与主线/元叙事咬合点

- **数值系统直接改写人格**：`[[RABIES]]` 事件以 sanity −10 / affection +1000 的系统公告形式呈现（[9143]–[9152]），末尾又有"affection has forcibly increased"（[11353]）——游戏机制不再是计量器，而是施加在角色身上的外部意志。
- **日期推进故障**：ERROR ADVANCING DAYS（[4204]–[4211]）与重置循环层的既有线索同构，提示 Chika 线所在的时间轴曾被强制干预或回滚。
- **模拟层裂缝**：Chinami 的循环台词（[9958]–[9996]）、退化旁白（[9987]）、十六进制消息（[10012]）、以及 vpa 对数十年后活动的精确到分钟倒计时（[10030]）共同表明：Chika 的日常本身可能运行在被脚本化的世界里，她的疯狂是对底层代码的部分感知。
- **divergence 登记制度**：Maya 将 maid cafe 相关事态定义为"世界第一个 major divergence"（[6548]），意味着 Chika 的转职在世界观层面具有分岔线级别的因果地位。
- **Truman 式自省的反向印证**：虽然该母题集中出现在 Imani 线，但 Chika 梦中被 cube 吸入、被告知"Just look at how she treats other customers"式的人设分工（u, [9672]），同样是"角色扮演既定原型"的元叙事投影。
- **Chinami 的有限时间**："Her time on this planet is limited!"（ch, [10390]）由 Chinami 本人口径说出，与其 glitch 表现互相印证，构成悬置于全线上方的死亡/回收倒计时。

## 五、未解伏笔

1. **Chinami 的真实身份**：NPC 循环、hex 文本、'limited time' 自述三者叠加，但她究竟是程序残响、某种存在拟态，还是被卷入重置的真孩童，digest 内无定论。
2. **Rabies 是否可逆**："sanity decreased by 10" 之后未见任何恢复机制；christmalloween1 显示病理仍在进展（rabies→cannibalism，[10699]）。
3. **"the worm of Giles Corey"**（N, [9944]）的所指——是具体实体、疾病命名还是元叙事玩笑——未被任何后续文本解释。
4. **Sensei 与 Chinami 的底线**：叙述明示"unless her boyfriend started fucking her little sister too"是 Chika 认知中的 rock bottom（N, [9938]），且 Sensei 曾在三 conversation 中提及 Chinami 的名字（[9941]）——这条最危险的伏笔处于持续通电状态。
5. **Yumi 母亲的癌症**（[10917]-[10926]）与 **Futaba 父母的失联**（[9415]）：两条外部家庭危机均停留在"已抛出、未展开"状态。
6. **Uta 的报复计划**："Uta-chan is going to make you pay for this transgression for *years* to come"（u, [9595]）。
7. **Chika–Rin 关系的最终形态**：告白+绝交的双重宣言后，两人约定"I'll still see you in school!"（c, [11339]）——这段关系是被搁置还是被引爆，尚无下文。
8. **梦境体系**：cube、Spacy's Summer Blast、Q 怪物、"Transpacific Sadness Symposium"（[10030]）构成一套未命名的超现实子系统，其与重置层的关系完全未知。

## 六、label 总表

| # | label | 内部起始行 | 归类 |
|---|-------|-----------|------|
| 1 | mall | [1] | 路由 |
| 2 | chikamaid | [25] | 路由 |
| 3 | chikainvite | [34] | 路由 |
| 4 | mallgen2 | [49] | love·约会 |
| 5 | chikainvitegen | [78] | love·通用 |
| 6 | callchikamorning | [136] | 路由 |
| 7 | callchikaafternoon | [207] | 路由 |
| 8 | chikanightgen2 | [217] | love·通用 |
| 9 | callchikanight | [256] | 路由 |
| 10 | firsttimemall | [324] | love·约会 |
| 11 | mall2to4 | [536] | love·约会 |
| 12 | mall5 | [562] | love·约会 |
| 13 | mall10 | [808] | love·约会 |
| 14 | mall15 | [1240] | love·约会 |
| 15 | mall20 | [1600] | love·约会 |
| 16 | chikainvite1 | [1921] | love·上门 |
| 17 | chikainvite2 | [2303] | love·上门 |
| 18 | chikainviteaff | [2426] | lust·分支 |
| 19 | chikainvitelicking | [2471] | lust·分支 |
| 20 | chikainvitehandjob | [2492] | lust·分支 |
| 21 | day272 | [2513] | 日程胶水 |
| 22 | chikaonsen1 | [2612] | love·温泉 |
| 23 | onsenbegin | [2687] | love·温泉 |
| 24 | chikaonsen2 | [3124] | love·温泉 |
| 25 | chikaonsen3 | [3596] | love·温泉 |
| 26 | chikaonsen4 | [3657] | love·温泉 |
| 27 | chikalust15skip | [4171] | lust·酒店 |
| 28 | chikalust15 | [4214] | lust·酒店 |
| 29 | chikainvitemissionary | [4318] | lust·分支 |
| 30 | chikaspecial40 | [4339] | love·special |
| 31 | mall40 | [4695] | love·约会 |
| 32 | mall40p2 | [4920] | love·约会 |
| 33 | chikadate45 | [5345] | love·约会 |
| 34 | restofchinamibr | [5433] | 日程胶水 |
| 35 | chikalust25skip | [5602] | lust·酒店 |
| 36 | chikalust25 | [5649] | lust·酒店 |
| 37 | mall45 | [6151] | love·约会 |
| 38 | chikaspecial45 | [6566] | love·special（转职 maid cafe） |
| 39 | chikadorm45 | [6939] | love·宿舍 |
| 40 | chikaspring1 | [7542] | love·spring 章 |
| 41 | chikaspring2 | [7944] | love·spring 章 |
| 42 | chikaspring3 | [8358] | love·spring 章 |
| 43 | chikaspring4 | [8701] | love·spring 章（对峙/RABIES） |
| 44 | chikaspring5 | [9161] | love·spring 章 |
| 45 | chikaspring6 | [9487] | love·spring 章（maid cafe 探班） |
| 46 | chikaspring7 | [9930] | love·spring 章（现实溶解/梦境） |
| 47 | chikaspring8 | [10315] | love·spring 章 |
| 48 | chikachristmalloween1 | [10690] | love·christmalloween |
| 49 | chikachristmalloween2 | [11013] | love·christmalloween（告白/绝交） |
