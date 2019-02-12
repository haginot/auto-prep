class Project:
    def __init__(self,
                 name: str,
                 training_storage: TrainingStorage,
                 model_storage: ModelStorage,
                 engine_manager: EngineManager):
        self.__name = name
        self.__training_storage = training_storage
        self.__model_storage = model_storage
        self.__engine_manager = engine_manager

    def get_name(self):
        return self.__name

    def add_engine(self):
        pass
