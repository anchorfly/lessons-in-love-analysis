# WorkBuddy 分析产出专区

> 本目录收录由 WorkBuddy 会话生成的《Lessons in Love》分析文档。源文位于 `../游戏文本/`（71 个 .rpy）。
> 生成时间：2026-08-22。方法：自研 digest 脚本（label+源行号+对话+跳转）→ 分批精读 → 六部分结构落盘 → Grep 全库复核引文。

## 目录结构

```
workbuddy分析/
├── 人物事件线/            # 37 个角色事件文件精读 + 汇总
│   ├── <角色名>.md ×37    # 基本盘 / love 线 / lust 线 / 主线咬合点 / 未解伏笔 / label 总表
│   ├── DormEvents.md      # 宿舍养成层 + roomwithclocks/ticktock/trinity1 神话核心簇
│   └── 人物事件线全梳理.md # 三层世界观、主线迭代重构、觉醒者网络、全员索引、母题词典
├── USER3与pareidolia源文分析.md   # pareidolia=USER3 证据链；三声分离判据；TEMPLATE9/USER4
├── 系统层文本母题表.md             # 全库系统消息/消字/status effect 修辞速查（附行号）
└── 主线章节脚本精读.md             # ch2script/chap3/chap4 核心 meta 弧：thirdreset、slumberreset、
                                    # endofgameworld、postfreddeathscene 起源场景
```

## 快速入口

| 想查什么 | 看哪份 |
|---|---|
| 单个角色的 love/lust 线与伏笔 | `人物事件线/<角色名>.md` |
| 世界观全貌、人物关系网 | `人物事件线/人物事件线全梳理.md` |
| 无框旁白归属（Sekai vs pareidolia） | `USER3与pareidolia源文分析.md` §四判别表 |
| hex 码/终端播报/`[[ ]]` 消字出处 | `系统层文本母题表.md` |
| 主线剧情（重置链、Ami 之死、Sekai 起源） | `主线章节脚本精读.md` |

## 相关区域

- `../GLM精读总结/`：GLM 生成的系统文件/特殊内容/主线六章/careCode 精读（编号 01–07），与本区互补。
- 引文格式：单文件报告 `[N]`＝源文件行号；跨文件报告 `文件名.rpy:[N]`。所有关键断言可回查 `../游戏文本/` 原文。
