from io import StringIO
from datetime import datetime as dt
import unittest
import pandas as pd
from autoprep.user_stage_encoder import UserStageEncoder


class TestUserStageEncoder(unittest.TestCase):
    test_content = """
customer_id,datetime,status
1,2012-04-11,proposal
2,2012-04-18,proposal
3,2012-04-25,proposal
4,2012-04-30,proposal
5,2012-05-04,proposal
6,2012-05-05,proposal
1,2012-05-11,negotiate
2,2012-05-16,negotiate
3,2012-05-22,negotiate
4,2012-05-28,negotiate
5,2012-05-29,negotiate
6,2012-06-01,negotiate
1,2012-06-10,close
3,2012-08-08,close
4,2012-08-12,failure
5,2012-09-07,close
"""
    df = pd.read_csv(StringIO(test_content))
    ust = UserStageEncoder(drop_days=124)

    def test_fit_transform(self):
        encoded = self.ust.fit_transform(s_session=self.df.loc[:, 'customer_id'],
                                         s_datetime=self.df.loc[:, 'datetime'],
                                         s_target=self.df.loc[:, 'status'],
                                         positive_targets=['close'],
                                         negative_targets=['failure'],
                                         end_of_term=dt.strptime('2012-09-30', '%Y-%m-%d'))
        self.assertEqual(list(encoded), [1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, 0, 1, 1, -1, 1])


if __name__ == "__main__":
    unittest.main()