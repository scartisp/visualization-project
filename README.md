# Voter Turnout Demographics Visualization

Interactive analysis of U.S. voter turnout by race and household income, 1978–2024, built from three
U.S. Census Bureau datasets. [Live site](https://scartisp.github.io/visualization-project/) · Python,
Pandas, Plotly, SciPy.

## Overview

The three source datasets ship as `.xlsx` exports with inconsistent, non-tabular layouts — merged
header cells, embedded footnotes, and in one case, year and category encoded in the same column. The
`reformatData/` scripts turn each into a clean CSV; `visualizationOne/`, `visualizationTwo/`, and
`visualizationThree/` each consume those CSVs to produce one group of Plotly charts, statistically
validate what the chart appears to show, and write a self-contained HTML fragment. `index.html` embeds
all three fragments in a tabbed interface.

## Data sources

| File | Contents | Source |
|---|---|---|
| `hst_vote01.xlsx` | Voting-age population turnout by race, 1978–2024 | Census Bureau, Table A-1 |
| `tableA2.xlsx` | Household income by race, 2002–2024 | Census Bureau, Table A-2 |
| `vote07_2024.xlsx` | Turnout by household income bracket, 2024 only | Census Bureau, Table 7 |

## Data cleaning

**Recovering a header buried in one column (`reformatA2.py`).** `tableA2.xlsx` interleaves its two
header dimensions instead of giving each its own column: a row holding a race name (`"WHITE ALONE, NOT
HISPANIC"`) is followed by ~20 data rows for that race, each starting with a year, until the next race
label appears. Splitting this into proper `Year` and `Race` columns takes three steps:

1. Extract a leading 4-digit token from column 0 with `str.extract(r"^\s*(\d{4})")`. Rows that succeed
   are data rows; rows that fail (the race-label rows, which start with text) come back `NaN`.
2. Take column 0's text *only* on the rows where that extraction failed, and forward-fill it
   (`.where(...).ffill()`) down through the data rows beneath it — replicating, on flattened rows, what
   a merged Excel cell would have done for you natively.
3. Drop every row that still has no year — those are the now-redundant label rows, having already
   propagated their value forward.

The same script locates the sheet's footnote block with a second regex (`^N Not available\.`) so it
never gets parsed as data.

**Reconciling duplicate years.** The Census re-surveyed mid-2013 (an added post-hurricane sample) and
changed its income-imputation methodology in 2017, and `tableA2.xlsx` records both the original and
revised figures for those two years under the same year/race label. `visualizationOne.py` walks the
cleaned rows for each race and skips the earlier of the two duplicates in both cases — a targeted,
hand-checked fix rather than a generic "drop duplicate years" rule, since a generic rule would silently
mask any *other* kind of duplicate the source introduces later without anyone noticing.

**Other reformatting.** `hst_vote01.xlsx` and `vote07_2024.xlsx` needed comparatively mechanical
cleanup: slicing out header/footer boilerplate by row position, dropping the margin-of-error columns
interleaved between data columns, replacing the Census's own `"N"` (not available) sentinel with a real
`NaN`, and relabeling verbose income-bracket strings (`"$150,000 to $199,999"`) to short, consistent
keys reused across all three visualizations.

## Statistical validation

Each chart's headline claim is backed by a `scipy.stats.pearsonr` computation rather than left as a
visual read of the plot:

- **Pooled vs. per-group correlation are both reported, deliberately.** The four race groups sit at
  different absolute income levels, so a coefficient computed across all of them pooled together and a
  coefficient computed within each group separately can disagree — pooling can flatten or even invert a
  real within-group relationship. Both figures are shown side by side rather than picking whichever one
  reads better.
- **Categorical axes get a numeric proxy, with a sensitivity check.** The 2024 income-bracket chart's
  x-axis is a set of labeled ranges, not a number, so a correlation isn't defined against it directly.
  Each bracket is mapped to its numeric midpoint before computing `r`. The top bracket (`"$150,000 and
  over"`) is open-ended, so before trusting the result, the script recomputes `r` after swapping in
  several different stand-in values ($160k–$250k) for that bracket — the reported coefficient only
  holds if it doesn't meaningfully move under that swap, and it doesn't.
- **No coefficient is forced where one isn't valid.** Race is an unordered category with no numeric
  axis, so the race-only bar charts report no Pearson r at all, rather than computing one against an
  arbitrary category ordering.

## Visualization design

- **Black chart background, `px.colors.qualitative.G10` palette.** Chosen for contrast — the animated
  scatter plots in particular lose points against a white background at this marker size.
- **Line charts (`visualizationOne`)** for the two long-run trends (turnout and income by race, both
  over time), kept as two separate charts rather than one dual-axis chart to avoid conflating two
  different units on one y-axis.
- **Animated scatter (`visualizationTwo`)** to show income vs. turnout evolving year over year without
  adding a third spatial dimension; split into three separate charts (all years / primary years /
  midterm years) because midterm turnout runs low enough to compress the primary-year trend when both
  share one frame range.
- **Bar charts (`visualizationThree`)** for the single-year 2024 snapshot — grouped, not stacked, since
  each race's income-bracket distribution isn't a component of one shared whole.
- Every fragment is written to its `.html` file by hand-assembling the page around the Plotly output
  (`to_html(full_html=False, ...)`), so hand-authored copy — the stat paragraphs, notes, and return
  link — survives re-running the generator script.

## Repo structure

```
data/                   Raw .xlsx exports and their cleaned .csv output
reformatData/            One cleaning script per raw dataset
visualizationOne/         Line charts: turnout and income by race over time
visualizationTwo/         Animated scatter: income vs. turnout by race and year
visualizationThree/       Bar charts: 2024 snapshot by income bracket and by race
styles/                  Shared CSS for the landing page and chart pages
index.html               Landing page — tabbed interface embedding the three chart pages
```

## Running locally

```
pip install pandas plotly scipy openpyxl
cd visualizationOne && python3 visualizationOne.py      # regenerates lineCharts.html
cd ../visualizationTwo && python3 visualizatinoTwo.py   # regenerates scatterPlots.html
cd ../visualizationThree && python3 visualizationThree.py  # regenerates visualizationThree.html
```

Then serve the repo root (`python3 -m http.server`) and open `index.html` — opening it directly via
`file://` will not load the embedded chart frames.

## Findings

No strong pooled correlation between race and income jointly predicts turnout — but race and income
each carry a significant, independent relationship to turnout on their own. See the [live
site](https://scartisp.github.io/visualization-project/) for the full breakdown, per-race figures, and
caveats on data completeness.

## Limitations & possible extensions

- Turnout-by-income-bracket data is only available for 2024; extending that relationship across time
  would need an equivalent historical source.
- All race figures use single-race respondents only, since one of the three source datasets doesn't
  track multiple-race respondents — excluding that group keeps the datasets comparable but understates
  the full population.
