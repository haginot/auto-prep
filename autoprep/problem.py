import abc


class Problem(abc.ABC):
    pass


class Classification(Problem):
    pass


class MultiClassClassification(Problem):
    pass


class MultiLabelClassification(Problem):
    pass


class Clustering(Problem):
    pass


class Regression(Problem):
    pass

