# ai-image-prompt — AI 生图提示词共创助手

把脑子里的碎片想法（哪怕只有「一男一女，朦胧感」这五个字），通过**最多四轮对话**收敛成一条能直接出图的高质量提示词。

作者：**AI绘梦师葉子**

---

## 它解决什么问题

写生图提示词，难的从来不是"不会写"，而是这几件事：

| 常见翻车 | 本 skill 的对策 |
|---|---|
| 图出来了没人小、看不清脸 —— 方向从一开始就跑偏 | **人物图第一个问题永远是「人在画面里多大」**，比画幅、风格、光线都更早定 |
| 说了「朦胧感 / 高级感」，AI 自己想当然翻译成一种做法 | **感受词先让用户选实现路径**再翻译 —— 选错路径 = 整张图的画面类型变了 |
| 提示词越写越长，四五百字还是不好看 | 真正的原因是**替你拍了板**：一堆你没要过的元素。分「中性默认」和「剧情化设定」两档处理 |
| 图不对，就整条重写，越改越乱 | **从症状进，只改那一槽**；同一个方向改到第 3 版还没动 → 卡的是结构不是措辞 |
| 光在光学上挑不出错，但整张图不好看 | 拆成**两道独立的关**：光对不对 ／ 图值不值得看。第二关有可执行的判据 |

## 核心设计（几条硬纪律）

- **默认动作是「问」，不是「出词」** —— 除非用户说「你定 / 直接出」，否则至少走一轮确认
- **主体 > 氛围** —— 默认不给剪影、不给背影、不给「望向远方」，那是一次偷换（把"人的美"换成"风景的美"）
- **人物图默认光位是「打脸光」**，不是逆光；逆光只镶边不打脸 = 主体不美
- **别默认把图压暗** —— 「朦胧 / 高级 / 氛围」≠ 要暗；影调（明暗）和色温（冷暖）必须分开定
- **光对了 ≠ 好看** —— 过第一关不会自动过第二关，第二关有构图六条判据
- **人像要「真」≠ 人像要「丑」** —— 默认走美，不主动加法令纹和不对称；塑料感的三个真正成因都不是"缺瑕疵"
- **名词自带的语义压得过任何形容词** —— 「光源在她正前方、和脸一样高」那个位置其实是镜头，模型会把光挪到身后

## 安装

把整个 `ai-image-prompt` 文件夹放进 skills 目录即可：

| 范围 | 放哪 |
|---|---|
| 个人级（所有项目可用） | `~/.workbuddy/skills/ai-image-prompt/` |
| 项目级（仅当前项目） | `<你的项目>/.workbuddy/skills/ai-image-prompt/` |

Windows 上就是 `C:\Users\<你的用户名>\.workbuddy\skills\ai-image-prompt\`。

放好后，跟带 Skill 机制的 AI 助手（WorkBuddy 等）说「帮我写个生图提示词」「画一张…」「这张图哪里不对」就会自动触发。

## 目录结构

```
ai-image-prompt/
├── SKILL.md                        主流程：四轮收敛 + 对话硬纪律 + 交付格式
├── references/                     按需加载的知识库（不要全读）
│   ├── 01-slots.md                 槽位骨架、12 类画面类型、装配顺序、缺省值
│   ├── 02-style-atlas.md           风格图谱 11 族、混风格、世界知识锚点
│   ├── 03-light-composition.md     光位判据、景别画幅、构图六条、名词定律
│   ├── 04-output-formats.md        输出形态、模型语法矩阵、Detail Mode、画面里的文字
│   ├── 05-quality-and-params.md    质感词、柔化实现、人像真实感、影调
│   ├── 06-diagnosis.md             症状诊断表（出图不对时从症状进）
│   └── 07-term-library.md          2550 条中英对照词表（检索用，别整份读）
├── scripts/
│   ├── lookup.py                   词表检索工具（推荐用它，别读 07 那 97KB）
│   └── build_terms.py              从原始词库 Markdown 重新生成上面两份产物
└── assets/
    └── terms.json                  结构化词表（供 lookup.py 检索）
```

## 词库（2550 条中英对照）

分类骨架：风格 554 ／ 主体 506 ／ 质量 390 ／ 场景 296 ／ 镜头构图 199 ／ 饰品 172 ／ 服装 162 ／ 神话 155 ／ 姿势 116，另含 Midjourney 参数 38 条、SD 通用正负向词 9 组。

**查词用脚本，不要读文件**：

```bash
python scripts/lookup.py --list                  # 看分类骨架
python scripts/lookup.py --group 天气            # 列某类全部候选
python scripts/lookup.py --kw 逆光               # 按中英关键词模糊查
python scripts/lookup.py --group 发型 --limit 40
```

## 词库维护

`assets/terms.json` 和 `references/07-term-library.md` 都是**脚本生成的产物，不要手改**（重跑会覆盖）。清理规则写在 `build_terms.py` 的 `FIX_ZH` / `FIX_PAIR` / `DROP` 里 —— 发现新错字就改规则后重跑。

重新生成需要一个源词库 Markdown（若干 `## 区块` + 每区块一张中英对照表）：

```bash
python scripts/build_terms.py <源md路径>
# 或者用环境变量指定：
#   set   AI_IMAGE_PROMPT_TERMS_SOURCE=<源md路径>     (Windows)
#   export AI_IMAGE_PROMPT_TERMS_SOURCE=<源md路径>    (macOS/Linux)
python scripts/build_terms.py
```

源词库里的推广行（加联系方式 / 扫码 / 引流之类）会被自动剔除。若你还有自己的推广语要一起清掉，用环境变量追加 —— **别写进脚本**，脚本是公开的：

```bash
#   set    AI_IMAGE_PROMPT_TERMS_BLOCK=词1|词2        (Windows)
#   export AI_IMAGE_PROMPT_TERMS_BLOCK="词1|词2"       (macOS/Linux)
```

> 说明：仓库里已经带好了生成好的产物，日常使用**不需要**跑这个脚本，也不需要源文件。

## 适配的模型

- **自然语言整段式**：GPT-Image-2、即梦、豆包、通义、Nano Banana、Seedream
- **参数式**：Midjourney（含参数指令写法）
- **节点式**：Stable Diffusion / ComfyUI（含通用正负向词）

负向词的写法按模型分档（GPT-Image 生效 / Nano Banana 需正向化），见 `references/04-output-formats.md` 的模型语法矩阵。

## 许可

代码与文档：**MIT**，见 [LICENSE](LICENSE)。

词库（`assets/terms.json`、`references/07-term-library.md`）由作者整理并清洗生成，随本仓库以同一许可提供，转载请注明出处。
