from autoprep.storage.file_storage import FileStorage


class Project:
    def __init__(self,
                 name: str,
                 training_storage: FileStorage,
                 model_storage: FileStorage):
        self.__name = name
        self.__training_storage = training_storage
        self.__model_storage = model_storage
        self.__engines = {}

    def get_name(self):
        return self.__name

    def add_engine(self):
        pass
