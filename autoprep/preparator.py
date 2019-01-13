import pandas as pd

from autoprep.training_data import TrainingData
from autoprep.type_detector import TypeDetector
import autoprep.constants as const


class Preparator:

    def __init__(self, input_path):
        self.input_path = input_path
        self.raw_data = TrainingData(self.input_path)
        self.concated_datas = []
        self._concat_schema()
        self.type_detector = TypeDetector()

    def _group_schema(self):
        unique_keys = []
        group_index = []
        for df in self.raw_data.dfs:
            keys = list(df.keys()), list(df.dtypes)
            if keys not in unique_keys:
                unique_keys.append(keys)
            group_index.append(unique_keys.index(keys))
        self.raw_data.schema = group_index

    def _concat_schema(self):
        self._group_schema()
        concated_dfs = []
        for ukey in set(self.raw_data.schema):
            concated_dfs.append(pd.concat(
                [self.raw_data.dfs[i] for i in [k for k, v in enumerate(self.raw_data.schema) if v is ukey]],
                axis=0,
                ignore_index=True
            ))
        self.concated_datas = concated_dfs

    def prepare(self):
        return [PreparedData(df, self.type_detector) for df in self.concated_datas] #List[PreparedData]


class PreparedData:
    def __init__(self,
                 df: pd.DataFrame,
                 td: TypeDetector):
        self.raw = df
        self.td = td
        self.keys = []
        self.serieses = []
        self.ptypes = []
        self.pmetas = []

        for k, s in self.raw.iteritems():
            if k in ['__NAME__']:
                self._set_column(k, s, const.TYPE_CAT, False)
                continue

            res = self.td.to_datetimelike(s)
            if res:
                self._set_column(k, res['datetime_like'], const.TYPE_DATE_LIKE, self.td.is_key_col(s))
                continue

            res = self.td.to_numeric(s)
            if res:
                self._set_column(k, res['num_int64'], const.TYPE_NUM_WITH_UNIT, self.td.is_key_col(s), res['unit'])
                continue

            try:
                distinct_count = s.value_counts(dropna=False).count()
                leng = len(s)

                if distinct_count <= 1:
                    ptype = const.TYPE_CONST
                elif pd.api.types.is_bool_dtype(s) or (distinct_count == 2 and pd.api.types.is_numeric_dtype(s)):
                    ptype = const.TYPE_BOOL
                elif pd.api.types.is_numeric_dtype(s):
                    ptype = const.TYPE_NUM
                elif pd.api.types.is_datetime64_dtype(s):
                    ptype = const.TYPE_DATE
                else:
                    ptype = const.TYPE_CAT
            except:
                ptype = const.TYPE_UNSUPPORTED

            if ptype is not const.TYPE_UNSUPPORTED:
                self._set_column(k, s, ptype, self.td.is_key_col(s))

        if len(self.serieses) > 1:
            self.df: pd.DataFrame = pd.concat(self.serieses, axis=1, keys=self.keys)


    def _set_column(self,
                    key_name: str,
                    series: pd.Series,
                    ptype: str,
                    is_key: bool,
                    unit: str = None):
        self.keys.append(key_name)
        self.serieses.append(series)
        self.ptypes.append(ptype)
        self.pmetas.append(PreparedMeta(is_key, unit))

    def to_csv(self, path):
        self.df.to_csv(path)

class PreparedMeta:
    def __init__(self,
                 is_key: bool,
                 unit: str = None):
        self.is_key = is_key
        self.unit = unit
