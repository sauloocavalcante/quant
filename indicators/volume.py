import pandas as pd
from utils.download_history import download_history


def compute_volume_ratio(volume: pd.Series, period: int = 20) -> pd.Series:
    """
    Razao entre o volume do dia e a media movel de volume dos ultimos
    `period` dias. Ratio > 1 significa volume acima do normal (mais
    participantes concordando com o movimento de preco do dia); ratio < 1
    significa volume fraco (movimento pode ser menos confiavel).
    """
    avg_volume = volume.rolling(window=period, min_periods=period).mean()
    ratio = volume / avg_volume
    return ratio


def calculate_volume(
    ticker: str,
    volume_period: int = 20,
    start: str = "2026-01-01",
    auto_adjust: bool = True,
    multi_level_index: bool = False,
) -> pd.DataFrame:
    df = download_history(
        ticker=ticker,
        start=start,
        auto_adjust=auto_adjust,
        multi_level_index=multi_level_index,
    )

    df["VOL_SMA"] = (
        df["Volume"].rolling(window=volume_period, min_periods=volume_period).mean()
    )

    df["VOL_RATIO"] = compute_volume_ratio(df["Volume"], period=volume_period)

    return df
