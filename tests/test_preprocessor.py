import unittest
import pandas as pd
from autoprep.preprocessor import Preprocessor


class TestPreprocessor(unittest.TestCase):

    def test_num_preprocessor(self):
        series = pd.Series([18, 18, 20, None, 20, 22, 22, 30])
        p = Preprocessor(series)
        res = p.apply()
        self.assertEqual(list(res),
              [-0.9035624609139906, -0.9035624609139906, -0.34752402342845795, -0.34752402342845795,
               -0.34752402342845795, 0.20851441405707474, 0.20851441405707474, 2.4326681639992054])


if __name__ == '__main__':
    unittest.main()
