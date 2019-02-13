import abc


class ModelStorageMixin(abc.ABC):
    @abc.abstractmethod
    def save_model(self):
        pass

    @abc.abstractmethod
    def get_model(self, name):
        pass
