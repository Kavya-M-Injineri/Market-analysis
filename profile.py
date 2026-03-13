import pandas as pd

print("--- Sentiment Data Profile ---")
sentiment = pd.read_csv("sentiment_data.csv")
print("Shape:", sentiment.shape)
print("Columns:", sentiment.columns.tolist())
print("\nMissing Values:\n", sentiment.isnull().sum())
print("\nDuplicates:", sentiment.duplicated().sum())
print("\nHead:\n", sentiment.head())

print("\n\n--- Trader Data Profile ---")
trader = pd.read_csv("trader_data.csv")
print("Shape:", trader.shape)
print("Columns:", trader.columns.tolist())
print("\nMissing Values:\n", trader.isnull().sum())
print("\nDuplicates:", trader.duplicated().sum())
print("\nHead:\n", trader.head())
