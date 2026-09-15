import pandas as pd
from utils.download_history import download_history


def compute_macd(
    close: pd.Series,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
) -> pd.DataFrame:
    """
    MACD = Moving Average Convergence Divergence.

    MACD_LINE  = EMA rapida (12) - EMA lenta (26)  -> momentum de curto prazo
    SIGNAL     = EMA(9) da propria MACD_LINE        -> versao suavizada dela
    HIST       = MACD_LINE - SIGNAL                 -> forca do momentum

    Quando MACD_LINE cruza SIGNAL de baixo pra cima (HIST vira positivo),
    o momentum de curto prazo acabou de virar pra alta. Cruzamento
    contrario = momentum virando pra baixa.
    """
    ema_fast = close.ewm(span=fast_period, adjust=False).mean()
    ema_slow = close.ewm(span=slow_period, adjust=False).mean()

    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    hist = macd_line - signal_line

    return pd.DataFrame({"MACD_LINE": macd_line, "SIGNAL": signal_line, "HIST": hist})


def calculate_macd(
    ticker: str,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
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

    macd_df = compute_macd(
        df["Close"],
        fast_period=fast_period,
        slow_period=slow_period,
        signal_period=signal_period,
    )

    df["MACD_LINE"] = macd_df["MACD_LINE"]
    df["MACD_SIGNAL"] = macd_df["SIGNAL"]
    df["HIST"] = macd_df["HIST"]

    return df
