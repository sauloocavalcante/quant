import streamlit as st
from config.tickers import tickers_list
from indicators.rsi_same_day_df import rsi_same_day_df
from utils.merged import merged_df

st.title("📊 Acompanhe seu portfólio - Tabela RSI")

tickers = tickers_list

# tickers = [
#     "CMIG4.SA",
#     "BBAS3.SA",
# ]

st.dataframe(merged_df, width="stretch")
