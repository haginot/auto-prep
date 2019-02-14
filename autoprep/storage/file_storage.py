from os import listdir, stat
from os.path import isfile, join
from typing import List, Dict, Any

import pandas as pd

from autoprep.storage.base.base_storage import BaseStorage
from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.train_storage_mixin import TrainStorageMixin


class FileStorage(BaseStorage, TrainStorageMixin, ModelStorageMixin):
    def __init__(self,
                 train_path: str,
                 model_path: str):
        self.__tables = {f.replace('.csv', ''): {
            'file_path': join(train_path, f),
            'file_size': stat(join(train_path, f)).st_size,
        } for f in [f for f in listdir(train_path) if isfile(join(train_path, f)) and f.endswith('.csv')]}
        self.__data_tables = {}

    def is_train_storage(self):
        return super().is_train_storage()

    def is_model_storage(self):
        return super().is_model_storage()

    def get_table_names(self) -> List[str]:
        return list(self.__tables.keys())

    def get_table_lists(self) -> Dict[str, Any]:
        return self.__tables

    def get_table_df(self, name: str):
        if name in self.__data_tables:
            return self.__data_tables[name]
        else:
            self.__data_tables[name] = pd.read_csv(self.__tables[name]['file_path'], index_col=None, encoding='UTF-8')
            return self.__data_tables[name]

    def save_model(self):
        pass

    def get_model(self, name):
        pass


