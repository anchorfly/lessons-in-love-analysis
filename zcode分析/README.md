# GLM 精读总结 · 生产区总览

> **定位**：本目录（`GLM精读总结/`）是《Lessons in Love》反编译脚本的**正式生产物区域**，收录对工作区全部 71 个 `.rpy` 文件的精读总结。此前的中间产物存于 `_tmp_match/`（临时区）与根目录单文件，本区为整理后的最终集合。
> **生成**：2026-08-22，GLM。方法：自研 digest 脚本提取（保留 label+源行号+对话+跳转）→ 逐文件/逐 label 精读 → 汇总落盘。
> **版本勘误（重要）**：旧报告标注 v0.55 有误——`options.rpy:27` 显示本反编译实为 **0.60.0**（`gui.about` 含版本号）。各子报告标题中的 "v0.55" 沿用旧称，实际内容均读自 0.60.0 源文。
> **分级说明**：本作含成人内容，全部报告一律抽象表述（如"发生亲密关系"），不复述露骨文本；bonus/双版本差异内容按约定忽略。

---

## 一、生产区文件导航

| 文件 | 内容 | 覆盖对象 |
|---|---|---|
| `README.md` | 本文件：总览、全文件索引、一页总结、勘误 | — |
| `01_系统与机制文件精读.md` | 19 个系统文件的机制、变量、解锁表与系统层元叙事 | Phone/PhoneStyles/definitions/screens/gui/options/setup/replace/autopatch/checker/newchecker/happytracker/headpatcentral/unlockables/dlcmenu/jukebox/mathhomework/carepackages/profile_outfits |
| `02_特殊内容与迷你游戏文件精读.md` | 5 个特殊文件：Build-A-Maya、Sensei-Quest、图片/动画/成人内容主文件 | flowers/senseiquest/nudes/animatedscenes/inappropriatecontent |
| `03_章节泛型与USER机制溯源.md` | 章节泛型日常与第四章枢纽调度器；USER1–4 全局溯源 | chap3generics/chap4generics/chap4hub + 全局 grep |
| `04_主线剧情全梳理与分析.md` | 主线六章逐 label 剧情详述、重置年表、谜团解析（扩写版，含 §5.1–5.10 暗线解析与附例） | script/ch2script/chap3/finalwarning/chap4/chap4part2 |
| `剧情全梳理与分析.md` | 本报告的会话编辑版（含附例：Abyss×温泉×Things That Hurt 事件链分析），与 04 同源但篇幅不同 | 同上 |
| `选择分析帖-全文翻译.md` | F95 论坛 CharlotteWiltshire26《选择》分析长文的全文翻译（外部社区分析，参考资料，非游戏源文） | — |
| `05_好叔叔与坏叔叔分支全对照.md` | 好/坏叔叔双路线全对照：amifingered/ami_virgin 双 flag 机制、Ami 线与跨角色（约 100 处引用）两版剧情、系统层惩罚（Maya 神社线门控）、整体画像 | 全库相关分支点 |
| `07_careCode场景解说精读.md` | 开发者 Selebus 的 8 篇 DVD 式场景解说（Prisoner/Stray Cat/Bluejay/Delirium/This Town Has Two Halves/Too Blind to See/Times New Roman/Il Cervo）逐篇精读，联系原事件本体定位与互证，横贯创作观与伏笔总线索 | 上级 `LIL/careCode/` 的 commentary label |

---

## 二、工作区全文件清单与覆盖索引（71 个 .rpy 全覆盖）

### 2.1 主线章节文件（6 个）→ 详见 `04_主线剧情全梳理与分析.md`

叙事顺序**与文件名不一致**（按 jump 衔接重建）：

| 顺序 | 文件 | 规模 | 内容 |
|---|---|---|---|
| 1 | `script.rpy` | 185 label / 4.1万行 | 第一章：日常筑基、创世神话（day102）、海滩/万圣节/trinity 特别篇、第一、二次重置、Ami 崩解与 USER 终端解谜 |
| 2 | `ch2script.rpy` | 131 label / 4.9万行 | 第二章：第一个冬天、宿舍战争 I、第三次重置（kindergartenclass 幸福课）、secondbeach、goodboy、christmastwo（Niki 信箱） |
| 3 | `chap3.rpy` | 110 label / 4万行 | 第三章：Ayane 觉醒、真名 Akira Arakawa 揭晓、宿舍战争 II/III、Ami 之死 |
| 4 | `finalwarning.rpy` | 67 label / 5千行 | 第六次重置：真名广播、纸片城、Maya 牺牲自我重置（**夹在第三与第四章之间，是第四章的门厅**） |
| 5 | `chap4.rpy` | 146 label / 4.3万行 | 第四章《春》：Sensei 夺回叙事权、卡带世界、童年闪回（Sekai 之死=循环起点）、christmalloween |
| 6 | `chap4part2.rpy` | 13 label / 5.3千行 | 宿舍战争 VI＋战后：最新进度，Kyoko 悬念（未完结） |

### 2.2 章节泛型与枢纽文件（3 个）→ 详见 `03_章节泛型与USER机制溯源.md`

| 文件 | 规模 | 内容 |
|---|---|---|
| `chap3generics.rpy` | 78 label | 74 个夏期泛型日常模板 ＋ 隐藏副本 "the great pareidolia mall"（Ami 镜像体 Amy、20 房间迷宫、全程禁回滚） |
| `chap4generics.rpy` | 65 label | 63 个春季泛型 ＋ alexisevent（故障角色喊 "WE EXIST OUTSIDE" 后被系统以 "lungrot" 抹除） |
| `chap4hub.rpy` | 17 label | **第四章玩法骨架**：三时段事件门按"星期+flag 链"投放；dellaslump（"The worm grows."）强制照顾 Ami 开场；37 女达标触发宿舍战争 VI |

### 2.3 角色事件文件（37 个）

每个文件 0.2–1.4MB，love/lust 双数值阶梯解锁。关键交叉点浓缩表：

| 角色组 | 角色（★=元叙事核心） |
|---|---|
| 核心层 ★★★★★ | **Ami**（USER1/voices/亲生女儿疑云/main heroine 之争）、**Maya**（重置执行者/三层同活/年龄[redacted]）、**Ayane**（Rooftop Squad/未来线 Himawari/GIRL MAKER）、**Makoto**（previous iteration/调查 Maya↔Akira） |
| 中坚层 ★★★★ | Kaori（USER2 离线/connor 开发者）、Yumi（knows how game works）、Yuki（Maya 伪造记录/original ten）、Tsuneyo（six 接入/cycle 将尽）、Niki（[uncle] 框架/Akira 揭露）、DormEvents（roomwithclocks/ticktock/trinity1 神话核心簇）、Dorm2（宿舍养成层） |
| 外围含要点 ★★★ | Nao（USER4/secret 21st/Sekai）、Nodoka（writer returns/Kyoko 线）、Wakana（Nothing is real/killed Maya）、Rika（Past-Maya/Real-Maya）、Miku/Haruka/Maki/Io/Futaba（creator 自指/not real）、Molly/Sara（prisoners to the protagonist）、Noriko/Osako/Otoha/Rin/Sana、Touka/Tsubasa/Tsukasa（Tsukioka 富家圈：barrier/failsafe）、Chika/Chinami/Imani/Karin/Kirin/Uta/Yasu |

### 2.4 系统与机制文件（19 个）→ 详见 `01_系统与机制文件精读.md`

| 文件 | 用途一句话 |
|---|---|
| `definitions.rpy` | 全局变量仓库：love/lust 数值、剧情 flag、USER 终端 flag 组（terminal23/ipaddress 等）、注册角色（含 `se`=Sekai、`you did it`、"众神"名单）、cp* 创世问卷 flag |
| `screens.rpy` | 全套 UI＋进度追踪：五条 reset 弧线留名、手机联系人直达 Trinity III |
| `Phone.rpy` / `PhoneStyles.rpy` | 手机系统：61 个"x"联系人直跳 Trinity III；删除线"{s}Maya{/s}"联系人唯一按钮 "There is something buried underneath your feet" |
| `replace.rpy` | **系统语言解码器**：伪语言 unnecessaryBS 把 hex/日/倒序/Zalgo 台词解码为红标英文（"am i okay"、"nothing falls but me"、"there is no god here. just noodles."） |
| `happytracker.rpy` | HAPPY SCENES 追踪器：23 项官方承认的真叙事层隐藏场景清单＋官方提示 |
| `mathhomework.rpy` | 名不符实的**电脑中枢**：完整作弊码表（wheredoesthetimego→"It's almost like real life now, isn't it?"） |
| `headpatcentral.rpy` | 摸头小游戏（5948 行）：藏最浓 meta 台词（Molly 谈 bug 与"这游戏有没有结局"、Tsuneyo 乌鸦劝玩家关游戏） |
| `jukebox.rpy` | 音乐室：曲名表本身是叙事文本 |
| `newchecker.rpy` / `checker.rpy` | 新旧版进度校验（全事件完成度核查） |
| `unlockables.rpy` | 解锁清单：服装/动画/短信图鉴及条件 |
| `options.rpy` / `gui.rpy` / `setup.rpy` / `autopatch.rpy` | 全局配置（版本号 0.60.0 所在）/GUI 变量/和谐版敏感词表/旧存档补丁 |
| `dlcmenu.rpy` / `carepackages.rpy` / `profile_outfits.rpy` | DLC 商店/DLC 框架（问卷正文实为 definitions cp* flag＋ch2script 文本）/菜单立绘换装 |

### 2.5 特殊内容与迷你游戏文件（5 个）→ 详见 `02_特殊内容与迷你游戏文件精读.md`

| 文件 | 内容一句话 |
|---|---|
| `flowers.rpy` | Build-A-Maya：赛道之神 Horseface Taki 命 Akira Arakawa 收集 6 块 Maya 碎片；结局宣布本次 reset "irreversible"；Sensei 吐露"幸好拼的不是 Sekai——她死时碎片更多" |
| `senseiquest.rpy` | 游戏中的游戏《Sensei-Quest》：Boss 战禁用回滚；杀死开发者 Fred 解锁童年闪回（Sekai 怀孕→与 Nozomu 双亡=循环起点） |
| `nudes.rpy` | 44 张手机图片解锁（Kaori 为动物科普图） |
| `animatedscenes.rpy` | 64 个 WebM 动画场景；bonus 自标"非正典、只为搞钱" |
| `inappropriatecontent.rpy` | 成人内容主文件（124 label/3.4万行）：six 的 hex 名、ticktockx 直言 "Nothing is real. This is just a game"、Maya 被明写"能把世界 reset 回万圣节"、8 处输入 "Selebus" 触发的开发者彩蛋 |

### 2.6 目录与其他文件

| 路径 | 说明 |
|---|---|
| `images/` | CG/背景/缩略图资源（BGs 含 dorm2frinodokagone、dormmonyumigone 等"缺席状态"背景，本身是剧情证据）；webp 需转码查看 |
| ~~`_tools/digest_events.py`、`_tmp_match/`~~ | 中间产物区已删除：digest 文本与工具脚本随整理清理，正式成果并入本区 |
| `.workbuddy/memory/` | 跨会话工作日志（方法与进度记录） |
| `.git/`、`.gitignore`、根目录 `README.md` | git 双仓库基础设施（公开文档仓＋私有全量快照仓）；根目录已清理，ZCODE 产出内容全部移入本生产区 |
| 本区 `剧情全梳理与分析.md` | 04 的会话编辑版（含附例：Abyss×温泉×Things That Hurt 事件链分析），与 04 同源但篇幅不同 |
| 本区 `选择分析帖-全文翻译.md` | F95 论坛 CharlotteWiltshire26"选择"分析长文的全文翻译（外部社区分析，参考资料，非游戏源文） |
| 上级 `LIL/` 目录 | 游戏本体 0.55、汉化补丁 `tl/`、重复反编译副本 `lilCode/`（与分析区逐一相同）、**未读的活动剧情 `careCode/`**（见下方备注） |

> **§2.6 备注——`careCode/` 未读活动剧情清单**（位于上级 `LIL/` 目录，工作区之外）：`fanfest25.rpy`（196KB / 11 label，2025 周年庆）、`fanfest26.rpy`（212KB / 21 label，2026 周年庆）、`hugfest25.rpy`（124KB，拥抱节）、`nov2022–aug2023` 月度礼包 ×8（16–36KB each，分析区 `carepackages.rpy` 仅为其 DLC 框架）、`nib/script.rpy`（60KB，礼包内附独立小游戏：Yuu/Reina/Saki/ikaS 等非 LIL 角色）。分析区内仅有 fanfest 的零星引用（animatedscenes/unlockables），**主体剧情从未精读**。另：`tl/`（74 个 rpy 汉化补丁）、`lilCode/`（与分析区二进制相同的副本）、两份 PDF（Uta 排名日记、五周年 Selebus 问答，记忆已登记）——均非待读源文。

---

## 三、全作内容一页总结

### 3.1 三层世界观

```
元层（玩家层）  旁白对屏幕喊话 / USER1–4 争终端23 / "Nothing is real" / 开发者 Selebus 自指
循环层（机制层） Maya 执行 reset / 记忆跨循环残留 / USER 备份 / six·te·sev 世界维护者 / USER3≈第三神（关切之神）
表层（恋爱层）  Kumon-mi 小城 / 太空战争征召 99% 男性 / 37 名可攻略角色 / love·lust 数值
```

### 3.2 主线六阶段（重置时间线）

1. **第一章**：失忆教师日常筑基 → 玩家经 trinity3 获得真实 IP，在终端输入 TERMINAL 23→IP→PORT 1024→USER2→密码 **Boobies123**，**亲手授权第二次重置**（玩家行使管理员级操作，凭据是 Sensei 的万能密码 Boobies123；USER2 自身无重置权限，玩家≠USER2——dormwar14 重置确认框为决定性证据，见 03 §2.5/§2.6）。
2. **第二章**：第一个冬天；第三次重置含 kindergartenclass（幼儿园幸福课，Sensei 童年创伤核心）与 goodboy（加害者逻辑镜像）。
3. **第三章**：Ayane 觉醒、真名 **Akira Arakawa** 广播、Ami 之死。
4. **第六次重置（finalwarning）**：纸片城密室逃脱；Maya 牺牲自我执行重置（记忆清零，只剩对 Akira 的爱）。
5. **第四章《春》**：Sensei 出关夺回叙事权；Sensei-Quest 杀 Fred 解锁童年闪回——少年 Akira 与嫂子 Sekai 的禁忌关系、Sekai 怀孕、与兄 Nozomu 双亡＝**reset 循环的情感起点**；USER2 在 halloweenfive13/14 被 3.4×10^15 未授权连接压垮、"USER2 has been removed!"。
6. **最新进度（chap4part2）**：宿舍战争 VI 战后；Kyoko（Nodoka 之母）暗线浮出。**未完结。**

### 3.3 人物格局速写

- **Akira Arakawa（Sensei）**：顶替者（flowers/senseiquest 旁白直证"接管"原 Sensei 身份）、创伤幸存者（幸福课＋Sekai 事件）、待清算者。
- **Maya**：重置执行者、被囚的锚、"main heroine of Lessons in Love. I do the time thing"（Karin 线显像）；Past-Maya/Real-Maya 双重结构（Rika 线）。
- **Ami**：疑似 Akira 与 Sekai 亲生女儿；从甜妹侄女到黑化"收藏家"；USER1。
- **觉醒者网络**：Makoto（最明确的跨迭代记忆者）、Ayane、Yumi（Rooftop Apocalypse Squad）＋ Kaori/Yuki/Tsuneyo/Nao 等。
- **元层存在**：six/te/sev（世界维护者）、Himawari/Shi（天界管理员双化身）、Horseface Taki、众神（Halftone, God of Save Slots 等）、开发者（Selebus/Fred/Connor）。

### 3.4 USER 机制（本次溯源定论）

| 实例 | 硬事实（附行号） | 身份判定 |
|---|---|---|
| USER1 | 仅两处：amidate50p4 结尾 "USER1 HAS SUCCESSFULLY LOGGED IN"（AmiEvents.rpy:5170，倒开公交到家一刻）；day220 终端查询 OFFLINE（script.rpy:36689-36690） | **未证实**。出场唯一绑定 Ami 深夜约会，"与 Ami 相关"为最强假说；旧表述"Ami 线玩家实例"证据不足，废弃 |
| USER2 | 全库 33 处（8 文件）。自称守护者："I HAVE WATCHED YOU GROW… I AM HERE TO PROTECT YOU… I CAN GUIDE YOUR VISION"（ch2script.rpy:20100-20115）；两度 LACKS THE PERMISSIONS NECESSARY TO RESET SYSTEM（script.rpy:30788/30793）；halloween4 改写关键事件防程序终止、世界只能部分回退（29974-29977）；共享屏幕伴随 Sensei、屋顶即失联（ch2script.rpy:21010-21011）；第四章杀毒失败→"UNABLE TO DETACH ITSELF FROM 'HOST BODY'"→感染→"USER2 has been removed!"（chap4.rpy:20496-20544） | **守护者型运营账户，≠玩家**。决定性证据：dormwar14 它接管终端后弹 "WOULD YOU LIKE TO PROCEED WITH FACTORY RESET?"，戏内 Maya 连喊 No、系统却注册 "YOU HAVE SELECTED 'Yes'"（ch2script.rpy:16522-16531）——应答者是屏幕外的玩家；day220 亦须玩家供密码才获接管权（script.rpy:36732-36743）。HOST BODY 用法证明它与某具躯体绑定（最合指向 Sensei 之躯，原文未点名） |
| USER3 | 仅两处：trinity3 结尾接管 Terminal 23，小写温柔腔向屏幕外确认 "can you see this?"→"i'm so glad / i was very concerned"（script.rpy:34092-34100）；day220 查询被拒 CONNECTION HAS BEEN REJECTED（36694-36698） | 独立存在；**疑同 pareidolia 但无直证（旧表误写为等号，已降级）**。更强内证：day220 创世神话预告"第三神 overcame with concern"（script.rpy:36140-36142）正接住 "i was very concerned"——USER3≈**第三神（关切之神）**比 =pareidolia 更有文本支撑 |
| USER4 | 三处：RESERVED ADDRESS（script.rpy:36701）；Nao 崩溃时 TEMPLATE9 由其备份恢复（NaoEvents.rpy:2454-2460）；ch4 杀毒日志 "A NEW ADMINISTRATIVE ACCOUNT HAS BEEN DETECTED / IF YOU TRUST 'USER4' PLEASE DISREGARD THIS MESSAGE"（chap4.rpy:20502-20503） | 世界外的备份/后门通道：木马与新管理员账户的最大嫌疑源；保留地址，玩家无法连接 |
| （玩家） | 不占编号：系统称玩家 FREE TRIAL USER（ch2script.rpy:46982）；持 Sensei 万能密码 Boobies123（script.rpy:35598-35605 自述设置、36735 验证通过）；工厂重置以其选择落地（ch2script.rpy:16522-16531） | 玩家是握有 Sensei 凭据的体外操作者——"占有了原主身份的人，自然持有其一切权限"；**管理员层真身未揭示**（候选：电线之神/开发者/原主） |
| USER5 | **不存在**（全局 0 处） | — |

> **2026-08-24 勘误说明**：本表曾写"USER2=主玩家""USER3=pareidolia"，经全库重查均无文本直证，已按上方硬事实改写。详见 `03_章节泛型与USER机制溯源.md` §2.4/§2.6。

---

## 四、本次补读的新发现与勘误（相对旧报告的增量）

1. **版本**：0.55 → **0.60.0**（options.rpy:27）。
2. **叙述声音勘误**：`s` = **Sensei**、`se` = **Sekai**（definitions.rpy:2322/2348）。此前把 `s` 误作 Sekai；"USER2 stuff" 质问出自 Sensei 之口。
3. **pareidolia 与 USER3 的关系修正**：旧结论"pareidolia=USER3 证据链闭合"**降级**——全库无任何文本把账号 USER3 与 pareidolia 直接画等号（Sana 自报家门与 gpm 商场名证明的是 pareidolia 实体本身，不是账号）。硬事实仅两条：trinity3 结尾 USER3 接管终端23、day220 拒绝连接；与小写语体的 pareidolia 仅文风/时序呼应。更硬的内证是 day220 创世神话的"第三神 overcame with concern"（script.rpy:36140-36142）正接住 USER3 的 "i was very concerned"——USER3≈第三神为强假说，=pareidolia 为弱假说。
4. **第二次重置的授权结构**：解谜链条（终端/IP/端口/用户名/密码）逐行定位至 script.rpy:36598–36750；IP 答案早在 trinity3 由旁白抄给玩家（33886–33888）；密码 Boobies123 是 Sensei 醒来后自设的万能密码（35598-35605）——世界系统的管理凭据与其个人身份绑定。
5. **USER2 退场**：chap4.rpy:20494–20544 被海量未授权连接压垮后移除；USER4 涉嫌木马源头。注意 "UNABLE TO DETACH ITSELF FROM 'HOST BODY'" 一句证明 USER2 与某具躯体绑定（最合指向 Sensei 之躯），且其行为模式（改写关键事件防程序终止）最接近"读档救场"，但文本同时明确它缺乏重置权限、须玩家授权——**玩家≠USER2**（dormwar14 工厂重置确认：Maya 喊 No、玩家选 Yes、系统照执行，ch2script.rpy:16522-16531）。
6. **replace.rpy 解码层**：此前未知的"系统语言解码器"，把 hex/日/倒序/Zalgo 台词还原为红标英文，是跨文件 hex 母题（"am i okay" 等）的机制解释。
7. **carepackages 勘误**：旧报告所称"月度礼包问卷"正文实为 definitions.rpy cp* flag＋ch2script.rpy:44103 起文本；carepackages.rpy 本体只是 DLC 框架。
8. **chap4hub 骨架**：第四章"三时段事件门＋dellaslump 强制开场＋37 女达标巨门"的玩法结构首次完整梳理。
9. **flowers/senseiquest 身份证据**：两处旁白（"我不是她真正的舅舅"、"真正的 Sensei、我接管之前"）与神明直呼全名构成互证，为"主角顶替原 Sensei"提供最直白源文。

---

## 五、方法论与信源分级

- **流程**：`_tools/digest_events.py` 生成带源行号摘要 → label 总表 → 定向精读 → 六部分结构落盘 → 跨文件交叉验证（grep 全局复核关键引文）。
- **引文格式**：单文件报告 `[N]`＝源文件行号；跨文件报告 `文件名.rpy:[N]`。所有关键断言可回查原文。
- **信源分级**：① 系统播报/终端文本（最高，世界机制直证）；② 角色清醒台词；③ 角色醉酒/故障/梦境台词；④ 旁白与元层喊话（需判定双声归属——Sensei `s` / Sekai `se` / pareidolia 无框旁白，判据见 03b §〇）；⑤ 戏内传闻与回忆（最弱，可能有误记）。
- **已知局限**：外围角色（批次 C/D）采用"交叉点浓缩"策略，完整养成链未逐事件线性复述；`inappropriatecontent.rpy` 按结构归类＋元叙事关键词定向精读，未逐行。
