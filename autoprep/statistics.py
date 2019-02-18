import pandas as pd
import numpy as np


class Stats:
    """
    TODO
    Create Stat each DataType and
    each Statistical DataType

    """

    def __init__(self, data: pd.Series):
        self.__data = data
        # Groupby Statistic
        self.__value_counts_with_nan = self.__data.value_counts(dropna=False)
        self.__value_counts_without_nan = self.__value_counts_with_nan.loc[self.__value_counts_with_nan.index.dropna()]
        self.__distinct_count_with_nan: int = self.__value_counts_with_nan.count()
        # Common
        self.__count = None
        self.__distinct_count = None
        self.__n_missing = None
        self.__p_missing = None
        self.__n_infinite = None
        self.__p_infinite = None
        self.__is_unique = None
        self.__memory_usage = None
        # ???
        self.__mode = None
        self.__p_unique = None
        # Numerical
        self.__min = None
        self.__max = None
        self.__range = None
        self.__mean = None
        self.__std = None
        self.__variance = None
        self.__percentile_5 = None
        self.__percentile_25 = None
        self.__percentile_50 = None
        self.__percentile_75 = None
        self.__percentile_95 = None
        self.__iqr = None
        self.__kurtosis = None
        self.__skewness = None
        self.__sum = None
        self.__mad = None
        self.__cv = None
        self.__n_zeros = None
        self.__p_zeros = None
        # Categorical
        self.__value_counts = None
        self.__top = None
        self.__freq = None


class NumericStats(Stats):
    def dtype_stats(self):
        self.__mean = self.__data.mean()
        self.__std = self.__data.std()
        self.__variance = self.__data.var()
        self.__min = self.__data.min()
        self.__max = self.__data.max()
        self.__range = self.__max - self.__min
        # self.__percentile = self.__data.dropna().quantile()
        self.__iqr = self.__percentile_75 - self.__percentile_25
        self.__kurtosis = self.__data.kurt()
        self.__skewness = self.__data.skew()
        self.__sum = self.__data.sum()
        self.__mad = self.__data.mad()
        self.__cv = self.__std / self.__mean if self.__mean else np.NaN
        self.__n_zeros = (len(self.__data) - np.count_nonzero(self.__data))
        self.__p_zeros = self.__n_zeros / len(self.__data)


class DateStats(Stats):
    def dtype_stats(self):
        self.__min = self.__data.min()
        self.__max = self.__data.max()
        self.__range = self.__max - self.__min


class CategoricalStats(Stats):
    def dtype_stats(self):
        self.__top = self.__value_counts_without_nan.index[0]
        self.__freq = self.__distinct_count_with_nan.iloc[0]


class BooleanStats(Stats):
    # Same as Categorical?
    pass


class ConstantStats(Stats):
    pass


class UniqueStats(Stats):
    pass


class SupportedStats(Stats):
    pass


class UnsupportedStats(Stats):
    pass
