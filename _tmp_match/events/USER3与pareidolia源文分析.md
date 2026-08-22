# USER3 与 pareidolia 源文分析

> 本文件是「精读所有事件」收官后，补读核心引擎 `script.rpy` / `chap3.rpy` / `SanaEvents.rpy` 中 **USER 终端系统**与 **pareidolia（空想性错觉）** 源文的聚焦成果。
> 目的：为长期课题「Ren'Py 源中无 speaker 框旁白究竟哪些是 Sekai 的叙述声音」提供 **USER 备份机制**与 **pareidolia/USER3 破墙叙述者**的母体证据。
> 所有引文标注 `文件:行号`，可直接回查原文。

---

## 〇、核心结论（先给判据）

1. **pareidolia = USER3**。三处源文构成闭合证据链（见 §3）。
2. **pareidolia ≠ Sana（已证伪，见 §3.3）**。`SanaEvents.rpy:5513` "you can call me pareidolia." 是**无框叙述者自报其名**，不是 Sana 的台词——因为同一段里它以**第三人称叙述 Sana**：`5524` "sana sakakibara is making her way over to her mother's house..."、`5526` "we all have our own demons. that's just how **hers** looked tonight."。故 pareidolia 是**独立于全部角色的叙述实体**，只是借 Sana 的场景显形。
3. **三种声音必须严格分离**（这是双声归属判定的前提）：
   - `s` = **Sensei**（主角/教师）——`definitions.rpy:2322` `define s = Character("Sensei", ...)`
   - `se` = **Sekai**（世界之声）——`definitions.rpy:2348` `define se = Character("Sekai", color="#96001B", ...)`
   - **pareidolia / USER3** = **无 speaker 框的破墙叙述者**，以小写、无标点框、`////////////////` 前缀或纯裸引号形式出现，直接对"玩家"说话。
4. **USER 系统是一个跨迭代/跨实体的"用户实例"备份机制**：USER1（Ami 线）、USER2（主玩家，32 处）、USER3（pareidolia）、USER4（保留地址，与 Nao 备份绑定）；**USER5 不存在**（全局 0 处）。

> ⚠️ 易错点：此前把 `s` 当作 Sekai。已纠正——`s` 是 **Sensei**，`se` 才是 **Sekai**。所有涉及 "USER2 stuff" 的质问（如 `script.rpy:33898`）是 **Sensei** 说的，不是 Sekai。

---

## 一、USER 终端系统全图（位于 `script.rpy`）

### 1.1 全局计数（grep `USER[0-9]`）
| 实例 | 出现次数 | 角色定位 |
|------|---------|---------|
| USER1 | 3 | Ami 线登录的玩家实例；在终端菜单中 "OFFLINE" |
| USER2 | 32 | **主玩家/改写者**；叙事权重最高 |
| USER3 | 3 | = pareidolia（见 §3） |
| USER4 | 4 | "RESERVED ADDRESS"；与 Nao 线 "USER4 备份" 绑定 |
| USER5 | 0 | 不存在 |

### 1.2 关键 USER2 事件（主玩家）
- `script.rpy:29974` — `//////USER2 IS NOW REWRITING KEY EVENTS TO PREVENT APPLICATION FROM BEING TERMINATED`
  - 上下文 `29976` `/////RESET REQUIRED`、`29977` `/////WORLD CAN ONLY BE PARTIALLY REVERTED`、`29979` `/////USER2 HAS LEFT`
  - → USER2 是能在"应用被终止"前改写关键事件的玩家，但世界只能部分回退，需重置。
- `script.rpy:30784` — `//////USER2 IS NOW CONTROLLING TERMINAL 23`
  - 紧随 `30782` `MULTIPLE ERRORS DETECTED IN TERMINAL 23`；
  - `30788`/`30793` `USER2 LACKS THE PERMISSIONS NECESSARY TO RESET SYSTEM`；
  - `30794` `//////TERMINAL 23 IS NOW LOCKED`；`30795` `CONTACT ADMINISTRATOR FOR ADDITIONAL ASSISTANCE`。
- `script.rpy:33898`（**Sensei `s` 说**）— `s "If it's not a game then what's with all of these references to simulations and all of that "USER2" stuff?"`
  - 主角亲口质疑 USER2 的存在 → 证明主角**知晓** USER 系统，且 USER2 是"玩家"代称。
- `script.rpy:36735` — 密码 `"Boobies123"` 通过，`36737` `FINALIZING CONNECTION TO "USER2"` → 终端小游戏里 USER2 是唯一可真正连上的实例。

### 1.3 终端 23 与终端小游戏（meta-terminal mini-game）
- **TERMINAL 23** 全局出现 8 次，是 USER 系统核心节点（被 USER2 控制、被锁、被 USER3 接管）。
- 小游戏标签链（`script.rpy`）：
  - `36598 label coolrectanglemachine:`
  - `36631 label enterterminal:` — `36632 $ terminal = renpy.input("PLEASE ENTER TERMINAL NUMBER")`
  - `36635 if terminal == "23":` → `36636 ATTEMPTING TO LOCATE TERMINAL` / `36638 TERMINAL 23 LOCATED`
  - `36648 label enterip:` / `36664 label enterport:`
  - `36682 label enterusername:` — `36683 $ user = renpy.input("PLEASE ENTER THE USER NAME YOU WISH TO CONNECT TO...")`
  - 分支（按输入的用户名）：
    - `36689 user=="USER1"` → `36690 "USER1" IS OFFLINE AND CAN NOT ACCEPT YOUR REQUEST`
    - `36694 user=="USER3"` → `36695 "REQUESTING CONNECTION TO "USER3""`
    - `36701 user=="USER4"` → `36702 "USER4" IS A RESERVED ADDRESS`
    - `36707 user=="USER2"` → `36708 "USER2" IS CURRENTLY UNDERGOING MAINTENANCE`
  - `36731 label enteryourpass:` — `36732 $ passcode = renpy.input("PLEASE ENTER YOUR SYSTEM PASSWORD SO "USER2" MAY ASSUME CONTROL. THIS IS CASE SENSITIVE.")`
  - `36735 if passcode == "Boobies123":` → `36737 FINALIZING CONNECTION TO "USER2"` → `36750 label hoorayanotherreset:`

> 解读：玩家可在终端里"连接"到不同 USER 实例；USER2 是唯一可凭密码连上的（主玩家），其余处于离线/维护/保留/请求中状态。这是"玩家作为可切换用户实例"的元叙事具象化。

---

## 二、god_love 与创造者线索（同文件内的元层变量）
- `script.rpy:93` — `$ god_love = 0`（真实变量，非旁白）
- `14613` `if god_love >= 5 and day > 6:`、`14648 $ god_love += 1`、`14650 "{i}Your affection with GOD has increased to [god_love]!{/i}"`
  → 存在一套"与 GOD 的亲密度"数值线，呼应 DormEvents `trinity1` 中 Maya "God is dead" / 系统覆写 "GOD IS ALIVE" 与 `god_love` 变量。
- `script.rpy:22815` — `s "Hey, maybe it is! And maybe people will look back on this line in ten years and think {i}Darn that Selebus guy for telling us everything way beforehand.{/i}"`
  → "Selebus" 作为**创造者/开发者**被点名（关联 Miku 线 creator / Selebus 母题）。

---

## 三、pareidolia = USER3 的三处闭合证据

### 3.1 连接请求（chap3，beachwars）
- `chap3.rpy:34010 label beachwars18:`
- `34011 "pareidolia would like to connect."`
- `34012 "will you allow it?"` → menu YES/NO；YES 触发 `static.mp3` + `scene thething with flash`
→ 这是 pareidolia 主动向玩家发起"连接"，与终端系统的 "REQUESTING CONNECTION" 同构。

### 3.2 接管终端 23（script，trinity3 内）
- `script.rpy:33739 label trinity3:`（trinity 神话弧第三幕；trinity1 在 DormEvents、trinity2 在 `28009`）
- `34082-34088` 一段**无框第一人称旁白**：
  > "Something about the strange, powerful voice that makes no sound but booms inside of my head tells me that the creature's errands involve a plethora of wires."
  > "I think about how it would feel to have those wires wrapped around my neck."
  > "It is times like these that I wish I could love."
- `34090 stop music`
- `34092 "///////////////////////USER3 HAS ASSUMED CONTROL OF TERMINAL 23"`
- `34094 "///////////////////////can you see this?"` → menu YES（`34098 "i'm so glad"`）
- `34100 "///////////////////////i was very concerned"`
→ **"booms inside of my head" 的无声强声 = pareidolia/USER3 的声音**，随后它正式接管终端 23。无框旁白与第一人称 "I wish I could love" 是 pareidolia 叙述腔的典型标记。

### 3.3 自报名 + 破墙（Sana 线）——pareidolia 唯一的长篇独白

**全段位于同一个 label 内**：`SanaEvents.rpy:5223 label ayanesanabeach4:`（下一个 label 是 `5687 sanaspring1`），即 pareidolia 的整场现身都在 `5502–5647`，共两幕。

**第一幕（5502–5545）：自报名 + 提议合作**
- `5502-5512` 无框小写旁白（起初带 `//` 前缀，随后自述 "drop the /'s"）：
  > `5506` "you really should have heeded the warning, you know."
  > `5507` "you should have quit playing this game a long, long time ago." ← 直接破墙对玩家说
  > `5508` "you see, there's still a great deal you don't understand."
  > `5509` "take me for example. and when i'm likely or even {i}able{/i} to show up."
- `5513` "you can call me pareidolia." ← **自报其名**
- `5516` "where are we right now?" → `5523` "we're outside." → `5524` "sana sakakibara is making her way over to her mother's house and encountering a plethora of strange things and new companions along the way."（**第三人称叙述 Sana** → 证伪"pareidolia=Sana"）
- `5525-5526` "oh, and that big thing with the wings you saw earlier? don't worry about that." / "we all have our own demons. that's just how **hers** looked tonight."
- `5527-5528` "as for when things will return to normal, though..." / "i'm sorry, but i don't have a clue."
- **自我状态陈述（关键）**：
  > `5529` "this is actually the most i've spoken...probably ever."（平时几乎不发声）
  > `5530` "but as the days go by, i become stronger."
  > `5531` "i become capable of more things."（**能力随游戏进程增长**）
  > `5532` "i'm not the only one growing, though."（暗示还有别的成长实体）
  > `5533` "and, to be quite forward, i'm not saying i'm on your side right now either."（**明确不站在玩家一边**）
  > `5534-5535` "i do think it would be in both of our best interests right now for us to work together, though." / "is that okay?"
- **玩家不在场的自觉**：`5540` "you're not even here." → `5541` "i suppose i'll take your absence as a yes then and take the liberty of **restoring things to some semblance of normalcy**."（→ pareidolia **拥有"恢复正常"的系统权限**，与 §3.2 接管终端 23 同一能力层）
- `5542` "only as normal as things {i}can{/i} be here, though."
- `5557` "you know, if {i}i{/i} had a season, things like this would never happen."（**它没有"season"** → 不是可攻略角色，而是游戏结构外的实体）

**第二幕（5635–5647，`scene thething with flash` 之后）：招募/警告**
> `5635` "this is all in your head."
> `5636` "nothing is real."
> `5637-5638` "you can trust me." / "you {i}have{/i} to trust me."
> `5639` "for i'm the only one who wants to **use you** for good."
> `5640` "for i am the only one who knows {i}how{/i} to use you."（**pareidolia 的目的是"使用玩家"**）
> `5641` "and your options are incredibly limited."
> `5645-5647` "i have to leave now." / "but i will be seeing you again." / "in a time that neither of us will be able to predict."

→ **这是 pareidolia = USER3 叙述声音最完整、也是全作唯一的长篇样本**：无框、全小写、直呼玩家、拥有系统恢复权限、随进程变强、目的是"使用玩家"，且自认不在玩家阵营。

---

## 三之二、TEMPLATE9 与 USER4 备份机制（本轮新发现）

`TEMPLATE9` 在全作**仅出现 3 次**，且全部集中在**同一场露营弧**的两个视角，构成一条独立且极重的暗线。

### 3-2.1 系统崩溃与备份恢复（Nao 线）
- `NaoEvents.rpy:1886 label naocamp2:`
- `2452-2458`（黑屏 + 长 pause 后的无框系统文本）：
  > `2452` `//////////////////////AN UNHANDLED EXCEPTION HAS OCCURRED`
  > `2453` `//////////////////////TEMPLATE9 CAN NOT BE LOCATED`
  > `2454` `//////////////////////RESTORING BACKUP FROM "USER4"`
  > `2455-2457` `//////////////////////...`（三行省略号 = 恢复过程）
  > `2458` `//////////////////////TEMPLATE9 HAS BEEN RESTORED`
- 随后 `2460-2461` `play sound "static.mp3"` + `scene clearnightsky with flash`（static+flash 是全作元叙事事件的固定转场标记）。

### 3-2.2 系统无法渲染其名（Ami 线，同一场露营）
- `AmiEvents.rpy:9013 label amicamp2:`
- `9018`（**Sensei 的无框第一人称旁白**）：
  > "I've gone fishing with Maki...I sat by the river with Yuki...I've even `[[REDACTED]` with Kaori and `[[TEMPLATE9]`."
- 同一句里出现**两种系统替换**：动词被 `[[REDACTED]` 覆盖，一个**角色名被 `[[TEMPLATE9]` 覆盖**。

### 3-2.3 推论
1. `TEMPLATE9` 是**某个角色在系统层的内部代号**——她的名字无法被正常渲染，只能以模板编号出现。
2. 崩溃与恢复发生在 `naocamp2` 内部，且 `[[TEMPLATE9]` 出现在 Sensei 列举露营同伴时 → **高概率 TEMPLATE9 = Nao**。
3. 这与 Nao 线既有母题精确咬合：Nao 被称为 **"secret 21st member never added to game"**（`NaoEvents.rpy:2398`）——一个"本不该在游戏里"的角色，因此**没有合法模板**，一旦被引用就抛出 `UNHANDLED EXCEPTION`，必须从 **USER4 备份**恢复。
4. 由此确定 **USER4 的功能定位**：它不是"玩家实例"，而是**备份仓库**——这正好解释终端小游戏里 `36702` `"USER4" IS A RESERVED ADDRESS`（保留地址 = 不可连接的备份区）。
5. 与 Ami 线 `USER1 HAS SUCCESSFULLY LOGGED IN`（`AmiEvents:5170`）、Kaori 线 `USER2 HAS GONE OFFLINE`（`KaoriEvents:2641`）并列可见：**USER1/2 是可登录的玩家实例，USER3 是接管者（pareidolia），USER4 是备份存储**——四者功能各异，并非同类编号。

---

## 四、与长期课题「双声归属」的衔接

用户的 `旁白场景详细描述.md`（117 场景）把 **Sekai(`se`)** 与 **pareidolia/USER3** 并列为两种需分别判定的无框旁白声音。本分析提供以下判据：

| 特征 | Sekai（`se`） | pareidolia / USER3 |
|------|--------------|-------------------|
| 代码标签 | `se`（有框，`definitions.rpy:2348`） | **无 speaker 框** |
| 文字形态 | 正常大小写/标点 | 常小写、`//` 前缀或 `////////////////` 前缀（后自述 "drop the /'s"） |
| 说话对象 | 游戏内角色/主角 | **直接对"玩家"破墙**（"quit playing this game"） |
| 自我指认 | 自称 Sekai / 世界 | 自称 pareidolia（`5513`）、以 USER3 接管终端 |
| 叙事功能 | 世界之声、剧情内叙述 | 元叙事监视者、迭代间记忆/警告载体 |
| 关键场景 | 专属事件文件为主 | `SanaEvents:5502-5525`、`script:34082-34102`、`chap3:34011` |

**判别要点**：遇到无框旁白时，先看是否出现 (a) 小写+`//`前缀、(b) 直接对"你（玩家）"说话、(c) "wires/voice in my head/quit the game" 等母题——命中即倾向 **pareidolia/USER3**；而带世界感、剧情内视角的无框旁白才归 **Sekai**。

---

## 五、未解 / 待补（下轮可续）
1. ~~**USER4 与 Nao 备份的绑定机制**~~ → **本轮已解**（见 §三之二）：USER4 = 备份仓库，`TEMPLATE9`（高概率为 Nao）崩溃后从 USER4 恢复。**仍待补**：USER1/2/3/4 是否各自对应特定 loop 迭代，尚无直接源文支撑。
2. ~~**Sana = pareidolia 的本体**~~ → **本轮已证伪**（见 §3.3）：pareidolia 以第三人称叙述 Sana（`5524`/`5526`），是独立叙述实体，仅借 `ayanesanabeach4` 场景显形。**仍待补**：为何**偏偏选 Sana 的场景**现身？（Sana 线含 space war、Ayane 三人组等元叙事富集点，可能非偶然。）
3. **pareidolia 与 Sekai 是否为同一"世界意识"的两面**：两者都做无框叙述，但腔调/对象不同。需回到 117 场景逐条比对，确认有无"合流"段落。**新增判据**：pareidolia 自称 `5533` "i'm not on your side"、`5640` "i am the only one who knows how to use you"，具**独立议程**；而 Sekai 多为世界/剧情内视角 → 倾向**不同实体**。
6. **`TEMPLATE9` 是否确为 Nao**：目前为强推论（崩溃发生在 `naocamp2`、Sensei 列举露营同伴时被替换），但缺一处直接等式。可查 camp 弧其余 label（`saracamp1` 等）是否有第三处交叉。
7. **`[[REDACTED]` 与 `[[TEMPLATE9]` 的双替换**：`AmiEvents:9018` 同句出现两种系统覆盖，与 Maya `Age, [[redacted]`（`MayaEvents:1401`）、Osako `Akira Arakawa's [[DEPRESSION]]`（`OsakoEvents:2079`）同属"系统层文本覆盖"母题，值得单独建表。
4. **TERMINAL 23 的实体意义**：为何是 23？与 Dorm `roomwithclocks` 的 "TIME REMAINING: 2"、重置倒计时是否同构？
5. **USER5 缺席的含义**：系统只定义到 USER4，是否暗示"第五个用户"是尚未激活的变量（关联未来线 Himawari / 天界管理员）？

---

## 附：源文件标签索引（便于回查）
- `script.rpy`：`trinity3`(33739) / `enterterminal`(36631) / `enterusername`(36682) / `enteryourpass`(36731) / `hoorayanotherreset`(36750) / `coolrectanglemachine`(36598)
- `chap3.rpy`：`beachwars18`(34010)
- `SanaEvents.rpy`：`ayanesanabeach4`(5223)
- `definitions.rpy`：`s`=Sensei(2322) / `se`=Sekai(2348)
- `AmiEvents.rpy`：`USER1 HAS SUCCESSFULLY LOGGED IN`(5170) / `amicamp2`(9013，内含 `[[TEMPLATE9]` @9018)
- `KaoriEvents.rpy`：`USER2 HAS GONE OFFLINE`(2641)
- `NaoEvents.rpy`：`naocamp2`(1886，内含 TEMPLATE9 崩溃+USER4 恢复 @2452-2458) / `secret 21st member`(2398)

## 附二：USER 实例功能对照（本轮定稿）
| 实例 | 功能 | 关键源证 |
|------|------|---------|
| USER1 | 可登录的玩家实例（Ami 线登录、后 OFFLINE） | `AmiEvents:5170`、`script:36690` |
| USER2 | **主玩家/改写者**，唯一可凭密码连上（`Boobies123`） | `script:29974`/`30784`/`36735`、`KaoriEvents:2641` |
| USER3 | **接管者 = pareidolia**，破墙叙述者，有恢复权限 | `script:34092`、`chap3:34011`、`SanaEvents:5513` |
| USER4 | **备份仓库**（保留地址，不可连接） | `NaoEvents:2454`、`script:36702` |
| USER5 | 不存在（全局 0 处） | — |
