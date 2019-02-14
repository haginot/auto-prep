import abc

from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.train_storage_mixin import TrainStorageMixin


class BaseStorage(abc.ABC):
    @abc.abstractmethod
    def is_train_storage(self) -> bool:
        return issubclass(TrainStorageMixin)

    @abc.abstractmethod
    def is_model_storage(self) -> bool:
        return issubclass(ModelStorageMixin)
