import pandas as pd

from autoprep.encoder_provider import EncoderProvider
from autoprep.profiler import Profiler


class Column:
    def __init__(self,
                 title: str,
                 data: pd.Series):
        self.__data = data
        self.__profiler = Profiler(data=self.__data)
        self.__dtype = data.dtype
        # TODO
        # self.stats = self.__profiler.get_stats(self.__data)
        # self.xdtype = self.__profiler.get_xdtype(self.__data)
        # self.null_count = self.__profiler.get_null_count(self.__data)
        # self.average = self.stats.avg
        # self.variance = self.stats.var
        # self.encoder = encoder_provider.get_encoder(self.__data)

    @property
    def data(self):
        return self.__data

    @property
    def dtype(self):
        return self.__dtype

    def unique(self):
        return self.__data.unique()



