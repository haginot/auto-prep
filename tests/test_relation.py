import unittest

import pandas as pd

from autoprep.relation import Relation
from autoprep.table import Table


class TestRelation(unittest.TestCase):
    def setUp(self):
        self.__source_table = Table(title='source', data=pd.DataFrame({
            'id': [1, 2, 3], 'name': ['Ichiro', 'Harper', 'Bonds']}))
        self.__target_table_related = Table(title='target', data=pd.DataFrame({
            'hitter_id': [1, 2, 3, 1, 2, 3], 'record': ['HIT', 'HIT', 'HR', 'HIT', '2B', 'HR']}))
        self.__target_table_unrelated = Table(title='target', data=pd.DataFrame({
            'hitter_id': [4, 5, 6, 7, 8, 9], 'record': ['HIT', 'HIT', 'HR', 'HIT', '2B', 'HR']}))

    def test_related(self):
        relation_related = Relation(source_table=self.__source_table, source_key='id',
                                    target_table=self.__target_table_related, target_key='hitter_id')

        self.assertTrue(relation_related.related)

        relation_unrelated = Relation(source_table=self.__source_table, source_key='id',
                                      target_table=self.__target_table_unrelated, target_key='hitter_id')

        self.assertFalse(relation_unrelated.related)


if __name__ == '__main__':
    unittest.main()
