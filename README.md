# Hong Kong Fertility Trends (1991–2021)

## Research question

How did Hong Kong’s fertility level and number of live births change from 1991 to 2021, and how did the trend compare with the population replacement level?

## Dataset source and permissions

The dataset is a compact transcription of Tables 1, 4 and 5 in the Hong Kong Census and Statistics Department feature article [Fertility Trend in Hong Kong, 1991 to 2021](https://www.censtatd.gov.hk/en/data/stat_report/product/FA100090/att/B72302FA2023XXXXB0100.pdf), published in February 2023. The department’s website states that statistical data are freely usable unless otherwise noted; this repository keeps the source link and attribution with the derived CSV. No personal data, credentials, API keys or restricted datasets are included.

## Methods and tools

The analysis uses Python, pandas and Matplotlib. The script reads the CSV, plots the total fertility rate against the 2,100-per-1,000-women replacement benchmark, and plots live births together with the crude birth rate on a second axis. All charts can be regenerated from the included source file.

## Key findings

- The total fertility rate fell from 1,281 in 1991 to 772 in 2021, remaining below the replacement benchmark throughout the period.
- Live births fell from 68,281 in 1991 to 36,953 in 2021. The series temporarily peaked at 95,451 in 2011 before declining.
- The 2012 rebound in fertility was followed by a pronounced decline through 2021; the 2020–2021 fall also coincided with the COVID-19 period.

One limitation is that this is an observational, aggregated time series. It describes changes over time but cannot identify causal effects, and the source article’s definitions and coverage should be checked before combining these measures with other datasets.

## Repository contents

- `data/hk_fertility_1991_2021.csv` — cleaned, attributed analysis data.
- `src/analyze.py` — reproducible chart-generation script.
- `outputs/tfr_trend.png` — total fertility rate visualization.
- `outputs/births_and_crude_rate.png` — live births and crude birth rate visualization.

## Run the analysis

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/analyze.py
```

The script writes the two PNG files to `outputs/`.
