from os import listdir
from os.path import isfile, join
from typing import List

import pandas as pd

from autoprep.feature import Feature


class TrainingData():
    def __init__(self,
                 features: List[Feature]):
        self.__features = features


