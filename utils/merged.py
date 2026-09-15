from indicators.rsi_same_day_df import rsi_same_day_df
from indicators.sma import calculate_sma
from indicators.macd import calculate_macd
from indicators.volume import calculate_volume
from utils.run_many import run_for_many
from config.tickers import tickers_list

tickers = tickers_list

df = rsi_same_day_df(
    tickers=tickers,
    buy_below=30,
    sell_above=70,
    rsi_period=14,
    start="2026-01-01",
    auto_adjust=True,
)

sma = run_for_many(
    tickers_list,
    calculate_sma,
    error_columns=["Close", "SMA", "ABOVE_SMA"],
    sma_period=200,
)

volume = run_for_many(
    tickers_list,
    calculate_volume,
    error_columns=["Close", "VOL_SMA", "VOL_RATIO"],
    volume_period=20,
)

macd = run_for_many(
    tickers_list,
    calculate_macd,
    error_columns=["Close", "MACD_LINE", "MACD_SIGNAL", "HIST"],
)

keys = ["ticker"]

merged_df = (
    df.merge(sma.drop(columns=["Close", "Date"]), on=keys, how="outer")
    .merge(volume.drop(columns=["Close", "Date"]), on=keys, how="outer")
    .merge(macd.drop(columns=["Close", "Date"]), on=keys, how="outer")
)

merged_df
