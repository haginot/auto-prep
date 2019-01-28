import pandas as pd


def select_column(df: pd.DataFrame, threshold: float):
    s = pd.Series([sum(s.isnull()) / s.size for k, s in df.iteritems()])
    return s[s <= threshold].index.tolist()
