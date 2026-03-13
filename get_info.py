import pandas as pd
import json

sentiment = pd.read_csv("sentiment_data.csv")
trader = pd.read_csv("trader_data.csv")

info = {
    "sentiment_cols": sentiment.columns.tolist(),
    "trader_cols": trader.columns.tolist(),
    "sentiment_head": sentiment.head(3).to_dict(orient="records"),
    "trader_head": trader.head(3).to_dict(orient="records")
}

with open("data_info.json", "w") as f:
    json.dump(info, f, indent=4)
