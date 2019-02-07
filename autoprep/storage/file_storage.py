from autoprep.storage.storage import Storage


class FileStorage(Storage):
    def __init__(self, input_path: str):
        self.input_path = input_path

    def get_table_names(self):
        pass

    def get_table_lists(self):
        pass

    def get_table_df(self, name: str):
        pass


