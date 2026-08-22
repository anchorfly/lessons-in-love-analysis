# Miku Maruyama 事件线梳理（MikuEvents.rpy，v0.55，约 9200 行 / 40 label）

> 基于 `_digest_Miku.txt`（4805 行）精读。Miku 是 **完全 loop/creator-aware** 的角色——她不仅知道 Sensei 真名 Akira，还知道所有人"都是游戏角色"、creator 叫 Selebus。所有结论标注源行号。

---

## 一、角色基本盘

- **身份**：足球部前锋（soccer 系列），精力过剩的运动少女；与 Ami 关系亲近（Ami 常对她喊"breed me"类玩笑 [8447]）。
- **表面性格**：大大咧咧、直言不讳、对 Sensei 用"Coach"称呼；在 Maki 的成人用品店打工/帮忙（mikupostnaming 附近）。
- **深层状态**：Miku 是少数**完全知悉元层级**的角色——她知道 Sensei 真名、知道《Lessons in Love》是游戏、知道 creator 是 Selebus，并能与 Sensei 讨论"游戏内是否也在发生同样的事"（[8455]）。
- **关键变量**：miku_love / miku_lust；bonus 分支。

## 二、love 线逐事件脉络

- **firsttimesoccer**（[354]）：初遇于足球场。
- **soccer5 → soccer35**（[652]–[2804]）：随 love 值递进的社团/约会（含 mikuwinterbeach1 [2754]）。
- **mikudorm45 / mikudorm45p2 / mikudorm50 / mikudorm55p1–p2**（[3145]–[5843]）：宿舍养成线。
- **mikuspecial50**（[3899]）：特殊事件。
- **mikuinvite1–2**（[4306]/[4649]）：上门节点。
- **mikupool / mikupool55**（[1]/[5132]）：泳池事件。
- **mikuspring1–7**（[6216]–[9041]）：第四章弹簧事件，**spring 含命名 meta 爆点**（见第四节）。

## 三、lust 线概貌（抽象概括）

lust 节点挂在 invite 菜单与 date 系列内（mikulust5 [8123] 等）。meta 含量集中在 mikunaming / mikupostnaming 的"creator"对话。

## 四、与主线咬合点

1. **Sensei 自报真名**（[5364]）：miku "That's my name. Just it isn't. My real name is Akira. Hello."——Sensei 在 Miku 线明确以 **Akira** 自称（与 Ami 线系统文本写出 "Akira Arakawa"、Maki/Haruka/Noriko 直呼 Akira 同构）。
2. **Miku 知悉角色非真实 + creator**（[8439]–[8455]）：miku "Lessons in Love. I know."（[8440]，指认游戏名）→ "we all are [made of polygons]. How'd ya not know that if you're askin' me to call you by the creator's name?"（[8453]）→ "So you're sayin' that what's happenin' now could be happenin' in the game version too?"（[8455]）。Sensei 由此陷入"元悖论"恐惧（[8454]），最终改口不叫 Selebus。这是全书对"游戏套游戏"最直白的讨论之一。
3. **Miku 知悉 Maya / Ayane 的"非人"特质**（[3949]）：a "the same way Maya can eat more than her body weight in food and Ayane can materialize guns and giant bananas out of thin air."——Miku 以"知道 Maya 暴食、Ayane 凭空造枪"来论证 Sensei 的荒谬，证明她把同伴当作"有超常设定的角色"看待。
4. **命名递归 meta**（mikunaming [8286] / mikupostnaming [8537]）：Sensei 让 Miku 以各种名字称呼自己（Selebus、Kirin 等），构成对"角色命名权"的自指玩笑。

## 五、未解伏笔

- Miku 的"creator 认知"从何而来？她是否读过游戏、还是被某存在告知？
- 她与 Ami 的"breed me"玩笑背后，是否暗示 Ami 对 Miku 有特殊执念？
- Miku 的完全 aware 状态为何未被循环"清洗"？

## 六、label 总表（40 个）

mikupool[1] · soccerfield[13] · callmikumorning[42] · callmikuafternoon[58] · callmikunight[141] · mikuinvite[231] · mikuinvitegen[242] · mikuinviteaff[286] · mikusoccergen2[323] · firsttimesoccer[354] · soccer2to4[619] · soccer5[652] · soccer10[951] · soccer15[1355] · soccer20[1651] · soccer25[2067] · soccer30[2439] · mikuwinterbeach1[2754] · soccer35[2804] · mikudorm45[3145] · mikudorm45p2[3496] · mikuspecial50[3899] · mikudorm50[4260] · mikuinvite1[4306] · mikuinvite2[4649] · mikupool55[5132] · mikudorm55p1[5481] · mikudorm55p2[5843] · mikuspring1[6216] · mikuspring2[6512] · mikuspring3[6993] · mikuspring4[7308] · mikuspring5[7652] · mikulust5[8123] · mikunaming[8286] · mikupostnaming[8537] · mikuspring6[8762] · mikuspring7[9041]
