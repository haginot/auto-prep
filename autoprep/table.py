import pandas as pd

from autoprep.column import Column


class Table:
    def __init__(self,
                 title: str,
                 data: pd.DataFrame,
                 id_key: str = None,
                 name_key: str = None,
                 target_key: str = None):
        self.__title = title
        self.__data = data
        self.__keys = data.keys()

        # self.__columns
        self.__columns = [Column(title=k, data=s) for k, s in self.__data.iteritems()]

        # search id_key
        # search name_key
        # validate target_key

    @property
    def title(self):
        return self.__title

    @property
    def data(self):
        return self.__data

    def get_column(self, title: str) -> Column:
        if title in self.__keys:
            return self.__columns[list(self.__keys).index(title)]
