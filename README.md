# 投资工具箱 investment-toolbox

个人收藏整理：选股清单、LOF 套利观察、IBKR 自查。内容来自我收藏的 X 帖子，每条都标了原作者和日期。

## 内容

| 文件 | 是什么 |
| --- | --- |
| [checklists/stock-picking-five-indicators.md](checklists/stock-picking-five-indicators.md) | 选股五指标清单：股息 > 5%、毛利 > 40%、负债 < 30%、ROE > 20%、PEG < 1 |
| [checklists/lof-arbitrage-watchlist.md](checklists/lof-arbitrage-watchlist.md) | LOF 套利观察清单：玩法、盯过的品种、只玩限购的规矩 |
| [checklists/ibkr-self-check.md](checklists/ibkr-self-check.md) | IBKR 自查清单：W-8 多扣税、免佣、阶梯费用、碎股、闲置资金利率 |
| [scripts/screener.py](scripts/screener.py) | 五指标筛选小脚本骨架：读本地 CSV，按五指标打分，不联网、不接实盘 |

## 用法

```bash
python3 scripts/screener.py scripts/example.csv
```

CSV 列：`ticker,dividend_yield,gross_margin,debt_ratio,roe,peg`，数值用小数（5% 写 0.05）。

## 先说清楚

- **不是投资建议，不接实盘，不荐股。** 清单只是筛选和自查的起点。
- **数字会变，用时现查。** LOF 溢价、限购、利率这些每天都可能变，收藏里的数字是发帖当天的旧数，只能复盘，不能直接照做。
- 他人项目只作参考，不直接抄：Financial-API、daily-stock-analysis 这类仓库不在这里。
