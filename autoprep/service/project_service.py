import abc
from typing import List, Dict

from autoprep.project import Project


class ProjectService(abc.ABC):
    @abc.abstractmethod
    def get_projects(self) -> Dict[str, Project]:
        pass

    @abc.abstractmethod
    def get_project(self, name) -> Project:
        pass

    @abc.abstractmethod
    def save_project(self, project: Project):
        pass
