#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词库与文档一致性校验 —— 退出码 0 = 全绿。

存在的理由（这条比什么都重要）：
    **「存在」不等于「正确」。**
    本项目历史上出过三次同型事故：
      ① 构建脚本 Traceback 中断，产物还是旧的，而校验只查「格式对不对」，
         于是得出「规则没生效」的假结论 —— 真相是**产物根本没重建**。
      ② 词库只查「引用了不存在的」这种**引用错**，没查「存在但没被引用」
         这种**遗漏** —— 引用错会报错，遗漏不报任何错。
      ③ 文档间的「按标题引用」在标题改了之后**静默失效**（曾有 12 处节号引用
         因插入章节而全废，改成按标题引用后，新风险变成「改了标题忘改引用」）。
    修法不是「下次仔细点」，而是**把一致性变成测试**。这个脚本就是那条测试。

    所以本脚本的核心断言不是「格式合法」，而是两类**一致性**：
      · **产物与唯一真源 `lexicon/*.md` 一致** —— 忘跑 `render_lexicon.py` 立刻变红
      · **文档间的标题引用能落到真实标题上** —— 改标题忘改引用立刻变红

用法：
    python scripts/check_terms.py            # 全部检查
    python scripts/check_terms.py --quiet    # 只报结论与失败项

退出码：0 = 全绿；1 = 有 FAIL。
"""
from __future__ import annotations

import collections
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import render_lexicon as R   # noqa: E402  —— 复用它的解析与体检，避免两套规则

TERMS = ROOT / "assets" / "terms.json"
TERM_MD = ROOT / "references" / "07-term-library.md"

# ── 用户点名的敏感词（第 6 点）—— 作为**回归护栏**，防止以后又混进来。
#    ⛔ 这份清单只用于"扫源"，绝不写进任何提示词产物。
SENSITIVE = [
    # 未成年性化
    "萝莉", "正太", "幼女", "幼男", "童颜巨乳", "洛丽塔", "loli", "shotacon",
    # 军警制服
    "警服", "警帽", "军装", "军服", "制服诱惑",
    # 性暗示 / 成人用品
    "乳胶", "latex", "内裤", "丁字裤", "情趣", "rape", "性奴",
    # 涉毒
    "毒品", "冰毒", "大麻",
    # 血腥虐待
    "割腕", "上吊", "内脏外露",
]

# ── 已废除的旧概念（用户第 8 点）—— 产物里不得再出现
RETIRED = [
    "midjourney", "midjourney_params", "sd_words", "painting_tree",
    "SD通用", "负向词", "绘画分类树", "反向提示词", "negative prompt",
]

# 要素条数上限 —— 装配台经验：「若某格词太多，正确解法是拆成更细的格，
# 而不是把词埋进『不常用』」。把「有没有超标」变成测试，就不会退化成埋词。
MAX_GROUP_SIZE = 90

results = []


def add(level, title, detail=""):
    results.append((level, title, detail))


# ══════════════════════════════════════════════
# 断言 ① 源本身全绿
# ══════════════════════════════════════════════
def check_source(domains, problems, fails):
    if problems:
        add("FAIL", f"源解析告警 {len(problems)} 条",
            "\n".join("    " + p for p in problems[:15]))
    else:
        add("PASS", "源解析无告警（字段数 / 状态 / 坏字符 / 英文列）")

    if fails:
        add("FAIL", f"源体检不通过 {len(fails)} 项",
            "\n".join("    " + f.splitlines()[0] for f in fails))
    else:
        add("PASS", "源体检通过（无重复词 / 慎用都带原因 / 中文列都是中文）")


# ══════════════════════════════════════════════
# 断言 ②③④ 产物与源一致 ← 本脚本的核心
# ══════════════════════════════════════════════
def check_artifacts(domains, stats):
    missing = [p.relative_to(ROOT) for p in (TERMS, TERM_MD) if not p.exists()]
    if missing:
        add("FAIL", "产物不存在：" + " / ".join(str(m) for m in missing) +
            "　→ 跑 `python scripts/render_lexicon.py`")
        return None

    # ② terms.json 条数与结构
    data = json.loads(TERMS.read_text(encoding="utf-8"))
    terms = data["terms"]
    src_n = stats["terms"]
    if len(terms) != src_n:
        add("FAIL", f"产物条数 {len(terms)} ≠ 源条数 {src_n}",
            "    → 源改过但没重跑渲染器。跑 `python scripts/render_lexicon.py`")
    elif data["stats"]["domains"] != stats["domains"]:
        add("FAIL", "产物域数 ≠ 源域数")
    else:
        add("PASS", f"terms.json 与源一致（{src_n} 条 / {stats['domains']} 域）")

    # ③ 无幽灵词：产物里的每一条都能在源里找到
    src_set = collections.Counter()
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    src_set[(d["name"], g["name"], t["zh"])] += 1
    ghost = [t for t in terms if (t["s"], t["g"], t["zh"]) not in src_set]
    if ghost:
        add("FAIL", f"幽灵词 {len(ghost)} 条（产物有、源里没有）",
            "\n".join("    %s/%s %s" % (t["s"], t["g"], t["zh"]) for t in ghost[:12]))
    else:
        add("PASS", "无幽灵词（产物每一条都来自源）")

    # ④ 07 对照表条数与源一致
    md = TERM_MD.read_text(encoding="utf-8")
    md_n = len(re.findall(r"^- .+ → .+$", md, re.M))
    if md_n != src_n:
        add("FAIL", f"07 对照表条数 {md_n} ≠ 源条数 {src_n}",
            "    → 同上，重跑渲染器")
    else:
        add("PASS", f"07-term-library.md 与源一致（{md_n} 条）")

    # ⑨ 已废除概念不得残留
    hits = [k for k in RETIRED if k.lower() in md.lower()]
    if hits:
        add("FAIL", "07 对照表残留已废除概念：" + " / ".join(hits))
    else:
        add("PASS", "07 对照表无 Midjourney / SD / 绘画分类树残留")

    return data


# ══════════════════════════════════════════════
# 断言 ⑤ 域集合与固定顺序一致
# ══════════════════════════════════════════════
def check_domains(domains):
    names = [d["name"] for d in domains]
    unknown = set(names) - set(R.DOMAIN_ORDER)
    if unknown:
        add("FAIL", "未登记的域：" + " / ".join(sorted(unknown)),
            "    → 请同时补进 render_lexicon.py 的 DOMAIN_ORDER，否则顺序不稳")
    else:
        add("PASS", f"域集合与 DOMAIN_ORDER 一致（{len(names)} 域）")


# ══════════════════════════════════════════════
# 断言 ⑥ 要素大小与空壳
# ══════════════════════════════════════════════
def check_group_size(data):
    by = data["by_group"]
    over = {k: v for k, v in by.items() if v > MAX_GROUP_SIZE}
    if over:
        add("FAIL", f"大块超标（>{MAX_GROUP_SIZE} 条）：{len(over)} 个 —— 请拆成更细的格，⛔ 不要埋词",
            "\n".join("    %s  %d 条" % (k, v) for k, v in sorted(over.items(), key=lambda x: -x[1])))
    else:
        add("PASS", f"无大块超标（最大 {max(by.values())} 条 / 上限 {MAX_GROUP_SIZE}）")

    empty = [k for k, v in by.items() if v == 0]
    if empty:
        add("FAIL", "空要素：" + " / ".join(empty))
    else:
        add("PASS", "无空要素")


# ══════════════════════════════════════════════
# 断言 ⑦ 状态取值合法 + 全覆盖
# ══════════════════════════════════════════════
def check_status(data):
    bad = {t["st"] for t in data["terms"]} - set(R.VALID_STATUS)
    if bad:
        add("FAIL", "非法状态值：" + " / ".join(sorted(bad)))
    else:
        add("PASS", "状态取值合法（仅 " + " / ".join(R.VALID_STATUS) + "）")

    no_st = [t["zh"] for t in data["terms"] if not (t.get("st") or "").strip()]
    if no_st:
        add("FAIL", f"缺状态 {len(no_st)} 条：{' / '.join(no_st[:8])}")
    else:
        add("PASS", "全部词条都有状态（无「未标」）")


# ══════════════════════════════════════════════
# 断言 ⑧ 敏感词回归护栏
# ══════════════════════════════════════════════
def check_sensitive(domains):
    """敏感词回归护栏。

    ⛔ 匹配规则要看**词是怎么写的**：
       中文词用子串匹配（中文没有词边界）；ASCII 词必须用**词边界**，
       否则 `parapet`（女儿墙）会被 `rape` 命中、`skyscraper` 会被 `rape` 命中、
       `draped` 也会 —— 一行三个误报，护栏就废了（踩过）。
    中文里以「洛丽塔」代指未成年性化的一律收进 `SENSITIVE` 的中文支。
    """
    zh_terms = [w for w in SENSITIVE if re.search(r"[\u4e00-\u9fff]", w)]
    en_terms = [w for w in SENSITIVE if not re.search(r"[\u4e00-\u9fff]", w)]
    en_pat = re.compile(r"\b(" + "|".join(re.escape(w) for w in en_terms) + r")\b", re.I) if en_terms else None

    hits = []
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    zh, en = t["zh"], t["en"]
                    for w in zh_terms:
                        if w in zh or w in en:
                            hits.append(f"{w} ← {d['name']}/{g['name']} {zh}")
                    if en_pat:
                        for m in en_pat.findall(f"{en} {zh}"):
                            hits.append(f"{m} ← {d['name']}/{g['name']} {zh}")
    if hits:
        add("FAIL", f"敏感词回归 {len(hits)} 处", "\n".join("    " + h for h in hits[:15]))
    else:
        add("PASS", f"无敏感词（已扫 {len(SENSITIVE)} 个词）")


# ══════════════════════════════════════════════
# ⑫ 开源脱敏护栏
# ══════════════════════════════════════════════
# 词库会随公开仓库一起发布，**除署名外不留任何个人痕迹**。
#   ⚠️⚠️ **护栏词表本身也是泄露源。** 把要藏的词逐条写在这里，等于随仓库一起公开
#      —— 「清洗规则里的词往往正是想藏的东西」，本项目历史上就栽过这一跤。
#      所以拆成两半：**通用规则写死，个人标识走外部注入**。
#   ⚠️ **平台限定词也算** —— 把通用排版技巧绑上某个平台名，词条就从通用知识
#      变成了个人履历（谁的主阵地一目了然）。写成 `自媒体封面` 这类中性说法即可。
#   ⚠️ 圈护栏时只圈**特指写法**，不圈普通名词（普通名词会误伤词库里的正常词条）。
PRIVACY_PLATFORM = ["公众号", "小红书", "抖音", "视频号", "快手", "微博", "哔哩哔哩", "B站"]


def _load_private_words() -> list[str]:
    """个人标识**不进代码**，运行时注入。两个来源，任一存在即生效：

    · 环境变量 ``AI_IMAGE_PROMPT_PRIVACY_WORDS``（逗号分隔）
    · 本地文件 ``scripts/.privacy-words.txt``（一行一个，``#`` 开头为注释）

    两者都没有 → 返回空表，护栏只剩平台词。克隆本仓库的人没有这些词，
    护栏本来就该是空的；需要自查的人把词写进本地文件即可（该文件已 gitignore）。
    """
    words: list[str] = []
    for w in re.split(r"[,，]", os.environ.get("AI_IMAGE_PROMPT_PRIVACY_WORDS", "")):
        w = w.strip()
        if w and w not in words:
            words.append(w)
    local = Path(__file__).with_name(".privacy-words.txt")
    if local.is_file():
        for line in local.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and line not in words:
                words.append(line)
    return words


PRIVACY_SELF = _load_private_words()


def check_privacy(domains):
    hits = []
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    blob = f"{t['zh']} {t['en']} {t.get('note') or ''}"
                    for w in PRIVACY_PLATFORM + PRIVACY_SELF:
                        if w.lower() in blob.lower():
                            hits.append(f"{w} ← {d['name']}/{g['name']} {t['zh']}")
    if hits:
        add("FAIL", f"脱敏护栏命中 {len(hits)} 处（平台限定词 / 个人标识）",
            "\n".join("    " + h for h in hits[:15]) +
            "\n    → 改写成中性词（`[平台名]封面` → `自媒体封面`）；署名只允许出现在 README")
    else:
        add("PASS", f"无脱敏风险（平台词 {len(PRIVACY_PLATFORM)} 个 · 个人词 {len(PRIVACY_SELF)} 个）")
        if not PRIVACY_SELF:
            add("INFO", "个人词表为空，护栏当前只拦平台词",
                "    要拦自己的署名 / 账号名 / 真名，把词写进 scripts/.privacy-words.txt\n"
                "    （一行一个，# 开头为注释；该文件已 gitignore，不会进仓库），\n"
                "    或设环境变量 AI_IMAGE_PROMPT_PRIVACY_WORDS=词1,词2。\n"
                "    格式示例见 scripts/.privacy-words.example.txt")


# ══════════════════════════════════════════════
# ⑪ 跨文件「按标题引用」是否落到真实标题上
# ══════════════════════════════════════════════
# 本项目约定：跨文件引用一律按「标题」引用，不按节号（节号会因插入章节全部失效）。
# 改用标题之后，新风险是**改了标题忘改引用** —— 这种失效不报错，只有读到时才发现。
# 所以把它变成断言。

# 引用形态：`05` 的「影调」  /  01 的「装配顺序」  /  SKILL.md 的「交付格式」
_CITE = re.compile(r"`?((?:SKILL|README)\.md|\d{2})`?\s*的\s*[「【]([^」】\n]{2,40})[」】]")

# ⚠️ 匹配必须**容忍装饰差异**：引用通常会省略 ⛔ / ⭐ 和引号，写成核心词形。
#    例：`04` 的「硬信息一个字都不能丢」
#        真标题是 `⛔⛔ 用户明确说过的「硬信息」一个字都不能丢`
#    ⛔ 不规范化就会全是误报，断言也就废了。
_DECOR = re.compile(r"[⛔⭐⚠️※·「」『』\"“”'‘’()（）\[\]【】、,，。.：:；;！!？?—\-_/\\|~～]")


def _norm(s: str) -> str:
    return _DECOR.sub("", s).strip().lower()


def check_cross_refs():
    docs = [ROOT / "SKILL.md", ROOT / "README.md"]
    docs += sorted((ROOT / "references").glob("*.md"))
    docs = [p for p in docs if p.exists() and not p.name.startswith("07")]  # 07 是产物

    # 收集每个文档的全部标题（规范化后）
    titles: dict[str, list[str]] = {}
    for p in docs:
        ts = []
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^#{2,4}\s+(.*)", line)
            if m:
                ts.append(_norm(m.group(1)))
        titles[p.name] = ts

    def _resolve(tok: str) -> str:
        return {"01": "01-slots.md", "02": "02-style-atlas.md",
                "03": "03-light-composition.md", "04": "04-output-formats.md",
                "05": "05-quality-and-params.md", "06": "06-diagnosis.md",
                "SKILL.md": "SKILL.md", "README.md": "README.md"}.get(tok, "")

    bad = []
    for p in docs:
        for ln, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for tok, target in _CITE.findall(line):
                fn = _resolve(tok)
                if not fn or fn not in titles:
                    continue          # 指向产物或不存在的文件：不归这条管
                nq = _norm(target)
                if not nq:
                    continue
                if not any(nq in nt or nt in nq for nt in titles[fn] if nt):
                    bad.append(f"{p.name}:{ln}  →  {tok} 的「{target}」")

    if bad:
        add("FAIL", f"跨文件标题引用失效 {len(bad)} 处（目标文件没有这个标题）",
            "\n".join("    " + b for b in bad[:15]) +
            "\n    → 改引用，或把该标题恢复；⛔ 不要放进任何产物里")
    else:
        add("PASS", "跨文件标题引用全部有效")


# ══════════════════════════════════════════════
# ⑩ 状态分布（信息）
# ══════════════════════════════════════════════
def report_status(data):
    add("INFO", "状态分布", "    " + " · ".join(
        f"{k} {data['status_dist'][k]}" for k in R.VALID_STATUS if data["status_dist"].get(k)))


def main():
    quiet = "--quiet" in sys.argv[1:]

    try:
        domains, problems = R.parse_files()
    except R.Problem as e:
        print(f"✘ {e}")
        return 1
    fails, warns, stats = R.lint(domains)

    print(f"词库校验　　源 {stats['terms']} 条 / {stats['domains']} 域 "
          f"/ {stats['dimensions']} 维度 / {stats['groups']} 要素")
    print("=" * 62)

    check_source(domains, problems, fails)
    data = check_artifacts(domains, stats)
    check_domains(domains)
    if data:
        check_group_size(data)
        check_status(data)
    check_sensitive(domains)
    check_privacy(domains)
    check_cross_refs()
    if data and not quiet:
        report_status(data)

    fails_n = 0
    for level, title, detail in results:
        if quiet and level in ("PASS", "INFO"):
            continue
        mark = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️ ", "INFO": "ℹ️ "}[level]
        print("%s %s" % (mark, title))
        if detail:
            print(detail)
        if level == "FAIL":
            fails_n += 1

    print("=" * 62)
    n_pass = sum(1 for r in results if r[0] == "PASS")
    print("通过 %d · 失败 %d" % (n_pass, fails_n))
    if fails_n:
        print("\n❌ 有断言未通过 —— 修完再提交。")
        return 1
    print("\n✅ 全部断言通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
