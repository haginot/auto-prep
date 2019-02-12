import pandas as pd
from sklearn.preprocessing import LabelEncoder


class ProblemTarget:
    encoder = LabelEncoder()

    def __init__(self,
                 data: pd.Series):
        self.__data = data
        self.__encoded_data = self.encoder.fit_transform(self.data)
        self.__classes = self.encoder.classes_

    def get_data(self):
        return self.__data

    def get_encoded_data(self):
        return self.__encoded_data

    def get_classes(self):
        return self.__classes
