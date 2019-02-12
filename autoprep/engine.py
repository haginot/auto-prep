from autoprep.problem import Problem
from autoprep.training_data import TrainingData


class Engine:
    def __init__(self,
                 problem: Problem,
                 training_data: TrainingData,
                 target: ProblemTarget):
        self.__problem = problem
        self.__training_data = training_data

    def train(self):
        pass

    def predict(self):
        pass
