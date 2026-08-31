# Rin 事件线全析

> 源文件：`游戏文本/RinEvents.rpy`（9871 行：`cafe` 路由 + `callrinmorning` / `callrinafternoon` / `callrinnight` + `cafe*` 系列 + `rindate50` / `rindorm55` 系列 + `rinspecial55` + `rinspring1`—`rinspring9` + `dormwarsfiverin1`）｜跨文件补充：`游戏文本/DormEvents.rpy` 的 `rindorm45` 与 `rindorm50special`。
> 定位：Rin 是全作里自我伤害被写得最实的角色，也是把"想要"与"自毁"明确绑到同一套止痛机制上的那一个。她与 Sensei 的关系到很晚才越过接吻，而"我爱你"却很早就由她说出口。
> 阅读提示：本文按 love 线主轴逐事件推进；涉及性内容的部分只记录源文对白与叙述中明确交代的事实。所有锚点均为 label 名。

## 一、角色基本盘

`rinspring2` 开头的叙述给了 Rin 一份相当完整的自我定位：她是"本地有名的双性恋"；"不如 Chika Chosokabe 那么外向成功"，"也没有室友 Futaba Fukuyama 那种日常不加掩饰的善意"；真正把她和她们区分开的，是一枚从商场折扣店买来的骷髅形发夹，她之后用它配过许多种发型。开学第一天她就占了教室后排那个"刻板意义上的主角位"，并接受自己"大体上不出众"——"如果要平庸，她就要做自己能做的最了不起的平庸之人"。但同一段叙述紧接着限定：**这种状态只在短时间里成立，"被放到关注中心不用多久，她就开始崩"。**

几个可在源文核实的固定属性：

- **职业**：Koi Cafe 的店员，老板是 Haruka。到 `rinspring4` 时她已经升成 supervisor，还专门要求别人别再叫她"穷 Rin"，改叫"财务稳定的 Rin"；`cafe50` 里她把 Koi Cafe 称作自己迟早要"继承的家族生意"，并把 Haruka 算作自己的"工作妈妈"。
- **音乐**：轻音部成员、会弹吉他。`rinspecial55` 里 Rin 用"我们在轻音部、我们玩音乐"来解释 Otoha 的比喻；`cafe35` 里她追着街头弹唱的 Otoha 跑下整段台阶，开口就是"也许我们可以一起玩点什么——我是说吉他"。
- **家庭**：由两位女性收养，一位是 Rika，另一位是 Rie。她对 Sara 数过这笔账——两个养母，加上 Sara 是三个，算上生母是四个，再把 Haruka 这个"工作妈妈"算进来就是五个（`rinspring2`）；生母"临床意义上的疯子"，生父"是一个存在过的人类"，是她"人生里最大的问号"。`rindorm55p2` 里她直接自称"严格来说我是个孤儿"。
- **自我伤害**：`cafe30` 里 Rin 说"我没法说丢就丢掉我已经有了好些年的习惯"，Sensei 的内独白被这三个字卡住——"几年？"；`rindorm50special` 里这个习惯第一次被别人当场撞破。

她的情感结构围绕几个人展开，且彼此的关系性质完全不同：

- **Sensei**：`rindorm45` 里她口头承认"还有，我可能喜欢你"；`rinspring4` 里她对 Futaba 承认自己"停不下来地想他"；`rinspring5` 里她一个人在宿舍自慰、编辑并发出挑逗短信。她给 Sensei 的定位是"homie"——`dormwarsfiverin1` 里她明说 homie"比朋友高四级"。
- **Chika**：`cafe15` 里她承认"我大概有整整两年没有停止想过她"，还存了一整个文件夹的 Instagram 照片；`rinspecial55` 里她对 Otoha 说"我确实爱过她……我愿意为她做任何事"。
- **Otoha**：`cafe35` 在街头结识，`cafe50` 时已经是女友，`rinspring1` 时两人已分手。分手后 Rin 说"我大概永远也走不出初恋被硬生生打碎这件事"（`rinspring1`）。
- **Futaba**：室友，`rinspring3` 里 Rin 说两人"practically sisters"（形同姐妹）。`rinspring4` 里 Rin 把 Futaba 称作"最好的朋友"，同时把 Sensei 称作"带引号的最好的朋友"——同一段话里出现了两个"最"。
- **Molly**：`cafe45` 的玩笑对白里，Rin 说"人永远不会忘记自己的初吻"，接的就是 Molly；`cafe35` 里也提到她帮 Molly 搬宿舍。
- **Sana**：`rinspring1` 里 Rin 说"我吻了 Sana"，时间是圣诞派对。
- **Sara**：Sana 的母亲、酒吧老板。`rinspring2` 结束时系统提示"{i}Rin and Sara are now friends!{/i}"。

## 二、love 线逐事件脉络

### 1. cafe 系列与日常电话事件

`cafe` 是个纯路由 label：按 `rin_love` 与各章节 flag 依次判定，命中哪个就跳哪个——`firsttimecafe`（≥0）、`cafesugar`（≥5）、`cafe10`（≥10）、`cafe15`（≥15 且已完成两个 dorm 事件）、`cafe20`（≥20）、`cafe25`（≥25）、`cafe30`（≥30）、`cafe35`（≥35）、`cafe40`（≥40）、`cafe45`（≥45）、`cafe50`（≥50）；`rinsad == True` 时一律改跳 `rincafegone`。这保证了 Rin 的主线是严格按好感度单线程推进的。

三个电话事件是低好感期的日常接口：

- `callrinmorning`：只要咖啡馆没关门，Sensei 就只会在心里说"Rin 应该在上班，去咖啡馆大概能见到她"，拨号分支根本走不到。
- `callrinafternoon`：先要 `dormwar17 == True`（否则 Sensei 会说"她还不知道我有她号码"）；`rinphoneblock`、`rinsad`、第三章激活三种情况下都无人接听。正常分支里 Rin 接起来就是一句"Greetings and salutations, Sensei!"，被问在干什么时答 **"Sad girl stuff."** ——"Coffee and loud music about girls."，然后把 Sensei 叫去另一家咖啡馆，结尾 `rin_love += 1`。
  这句台词的叙事功能是把情绪基线提前埋下：紧接着的叙述写得很明白——"尽管自称 sad girl，她今天看起来相当好"，但 Sensei 补了一句，"真正的绝望随时可能袭来，而且更多时候它潜伏在背景里，等着把她这样的人整个吞掉"。而那一晚"没有人被吞掉，我们玩得很开心"。**玩家在早期就被明确告知 Rin 有低落状态，但此时还不知道深度。**
- `callrinnight`：若 `rinbetrayed == False`、`rindorm50special == True` 且 `rindate50 == False`，直接跳 `rindate50`——也就是说割伤事件之后，夜里打电话是触发下一节点的唯一入口。否则正常分支是 Rin 让 Sensei 自己走到宿舍去（"Just some LOSER!"，"你知道在哪儿能找到我"）。

早期咖啡馆日常本身（`firsttimecafe` / `chosedrink` / `cafesugar` / `cafe2to4` / `cafe6to9`）建立的是一段固定格式：Sensei 点单，Rin 把单子扔掉，随手调一杯"特调"塞给他，理由是拿他当实验鼠、好说服经理把配方上菜单。这套玩笑在 `cafesugar` 里被她自己总结成一句能被当作全作注脚的话——"我做的每一样东西里都有爱给，Sensei"，"爱尝起来像香草"。

### 2. 自我伤害的揭露与"骂我"请求

真正的揭露点在 **`rindorm50special`**（`DormEvents.rpy`，不在 RinEvents 里）。Molly 敲开 Rin 的门，撞见她用一把新的美工刀把手臂割得很深。Sensei 压住她的手腕止血，打电话把 Futaba 从餐厅叫回宿舍。这段里 Rin 说的话构成了她自述的核心：

- "这不是蠢……只是有点自毁。"
- "这是我能控制的东西。当我的其他部分被剥光时，我还能对它拥有权力。"
- 止血时她才反应过来自己在流多少血，随即崩溃地反复追问"What am I gonna tell Otoha?"，并连说数遍 "I have to be wanted. I need her to want me. I can't lose her now."
- 她承诺"I won't cut myself anymore. I'll be happier."，然后立刻反问"我什么都有了，我到底为什么会难过？"，最后是那句"Why can't I fucking feel anything?!" 和"Sensei... Why can't I feel anything?"

事件以 `$ rinsad = True` 收尾。

紧随其后的是 **`rindate50`**。Rin 主动打电话约 Sensei 去 Kumon-mi 一个偏僻地段见面，明确要求"这次别带上 Futaba"、"我只想要是你"（"I kind of just want it to be you"），并给出理由：这件事她跟 Otoha 说不了，Futaba 已经担心坏了。见面后她给出伤口的最新状态——"我得穿毛衣遮住所有地方，但袖子会粘在正在结痂的伤口上；每次手臂动快一点，痂就被撕开、重新裂开，就是 rinse-repeat, rinse-repeat"，并且"割的时候我几乎感觉不到，最疼的永远是之后的几天"。

然后是那组关键对话。源文里的顺序是：

1. Rin 说"Futaba 很好，但她在这种事上太感性了。你会直接给我实话"——**"Call me a fucking idiot, Sensei. Do it."**
2. Sensei **照做了**："Okay. You're a fucking idiot."
3. Rin 接着要他"叫我去揍这该死的抑郁那张蠢脸"，Sensei 也照做了。
4. Rin 说"Now tell me you love me!"，Sensei 回 **"No."**
5. Rin 说："Aww. Mean."，然后自己说 **"I love you."**

所以准确的结构是：**Sensei 在"否定"上完全配合她，收住的只有"我爱你"这一句。** 她要的从来不是惩罚被外包，而是"不含温柔的直球"——她把这句话的前提说得很清楚：Futaba 太感性，只有 Sensei 会给她说实话。

这一趟她真正的诉求有两个：一是"教我怎么控制住自己"，因为她怕自己在 Otoha 准备好之前越界；二是她已经把割伤瞒着 Otoha——"我已经因为对她藏着 cutting 而离搞砸更近一步了"。事件结尾 `rin_love += 1`、`rinsad = False`。

### 3. Sara 线：rinspring2

这段的人设需要先说清两点：**Sara 不是同龄朋友，她是 Sana 的母亲、一家酒吧的老板**；**这段关系也不是无张力的纯友谊样本，只是没有越界**。

事件起因是 Haruka 让 Rin 陪"一位朋友"去取一台新的咖啡机，而机器其实已经被一个戴紫帽子的人修好了。来的人是 Sara。核心秘密是 Sara 在 Haruka 面前装会开车——"她觉得我会开车，所以觉得我更酷"——实际上她这辈子只摸过几次方向盘，"每一次都极其恐怖"，因此她自己是打车来的，还打算让车停在一条街之外再走过去，好让 Haruka 不起疑。Rin 也有对称的小谎：宿舍里放着滑板，但她根本不会 ollie。

两人在公园长椅上等车时的对话，把这段关系的性质钉死了：

- 叙述直接点明两人的共同点："两个人都不会 ollie。两个人都不会开车。连她们抚摸自己时被幻想包裹的脑子都是相似的。" 并且补了一句：这种事不该在第一次见面就聊，"得等到第三、第四、第五次"。
- Rin 说漏嘴自己吻过 Sana，先否认、再承认、再改口，说是圣诞派对上的"转瓶游戏"事故，"她只是今年的众多'受害者'之一"，并明确说对 Sana 没有那种感情。Sara 半开玩笑地回："我忍不住对 Sana 和她的朋友们心软，尤其是那些在圣诞派对上继续亲下去、可能会从朋友变成'不只是朋友'的朋友。"
- Rin 摊开自己的家庭：被两个女人收养，"我很爱我的父母"，生母"临床意义上的疯子"，生父是她"人生里最大的问号"，但她不想去翻石头找答案。
- Sara 摊开自己的过去：高一的时候和自己的老师在一起，对方年长很多，"那时候我特别缺关注，所以年龄差没所谓"；后来独自把 Sana 带大，"我不知道自己是怎么撑过来的"。
- 结尾 Sara 说："如果你的另外几个好妈妈都忙，而你需要第四个妈妈来不小心向你套出更多秘密……你知道我的酒吧在哪儿。" 系统提示"{i}Rin and Sara are now friends!{/i}"，随后画面切到"几英里外有人提前结束了这一晚"——Sensei 倒在床上。

Rin 自己也在这段里说清了她为什么需要这样的关系："我脑子里塞满了说出来就能毁掉基本上一切的事情，已经到了每说一句话都要在脑子里过五遍的地步。我大概很快就得开始记笔记了，我快记不住谁知道什么了。" 所以 Sara 的价值不是"Rin 反过来照顾对方"，而是**多出一个不需要她演、也不会被她一句话毁掉的大人**。

### 4. rinspring 系列

**`rinspring1`** 不是两人独处，而是四人堵在学校侧门：Rin、Molly、Sana、Futaba 分头守株待兔，把刚从 Ami 事件里脱身的 Sensei 拖去咖啡馆。信息点密集：Rin 与 Otoha 已分手；Rin 说"我吻了 Sana"，并补一句"奇怪的是那对我没起多大作用，所以要么我排除了 exhibitionist 这条，要么我就是更把 Sana 当朋友而不是性练习对象"（Sana 当场说"谢了，Rin"）；Rin 描述自己的抑郁发作会"把整整几天甚至几周屏蔽掉"，"唯一能把我拉出来的只有时间"，由此陷入一个悖论——"你需要靠时间来愈合，可你又完全失去了对时间的感知"。结尾四人好感各 +10，跳 `sanaspring1`。

**`rinspring3`** 里那段"名单"盘的是 **Sensei 的名单，不是 Rin 的**——Sensei 问的原话是 "which girls do you know about?"。Rin 已经确知的：Chika、Futaba（她说"我们简直是姐妹，她自己会讲，只是没 Chika 讲得细"）、Sana、Nodoka、Haruka；她"mega 震惊"他居然没有 Ayane，并猜了 Makoto。她追问 Noriko 与 Kirin，Sensei 答 **"Noriko, no. Kirin, yes."**；Rin 惊讶的是 Noriko 居然是"没有"，理由是"她为你神魂颠倒啊老兄"，而 Sensei 的解释恰恰就是"就因为如此"——"Noriko 聪明又有干劲，把她拖进我正在拖所有人的那片流沙里我觉得不太对"。**说"Noriko 没有"的是 Sensei，不是 Rin。**

同段其他要点：Rin 承认自己曾在 Ayane 家病房的帘子后自慰，而 Sensei 就在帘子另一侧和 Sana 发生关系；她承认把 Chika 的事泄露给过 Otoha 一次，但从没漏给 Chika，"我不想你最后死在哪条沟里"；她说"我还是支持 Chika"；Sensei 说"不久之前我们还都在争 Chika 的芳心"，Rin 接"我当时试图让她看我一眼惨败，而你的手指已经在她里面了"。她也把两人的现状说清楚了——"我现在单身，也没有在追谁"，"如果哪天我们同时做了同一个决定，也许我们终于就不用再管住自己的手了"。

**`rinspring4`** 是宿舍管道爆裂后的澡堂戏。Rin 把 Futaba 拉到一边，被 Futaba 直接点破："所以我们要不要聊聊你现在爱上 Sensei 的事？"Rin 的回应是"奇怪的是，你们所有人都比我自己先发现"，并承认"我确实停不下来地想他"、"我的振动棒快炸了"。但她拒绝行动，理由是"我不想毁掉我和他现有的关系，说实话那是我身上发生过的最好的事情之一"。Futaba 的立场是"把感觉付诸行动，好过为了朋友藏着掖着"，并提醒她最该怕的是 Chika。

**`rinspring5`** 是 Rin 一个人在宿舍的那晚。她试图用一堆美女图片和视频把自己"掰回去"，失败，然后开始编辑发给 Sensei 的短信——试过"Greetings...homie. Would you like...to fuck?"、"Give me...the wiener."，最后发出去的是包括"摩西分红海"和"一百次口交兑换券"在内的十几段。她以为 Sensei 回信说要来，开门却是母亲 Rika——Rika 手里拿的正是 Sensei 落在她家的手机。Rika 当着她的面念出短信，没收手机（`rinphoneblock = True`）。Rin 崩溃："I'm confused! I'm scared! I'm horny! And I want to die, but I don't! ... We already know medication doesn't work!"；Rika 反问"你以为我是来罚你的吗"。Chika 听到吵闹推门进来，事件直接切入 `rinspring6`。

**`rinspring6`**：先是 Rika 宣布 Rin"无限期禁足"，收走手机，说要去告诉 Rie。Rin 向 Chika 承认"我想我是对 Sensei 有感觉"，并交代自己发了十几段短信和一段自慰视频（"而且我他妈的妈妈还看了！"）。Chika 没有生气，追问"如果他今晚来了你会不会做"，Rin 答"会"。随后 Chika 主动为 Rin 口交（自称第一次），并把这一过程里的对话引向那条协议；Rin 提出回报时被拒（"我自己去隔壁解决就行"），两人接着约定"无论发生什么，都承诺永远在一起，这样就永远不必说再见"。事件随后被 `DEVIATION DETECTED` / `THIS IS NO NIGHT TO REMEMBER` 的字卡切断。

**`rinspring7`**：Rin 拿回手机，约 Sensei 去新开的商场。两人一路打闹，Rin 得知 Sensei 和她母亲 Rika 发生过关系（不止一次，后面几次 Imani 也在场），她的反应不是发怒，而是"Chika 那件事其实比这个糟糕多了"。她也在这里说了自己和 Chika"正在闹别扭（spat）"，并拒绝了让 Sensei 出面调解——"我不该靠别人来解决我的问题"。

**`rinspring8`**：Rin 带 Sensei 去 Uta 与 Chika 打工的女仆咖啡厅，点名要 Chika 服务，逼她正面对话。Chika 后台崩溃："她故意来惹我！""这身制服让我觉得像被当成玩具"；出来点单后两人互相刺——Rin 说"我要你每分每秒都为这件事痛苦，因为从 Christmalloween 起我一直在这么过"，Chika 回"那你是白跑一趟，我本来就已经在痛苦了"。Chika 端上"非常快乐樱桃莓王子公主芭菲"。

**`rinspring9`**：Rin 还没动那份芭菲，意识就断裂了——Chika 与 Sensei 的脸扭曲成反复命令她"Eat."的东西，说"你从来就不是 Rin"、"你的思想不属于你自己"；接着是机械广播"祝贺你……请享受为你量身定制的一个免费世界"；再接着是会说话的自慰杯反复说"来。拿走我。喂饱我"，并说"你只感受得到一半的东西"；最后她在房间角落看见一个"也是我"的盲眼少女（"HOPE 拿走了我的眼睛"、"这不是梦……这是结果"），以及用十六进制说话的 Maya（解码为"你不该在这里"、"这是怎么发生的"、"我看见了"、"看来我们又失败了"）。她回过神时，Chika 正重复她之前的台词。结尾 Sensei 送她回宿舍，`rinphoneblock = False`。

**`dormwarsfiverin1`**：Rin 把染过的头发染回原本的颜色，说"我厌倦了不停改变，终于准备好对一件事定下来——当你的 homie"，并说"这是我为你染的"。这是她在"约会战"里的场次，但她直说自己不在乎输赢，"我只是想和你像从前那样待着"。她解释原因：和 Chika 在一起时她藏起了自己的宅属性，"我花了好几年在 Chika 面前藏起我宅的那一面，可我根本不必那么做"；和 Otoha 在一起时"连 cutting 这种极私密的事都没法跟她说，因为感觉不对"；"唯独在你面前，这种事从来没发生过。我不需要改变，也不需要变成某个特定的人。我可以只是 Rin。" 两人在她房间接吻，她随即要求"慢慢来"——"我想让它有一天能让我们回头看时，发现我们是自然地从朋友变成恋人的"，Sensei 指出那在法律上叫 grooming。事件以两人接吻、`rin_love += 10` 结束。

### 5. Chika 协议与欲望对象的转移

出处是 **`rinspring6`，不是"Chika 与 Sensei 的性场景"**。现场只有 Chika 和 Rin 两个人，Sensei 不在场；Chika 是在为 Rin 口交的过程中说出这句协议的：

> "他可以……拥有任何他想要的女孩……只要他爱她们……只要他……最爱的是……我……"
> "那我也可以做同样的事，对吧？"
> "所以我才说我变了，我成长了。而且你知道吗，Rin？我现在更快乐了……因为这样我就能同时拥有你们两个。"

Rin 在这一过程中的内心方向，源文写得非常明确：

- "关于**他**的幻想消失了。但就在刚才她还拼命想把它们赶走，现在她却在拼命想把它们召回来——因为'这'不知怎么感觉更糟。感觉不对。"
- 她想抓住 Chika 的头、把手指插进她头发里，"但她的手臂动不了。什么都没用。"
- "而就在那一刻，她意识到自己从来没有真正爱过 Otoha。只有 Chika 能让她有这种感觉。Chika，还有某个不在场、不该来这里的人——某个错的、年长的、不忠的、好色的、能随口就列出一堆负面形容词的人。"

所以 **`rinspring6` 不是"欲望对象从 Chika 转向 Sensei"的位移发生点**——这个转向在 `rinspring4`（对 Futaba 承认）与 `rinspring5`（独自自慰、发出挑逗短信）里已经完成了。`rinspring6` 写的是转向完成之后的代价：**当 Chika 真的把 Rin 曾经想要的东西给了她，Rin 发现自己已经在别处了，于是这件事本身变成了一件"错"的事。**

"Chika 回避 Rin"的时间线同样要按源文排：

1. `cafe30`：在海边那晚之后，Rin 哭了一整夜、天亮前独自离开，之后一直在躲 Chika——Sensei 问的是"Chika 到底对你说了什么，让你这么想躲她"，Rin 答"她其实什么都没说，但我从她眼神里看出来了，永远不可能"。
2. `rinspecial55`：Chika 和 Rika 坐在屋里看着窗外的 Rin 与 Otoha，Chika 说"我希望她们不是在分手，我喜欢那两个人在一起"、"Rin 已经受够了，我真的很讨厌看她那样"，末了补一句"她运气真的很差"。
3. `rinspring7`：Rin 说两人正在"闹别扭"，且"Chika 那件事最近完全是另一回事了，我现在有点累"。
4. `rinspring8` / `rinspring9`：主动切断联系的是 Chika——她在后台说"我告诉过她离我远点"，Rin 则用女仆咖啡厅这一招逼她出来正面对话，并对 Sensei 说"我能修好她"。

也就是说，**是 `rinspring6` 之后 Chika 先退开、Rin 才追上去**，而不是 Rin 一早察觉 Chika 在躲她、到最后才明白原因。

### 6. Haruka 咬合点：cafe20

这里最容易记反的一点是：**给号码的是 Haruka，不是 Sensei**——是 Haruka 主动把号码写给 Sensei，好让他去探望 Rin 之后回个话。

`cafe20` 的本体是 Rin 的一次崩塌：她看到 Sensei 进门后不是打招呼，而是转过身去假装擦东西。被反复要求转身后，露出的脸"像是几个星期没睡"，满头汗、眼睛肿到睁不开，自述"大概一周没洗澡"，连上一次睡觉是三天前、四天前还是一周前都说不清。Haruka 直接让她回家、把她从排班表上撤下来；Sensei 拦住她的说辞："别再说你会没事了，你根本不知道那是不是真的。"

Haruka 随后把话挑明："她从你开始来咖啡馆之后就一直念叨你，每次你一来她就兴奋得事后还要讲上一个小时——我从没见过她对谁这样，连她暗恋的那个金发女孩都没有。" 她也承认自己知道 Rin 喜欢 Chika。然后她请 Sensei 去看望 Rin 时通知她一声，并特意去找了支笔，把号码写在餐巾纸背面——"每写一个数字都有轻微的犹豫，像是在说服自己这样做没问题"。

结尾 Sensei 一杯饮料也没买就走了："如果不是 Rin 做的，那就不一样了。" `rin_love += 1`。

附带一点：`cafe` 路由里 `rinsad == True` 时改跳 `rincafegone`，那个 label 里 Sensei 只能和 Haruka 闲聊，而 Haruka 说"她可能比我还要担心 Rin"——Haruka 对 Rin 的关注在源文里是持续的，不是一次性支线。

## 三、lust 线概貌

先纠正一个前提：**`inappropriatecontent.rpy` 中不存在以 Rin 为名的 X 事件 label**（该文件里所有含 "rin" 的 label 全部属于 Kirin）。Rin 的性内容在源文中**全部由台词与叙述回溯交代，没有独立展开的场次**。可核实的状态是：

- `rinspring3` 开头 Sensei 的内独白就是"那个我没有和她上床的人"。
- 截至 `rinspring9`，Rin 与 Sensei 只到接吻——`rinspring8` 里 Rin 当着 Uta 的面说"我们其实只接过吻而已"，`dormwarsfiverin1` 里她主动要求"慢慢来"，理由是想让关系看起来是长时间的自然演化；同一段里她也承认"如果你现在把我按倒、为所欲为，我会很乐意顺从，大概十秒内就会到"。

Rin 被明确陈述出来的性经历：

- **Otoha**：只有手和口——`rinspring4` 里她自己说"连 Otoha 也只用了手和嘴"；`rindorm55p2` 里她说"我摸了她胸大概五分钟。很赞，很结实"。
- **Sana**：`rinspring1` 里承认圣诞派对上接过吻，并说那次没起多大作用。
- **Molly**：`cafe45` 的玩笑对白里，她说"人永远不会忘记自己的初吻"，接的就是 Molly。
- **Chika**：`rinspring6` 里被 Chika 口交，Chika 自称第一次。

Rin 的自慰在源文中是明写的，而且和自毁被放在同一套机制里：`rinspring5` 整段就是她一个人自慰、编辑短信、发送；`rinspring3` 与 `dormwarsfiverin1` 两次提到她曾在 Ayane 家病房的帘子后，趁 Sensei 与 Sana 发生关系时自慰。`rinspring5` 的叙述把振动棒和割伤直接并列——"一件用来带走痛的工具。你习惯了那种东西。我们都见过你对自己做的事。你当时让他进去了，现在让他进去又有什么不同？"

所以 Rin 的性内容不承担"色情"功能，而承担证词功能：每一段身体描写都在为 love 线的某个断言提供物证——她停不下来地想 Sensei，而她用来压住这份想念的工具，和她用来压住别的东西的工具，是同一套。

## 四、与主线/元叙事咬合点

1. **重置按钮**：`cafe30` 里 Rin 讲了一个梦——"和这个世界一样的世界，但我们可以重做所有做错的事"，"就像一个 reset 按钮"；被 Chika 拒绝之后，她"一遍又一遍、又一遍地按那个按钮，直到找到一个她爱我的世界"，"最后成了。我还顺便体验了她接吻有多好"。这是源文里最直接的重置隐喻，但**它被明确写成一个梦**："然后，在任何好事发生之前，我醒了。" 不能读成她记得循环内容。
2. **断片与屏蔽的对称**：`rinspring1` 里 Sana 问 Sensei 失神时看到了什么，Sensei 答"两种都有一点，但我被拉回现实之后几乎什么都不记得"；紧接着 Rin 说自己的抑郁发作"会把整整几天甚至几周屏蔽掉"，"唯一能把我拉出来的只有时间"，而这构成一个悖论——"你需要靠时间愈合，却因为和时间失去接触而不知道过去了多久"。两人症状被并排放在同一段对话里，Molly 把这形容成"像时间跳跃"。
3. **元叙事入侵**：`cafe15` 里 Rin 说到一半，画面被打断为 `TERMINAL 23 IS EXPERIENCING A DISRUPTION IN SERVICE`、`GREETINGS, YOU WHO ARE HIGHLY FAVORED`、`SHE HURTS WHILE SHE WAITS`、`HER BODY IS FULL OF NEW GUINEA FLATWORMS`、`GIVE HER WHAT SHE WANTS`，随后对话无缝接回——Sensei 那句台词里被划掉的正是 "Why won't you tell me what's wrong with you?"。`rinspring6` 结尾直接打出 `DEVIATION DETECTED` / `THIS IS NO NIGHT TO REMEMBER`；`rinspring9` 里出现用十六进制说话的 Maya（"看来我们又失败了"）与一个自称被夺走眼睛的"第二个 Rin"，后者明说 "This is no dream... A result"。
4. **Chika 协议作为后宫结构的条款**：见「二、love 线逐事件脉络」第 5 小节。Rin 在这条协议里的位置不是旁观者，而是直接受益者——Chika 说"因为这样我就能同时拥有你们两个"。

## 五、未解伏笔

1. **Rin 与 Sensei 是否会越过接吻**：`dormwarsfiverin1` 里她要求"慢慢来"，`rinspring7` / `rinspring8` 里两人仍在互相挑逗而不越线；源文在 `rinspring9` 结束时没有给出答案。
2. **药的说法互相打架**：`rinspring5` 里 Rin 对母亲喊"我们已经知道药没用了"；`rindorm50special` 里 Sensei 说的是她曾坦白自己不肯穿那件"救生衣"，因为它让她感觉不对，Rin 则回了句"救生衣就是药，我懂"。到底是不吃药还是吃了没用，她的治疗史在源文中没有补全。
3. **另一位母亲 Rie 从未在 RinEvents 中出场**：`rinspring6` 里 Rika 说"你知道我得把这件事告诉 Rie"，Rin 随后说"我另一个妈妈会知道，而她是比较严格的那个"；这条支线在 Rin 的事件里没有被展开。
4. **Chika 切断关系的处理停在半途**：`rinspring8` 里 Rin 说"我能修好她"，`rinspring9` 结束时 Chika 仍在躲；两人之间的"Spat"在 Rin 的事件线里没有收口。
5. **生父**：`rinspring2` 里 Rin 说"他是我人生里最大的问号"，并说"没有意义去翻石头找答案"——源文只留了缺口。
6. **`rinspring9` 里的"第二个 Rin"与 Maya 究竟是什么**：那段被写成"不是梦，是结果"，但源文没有解释"结果"指的是什么，也没有交代 Rin 本人记住了多少。

> 按源行号检索本角色 label，见 `索引/Rin索引.md`。
