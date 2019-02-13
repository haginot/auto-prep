from typing import List

from autoprep.storage.base.training_storage_mixin import Storage


class DataManager:
    def __init__(self, storage: Storage):
        self.__storage = storage
        self.__tables: List[Table] = None
        self.__relations: List[Relation] = None
