from indicators.rsi import calculate_rsi
import pandas as pd


def rsi_same_day(
    ticker: str,
    buy_below: float,
    sell_above: float,
    rsi_period: int = 14,
    start: str = "2026-01-01",
    auto_adjust: bool = True,
) -> pd.DataFrame:

    rsi = calculate_rsi(
        ticker=ticker,
        buy_below=buy_below,
        sell_above=sell_above,
        rsi_period=rsi_period,
        start=start,
        auto_adjust=auto_adjust,
    )

    last_index = rsi.index[-1]
    last_price = float(rsi.loc[last_index, "Close"])
    last_rsi = float(rsi.loc[last_index, "RSI"])

    if last_rsi < buy_below:
        signal = "BUY"
    elif last_rsi > sell_above:
        signal = "SELL"
    else:
        signal = "HOLD"

    result = pd.DataFrame(
        {
            "signal": [signal],
            "ticker": [ticker],
            "date": [str(last_index.date())],
            "price": [last_price],
            "rsi": [last_rsi],
        }
    )

    return result
