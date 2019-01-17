from typing import List

from datetime import datetime
from datetime import timedelta
import pandas as pd


class UserStageEncoder:
    classes_ = None

    def __init__(self, drop_days):
        self.drop_days = 30 if not drop_days else drop_days
        self._closed_session = []
        self._dropped_session = []
        self._expired_session = []

    def _encode(self, session: str):
        if session in self._closed_session:
            return 1
        elif session in self._dropped_session:
            return -1
        else:
            return 0

    def fit(self,
            s_session: pd.Series,
            s_datetime: pd.Series,
            s_target: pd.Series,
            positive_targets: List[str],
            negative_targets: List[str],
            end_of_term: datetime):
        try:
            s_datetime = pd.to_datetime(s_datetime)
        except:
            s_datetime = pd.Series([end_of_term for n in range(0, s_session.size)])


        self._closed_session = s_session[s_target.apply(lambda x: x in positive_targets)].unique()

        self._dropped_session = s_session[s_target.apply(lambda x: x in negative_targets)].unique()

        session_last_deal = pd.concat([s_session, s_datetime], axis=1).groupby(s_session.name).max().reset_index()
        self._expired_session = session_last_deal.iloc[:, 0][end_of_term - session_last_deal.iloc[:, 1] > timedelta(days=self.drop_days)].unique()

        self._dropped_session = list(set.union(set(self._dropped_session), set(self._expired_session)))

        self.classes_ = [0, 1, -1]

    def transform(self, s_session: pd.Series):
        encoded = s_session.apply(lambda x: self._encode(x))
        return encoded

    def fit_transform(self,
                      s_session: pd.Series,
                      s_datetime: pd.Series,
                      s_target: pd.Series,
                      positive_targets: List[str],
                      negative_targets: List[str],
                      end_of_term: datetime):
        self.fit(s_session, s_datetime, s_target, positive_targets, negative_targets, end_of_term)
        return self.transform(s_session)

    def get_params(self):
        pass

    def inverse_transform(self):
        pass

    def set_params(self):
        pass
