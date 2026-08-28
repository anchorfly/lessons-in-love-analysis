# Ami 事件线分析

> 源文件：`游戏文本/AmiEvents.rpy`（真实 label 数：52）｜按 label 名回源。
>   
> 定位：USER1 线实例、已故母亲 Sekai 之女；love/lust 双轨最长的角色线之一。源文在 amidate50p4 收束处出现系统提示 "USER1 HAS SUCCESSFULLY LOGGED IN"，印证其作为 USER1 观察样本的设定。
>   
> 阅读提示：台词直引为源文英文原文；a=Ami、se=Sensei（内心声部）、ri=Rika、tk=Tsukasa。label 名是唯一的回源锚点。

## 一、角色基本盘

Ami 是 love 线中与"真实/虚构"命题绑定最深的女主角。她是已故母亲 Sekai 的女儿，由 Sensei 以半监护者、半恋人的模糊关系照看（firsttimeamisroom 中 Sensei 称她为 "slightly-official niece"）。表层设定是活泼的漫画宅少女：住校生、maid 咖啡店打工（amimaid30 / amimaid50）、manga club 成员（amidate50 墓前独白提到 "the manga club is going well"），对 Sensei 的感情混合依恋与早熟的占有欲。文本在她身上留下"非人"裂缝——amispecial50 的内心独白把自身比作"困在罐中的主角"，amiinvite4 的咖喱以血代盐玩笑，amimaid50 写她"唯一能让血液沸腾的是同类的血"，都对"血"表现出异样亲近。作为 USER1 线实例，她既是攻略对象，也是元叙事层拷问"虚构角色能否被爱"的载体。墓前独白（amidate50）揭示其情感内核：孤独、把 Sensei 当作 "my new dad" 的自我说服，以及被 Sensei 以 "my sweet girl" 回应却仍隔着生死与不可见距离的隔阂。

## 二、love 线逐事件脉络

### 1. amisroom 路由桩与邀请系统

amisroom 是纯路由桩：按 ami_love 与前置 flag，依次跳转 firsttimeamisroom、amisroom5/10/15/20/25，否则跳 amisroom3to4。amiinvitegen 中 Sensei 打电话邀请 Ami，Ami 吐槽："Gonna invite me to my own house again?"——两人日常已互相渗透。邀请菜单提供 Hang Out、Headpat 等选项；在 bonus==False 模式下，Hug 跳 amiinvitethighjob、Hold Hands 跳 amiinvitereverse，选项文案与跳转目标存在系统性错位，使好感度菜单实际通向 lust 内容（amiinvitethighjob / amiinvitereverse）。

### 2. firsttimeamisroom：初次同处一室

amisroom 在首次进入（firsttimeamisroom==False）时跳转此处，是 Sensei 第一次正式进入 Ami 房间、两人关系越界叙事的起点。开场 Sensei 自述身处 "the early stages of a harem"，敲 Ami 的门并被迎入，奠定"半监护、半恋人"的暧昧基调。

### 3. amisroom3to4 / 5 / 10 / 15 / 20 / 25：好感度递进的同居化阶梯

amisroom 按 ami_love（5/10/15/20/25）配合相应前置 flag 逐段跳转，构成两人关系从相遇到同居生活的进阶。其中 amisroom25 要求 ami_virgin==False 且 amidorm20==True，是亲密同居生活的深层节点，为后续事件提供情感基线。

### 4. amisroom15：看动漫的日常

Ami 追番时剧透："Oh. Wait. I remember who wins now. It's the protagonist." Sensei 反问："Are you just going to spoil everything today?" 随后两人讨论作品里的审查设定："They got rid of censorship laws here years ago...as long as it's not a penis"。这段以玩笑完成的审查制度吐槽，同时是世界观自指——游戏世界对禁忌的容忍度被规则明文规定，正如角色行为被 label 结构规定。

### 5. amiinvite1–4：四次登门

- amiinvite1 / 2 / 3：邀约型日常事件，维持关系温度，把"房间"这一封闭空间逐步扩展到校园外的日常场景。
- amiinvite4：全 love 线重要转折之一。Ami 暂时离场后，Sensei 独白："She reminds me a lot of someone else I used to know... It's someone I try not to think about because it hurts when I do."——他主动掐断的思绪。Ami 回来端出咖喱，宣布 "It's full of my blood. I used it in place of salt"，Sensei 回应 "I love your blood"，Ami 补一句 "I was just kidding... This is normal curry without any Ami in it." 血的真实性与玩笑的收回性并置：读者无法判定哪句是真，这正是 Ami 角色"非现实"状态的具象化。

### 6. amimaid30 / amidate35：打工与约会的日常节点

- amimaid30：Sensei 到 maid 咖啡店探班，Ami 提到为他做了早餐、两人聊到账单与她的新工作，是"女仆"社会身份的展示。
- amidate35：Sensei 打电话约 Ami 去商场挑新泳衣的约会事件，巩固两人日常亲密。

### 7. amidate50：扫墓（墓前独白的情感顶点）

amidate50 是 date50 事件，包含 Sensei 被"吞没"的梦境（q 低语 "I can't sleep."、te 身影），以及 Ami 穿上亡母旧衣（"I remember that dress"）后于墓前的独白——这是 love 线情感浓度最高的段落：

> a: I miss you, Mom...Sensei misses you too, but he's too afraid of looking weak around me to admit it.

她报告 maid 咖啡店与 manga club 近况，又说："Daddy, too. Can you tell him that? Sensei's been doing an okay job as my new dad." 随后出现异常声部——Sensei 的内心回应："I miss you too, my sweet girl...I'm sorry you feel so alone. I do too. I'm always here, though. Even if you can't see me." "Even if you can't see me" 字面是活人对死者说话，但在重置／元叙事读法里，也可读作一个无法被角色感知的系统声部。亡母"回应"究竟是心理描写还是元叙事泄漏，文本拒绝裁决。

### 8. aminew1 / aminew2：新年事件

- aminew1：新年框架，Ami、Ayane、Maya 等结伴（源文称 "three girls who could pass for my daughters"）去咖啡店蹭情侣折扣，Ayane 以富家姐姿态宣称 "I am rich and can get you out of trouble if I have to"。多女主同框被处理成替代性家庭结构的展演。
- aminew2：新年次日清晨，Sensei 与这位"侄女"的亲密场景，明确以"即便我们 related，也不妨碍彼此贴近"的乱伦框架推进关系确认。

### 9. amilust35skip / amilust35intro / amilust35：love 线内置的中段欲望分支

amilust35skip 以 sauna 场景提供跳过入口（"No one can see us" 后 Ami 直言愿当下发生关系），说明该欲望分支的可选择性；amilust35intro / amilust35 为其中段 lust 内容。

### 10. amimaid50 → amispecial50：打工线与特殊事件的收束

amimaid50 是 maid 咖啡店更衣室场景（Ami 近乎全裸把 Sensei 拽进 locker room）；amispecial50 则是高度元叙事的内心独白（"the jar I'm trapped inside reflects not the me that I see but the one that you do"），把 Ami 的社会身份（女仆、社团成员）与私人身份（恋人、Sekai 之女）在文本层完成一次合流。

### 11. amilust50intro / amilust50：高好感度欲望场景

amilust50intro / amilust50 是 ami_love>=50 阶段的高好感度 lust 内容。

### 12. amispring1–5：春季篇章五连

时间线在春季明显加速，事件从"约会／打工"转向存在论与集体活动。amispring1 以"worm／Giles Corey"的元叙事引子与 Ami 反复吟唱 "Daisy Bell" 开场，把身体与文本、被书写与重生主题抛向台前；amispring2–5 延续这一季章节。全作中"reset"母题在 Ami 线确有落点：Ami 曾把某种打击比作 "pressing a reset button"，叙述者亦言 "awaits the next reset"，与"如果一切都会重置，此刻意义何在"的追问彼此呼应。

### 13. amicamp1 / amicamp2：归家与门廊的元叙事

amicamp1 写 Sensei 离开 Makoto 后回家找 Ami，在敲门时浮现 "The hallway of life is door upon door... Each door has a doorknob. Each opens to secrets" 的诗句，把日常归家升格为关于"选择／重生"的元叙事段落；amicamp2 延续 camp 章节。Ami 在此被重新定位在与其他女主的关系网中。

### 14. halloweenami1：万圣节特别事件

halloweenami1 以 Maya（"skinwalker"）走失、Ami 扮 "Sakura Sunlight" 寻友的万圣节戏谑开场；其后接入 Niki（ni）与经纪人 Patrice 的豪车情节——叙述者写 Niki "faith that she'd fulfill the role she needed to fill to keep the wheels of time spinning while everything else has stopped"，并以 "A pencil in the hand of God is as good as a pen in the hand of the Pope. But when both of those tools are taken away, only one can write in blood" 收束 pencil／pen／blood 的书写工具隐喻；Patrice 与 Niki 关于行李（"you only brought one bag"）的对话则把情节推向转移／离开。Ami 线的欢乐日常由此直接接入主线的时间停滞母题：车轮仍在转，而故事内的一切已被冻结。

## 三、lust 线概貌

Ami 的 lust 轨道由 amiinvitethighjob、amiinvitereverse、amigenafternoon、amigennight(2)、amilust15/35/50/60 等 label 构成，多数经由 amisroom 路由桩或 amiinvite 菜单错位进入。各段落功能高度一致：将 Ami 的身体作为可重复调用的场景资源，与 love 线的情感积累并行供给。值得注意的是 lust 内容从不质疑关系本身——质疑只发生在 love 线（如 amiinvite4 的 "someone else I used to know" 独白、amidate50 墓前对"看不见的存在"的困惑），欲望场景因此成为元叙事层之外的"安全区"，其空洞的重复性恰恰反衬 love 线每一次情感推进的不可复制性。

## 四、与主线／元叙事咬合点

1. **USER1 实例**：Ami 线含系统提示 "USER1 HAS SUCCESSFULLY LOGGED IN"（amidate50p4 收束处），她被明确置于 USER1 观察之下；三层世界观（恋爱表层／重置循环层／元叙事层 USER1-4）中，她位于最底层却被上层持续注视。
2. **"不真实者"命题**：咖喱以血代盐的真假并置（amiinvite4）、amispecial50 中"罐中主角／你眼中的我"的独白，把恋爱故事升格为本作"虚构角色能否被爱"的题眼；类似质询散见于其他觉醒角色线，Ami 是被说破最直白的一例。
3. **Sekai 遗产**：作为 Sekai 之女，Ami 承接 Sensei 对亡者的移情；amidate50 墓前"看不见的存在"双关使她同时成为哀悼者与被哀悼结构的继承者。
4. **血 motif**：血咖喱（amiinvite4）与 pencil／pen／blood 书写隐喻（halloweenami1："only one can write in blood"）共享同一符号链——血液既是生命真实性证明，又是剧本（用笔写就之物）的原料；角色的血进入叙事，等于承认自己被书写。
5. **时间停滞**：halloweenami1 中 Niki 相关的 "everything else has stopped" 表明 Ami 线的欢乐日常发生在被冻结的世界里，她的每一次微笑都是循环内的表演。

## 五、未解伏笔

- Ami 的血咖喱到底是玩笑还是真实？若是真实，她的生理构造指向非人设定。
- amidate50 墓前 Sensei 回应声部是内心独白还是系统级插话？"Even if you can't see me" 的主语究竟是谁。
- Sensei 说 Ami "reminds me a lot of someone else"——那个"别人"是否就是 Sekai（她已故的母亲），还是更早循环中的某个 Ami；源文只说 "It's someone I try not to think about because it hurts"。
- amiinvite 菜单选项与跳转目标的系统性错位是有意设计还是残留缺陷；若是有意，谁在改写菜单。
- halloweenami1 尾部 Niki／Patrice 的行李对话指向离开／转移，Ami 是否会在下一阶段被"打包"进新的循环。
- pencil／pen／blood 隐喻的具体机制从未被正面解释。

> 按源 label 名回源见 `游戏文本/AmiEvents.rpy`。
