import abc
from pandas import DataFrame
from typing import List, Dict


class Storage(abc.ABC):
    @abc.abstractmethod
    def get_table_names(self) -> List[str]:
        pass

    @abc.abstractmethod
    def get_table_lists(self) -> Dict[str, Dict]:
        pass

    @abc.abstractmethod
    def get_table_df(self, name: str) -> DataFrame:
        pass
