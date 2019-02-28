from autoprep.column import Column
from autoprep.table import Table


class Relation:
    def __init__(self,
                 source_table: Table,
                 source_key: str,
                 target_table: Table,
                 target_key: str):
        self.__source_table = source_table
        self.__source_key = source_key
        self.__target_table = target_table
        self.__target_key = target_key

        self.__source_col: Column = self.__source_table.get_column(self.__source_key)
        self.__target_col: Column = self.__target_table.get_column(self.__target_key)

        self.__related = self.__source_col.dtype == self.__target_col.dtype \
                         and set(self.__target_col.unique()).issubset(set(self.__source_col.unique()))

    @property
    def related(self):
        return self.__related

