from pandas import DataFrame
from pandas import read_csv
from random import sample


def csv_sampling(file: str, size: int) -> DataFrame:
    n = read_csv(file, usecols=[0]).shape[0]
    skiprows = sorted(sample(range(1,n+1), n-size))
    df = read_csv(file, skiprows=skiprows)
    return df
