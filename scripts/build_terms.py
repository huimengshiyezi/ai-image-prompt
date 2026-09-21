# -*- coding: utf-8 -*-
"""
把一份「词库 Markdown」解析成结构化词表。

产出两份（都由脚本生成，**不要手改**）：
    assets/terms.json             结构化词表，供 lookup.py 检索
    references/07-term-library.md 分类中英对照表，供人翻查

源文件结构：若干 `## 区块`，每个区块一张 markdown 表格，表头是成组的列名，
数据行按 (中文, 英文) 或 (中文, 英文, 说明) 成对出现，不同组横向并排。

用法：
    python scripts/build_terms.py                 # 用下面的默认源路径
    python scripts/build_terms.py <源md路径>       # 换源文件
    python scripts/build_terms.py <源md路径> <输出json路径>

清理规则在下面的 FIX_ZH / FIX_PAIR / DROP 里。**发现新错字请改规则后重跑**，
不要直接改产物 —— 下次重跑会把手工修改覆盖掉。
"""
import json
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path

# 默认源文件：本地词库 Markdown（若干 `## 区块` + 每区块一张中英对照表）。
# 优先级：命令行参数 > 环境变量 AI_IMAGE_PROMPT_TERMS_SOURCE > 下面的默认值。
# 源文件不在手边时不用管它 —— 仓库里的 assets/terms.json 与 references/07
# 已经是从源文件生成好的产物，日常检索直接用那两个即可。
SOURCE_MD = os.environ.get(
    "AI_IMAGE_PROMPT_TERMS_SOURCE", "terms-source.md"
)

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "assets" / "terms.json"

# 推广 / 水印行拦截：命中任一关键词的单元格直接丢弃，不进产物。
# 这里只放**通用**推广动作词。若自己的源词库里还有自定义推广语或账号名，
# 用环境变量追加进来 —— 本脚本会公开，别把个人信息写死在这里：
#     set    AI_IMAGE_PROMPT_TERMS_BLOCK=推广词1|推广词2   (Windows cmd)
#     $env:AI_IMAGE_PROMPT_TERMS_BLOCK="推广词1|推广词2"    (PowerShell)
WATERMARK_PAT = re.compile(
    "|".join(
        [r"加我", r"扫码", r"二维码", r"联系我", r"私信", r"关注我", r"引流"]
        + [w for w in os.environ.get("AI_IMAGE_PROMPT_TERMS_BLOCK", "").split("|") if w]
    )
)

SECTION_GROUP = {
    "标准-风格": "风格",
    "内容-主体": "主体",
    "人物-姿势": "姿势",
    "人物-服装": "服装",
    "人物-饰品": "饰品",
    "内容-场景": "场景",
    "内容-视角": "镜头构图",
    "标准-质量": "质量",
    "神话|专栏": "神话",
}

# ---- 清理层 ----
# 1) 用「英文相同、中文不同」的两两比对 + 人工核对源文定位出来的错字/错行。
#    只在 zh 上做子串替换，不做模糊匹配，避免误伤。
FIX_ZH = [
    ("流海", "刘海"),
    ("副画幅相机", "APS-C 画幅相机"),
    ("中远暴", "中远景"),
    ("中暴", "中远景"),
    ("中中特写", "中特写"),
    ("免耳", "兔耳"),
    ("鹏哎白眼", "翻白眼"),
    ("六妹，财富和繁荣之神", "刘海，财富和繁荣之神"),
    ("轮樹灯", "轮廓光"),
    ("嫁金室", "炼金室"),
    ("0C 渲染", "Octane 渲染"),
    ("手细蹦夹腿间", "手夹在腿间"),
    ("浴巾校服", "校服"),
    ("皮克期", "皮克斯"),
    ("克芳德莫奈", "克劳德·莫奈"),
    ("Jolo的奇妙冒险", "JOJO的奇妙冒险"),
    ("乔乐奇妙冒险", "JOJO的奇妙冒险"),
    ("梦工厂动西风格", "梦工厂动画风格"),
    ("桁缝纸", "衍纸"),
    ("纺缝艺术", "绗缝艺术"),
    ("折迭马尾辫", "折叠马尾辫"),
    ("侧织辫", "侧编辫"),
    ("编制马尾辫", "编织马尾辫"),
    ("两景(25)", "两景(2S)"),
    ("(核桃)的横截面图", "横截面图"),
    ("奈方山水画", "东方山水画"),
]

# 2) 同一个中文在不同英文下含义不同，不能靠子串替换，按 (中文, 旧英文) → 新值 定点修
FIX_PAIR = {
    ("爆头", "headshot"): ("头部特写", "headshot"),
    ("黑色背景为中心", "Song Huizong Zhao Ji"): ("宋徽宗赵佶", "Song Huizong Zhao Ji"),
    ("日记本", "Risograph"): ("riso 印刷风格", "Risograph"),
    ("奢华金色系", "Natural Green Series"): ("奢华金色系", "Luxury Gold Tones"),
    ("乌拉诺", "Uranus"): ("乌拉诺斯", "Uranus"),
    ("冥王星，冥界和财富之神", "Pluto"): ("冥王普鲁托，冥界和财富之神", "Pluto"),
    ("普丝佩尼，春天之女神和冥界之王后", "Persephone"): ("佩尔塞福涅，冥王后和春天女神", "Persephone"),
    ("弗博斯，恐惧和惊慌之神", "Phobos"): ("福波斯，恐惧之神", "Phobos"),
    ("尼墨西斯，惩罚和复仇之女神", "Nemesis"): ("涅墨西斯，报复和惩罚之女神", "Nemesis"),
    ("海斯提亚，壁炉、家和家庭之女神", "Hestia"): ("赫斯提亚，炉灶、家庭和家族之神", "Hestia"),
    ("相机型号 焦段 光圈", "canon 5d,1fujifilm xt100,Sony alpha"):
        ("相机型号 焦段 光圈", "Canon 5D, Fujifilm XT100, Sony Alpha"),
    # 源文件把英文列填错了（不是 OCR，是原表就错）
    ("皮克斯风格", "Picos style"): ("皮克斯风格", "Pixar style"),
    ("梦工厂动画风格", "CGSociety"): ("梦工厂动画风格", "DreamWorks Animation style"),
    ("等距线描", "Hatching"): ("等距线描", "Isometric line drawing"),
    # 同一件东西在源表里录了两遍，一次中文错（奈方山水画）一次英文错（Tradition→Traditional）
    ("东方山水画", "Tradition Chinese Ink Painting"):
        ("东方山水画", "Traditional Chinese Ink Painting"),
    ("国风", "Tradition Chinese Ink Painting style"):
        ("国风", "Traditional Chinese Ink Painting style"),
    ("立绘阴影", "drop shadow"): ("投影阴影", "drop shadow"),
}

# 3) 源表里明确无意义或残缺的条目
DROP = {
    ("镜头构图", "群景(GS)", "Scenery Shot"),
    ("镜头构图", "风景照", "Bokeh"),
    ("镜头构图", "背景虚化", "Foreground"),
    ("镜头构图", "前景", "Background"),
    ("镜头构图", "背景", "Full Length Shot (FLS)"),
}

# 4) 源词库缺失、但用户高频使用的词 —— 写死在这里，重跑时注入。
#    格式：(大类, 小类, 中文, 英文)
#    ⛔ 加词前先用 lookup.py 查一遍，不要和源词库重复。
EXTRA_TERMS = [
    # 「3D 动漫」这一支源词库完全空白（族 4b），补齐日式卡渲（三渲二）
    ("风格", "动漫/动画/游戏风格", "赛璐璐着色", "cel shading"),
    ("风格", "动漫/动画/游戏风格", "赛璐璐风格", "cel-shaded style"),
    ("风格", "动漫/动画/游戏风格", "卡通渲染", "toon shading"),
    ("风格", "动漫/动画/游戏风格", "三渲二", "3D cel-shaded"),
    ("风格", "动漫/动画/游戏风格", "3D 动漫", "3D anime"),
    ("风格", "动漫/动画/游戏风格", "动漫渲染", "anime-style rendering"),
    ("风格", "动漫/动画/游戏风格", "等距卡通渲染", "isometric cel shading"),
    # 「3D 动漫」欧美支线
    ("风格", "动漫/动画/游戏风格", "3D 动画电影风格", "3D animated feature film style"),
    # 两条支线共用的渲染特征词（源词库的「渲染」全是产品渲染器，缺这一整类）
    ("质量", "画质", "硬边阴影", "hard-edged shadow"),
    ("质量", "画质", "块状高光", "blocky specular highlight"),
    ("质量", "画质", "描边线", "outline stroke"),
    ("质量", "画质", "块面头发", "blocky anime hair"),
    ("质量", "画质", "次表面散射", "subsurface scattering"),

    # ── 产品 / 静物（源词库这一支几乎空白：香水 / 静物 / 棚拍全部零命中）──
    ("主体", "主体、角色", "香水瓶", "perfume bottle"),
    ("主体", "主体、角色", "化妆品瓶", "cosmetic bottle"),
    ("风格", "形式", "静物摄影", "still life photography"),
    ("风格", "形式", "产品摄影", "product photography"),
    ("风格", "形式", "商业棚拍", "commercial studio photography"),
    # 产品摄影的高光行为词（源词库的材质只有材质名，没有"光照上去是什么样"）
    ("质量", "材质", "镜面高光", "specular highlight"),
    ("质量", "材质", "内部折射", "internal refraction"),
    ("质量", "材质", "水面倒影", "water reflection"),
    ("质量", "材质", "露珠", "dew drops"),
    ("质量", "材质", "高光过渡", "highlight rolloff"),

    # ── 建筑形制（源词库「建筑」只有 7 条，缺全部形制词）──
    ("场景", "场景", "马头墙", "horse-head gable wall"),
    ("场景", "场景", "悬山顶", "overhanging gable roof"),
    ("场景", "场景", "歇山顶", "hip-and-gable roof"),
    ("场景", "场景", "飞檐", "upturned eaves"),
    ("场景", "场景", "月洞门", "moon gate"),
    ("场景", "场景", "美人靠", "waterside bench railing"),
    ("场景", "场景", "影壁", "spirit screen wall"),
    ("场景", "场景", "斗拱", "bracket set"),
    ("质量", "材质", "清水混凝土", "fair-faced concrete"),

    # ── 水墨 / 国画（源词库：宣纸、留白、焦墨全部零命中）──
    ("质量", "材质", "宣纸", "xuan paper"),
    ("镜头构图", "构图", "留白", "negative space"),
    ("风格", "形式", "焦墨", "dense black ink"),
    ("风格", "形式", "泼墨", "splashed ink"),
    ("风格", "形式", "飞白", "dry brush"),
    ("风格", "形式", "皴法", "texture stroke"),
    ("风格", "形式", "墨色层次", "tonal gradation of ink"),
    ("风格", "中式元素", "朱红印章", "vermilion seal"),
    ("风格", "中式元素", "题字", "calligraphic inscription"),

    # ── 三视图 / 角色设定（源词库「姿势」64 条一个设定图站姿都没有）──
    ("姿势", "整体姿势", "A字站姿", "A-pose"),
    ("姿势", "整体姿势", "T字站姿", "T-pose"),
    ("姿势", "整体姿势", "三视图站姿", "three-view neutral stance"),
    ("姿势", "整体姿势", "正面站姿", "front-facing neutral pose"),
    ("风格", "形式", "角色三视图", "character turnaround sheet"),
    ("风格", "形式", "角色设定图", "character design sheet"),
    ("风格", "形式", "立绘", "character illustration"),
    # 「四视图」（左脸特写 + 正/侧/背）是中文用户说「人物设定」时的默认排布，
    # 源词库没有这个词，而 2016~2026 这十年里它一直是中文 AI 绘图的通行说法
    ("风格", "形式", "角色四视图", "character four-view sheet"),
    ("风格", "形式", "转面图", "character turnaround"),
    ("镜头构图", "构图", "面部特写格", "face close-up panel"),
    ("镜头构图", "构图", "侧视图", "side view"),
    ("镜头构图", "构图", "背视图", "back view"),
    ("场景", "背景", "纯色背景", "solid color background"),
    ("场景", "天气、灯光、光线", "均匀平光", "flat even lighting"),
    ("姿势", "整体姿势", "中性站姿", "neutral stance"),
]


def inject_extra(records):
    """把 EXTRA_TERMS 注入词条列表。在去重之前调用。"""
    for sec, grp, zh, en in EXTRA_TERMS:
        records.append({"s": sec, "g": grp, "zh": zh, "en": en, "extra": True})


def apply_fixes(zh, en):
    for a, b in FIX_ZH:
        zh = zh.replace(a, b)
    if (zh, en) in FIX_PAIR:
        return FIX_PAIR[(zh, en)]
    return zh, en


def split_cells(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_sep_row(cells):
    return all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c != "")


def clean_en(s):
    s = s.replace("\u3000", " ")
    s = re.sub(r"\s+", " ", s).strip()
    s = s.strip("`*")
    s = re.sub(r"^[（(]\s*", "(", s)
    return s.strip()


def clean_zh(s):
    s = s.replace("\u3000", " ").strip()
    s = re.sub(r"\s+", " ", s)
    return s.strip("`*｜| ")


def parse_blocks(text):
    """切成 {区块标题: [表格行]} """
    blocks = OrderedDict()
    cur = None
    buf = []
    for raw in text.splitlines():
        if raw.startswith("## "):
            if cur is not None:
                blocks[cur] = buf
            cur = raw[3:].strip()
            buf = []
        elif cur is not None:
            buf.append(raw)
    if cur is not None:
        blocks[cur] = buf
    return blocks


def parse_table(lines):
    """从区块行里取第一张 markdown 表格，返回 (表头cells, [数据行cells])"""
    header = None
    rows = []
    for ln in lines:
        if not ln.strip().startswith("|"):
            if header and rows:
                break
            continue
        cells = split_cells(ln)
        if header is None:
            header = cells
        elif is_sep_row(cells):
            continue
        else:
            rows.append(cells)
    return header or [], rows


def group_starts(header):
    idx = [i for i, c in enumerate(header) if c.strip()]
    if not idx:
        return [], 2
    if len(idx) == 1:
        return [0], 2
    steps = [b - a for a, b in zip(idx, idx[1:])]
    size = min(steps)
    return idx, size


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(SOURCE_MD)
    if not src.exists():
        sys.exit(f"找不到源文件：{src}\n请用 python build_terms.py <源md路径> 指定。")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    text = src.read_text(encoding="utf-8")

    records = []
    report = OrderedDict()
    suspects = []
    params = []
    sd_words = []
    tree = []

    for section, lines in parse_blocks(text).items():
        header, rows = parse_table(lines)
        if not header:
            continue
        starts, size = group_starts(header)
        kept = 0

        if section == "绘画分类方式":
            for r in rows:
                for si in starts:
                    if si + 1 >= len(r):
                        continue
                    parent, child = clean_zh(r[si]), clean_zh(r[si + 1])
                    if parent and not WATERMARK_PAT.search(parent):
                        tree.append({"group": header[si], "parent": parent, "child": ""})
                        last = parent
                    if child and not WATERMARK_PAT.search(child):
                        tree.append({"group": header[si], "parent": "", "child": child})
            continue

        for r in rows:
            for si in starts:
                gname = clean_zh(header[si])
                zh = clean_zh(r[si]) if si < len(r) else ""
                en = clean_en(r[si + 1]) if si + 1 < len(r) else ""
                note = clean_en(r[si + 2]) if size >= 3 and si + 2 < len(r) else ""
                if WATERMARK_PAT.search(zh) or WATERMARK_PAT.search(en):
                    continue
                if not zh:
                    continue

                if section == "midjourney参数指令":
                    if en:
                        params.append({"group": gname, "name": zh, "desc": en})
                        kept += 1
                    continue

                if section == "SD通用提示词":
                    if en:
                        sd_words.append({"group": gname, "label": zh, "value": en})
                        kept += 1
                    continue

                if not en:
                    suspects.append({"section": section, "group": gname, "zh": zh, "en": "", "why": "缺英文"})
                    continue

                zh, en = apply_fixes(zh, en)
                sec = SECTION_GROUP.get(section, section)
                if (sec, zh, en) in DROP:
                    continue

                rec = {"s": sec, "g": gname, "zh": zh, "en": en}
                if note:
                    rec["note"] = note
                records.append(rec)
                kept += 1

        if kept:
            report[section] = kept

    # 注入补充词条（源词库缺失的高频词），放在去重之前
    inject_extra(records)

    # 去重：神话按英文名（同一神祇在源表里被写了两遍、措辞不同），其余按 (区块, 分组, 中文)
    seen = OrderedDict()
    variants = {}
    for rec in records:
        if rec["s"] == "神话":
            key = (rec["s"], rec["en"].lower().strip())
        else:
            key = (rec["s"], rec["g"], rec["zh"])
        if key in seen:
            continue
        seen[key] = rec
        variants.setdefault((rec["s"], rec["zh"]), []).append(rec["en"])

    alt_n = 0
    for rec in seen.values():
        alts = [e for e in variants.get((rec["s"], rec["zh"]), []) if e != rec["en"]]
        if alts:
            rec["alt"] = alts
            alt_n += 1

    payload = {
        # 固定中性值：产物会公开，源文件名/路径可能含个人信息，一律不写进去
        "source": "本地词库 Markdown",
        "stats": {
            "terms": len(records),
            "unique": len(seen),
            "dup_removed": len(records) - len(seen),
            "with_alt": alt_n,
            "extra": len(EXTRA_TERMS),
            "params": len(params),
            "sd_words": len(sd_words),
        },
        "by_section": report,
        "terms": list(seen.values()),
        "midjourney_params": params,
        "sd_words": sd_words,
        "painting_tree": tree,
        "suspects": suspects,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    md = render_md(payload)
    md_path = out.parent.parent / "references" / "07-term-library.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md, encoding="utf-8")

    print("== 各区块词条数 ==")
    for k, v in report.items():
        print(f"  {k}: {v}")
    print("== 总计 ==")
    for k, v in payload["stats"].items():
        print(f"  {k}: {v}")
    groups = OrderedDict()
    for rec in seen.values():
        groups.setdefault(rec["s"], OrderedDict()).setdefault(rec["g"], 0)
        groups[rec["s"]][rec["g"]] += 1
    print("== 分类骨架 ==")
    for s, gs in groups.items():
        print(f"  [{s}] " + " / ".join(f"{g}({n})" for g, n in gs.items()))
    print("== 可疑样例（前20）==")
    for x in suspects[:20]:
        print(f"  {x['section']} | {x['group']} | {x['zh']} => {x['en']} ({x['why']})")
    print(f"已写出: {out} ({out.stat().st_size // 1024} KB)")
    print(f"已写出: {md_path} ({md_path.stat().st_size // 1024} KB)")


SECTION_ORDER = ["风格", "主体", "姿势", "服装", "饰品", "场景", "镜头构图", "质量", "神话"]


def render_md(payload):
    lines = [
        "# 07 · 词表（AI 绘画提示词库 · 清理版）",
        "",
        "> 本文件由 `scripts/build_terms.py` 从词库 Markdown 自动生成，**不要手改**——",
        "> 改规则请改脚本里的 `FIX_ZH` / `FIX_PAIR` / `DROP`，然后重跑。",
        "> 原始素材：本地词库 Markdown（若干 `## 区块` + 中英对照表）",
        "",
        "**用法**：先用 `scripts/lookup.py --list` 看分类，再 `--group 场景/天气、灯光、光线` 列候选，",
        "或 `--kw 逆光` 按中英关键词模糊查。**不要整份读完**——本文件只为检索而生。",
        "",
        f"共 {payload['stats']['unique']} 条，其中 {payload['stats']['with_alt']} 条带英文异名（写作 `(亦作: …)`）。",
        "",
        "---",
        "",
    ]
    bucket = OrderedDict()
    for rec in payload["terms"]:
        bucket.setdefault(rec["s"], OrderedDict()).setdefault(rec["g"], []).append(rec)

    for sec in SECTION_ORDER:
        if sec not in bucket:
            continue
        lines.append(f"## {sec}")
        lines.append("")
        for gname, recs in bucket[sec].items():
            lines.append(f"### {sec} / {gname}（{len(recs)}）")
            lines.append("")
            for r in recs:
                alts = r.get("alt") or []
                tail = f"　(亦作: {'; '.join(alts)})" if alts else ""
                lines.append(f"- {r['zh']} → {r['en']}{tail}")
            lines.append("")

    lines += ["---", "", "## 附：Midjourney 参数指令", ""]
    for p in payload["midjourney_params"]:
        lines.append(f"- `{p['name']}`（{p['group']}）— {p['desc']}")
    lines += ["", "## 附：SD 通用正/负面词", ""]
    for w in payload["sd_words"]:
        lines.append(f"### {w['label']}")
        lines.append("")
        lines.append(f"```\n{w['value']}\n```")
        lines.append("")
    lines += ["## 附：绘画分类树（技法 / 内容 / 时代 / 材料）", ""]
    for t in payload["painting_tree"]:
        tag = f"**{t['parent']}**" if t["parent"] else f"　└ {t['child']}"
        lines.append(f"- {tag}　`{t['group']}`")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
