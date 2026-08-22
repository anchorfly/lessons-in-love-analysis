# USER3 与 pareidolia 源文分析

> 本文件是「精读所有事件」收官后，补读核心引擎 `script.rpy` / `chap3.rpy` / `SanaEvents.rpy` 中 **USER 终端系统**与 **pareidolia（空想性错觉）** 源文的聚焦成果。
> 目的：为长期课题「Ren'Py 源中无 speaker 框旁白究竟哪些是 Sekai 的叙述声音」提供 **USER 备份机制**与 **pareidolia/USER3 破墙叙述者**的母体证据。
> 所有引文标注 `文件:行号`，可直接回查原文。

---

## 〇、核心结论（先给判据）

1. **pareidolia = USER3**。三处源文构成闭合证据链（见 §3）。
2. **Sana 自承 pareidolia**（`SanaEvents.rpy:5513` "you can call me pareidolia."）——但这是人格/身份声明还是附身/代言，需结合 §5 待补判定。
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

### 3.3 自报名 + 破墙（Sana 线）
- `SanaEvents.rpy:5223 label ayanesanabeach4:`
- `5502-5512` 无框小写旁白（带 `//` 后自述 "drop the /'s"）：
  > "hello again"
  > "you really should have heeded the warning, you know."
  > "you should have quit playing this game a long, long time ago." （`5507`，直接破墙对玩家说）
  > "take me for example. and when i'm likely or even able to show up."
- `5513 "you can call me pareidolia."` ← **自报其名**
- `5516 "where are we right now?"` → `5523 "we're outside."` `5524 "sana sakakibara is making her way over to her mother's house..."`
→ 叙述者以 pareidolia 之名，用无框小写旁白直接对玩家说话，并同步叙述 Sana 的行动。**这是 pareidolia = USER3 叙述声音最完整的样本**。

### 3.4 栖居于 Yumi 脑内（chap4part2 six9，二轮修订新增）
- `chap4part2.rpy` 源 3582–3612（Obstacle Course 尾声）：Yumi 与小写斜体旁白的直接对话——
  > N: {i}told you it would work. now speak to the weird fucking turtle thing so we can get out of here and go back to being best friends.{/i}
  > y: I don't know how many times I need to tell you that you're not my friend… **You're not my friend.**
  > N: {i}if i'm not your friend, how come we're always spending so much time together?{/i}
  > y: Because you live inside of my fucking {i}head,{/i} maybe?
  > N: {i}or maybe you just like me — and you look forward to the way i think for you so you don't have to think for yourself.{/i}
- 随后 Yumi 请 Wise Turtle "vaporize Pareidolia"（3594），Turtle 答复后 Yumi 与脑内声音**同时**惊愕 "You actually talk? / {i}it actually talks?{/i}"，并互相确认 "We didn't just mutually imagine that, did we?"（3611）。
- **结论**：pareidolia 不只做破墙旁白，还以"脑内声音"形式寄生于特定角色（Yumi），并自述职能——"i think for you so you don't have to think for yourself"。这与 YumiEvents 2790 的小写 `hello.` 同腔调互相印证：**Yumi 是 pareidolia 的宿主之一**。

### 3.5 终端小游戏中的 USER1 特殊行为（二轮修订新增）
- `script.rpy:36686`（enterusername，USER1 分支）：`"USER1" IS OFFLINE AND CAN NOT ACCEPT YOUR REQUEST` 之后**直接 `jump babyfinches`**——连接 USER1 不返回错误菜单，而是把玩家坠入甜系平行世界场景（Sensei×Maya 恋人日常、循环对话崩塌、hex 独白）。
- **解读**：USER1（Ami 线实例）的"离线"不是拒绝而是**重定向**——babyfinches 世界即 USER1 的运行现场（或其备份快照）。这与 AmiEvents 5170 "USER1 HAS SUCCESSFULLY LOGGED IN" 呼应：Ami 线是一个独立运行的用户实例。

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
1. **USER ↔ loop 迭代映射**：USER1/2/3/4 各自对应哪一次迭代？USER4 与 Nao "USER4 备份" 的具体绑定机制未读 Nao 源段验证。
2. **Sana = pareidolia 的本体**：是 Sana 的隐藏人格、被 pareidolia 附身、还是 pareidolia 借 Sana 场景显形？需结合 `sanaspring1-3`（`5687/6040/6379`）与 Sana 其余无框段落判定。
3. **pareidolia 与 Sekai 是否为同一"世界意识"的两面**：两者都做无框叙述，但腔调/对象不同。需回到 117 场景逐条比对，确认有无"合流"段落。
4. **TERMINAL 23 的实体意义**：为何是 23？与 Dorm `roomwithclocks` 的 "TIME REMAINING: 2"、重置倒计时是否同构？
5. **USER5 缺席的含义**：系统只定义到 USER4，是否暗示"第五个用户"是尚未激活的变量（关联未来线 Himawari / 天界管理员）？
6. **（二轮修订新增）Yumi 宿主化的时点**：pareidolia 何时入住 Yumi 脑内？与 Yuki[2952] "how Yumi was made"、Yumi 线 "aware again" 是否同一事件？
7. **（二轮修订新增）postwarsix1 hex 双行**（chap4part2 源 5051–5052）"we are being watched again / i hope they can not read numbers" 的书写者归属——旁白本体还是 USER3 代笔？"they" 指谁（其他玩家？系统管理员？）。

---

## 附：源文件标签索引（便于回查）
- `script.rpy`：`trinity3`(33739) / `enterterminal`(36631) / `enterusername`(36682) / `enteryourpass`(36731) / `hoorayanotherreset`(36750) / `coolrectanglemachine`(36598)
- `chap3.rpy`：`beachwars18`(34010)
- `SanaEvents.rpy`：`ayanesanabeach4`(5223)
- `definitions.rpy`：`s`=Sensei(2322) / `se`=Sekai(2348)
- `AmiEvents.rpy`：`USER1 HAS SUCCESSFULLY LOGGED IN`(5170)
- `KaoriEvents.rpy`：`USER2 HAS GONE OFFLINE`(2641)
