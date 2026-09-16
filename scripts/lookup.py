# -*- coding: utf-8 -*-
"""
在词库里按分类或关键词查候选词，输出中英对照。

用法：
    python scripts/lookup.py --list
    python scripts/lookup.py --section 风格
    python scripts/lookup.py --group 天气
    python scripts/lookup.py --kw 逆光
    python scripts/lookup.py --kw rim
    python scripts/lookup.py --group 发型 --limit 30
    python scripts/lookup.py --group 风格 --json
"""
import argparse
import json
import sys
from pathlib import Path

TERMS = Path(__file__).resolve().parent.parent / "assets" / "terms.json"


def load():
    if not TERMS.exists():
        sys.exit(f"找不到词表 {TERMS}，先跑 scripts/build_terms.py 生成。")
    return json.loads(TERMS.read_text(encoding="utf-8"))


def fmt(rec):
    tail = ""
    if rec.get("alt"):
        tail = "　(亦作: " + "; ".join(rec["alt"]) + ")"
    return f"- {rec['zh']} → {rec['en']}{tail}"


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--list", action="store_true", help="列出所有分类与词条数")
    ap.add_argument("--section", help="按大类过滤，如 风格 / 主体 / 场景")
    ap.add_argument("--group", help="按小类过滤，支持部分匹配，如 天气 / 发型")
    ap.add_argument("--kw", help="按中英文关键词模糊查")
    ap.add_argument("--limit", type=int, default=200, help="最多输出多少条，默认 200")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    data = load()
    terms = data["terms"]

    if args.list or not any([args.section, args.group, args.kw]):
        print("== 分类骨架 ==")
        stat = {}
        for r in terms:
            stat.setdefault(r["s"], {}).setdefault(r["g"], 0)
            stat[r["s"]][r["g"]] += 1
        for s, gs in stat.items():
            total = sum(gs.values())
            print(f"[{s}] 共 {total}")
            for g, n in gs.items():
                print(f"   - {s}/{g}  ({n})")
        print(f"\n总计 {data['stats']['unique']} 条")
        print("另有：midjourney_params %d 条、sd_words %d 条、painting_tree %d 条"
              % (len(data["midjourney_params"]), len(data["sd_words"]), len(data["painting_tree"])))
        print("\n查法：--group <小类名，可部分匹配> 或 --kw <关键词>")
        return

    sel = terms
    title = []
    if args.section:
        sel = [r for r in sel if args.section in r["s"]]
        title.append(f"大类={args.section}")
    if args.group:
        sel = [r for r in sel if args.group in r["g"]]
        title.append(f"小类≈{args.group}")
    if args.kw:
        k = args.kw.lower()
        sel = [r for r in sel
               if k in r["zh"].lower() or k in r["en"].lower()
               or any(k in a.lower() for a in r.get("alt", []))]
        title.append(f"关键词={args.kw}")

    if not sel:
        print("没查到。先用 --list 看看分类名。")
        return

    if args.json:
        print(json.dumps(sel[: args.limit], ensure_ascii=False, indent=1))
        return

    print(f"# 命中 {len(sel)} 条　({'，'.join(title)})")
    cur = None
    for r in sel[: args.limit]:
        if r["s"] != cur:
            print(f"\n[{r['s']}]")
            cur = r["s"]
        print(f"  {r['g']} | " + fmt(r)[2:])
    if len(sel) > args.limit:
        print(f"\n…还有 {len(sel) - args.limit} 条，用 --limit 调大")


if __name__ == "__main__":
    main()
