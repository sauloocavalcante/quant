import pandas as pd
from utils.download_history import download_history
from datetime import date, timedelta


def start_date_for_period(period_dias_pregao: int, buffer_dias: int = 30) -> str:
    dias_corridos = int(period_dias_pregao * 1.45) + buffer_dias
    start = date.today() - timedelta(days=dias_corridos)
    return start.strftime("%Y-%m-%d")


def compute_sma(close: pd.Series, period: int = 200) -> pd.Series:
    return close.rolling(window=period, min_periods=period).mean()


def calculate_sma(
    ticker: str,
    sma_period: int = 200,
    start: str | None = None,
    auto_adjust: bool = True,
    multi_level_index: bool = False,
) -> pd.DataFrame:
    if start is None:
        start = start_date_for_period(sma_period)

    df = download_history(
        ticker=ticker,
        start=start,
        auto_adjust=auto_adjust,
        multi_level_index=multi_level_index,
    )

    df["SMA"] = compute_sma(df["Close"], period=sma_period)
    df["ABOVE_SMA"] = df["Close"] > df["SMA"]

    return df
