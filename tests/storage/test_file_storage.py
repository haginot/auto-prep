import unittest
import os
import tempfile
import shutil
from genericpath import isfile
from os.path import join

from autoprep.storage.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    num_test_file = 3
    test_content = ["""
No.,選手名,守備,生年月日,年齢,年数,身長,体重,血液型,投打,出身地,年俸(推定)
0,上本　崇司,内野手,1990/08/22,28歳,6年,170cm,71kg,A型,右両,広島,800万円
2,田中　広輔,内野手,1989/07/03,29歳,5年,171cm,85kg,A型,右左,神奈川,"14,000万円"
4,小窪　哲也,内野手,1985/04/12,33歳,11年,175cm,83kg,O型,右右,奈良,"3,300万円"
6,安部　友裕,内野手,1989/06/24,29歳,11年,181cm,81kg,O型,右左,福岡,"4,600万円"
7,堂林　翔太,内野手,1991/08/17,27歳,9年,183cm,88kg,A型,右右,愛知,"1,500万円"
9,丸　佳浩,外野手,1989/04/11,29歳,11年,177cm,90kg,AB型,右左,千葉,"21,000万円"
10,岩本　貴裕,外野手,1986/04/18,32歳,10年,182cm,96kg,A型,左左,広島,"1,600万円"
11,福井　優也,投手,1988/02/08,30歳,8年,178cm,85kg,A型,右右,岡山,"3,100万円"
12,九里　亜蓮,投手,1991/09/01,27歳,5年,187cm,92kg,A型,右右,鳥取,"3,800万円"
""", """
No.,選手名,守備,生年月日,年齢,年数,身長,体重,血液型,投打,出身地,年俸(推定)
0,吉川　尚輝,内野手,1995/02/08,23歳,2年,177cm,79kg,A型,右左,岐阜,"1,300万円"
0,寺内　崇幸,内野手,1983/05/27,35歳,12年,177cm,73kg,B型,右右,栃木,"3,200万円"
1,比嘉　賢伸,内野手,2000/01/12,18歳,1年,180cm,82kg,A型,右左,大阪,250万円
2,陽　岱鋼,外野手,1987/01/17,31歳,13年,183cm,89kg,A型,右右,台湾,"30,000万円"
2,加藤　脩平,外野手,1999/03/28,19歳,2年,178cm,79kg,O型,右左,静岡,250万円
3,山川　和大,投手,1995/01/04,24歳,2年,166cm,74kg,A型,右左,兵庫,250万円
4,笠井　駿,外野手,1995/04/20,23歳,1年,180cm,80kg,B型,右右,東京,250万円
5,ゲレーロ,外野手,1986/11/20,32歳,2年,182cm,99kg,不明,右右,キューバ,"40,000万円"
5,広畑　塁,捕手,1995/06/17,23歳,1年,177cm,72kg,O型,右左,福岡,250万円
""", """
No.,選手名,守備,生年月日,年齢,年数,身長,体重,血液型,投打,出身地,年俸(推定)
0,比屋根　渉,外野手,1987/06/20,31歳,7年,180cm,70kg,O型,右右,沖縄,"1,500万円"
1,山田　哲人,内野手,1992/07/16,26歳,8年,180cm,76kg,O型,右右,兵庫,"28,000万円"
2,大引　啓次,内野手,1984/06/29,34歳,12年,178cm,84kg,A型,右右,大阪,"6,000万円"
3,西浦　直亨,内野手,1991/04/11,27歳,5年,178cm,75kg,B型,右右,奈良,"1,700万円"
4,バレンティン,外野手,1984/07/02,34歳,8年,185cm,100kg,不明,右右,アンティル,"33,300万円"
5,川端　慎吾,内野手,1987/10/16,31歳,13年,185cm,86kg,O型,右左,大阪,"14,000万円"
8,武内　晋一,内野手,1983/12/10,35歳,13年,175cm,90kg,O型,左左,兵庫,"1,700万円"
9,塩見　泰隆,外野手,1993/06/12,25歳,1年,179cm,76kg,B型,右右,神奈川,"1,000万円"
10,荒木　貴裕,内野手,1987/07/26,31歳,9年,180cm,84kg,AB型,右右,富山,"2,300万円"
"""]

    def setUp(self):
        self.test_train_dir = tempfile.mkdtemp()
        self.test_model_dir = tempfile.mkdtemp()
        for i in range(0, self.num_test_file):
            self.test_file = os.path.join(self.test_train_dir, f"test_data_{i}.csv")
            with open(self.test_file, 'w') as fp:
                fp.write(self.test_content[i])

    def tearDown(self):
        shutil.rmtree(self.test_train_dir)
        shutil.rmtree(self.test_model_dir)

    def test_instance_file_storage(self):
        fs = FileStorage(
            train_path=self.test_train_dir,
            model_path=self.test_model_dir
        )
        self.assertEqual(fs.get_table_names(), ['test_data_0', 'test_data_1', 'test_data_2'])
        self.assertEqual(fs.get_table_lists()['test_data_0']['file_size'], 951)
        self.assertEqual(fs.get_table_df('test_data_0').shape, (9, 12))


if __name__ == '__main__':
    unittest.main()
