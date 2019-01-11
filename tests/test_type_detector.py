import unittest
import pandas as pd

from autoprep.type_detector import TypeDetector


class TestTypeDetector(unittest.TestCase):

    td = TypeDetector()

    def test_is_key_col(self):
        s = pd.Series([123, 456, 789])
        self.assertTrue(self.td.is_key_col(s))

        s = pd.Series([123, 456, 123])
        self.assertFalse(self.td.is_key_col(s))

        s = pd.Series(['abc', 'def', 'ghi'])
        self.assertTrue(self.td.is_key_col(s))

        s = pd.Series(['abc', 'def', 'abc'])
        self.assertFalse(self.td.is_key_col(s))

        s = pd.Series(['abc', 'def', None])
        self.assertFalse(self.td.is_key_col(s))

    def test_to_numeric(self):
        s = pd.Series(['1,280pt', '2,400pt', '3,360pt'])
        n = self.td.to_numeric(s)
        self.assertIn('num_int64', n.keys())
        self.assertIsInstance(n['num_int64'], pd.Series)
        self.assertEqual(n['num_int64'][0], 1280)
        self.assertEqual(n['unit'], 'pt')

        s = pd.Series(['1,280pt', '2,400', '3,360pt'])
        n = self.td.to_numeric(s)
        self.assertIn('num_int64', n.keys())
        self.assertIsInstance(n['num_int64'], pd.Series)
        self.assertEqual(n['num_int64'][0], 1280)
        self.assertEqual(n['unit'], 'pt')

        s = pd.Series(['1280pt', None, '3360pt'])
        n = self.td.to_numeric(s)
        self.assertIn('num_int64', n.keys())
        self.assertIsInstance(n['num_int64'], pd.Series)
        self.assertEqual(n['num_int64'][0], 1280)
        self.assertEqual(n['num_int64'][1], 0)
        self.assertEqual(n['unit'], 'pt')

        s = pd.Series(['1280pt', 'NaN', '3360pt'])
        n = self.td.to_numeric(s)
        self.assertEqual(n, None)

        s = pd.Series(['first', 'second', 'third'])
        n = self.td.to_numeric(s)
        self.assertEqual(n, None)

    def test_to_datetimelike(self):
        s = pd.Series(['2019/01/11', '2019/01/21'])
        d = self.td.to_datetimelike(s)
        self.assertIn('datetime_like', d.keys())
        self.assertIsInstance(d['datetime_like'], pd.Series)
        self.assertEqual(d['datetime_like'].astype(object).astype(str)[0], '2019-01-11 00:00:00')

        s = pd.Series(['2019年01月11日', '2019年01月21日'])
        d = self.td.to_datetimelike(s)
        self.assertIn('datetime_like', d.keys())
        self.assertIsInstance(d['datetime_like'], pd.Series)
        self.assertEqual(d['datetime_like'].astype(object).astype(str)[1], '2019-01-21 00:00:00')


if __name__ == '__main__':
    unittest.main()