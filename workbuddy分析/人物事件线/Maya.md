# Maya Makinami 事件线梳理（MayaEvents.rpy，v0.55，约 10500 行 / 39 label）

> 基于 `_digest_Maya.txt`（5895 行）精读。Maya 是**全作神话核心**——神社巫女、"做时间的事"、唯一明确知道"这是一个大循环"并"同时活在所有三层"的角色；年龄被系统涂黑（[[redacted]）。所有结论标注源行号。

---

## 一、角色基本盘

- **身份**：神社巫女（shrine 系列主场景）， cryptic、对 Sensei 既驱逐又吸引。sportswars / halloweenmaya / mayafestival 显示她是主角圈核心成员。
- **表面性格**：沉默、毒舌、死鱼眼；反复命令 Sensei 远离自己却又在循环中等待他。自称 "Maya Makinami. My hobbies include watermelons and the violin. My past is of none of your concern."（[1401]）。
- **深层状态（全作最关键）**：
  - 她的**年龄被系统涂黑**（[1401] "Age, [[redacted]"）——她不是普通学生，是某种非人/被囚实体。
  - 她**知道这是一个大循环**（[920] "if this really is one big cycle"）。
  - 她**同时活在过去/现在/未来三层**（[906] "Maya has somehow found a way to live in all three at once"）。
  - 神社是"无论何时访问都不变"的固定点（[102] "some places remain unchanged no matter when you visit them"）——即重置循环中不被清除的锚点。
- **关键变量**：maya_love / maya_lust；bonus 分支。
- **与 Ami 的互文**：Ami 线 halloweenami1 称 Maya 为 "the tragic tale of Maya Makinami (or the one who wears her skin)"（skinwalker 措辞）；Ayane 线揭示 "Maya is lucky that I feel like my existence rests in the palms of her hands"（[5257]，Maya 掌控 Sensei）；未来线 Himawari 称 "Maya Makinami does not exist"（[14009]）。

## 二、love 线逐事件脉络

- **firsttimeshrine**（[125]）：初遇。神社在雪中"未被积雪覆盖"（[98]），Maya 给出"有些地方无论何时访问都不变"的 cryptic 回答（[102]）——奠定"固定点"母题。
- **shrine5 → shrine40**（[483]–[4350]）：随 love 值递进的神社日常，Maya 逐渐从"驱逐"转为默许陪伴。
- **mayafestival1–4**（[2715]–[3936]）：祭典四部曲，情感推进。
- **mayadate45 / mayaspecial45**（[4610]/[5059]）：高阶约会/特殊事件。
- **sportswars5 / sportswars10 / sportswars14**（[5490]/[5898]/[6216]）：Dorm Wars 与主角圈交叉（与 Ayane 线的"三人协商"呼应）。
- **halloweenmaya1–3**（[6438]–[7095]）：万圣节，Maya 的悲剧被以戏谑方式触及（"wears her skin" 同位的皮肤/替身议题）。
- **mayaspring1–5**（[7571]–[10191]）：第四章弹簧事件，**spring 是她"做时间的事"的收束段**（与 DormEvents 的 roomwithclocks / ticktock / trinity1 神话簇直接咬合）。

## 三、lust 线概貌（抽象概括）

lust 节点不显式见于 label 名（Maya 线以 shrine/date/festival/spring 命名），meta 密度在 love 线本身已极高，lust 段多被含蓄处理。Karin 线中 Maya 自述 "I do the time thing"（[4174]）可视为对其"职能"的元说明。

## 四、与主线咬合点（核心）

1. **神社 = 重置循环中的固定锚点**（[98]–[102]）：雪覆全城唯神社无雪；Maya "some places remain unchanged no matter when you visit them"——神社是循环中不被 wipe 的记忆/实体锚点，类比 DormEvents 的 clocks 房间。
2. **"同时活在所有三层"**（[906]）：旁白 "Maya has somehow found a way to live in all three at once"——明示 Maya 跨越"恋爱模拟表层 / 重置循环层 / 元叙事玩家层"三层存在，是全书对世界观结构最凝练的注脚。
3. **她知道这是一个大循环**（[920]）：s "Maya, if this really is one big cycle...what I decide to do right now won't make much of a difference in the long run, right?"——Sensei 在此直接向 Maya 求证循环本质，而 Maya 未否认，仅怨 Sensei "理解力太差"（[925]）。
4. **年龄被涂黑 = 非人/被囚**（[1401]）："Maya Makinami. Age, [[redacted]."——系统级信息遮蔽，与 Ami 线 amispring5 所指"被囚在秘密性牢笼数月的女孩"（[11138]）、未来线 "Maya Makinami does not exist"（[14009]）共同指向：**Maya 本体可能并不以"学生"身份真实存在**。
5. **"做时间的事"**（Karin 线 [4174]）：Maya 在 Karin 面前自陈 "the main heroine of Lessons in Love. I do the time thing."——将"时间操控"归为自己的职能，与 DormEvents ticktock / roomwithclocks 的时钟机制、Ami 线 amiinvite4 的强制重复重置同属"时间/重置"神话簇。
6. **Haruka 让出主角席位**（Haruka 线 [3344]）："I'm actually going to give the main heroine spot to Maya"——第三方角色公开确认 Maya 的 main heroine 地位，与 Ami（自称 main heroine）、Karin 线 Maya 自述形成"谁是真主角"的三角张力。
7. **shrine30 门控挂在 Ami 的 virgin flag 上**（MayaEvents.rpy:18）：`maya_love >= 30 and mayadorm30 == True and ami_virgin == False and shrine30 == False` 才能进入 shrine30——**Maya 神社线的推进以"Sensei 已夺走 Ami 处女"（坏叔叔状态）为硬前提**；进度校验（newchecker.rpy:2041）与 Progress UI（screens.rpy:3980）同步该条件。机制层把 Maya—Ami 双姝绑定为道德/剧情共同体（详见 `Ami.md` 好/坏叔叔标识一节）。

## 五、未解伏笔

- Maya 的"被涂黑的年龄"与"不存在论"（未来线）如何调和？她究竟是囚徒、神、还是玩家投射？
- "做时间的事"具体指什么机制？她能否主动重置，还是被重置束缚？
- 神社为何是固定锚点？是否与她"被囚"的地点重合？
- Maya 与 Ami 的血缘/镜像关系（Ami 疑似 Akira 亲生女，Maya 疑似被囚本体）尚待汇总文档厘清。

## 六、label 总表（39 个）

shrine[1] · callmayamorning[33] · callmayaafternoon[53] · callmayanight[69] · mayanoongen2[93] · firsttimeshrine[125] · shrine2to4[457] · shrine5[483] · shrine10[708] · shrine15[969] · shrine20[1317] · shrine25[1641] · shrine30[1939] · shrine35[2275] · mayafestival1[2715] · mayafestival2[3114] · mayafestival3[3540] · mayafestival4[3936] · shrine40[4350] · mayadate45[4610] · mayaspecial45[5059] · sportswars5[5490] · sportswars10[5898] · sportswars14[6216] · halloweenmaya1[6438] · halloweenmaya2[6743] · halloweenmaya3[7095] · mayaspring1[7571] · mayaspring2[8053] · mayaspring3[8409] · mayachristmalloween1[8759] · mayachristmalloween2[9002] · mayachristmalloween3[9301] · dormwarssixmaya1[9549] · mayaspring4[9807] · mayaspring5[10191]
