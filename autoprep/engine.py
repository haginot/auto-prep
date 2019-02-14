from autoprep.problem import Problem
from autoprep.problem_target import ProblemTarget
from autoprep.train_data import TrainData


class Engine:
    def __init__(self,
                 problem: Problem,
                 train_data: TrainData,
                 target: ProblemTarget):
        self.__problem = problem
        self.__train_data = train_data

    def train(self):
        pass

    def predict(self):
        pass
