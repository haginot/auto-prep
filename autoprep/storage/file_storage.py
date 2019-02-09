from os import listdir, stat
from os.path import isfile, join
import pandas as pd

from autoprep.storage.storage import Storage


class FileStorage(Storage):
    def __init__(self, path: str):
        self.__tables = {f.replace('.csv', ''): {
            'file_path': join(path, f),
            'file_size': stat(join(path, f)).st_size,
        } for f in [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]}
        self.__data_tables = {}

    def get_table_names(self):
        return list(self.__tables.keys())

    def get_table_lists(self):
        return self.__tables

    def get_table_df(self, name: str):
        if name in self.__data_tables:
            return self.__data_tables[name]
        else:
            self.__data_tables[name] = pd.read_csv(self.__tables[name]['file_path'], index_col=None, encoding='UTF-8')
            return self.__data_tables[name]


