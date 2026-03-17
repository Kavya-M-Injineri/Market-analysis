#  Hyperliquid Trader Sentiment Analysis..........

> **How does Bitcoin market fear and greed shape trader behavior and profitability on Hyperliquid?**  
> This project answers that — with data, statistics, and a predictive model.

---

## What This Project Does

This repository mines the relationship between the **Bitcoin Fear & Greed Index** and real trader activity on **Hyperliquid**, a decentralized perpetuals exchange. It extracts, processes, and models daily trader behavior to surface patterns that matter:

- Do traders perform better during Fear or Greed?
- Does sentiment shift long/short bias?
- Can we predict next-day profitability from today's sentiment?

---

## Project Structure

```
├── download_data.py      # Fetches datasets from Google Drive
├── data_prep.py          # Cleans, aligns, and merges CSVs → merged_data.csv
├── analysis.py           # Statistical analysis + chart generation → charts/
├── model.py              # Random Forest classifier for next-day profitability
├── report.md             # Full findings, insights, and strategy frameworks
└── charts/               # Auto-generated visualization outputs (.png)
```

---

## Quickstart

### 1. Set Up Environment

```bash
python -m venv venv
.\venv\Scripts\activate       # Windows
# source venv/bin/activate    # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn gdown
```

### 3. Run the Pipeline

```bash
# Step 1 — Download raw data
python download_data.py
# → Produces: sentiment_data.csv, trader_data.csv

# Step 2 — Process and merge
python data_prep.py
# → Produces: merged_data.csv

# Step 3 — Analyze and visualize
python analysis.py
# → Produces: charts/*.png

# Step 4 — Predictive model (bonus)
python model.py
# → Produces: charts/feature_importances.png
```

---

## Key Metrics Computed

| Metric | Description |
|---|---|
| **Win Rate** | % of profitable trades per trader per day |
| **Daily PnL** | Aggregate realized profit/loss per day |
| **Long/Short Bias** | Directional skew of open positions |
| **Trader Segment** | Behavioral classification by activity patterns |

---

## Deliverables

| File | Contents |
|---|---|
| `report.md` | Methodology, 4 core insights, 2 strategy frameworks, model explanation |
| `charts/` | All generated visualizations |
| `merged_data.csv` | Final processed dataset ready for analysis |

---

## Tech Stack

`Python` · `Pandas` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `gdown`
