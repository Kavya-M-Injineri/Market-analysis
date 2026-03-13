import pandas as pd
import numpy as np

print("Loading Data...")
sentiment = pd.read_csv("sentiment_data.csv")
trader = pd.read_csv("trader_data.csv")

# Sentiment Date Parsing
sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# Trader Date Parsing
# Some timestamps might be messed up, we'll use 'Timestamp' in ms primarily or IST
trader['datetime'] = pd.to_datetime(trader['Timestamp'], unit='ms', errors='coerce')
# For some reason, if Timestamp is nan, try parsing IST:
mask = trader['datetime'].isna()
if mask.any():
    trader.loc[mask, 'datetime'] = pd.to_datetime(trader.loc[mask, 'Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce')

trader['date'] = trader['datetime'].dt.date

# Calculate Win (1 if PnL > 0, else 0)
trader['is_win'] = (trader['Closed PnL'] > 0).astype(int)
trader['is_loss'] = (trader['Closed PnL'] < 0).astype(int)
trader['has_pnl'] = (trader['Closed PnL'] != 0).astype(int)

trader['is_long'] = (trader['Direction'].str.lower() == 'buy').astype(int)
trader['is_short'] = (trader['Direction'].str.lower() == 'sell').astype(int)

long_vol = trader['Size USD'] * trader['is_long']
short_vol = trader['Size USD'] * trader['is_short']
trader['Long_Volume'] = long_vol
trader['Short_Volume'] = short_vol

print("Aggregating...")
# Group by date and Account
daily_trader = trader.groupby(['date', 'Account']).agg(
    daily_pnl=('Closed PnL', 'sum'),
    num_trades=('Trade ID', 'count'),
    avg_trade_size=('Size USD', 'mean'),
    total_volume=('Size USD', 'sum'),
    wins=('is_win', 'sum'),
    losses=('is_loss', 'sum'),
    pnl_events=('has_pnl', 'sum'),
    long_volume=('Long_Volume', 'sum'),
    short_volume=('Short_Volume', 'sum')
).reset_index()

# Calculate Win Rate (wins / pnl_events), defaults to 0 if no pnl events
daily_trader['win_rate'] = np.where(daily_trader['pnl_events'] > 0, 
                                    daily_trader['wins'] / daily_trader['pnl_events'], 
                                    np.nan)

# Long/Short ratio
daily_trader['long_short_ratio'] = np.where(daily_trader['short_volume'] > 0,
                                            daily_trader['long_volume'] / daily_trader['short_volume'],
                                            np.nan)

print("Merging with Sentiment...")
merged = pd.merge(daily_trader, sentiment[['date', 'value', 'classification']], on='date', how='inner')
merged.rename(columns={'value': 'sentiment_value', 'classification': 'sentiment_class'}, inplace=True)

print("Saving merged_data.csv...")
merged.to_csv("merged_data.csv", index=False)

print("Merged Data Info:")
print(merged.info())
print("\nUnique Sentiment Classes in merged data:", merged['sentiment_class'].unique())
