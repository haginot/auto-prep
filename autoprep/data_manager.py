from typing import List

from autoprep.relation import Relation
from autoprep.storage.base.train_storage_mixin import TrainStorageMixin
from autoprep.table import Table


class DataManager:
    def __init__(self, storage: TrainStorageMixin):
        self.__storage = storage

        self.__tables = {name: Table(title=name, data=self.__storage.get_table_df()) for name in self.__storage.get_table_names()}

        # TODO Implement CRUD

        self.__tables: List[Table] = None
        self.__relations: List[Relation] = None
