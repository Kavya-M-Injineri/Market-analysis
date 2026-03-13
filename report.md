# Market Sentiment and Trader Behavior Analysis

## Overview
This report analyzes how market sentiment (Bitcoin Fear/Greed Index) affects trader behavior and performance on the Hyperliquid decentralized exchange. 

## Methodology
1. **Data Preparation**: Two datasets (Sentiment and Trader Data) were loaded, profiled, and aligned matching the `Timestamp IST` or `Timestamp` to proper daily boundaries.
2. **Metric Engineering**: We aggregated transaction-level data to daily metrics per trader, calculating daily PnL, number of trades, win rate (using positive PnL events), average trade size, and long/short volume ratios.
3. **Analysis**: We compared these exact metrics grouped by Fear vs. Greed days, analyzed how behavior shifted among sentiment days, and segmented traders into 'Frequent' vs 'Infrequent' cohorts based on median trade counts.
4. **Predictive Modeling**: Developed a Random Forest Classifier using Scikit-Learn to predict next-day profitability bucket based on a trailing combination of behavior and sentiment.

## Key Insights
1. **Dramatically Higher Profitability During Fear**: 
   Traders significantly outperformed on Fear days (Average Daily PnL: ~$209,372) compared to Greed days (Average Daily PnL: ~$90,988). The win rate also slightly improved (86.9% vs. 84.6%).
2. **Behavioral Metamorphosis (Volume & Frequency)**: 
   Traders were considerably more active when the market was fearful. The median number of trades per day skyrocketed to 2763 on Fear days, compared to just 283 on Greed days. The average trade size also increased from ~$2,786 (Greed) to ~$3,207 (Fear).
3. **Long/Short Demand Shifts**: 
   Traders maintained a highly balanced long/short position ratio (~0.99) during Fear days but exhibited a considerable short-selling bias (~0.64) during Greed days, suggesting traders aggressively short the market when public sentiment is overwhelmingly greedy.
4. **Cohort Dynamics (Frequent vs. Infrequent)**:
   Frequent traders capitalized far better on Fear regimes ($324K avg PnL vs. Infrequent traders at $94K). This gap shrank heavily during Greed days.

## Strategy Recommendations (Actionable Rules)
1. **"Ride the Fear Wave with Frequency"**: 
   *Rule of Thumb*: During Fear days, algorithmic and high-frequency systems should increase trade frequency and slightly scale up position sizes. Keep directional bias balanced (long/short ratio ~1.0). The data proves that elevated volatility during fear regimes heavily rewards active participation.
2. **"Cautious Greed Strategy"**: 
   *Rule of Thumb*: On Greed days, reduce position size (aligning with lower empirical avg trade size) and decrease trade frequency. If building a directional book, adopt a slight short bias to align with profitable historical precedents during greedy market extremes.

## Bonus: Predictive Model
A Random Forest Classifier was trained to predict whether a given trader account would be profitable the *next day* based on today's `num_trades`, `avg_trade_size`, `total_volume`, `win_rate`, and `sentiment`. 
* **Accuracy:** 87.5%
* **Feature Importance:** Available in `charts/feature_importances.png`. Trader-specific behavioral metrics (total volume, win rate) often override broad market sentiment strings when predicting individual next-day success.
