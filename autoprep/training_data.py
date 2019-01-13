from os import listdir
from os.path import isfile, join
import pandas as pd

class TrainingData():
    def __init__(self, path, name = True):
        self.path = path
        self.files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]
        self.file_paths = [join(self.path, f) for f in self.files]
        self.dfs = [pd.read_csv(fp, index_col=None, encoding='UTF-8') for fp in self.file_paths]
        self.schema = [x for x in range(0, len(self.dfs))]
        if name:
            self._update_source()

    def get_raws(self):
        return self.dfs

    def _update_source(self):
        for i, file_name in enumerate(self.files):
            self.dfs[i]['__NAME__'] = file_name
