import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as plt_sns
import os
import seaborn as sns

df = pd.read_csv("merged_data.csv")

os.makedirs('charts', exist_ok=True)

# Helper function mapping sentiment classification
def map_sentiment(sc):
    sc = str(sc).strip().lower()
    if 'fear' in sc:
        return 'Fear'
    elif 'greed' in sc:
        return 'Greed'
    else:
        return 'Neutral'

df['Fear_Greed'] = df['sentiment_class'].apply(map_sentiment)
# Filter out neutral for direct comparison, or keep it. Let's keep it but focus on Fear/Greed.

print("--- Overall Count by Sentiment ---")
print(df['Fear_Greed'].value_counts())

# 1. Performance: PnL and Win Rate
print("\n--- 1. Performance by Sentiment ---")
perf = df.groupby('Fear_Greed')[['daily_pnl', 'win_rate']].mean().reset_index()
print(perf)

sns.barplot(data=df[df['Fear_Greed'].isin(['Fear', 'Greed'])], x='Fear_Greed', y='daily_pnl')
plt.title('Average Daily PnL per Trader (Fear vs Greed)')
plt.savefig('charts/pnl_by_sentiment.png')
plt.close()

sns.boxplot(data=df[df['Fear_Greed'].isin(['Fear', 'Greed'])].dropna(subset=['win_rate']), x='Fear_Greed', y='win_rate')
plt.title('Win Rate Distribution (Fear vs Greed)')
plt.savefig('charts/win_rate_by_sentiment.png')
plt.close()

# 2. Behavior Changes: Trade Frequency, Volume, Long/Short Bias
print("\n--- 2. Behavior by Sentiment ---")
behavior = df.groupby('Fear_Greed')[['num_trades', 'avg_trade_size', 'total_volume', 'long_short_ratio']].median().reset_index()
print("Medians:\n", behavior)

sns.barplot(data=df[df['Fear_Greed'].isin(['Fear', 'Greed'])], x='Fear_Greed', y='num_trades', estimator=np.median)
plt.title('Median Trades per Day (Fear vs Greed)')
plt.savefig('charts/num_trades_by_sentiment.png')
plt.close()

# 3. Segmentation
# Segment traders based on their overall trading frequency
trader_freq = df.groupby('Account')['num_trades'].sum().reset_index()
freq_threshold = trader_freq['num_trades'].median()
frequent_traders = trader_freq[trader_freq['num_trades'] > freq_threshold]['Account']
df['Segment'] = np.where(df['Account'].isin(frequent_traders), 'Frequent', 'Infrequent')

print("\n--- 3. Behavior by Segment and Sentiment (Avg PnL) ---")
segment_perf = df.groupby(['Segment', 'Fear_Greed'])['daily_pnl'].mean().unstack()
print(segment_perf)

plt.figure(figsize=(8,6))
sns.barplot(data=df[df['Fear_Greed'].isin(['Fear', 'Greed'])], x='Segment', y='daily_pnl', hue='Fear_Greed')
plt.title('Average PnL by Segment and Sentiment')
plt.savefig('charts/segment_pnl_by_sentiment.png')
plt.close()

print("\nAnalysis generated and charts saved in 'charts' folder.")
