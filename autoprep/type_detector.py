import re
from datetime import datetime as dt
import pandas as pd
from pandas import Series


class TypeDetector:

    @staticmethod
    def is_key_col(s: Series):
        return s.notnull().all() and s.unique().size == s.size

    @staticmethod
    def to_numeric(s: Series):
        num_extracted = s.fillna('0').str.extract(r'^[^0-9]*([0-9,]+)([^0-9]*)$')
        unit = ''
        if num_extracted.keys().size > 1:
            unit = num_extracted[1].unique()[0]
        try:
            num_int64 = num_extracted[0].str.replace(',', '').astype('int64')
            return {
                "num_int64": num_int64,
                "unit": unit
            }
        except Exception as e:
            return None

    @staticmethod
    def to_datetimelike(s: Series):
        sample = s.unique()[0]
        groups = []
        while True:
            match = re.search(r'^([0-9]+)([^0-9]?)(.*)$', sample)
            if match is None:
                break
            g = tuple([n for n in match.groups() if n is not ''])
            if len(g) > 2:
                groups.append(g[:2])
                sample = g[2]
            else:
                groups.append(g if len(g) > 1 else (g[0], ''))
                break
        if len(groups) < 2:
            return None

        delimiters = {g[1] for g in groups if g[1]}
        pattern = '[^0-9]*'.join(['([0-9]+)' + g[1] for g in groups])
        if (s.str.match(pattern) ^ s.notnull()).any():
            return None

        tmp = s.str.extract(pattern)
        datetime_like = {}
        for key, col in tmp.iteritems():
            try:
                col_int64 = col.astype('int64')
                if col_int64.max() < 13 and col_int64.min() > 0:
                    datetime_like['month'] = col_int64
                elif col_int64.max() < 32 and col_int64.min() > 0:
                    datetime_like['day'] = col_int64
                elif col_int64.max() < dt.now().year+100 and col_int64.min() > 1969:
                    datetime_like['year'] = col_int64
            except Exception as e:
                return None
        # the case statement without year
        if 'year' not in datetime_like:
            datetime_like['year'] = dt.now().year - 1
        if len(datetime_like.keys()) == 3:
            series = pd.to_datetime(pd.DataFrame(datetime_like))
            return {
                'datetime_like': series,
                'pattern': pattern,
                'delimiters': delimiters
            }
        else:
            return None
