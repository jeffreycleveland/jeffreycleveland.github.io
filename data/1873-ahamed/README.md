# 1873 (Liaquat Ahamed) — quantitative claims, extracted

Every number stated in a set of reading highlights from Liaquat Ahamed's *1873*, pulled
out into a chart-ready form. Two files:

| File | What it is | Rows |
|---|---|---|
| `claims.csv` | Every quantitative claim in the highlights, one row each, with the verbatim sentence it came from | 152 |
| `series.csv` | The subset that plots directly, reshaped into tidy long format and grouped into 22 candidate charts | 100 |

## `claims.csv`

| Column | Notes |
|---|---|
| `id` | `C001`–`C152`. `series.csv` points back here via `claim_ids`. |
| `category` | `boom`, `bubble`, `panic`, `deflation`, `debt`, `money`, `flows`, `banking`, `returns`, `infra`, `trade`, `politics` |
| `region` | Country or market. Some claims are explicitly multi-country (`Britain/US/France/Germany`). |
| `metric` | What is being measured. |
| `unit` | See the unit list below. |
| `period_start`, `period_end` | Equal for point-in-time facts. Some are decade labels (`1840s`) or spans (`1848-1873`) rather than years — the book often states them that way. |
| `value_start`, `value_end` | `value_end` is blank for point-in-time facts. |
| `pct_change` | Populated only where the book states a change, or where it follows arithmetically from the two values. |
| `chart_ready` | `yes` on the 91 claims worth plotting; `no` on the rest (still useful as annotation or footnote material). |
| `quote` | The sentence the number came from, so any figure can be traced without reopening the book. |

## `series.csv`

Tidy long format — one observation per row, so it feeds straight into ggplot/Vega/matplotlib
without reshaping.

| Column | Notes |
|---|---|
| `series_id` | One of the 22 chart candidates listed below. |
| `series_label` | A working chart title. |
| `suggested_chart` | `line`, `bar`, `stacked_bar`, `slope`, `dumbbell`, `area`. A suggestion, not a constraint. |
| `region` | Doubles as the series/legend key within a chart. |
| `unit` | See below. |
| `period` | Ordered label for the x-axis. Not always a clean date — the source often gives spans. |
| `value` | Numeric. |
| `basis` | **Read this before plotting.** `stated` / `derived` / `assumed` — see below. |
| `claim_ids` | Back-reference into `claims.csv`. |

### The `basis` column

- **`stated` (68 rows)** — the number appears in the book as written.
- **`derived` (29 rows)** — computed from a stated percentage change or ratio in order to
  anchor an index. Example: the book says Vienna's listed stocks "had gone up an eyewatering
  300 percent over the previous three years," so the 1870 point is set to 25 against a 1873
  peak of 100. Arithmetic only, but the level is a construction, not a quotation.
- **`assumed` (3 rows)** — an anchor the book does not supply. All three are the U.S. line in
  `tariffs_manufactures`, held flat at 40% through the boom years on the strength of
  "maintaining tariffs of 40 percent or more... even during the boom years." Replace with a
  real series before publishing.

Where the book gave no starting level at all, no starting point was invented: French grain
tariffs (`C130`) carry only their 1890s endpoint.

### The 22 chart candidates

| `series_id` | Idea |
|---|---|
| `savings_rate` | Savings rates in four countries, 1840s → 1860s — the fuel for the boom |
| `real_rates` | London long real rates halving, pre-1840 → 1850s-60s |
| `infra_investment` | Global infrastructure investment, $1bn/yr → $4bn/yr |
| `boom_index` | GDP, world trade and the bond market indexed to 1848/1850 |
| `growth_acceleration` | Trend growth vs. the 1872–73 blow-off in output and trade |
| `exchange_size` | London $12bn vs. Paris $8bn vs. New York $4bn |
| `bubble_run_up` | Four bubbles on one peak-indexed axis: tulips, British rails, Vienna, Berlin |
| `vienna_land` | Viennese land prices, pre-boom vs. 1873 peak |
| `german_float` | Gründerjahre company formation, 850 founded / 450 floated |
| `panic_1873_stocks` | Western Union, NY Central, Union Pacific through September–November 1873 |
| `rr_bond_default` | Cumulative default rate on the $2.2bn of listed U.S. railway bonds |
| `price_level` | The great deflation, 1873 = 100, in three variants |
| `silver_price` | Silver, $1.32/oz (1872) → $0.83/oz (1892) |
| `uk_capital_outflows` | British capital exports: $500m → <$100m → back to $500m |
| `equity_returns` | Real equity returns, the quarter century before vs. after 1873 |
| `transport_costs` | Freight costs per bushel — the *other* deflation |
| `tariffs_manufactures` | Europe abandons free trade, 1850 → 1890s |
| `tariffs_grain` | Grain tariffs after the price collapse |
| `egypt_debt` | Egypt's $500m debt stack at default, by creditor type |
| `rothschild_scale` | Rothschild capital and profits, 1815 → 1900 |
| `bank_capital_1865` | Rothschild $150m vs. Baring $15m vs. Jay Cooke $10m |
| `then_and_now` | The book's own comparison: 1870s railway bonds ≈ 2026 tech capex |

## Units and conventions

All dollar figures are **nominal contemporary U.S. dollars**, normalised to
**millions** (`usd_million`) wherever the underlying claim was in millions or billions, so
$2.2 billion of railway bonds is stored as `2200`. Smaller sums stay in whole dollars (`usd`).

Ahamed gives one conversion factor for the whole book: **multiply 1870s dollars by 1,200** for
2026 magnitudes. Rows already expressed on that basis are tagged `usd_million_2026` — there
are three, all in the `then_and_now` series, and they are the book's own arithmetic rather
than mine.

Full unit list: `acres`, `cents_on_the_dollar`, `cents_per_bushel`, `count`, `days`,
`index_1848_100`, `index_1850_100`, `index_1870_100`, `index_peak_100`, `miles`,
`miles_per_year`, `months`, `percent`, `percent_growth`, `percent_of_gdp`,
`percent_per_year`, `persons`, `ratio`, `usd`, `usd_million`, `usd_million_2026`,
`usd_per_mile`, `usd_per_ounce`, `usd_per_share`, `usd_per_sq_ft`, `years`.

## Caveats

1. **These are the book's figures, not independently sourced data.** Ahamed is working from
   nineteenth-century statistics that are themselves estimates, and the highlights carry no
   footnotes. Anything headed for publication should be re-sourced.
2. **The source is a highlight set, not the full book.** A number Ahamed states in an
   unhighlighted passage is not here.
3. **Periods are as loose as the prose.** Many claims are anchored to "the early 1870s" or
   "the quarter century before 1873" rather than a year. The period labels preserve that
   looseness rather than papering over it with a false precision.
4. **Ranges were collapsed to midpoints** in a few places where a single value was needed to
   plot — world prices falling "20 to 25 percent" is stored as −22.5%, European manufacturing
   duties pushed back to "15 to 20 percent" as 17.5%. Both retain the full range in the quote.
5. `series.csv` values marked `derived` or `assumed` are constructions. See above.

## Rebuilding

Generated by `build.py` and `build_series.py` (kept alongside the CSVs). Edit the claim
tuples and re-run; both scripts are self-contained and write into this directory.
