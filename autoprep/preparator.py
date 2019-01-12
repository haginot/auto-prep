from autoprep.training_data import TrainingData

import pandas as pd


class Preparator:

    input_path = None
    raw_data = None
    concat_df = None

    def __init__(self, input_path):
        self.input_path = input_path
        self.raw_data = TrainingData(self.input_path)
        self.prepared_data = PreparedData()

    def group_schema(self):
        unique_keys = []
        group_index = []
        for df in self.raw_data.dfs:
            keys = list(df.keys()), list(df.dtypes)
            if keys not in unique_keys:
                unique_keys.append(keys)
            group_index.append(unique_keys.index(keys))
        self.raw_data.schema = group_index

    def concat_schema(self):
        self.group_schema()
        concated_dfs = []
        for ukey in set(self.raw_data.schema):
            concated_dfs.append(pd.concat(
                [self.raw_data.dfs[i] for i in [k for k, v in enumerate(self.raw_data.schema) if v is ukey]],
                axis=0,
                ignore_index=True
            ))
        self.prepared_data.concated_dfs = concated_dfs

    def prepare(self):
        return {} #List[PreparedData]

class PreparedData:
    # TODO To be constructed
    def to_csv(self):
        # TODO To be constructed
        pass
