import pandas as pd


def run_for_many(
    tickers: list[str],
    calculate_fn,
    error_columns: list[str],
    **kwargs
) -> pd.DataFrame:
    dfs = []
    drop_columns = ["High", "Low", "Open", "Volume"]

    for ticker in tickers:
        try:
            df = calculate_fn(ticker=ticker, **kwargs)
            df = df.drop(columns=drop_columns, errors="ignore")
            df = df.tail(1).copy()
            df = df.reset_index()
            df.insert(0, "ticker", ticker)
            dfs.append(df)
        except Exception:
            dfs.append(pd.DataFrame(
                {"ticker": [ticker], **{col: [None] for col in error_columns}}
            ))

    return pd.concat(dfs, ignore_index=True)
