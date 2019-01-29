import os
import tempfile
import shutil
import unittest
from autoprep.utils import sampling


class TestUtils(unittest.TestCase):
    num_test_file = 1
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
"""]

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        for i in range(0, self.num_test_file):
            self.test_file = os.path.join(self.test_dir, f"test_data_{i}.csv")
            with open(self.test_file, 'w') as fp:
                fp.write(self.test_content[i])

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_sampling(self):
        df = sampling.csv_sampling(os.path.join(self.test_dir, 'test_data_0.csv'), 6)
        self.assertEqual(df.shape[0], 6)
        self.assertNotEquals(list(df.iloc[:, 0]), [0, 2, 4, 6, 7, 9])


if __name__ == "__main__":
    unittest.main()
