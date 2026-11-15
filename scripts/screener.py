#!/usr/bin/env python3
"""Five-indicator stock screener (skeleton).

Reads a local CSV and scores each row against the five indicators from
checklists/stock-picking-five-indicators.md:
    dividend yield > 5%, gross margin > 40%, debt ratio < 30%,
    ROE > 20%, PEG < 1.

No network, no API key, no real trading. Values are decimals
(5% is written as 0.05).

Usage:
    python3 screener.py example.csv
"""

import csv
import sys

CHECKS = [
    ("dividend_yield", lambda v: v > 0.05, "股息 > 5%"),
    ("gross_margin", lambda v: v > 0.40, "毛利 > 40%"),
    ("debt_ratio", lambda v: v < 0.30, "负债 < 30%"),
    ("roe", lambda v: v > 0.20, "ROE > 20%"),
    ("peg", lambda v: v < 1.0, "PEG < 1"),
]


def screen(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    results = []
    for row in rows:
        passed = []
        failed = []
        for key, test, label in CHECKS:
            try:
                value = float(row[key])
            except (KeyError, TypeError, ValueError):
                failed.append(f"{label}（缺数据）")
                continue
            (passed if test(value) else failed).append(label)
        results.append((row.get("ticker", "?"), len(passed), passed, failed))
    return results


def main(argv):
    if len(argv) != 2:
        print("用法: python3 screener.py <csv 文件>")
        print("列: ticker,dividend_yield,gross_margin,debt_ratio,roe,peg")
        return 2
    results = screen(argv[1])
    print(f"{chr(20195)+chr(30721):<14}{chr(36890)+chr(36807):<8}未通过")
    print("-" * 60)
    for ticker, n, passed, failed in results:
        mark = "✅ 进观察池" if n == len(CHECKS) else ""
        print(f"{ticker:<14}{n}/5      {chr(44).join(failed) or chr(20840)+chr(37096)+chr(36890)+chr(36807)} {mark}")
    watch = sum(1 for _, n, _, _ in results if n == len(CHECKS))
    print("-" * 60)
    print(f"共 {len(results)} 只，{watch} 只五项全过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
