from autoprep.storage.file_storage import FileStorage


class Project:
    def __init__(self,
                 name: str,
                 train_storage: FileStorage,
                 model_storage: FileStorage):
        self.__name = name
        self.__train_storage = train_storage
        self.__model_storage = model_storage
        self.__engines = {}

    def get_name(self):
        return self.__name

    def add_engine(self):
        pass
