import pandas as pd

from autoprep.statistics import Stats


class Profiler:
    def __init__(self, data: pd.Series):
        self.__data_type = data.dtype
        self.__stat_type = None #TypeDetector(data).stat_type
        self.__stats = Stats(data)

    @property
    def stats(self):
        return self.__stats
