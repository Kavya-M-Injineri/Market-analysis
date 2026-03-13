import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

st.set_page_config(page_title="Primetrade Analysis", layout="wide")

st.title("Primetrade.ai - Hyperliquid Trader Analysis")
st.markdown("Exploring the relationship between Bitcoin Fear/Greed Sentiment and Trader Behavior.")

@st.cache_data
def load_data():
    if os.path.exists('merged_data.csv'):
        return pd.read_csv('merged_data.csv')
    return None

df = load_data()

tab1, tab2, tab3 = st.tabs(["Overview & Data", "Analysis Charts", "Predictive Model"])

with tab1:
    st.header("Merged Dataset Overview")
    if df is not None:
        st.dataframe(df.head(100))
        st.write("Total Records:", len(df))
    else:
        st.error("merged_data.csv not found. Please run data_prep.py first.")

with tab2:
    st.header("Behavior & Performance by Sentiment")
    col1, col2 = st.columns(2)
    
    with col1:
        if os.path.exists("charts/pnl_by_sentiment.png"):
            st.image(Image.open("charts/pnl_by_sentiment.png"), caption="Average Daily PnL")
        if os.path.exists("charts/num_trades_by_sentiment.png"):
            st.image(Image.open("charts/num_trades_by_sentiment.png"), caption="Median Trades per Day")

    with col2:
        if os.path.exists("charts/win_rate_by_sentiment.png"):
            st.image(Image.open("charts/win_rate_by_sentiment.png"), caption="Win Rate Distribution")
        if os.path.exists("charts/segment_pnl_by_sentiment.png"):
            st.image(Image.open("charts/segment_pnl_by_sentiment.png"), caption="PnL by Trader Segment")

with tab3:
    st.header("Next-Day Profitability Model")
    if os.path.exists("charts/feature_importances.png"):
        st.image(Image.open("charts/feature_importances.png"), caption="Random Forest Feature Importances")
    
    if os.path.exists("model_output_utf8.txt"):
        with open("model_output_utf8.txt", 'r', encoding='utf-8') as f:
            st.code(f.read(), language='text')
    elif os.path.exists("model_output.txt"):
        with open("model_output.txt", 'r', encoding='utf-16le') as f:
             st.code(f.read(), language='text')

st.markdown("---")
st.markdown("Built for the Primetrade Evaluation.")
