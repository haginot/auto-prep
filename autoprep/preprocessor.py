from scipy import stats
import pandas as pd


class Preprocessor:
    def __init__(self, series: pd.Series):
        print(series.dtype.name)
        if series.dtype.name == 'int64':
            self.prep = NumPreprocessor()
        elif series.dtype.name == 'float64':
            self.prep = NumPreprocessor()
        elif series.dtype.name == 'bool':
            self.prep = BoolPreprocessor()
        elif series.dtype.name == 'datetime64':
            self.prep = DatePreprocessor()
        else:
            self.prep = CatPreprocessor()
        self.series = series

    def apply(self):
        return self.prep.apply(self.series)


class NumPreprocessor:
    @staticmethod
    def _fill(series: pd.Series):
        return series.fillna(series.median())

    @staticmethod
    def _normarize(series: pd.Series):
        return pd.Series(stats.zscore(series))

    def apply(self, series: pd.Series):
        return self._normarize(self._fill(series))


class BoolPreprocessor:
    @staticmethod
    def _fill(series):
        pass

    def apply(self, series):
        pass


class DatePreprocessor:
    @staticmethod
    def _fill(series):
        pass

    def apply(self, series):
        pass


class CatPreprocessor:
    def _fill(self):
        pass

    def _encoding(self):
        pass

    def apply(self, series):
        pass
