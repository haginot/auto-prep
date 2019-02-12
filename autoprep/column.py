import pandas as pd

from autoprep.encoder_provider import EncoderProvider
from autoprep.profiler import Profiler


class Column:
    def __init__(self,
                 data: pd.Series,
                 profiler: Profiler,
                 encoder_provider: EncoderProvider
                 ):
        self.__data = data
        self.profiler = profiler
        self.stats = self.profiler.get_stats(self.__data)
        self.xdtype = self.profiler.get_xdtype(self.__data)
        self.null_count = self.profiler.get_null_count(self.__data)
        self.average = self.stats.avg
        self.variance = self.stats.var
        self.encoder = encoder_provider.get_encoder(self.__data)


