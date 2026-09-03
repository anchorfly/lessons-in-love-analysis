# 0.61.0 版本更新事件（beachseven 第七届海滩）分支梳理

> 对象：guide.html 中 `RELEASE.version = "0.61.0"` 的 15 个版本更新事件（全部为 `beachseven*` 系列）
> 方法：从 `游戏文本/*.rpy` 提取 15 个 label 的原始 Ren'Py 块，分析 menu / if-else / jump 分支结构
> 结论：**整体线性贯通，玩家可干预的分支仅 1 处（beachseven4intro），另 1 处结局自动分流（beachseven5）**

---

## 一、总体结构：线性主链 + 2 个真实分支点

```
beachseven1 → 2 → 3 → io1 → ami1 → chika1 → touka1 → wakana1 → wakana2
            → karin1 → chika2 → rin1 → imani1 → 4intro → 5(大结局)
                                                  │
                                   ┌──────────────┴──────────────┐
                              [menu 选项]                  [自动按 flag]
                          Floor1 → 4f1                  dormwarssixfloor1win
                          Floor2 → 4f2                  → 4f1 / 否则 → 4f2
                                   │                          │
                                   └──── 都 jump 回 beachseven5 ┘
```

- 主链 15 个事件在 playback_order.json 中连续（§11.7 + §2.65 已验证互逆/无环）
- 14 个事件**无任何玩家选项（menu=0）**，仅 `beachseven4intro` 含 1 个 menu
- 事件内部 `if/else` 绝大多数出现在**对话文本**（英语 "if"），真正的分支语句极少

---

## 二、真实分支点（会改变路线的分叉）

### 分支点 1：`beachseven4intro`（唯一玩家选项）
来源 chap4part2.rpy，约 2KB。

```
menu:
  • "Floor 1 Version"  → jump beachseven4f1
  • "Floor 2 Version"  → jump beachseven4f2
```
- 同时有自动分支：`if dormwarssixfloor1win == True → jump beachseven4f1` / `else → jump beachseven4f2`（重放 _in_replay 时跳过 menu 直接按 flag 走）
- **延伸分支**（不在 15 个主事件内）：
  - `beachseven4f1`（chap4part2.rpy，451 行 / ~28KB）— 一楼队赢的决赛线，结尾 `jump beachseven5`
  - `beachseven4f2`（chap4part2.rpy，460 行 / ~28KB）— 二楼队赢的决赛线，结尾 `jump beachseven5`
  - 两者内部各有子菜单 `beachsevenf1menu` / `beachsevenf2menu`（3 处跳转，更细的选项层）
- **两条线最终都汇合回 `beachseven5`（大结局）**

### 分支点 2：`beachseven5`（大结局，按时间自动分流，非玩家选择）
来源 chap4part2.rpy，约 23KB，是第七届海滩收束。
```
if day >= 6:
    jump endofsatch4        # 周末版后日谈
else:
    jump endofweekdaych4    # 工作日版后日谈
```
- 由游戏内 `day` 变量（周末/工作日）决定两种结局变体，玩家无法干预

---

## 三、条件呈现分歧（不改变路线，仅按前置 flag 显示不同段落）

这些 `if` 检查的是**其他角色线 / 全局状态**是否已推进，从而呈现交叉对话或回忆差异——属于"剧情联动"而非"分支选择"：

| 事件 | 条件 | 触发内容（abstract） |
|---|---|---|
| beachseven1 | `if otohaspring6 == True` | Otoha 春线交叉对话 |
| beachseven2 | `if mayaspring4 == True` / else | Maya 已发生对话 vs 遗忘版对话 |
| beachseven3 | `if nikinudetrade == True` / else | Niki 相关分歧对话 |
| beachsevenio1 | `if _in_replay` | 重放模式下的演出差异 |
| beachsevenrin1 | `if _in_replay` | 重放模式下的演出差异 |
| beachseven4intro | `if _in_replay` / `if dormwarssixfloor1win` | 重放 / 楼层胜负自动选线 |

其余 9 个事件（ami1, chika1, touka1, wakana1, wakana2, karin1, chika2, imani1, 以及部分）**内部无任何 if/else 分支语句，纯线性叙事**。

---

## 四、一句话结论

0.61.0 的 15 个 beachseven 事件是**第七届海滩的线性主线**，玩家能主动做的选择只有 `beachseven4intro` 一处（选一楼/二楼决赛线 → f1/f2，最终汇合大结局）；大结局 `beachseven5` 按周末/工作日自动分两个后日谈。其余 `if` 均为跨角色 flag 联动或重放差异的"条件呈现"，不创造新路线。

---

### 附：15 个事件清单（label / title / 所在文件）
| # | label | title | 文件 |
|---|---|---|---|
| 1 | beachseven1 | Make Me Into Gyoza | chap4part2.rpy |
| 2 | beachseven2 | Male-Enhancement | chap4part2.rpy |
| 3 | beachseven3 | Shaken, Not Stirred | chap4part2.rpy |
| 4 | beachsevenio1 | My Anchor & Me | IoEvents.rpy |
| 5 | beachsevenami1 | Antarctic Treaty System | AmiEvents.rpy |
| 6 | beachsevenchika1 | Melancholera | ChikaEvents.rpy |
| 7 | beachseventouka1 | Hitohira | ToukaEvents.rpy |
| 8 | beachsevenwakana1 | The Cask of Amontillado | WakanaEvents.rpy |
| 9 | beachsevenwakana2 | Les Fleurs du Mal | WakanaEvents.rpy |
| 10 | beachsevenkarin1 | Same Time Tomorrow | KarinEvents.rpy |
| 11 | beachsevenchika2 | Storybook Romance | ChikaEvents.rpy |
| 12 | beachsevenrin1 | Little Waves | RinEvents.rpy |
| 13 | beachsevenimani1 | ELATION PROTOCOL 99: HASSAN, HOSANNA | ImaniEvents.rpy |
| 14 | beachseven4intro | A Night of Just One Prize This Time | chap4part2.rpy |
| 15 | beachseven5 | The End Complete | chap4part2.rpy |
