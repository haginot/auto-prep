import pandas as pd


class Profiler:
    def __init__(self, data: pd.Series):
        self.__data_type = data.dtype
        self.__stat_type = None #TypeDetector(data).stat_type
        self.__stats = _Stats(data)

    @property
    def stats(self):
        return self.__stats
