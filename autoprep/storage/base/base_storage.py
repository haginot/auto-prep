import abc

from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.training_storage_mixin import TrainingStorageMixin


class BaseStorage(abc.ABC):
    @abc.abstractmethod
    def is_training_storage(self) -> bool:
        return issubclass(TrainingStorageMixin)

    @abc.abstractmethod
    def is_model_storage(self) -> bool:
        return issubclass(ModelStorageMixin)
