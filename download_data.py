import gdown

print("Downloading Bitcoin Market Sentiment Data...")
file_id1 = "1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf"
output1 = "sentiment_data.csv"
gdown.download(id=file_id1, output=output1, quiet=False)

print("Downloading Historical Trader Data (Hyperliquid)...")
file_id2 = "1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs"
output2 = "trader_data.csv"
gdown.download(id=file_id2, output=output2, quiet=False)

print("Download complete.")
