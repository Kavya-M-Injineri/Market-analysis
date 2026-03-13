# Hyperliquid Trader Sentiment Analysis

This repository contains the data extraction, preprocessing, analysis, and modeling scripts to understand how Bitcoin Fear/Greed market sentiment correlates with trader behavior and profitability on Hyperliquid.

## Project Structure
- `download_data.py`: Automates downloading the datasets sequentially from Google Drive.
- `data_prep.py`: Processes the CSVs, aligns timestamps to daily level, calculates key metrics (Win Rates, Daily PnL, Long/Short Bias), and merges them into `merged_data.csv`.
- `analysis.py`: Runs statistical comparisons grouped by sentiment, maps trader segments, and saves visualizations to the `charts/` directory.
- `model.py`: Trains a classification model (Random Forest) to predict next-day trader profitability.
- `report.md`: Summarizes methodology, uncovers 4 insights, proposes 2 actionable strategy frameworks, and explains the bonus model.
- `charts/`: Directory automatically generated containing the plots.

## Setup Requirements

1. **Python Virtual Environment** (Recommended)
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. **Install Dependencies**
   ```cmd
   pip install pandas matplotlib seaborn scikit-learn gdown
   ```

## Instructions to Run

1. **Download the Data**
   Run the download script to fetch data from the provided GDrive links:
   ```cmd
   python download_data.py
   ```
   *(Two files: `sentiment_data.csv` and `trader_data.csv` will be downloaded).*

2. **Prepare Data & Calculate Metrics**
   ```cmd
   python data_prep.py
   ```
   *(Will generate `merged_data.csv`).*

3. **Run Analysis & Generate Charts**
   ```cmd
   python analysis.py
   ```
   *(Check the `charts/` directory for `.png` outputs).*

4. **Predictive Modeling (Bonus)**
   ```cmd
   python model.py
   ```
   *(Evaluates the Random Forest model and generates `charts/feature_importances.png`).*

## Key Deliverables
Please review `report.md` for the analysis answers, findings, and strategy formulation per the evaluation criteria.
