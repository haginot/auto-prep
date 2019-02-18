from autoprep.project import Project
from autoprep.service.project_service import ProjectService
from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.train_storage_mixin import TrainStorageMixin


class ProjectManager:
    def __init__(self,
                 project_service: ProjectService,
                 default_train_storage: TrainStorageMixin,
                 default_model_storage: ModelStorageMixin):
        self.__projects = {}
        self.__project_service = project_service
        self.__projects = self.__project_service.get_projects()
        self.__default_train_storage = default_train_storage
        self.__default_model_storage = default_model_storage

    def add_project(self, name):
        self.__projects.update({
            name: Project(
                name=name,
                train_storage=self.__default_train_storage,
                model_storage=self.__default_model_storage
            )
        })

    def get_projects(self):
        return [k for k in self.__projects.keys()]

    def get_project(self, name):
        return self.__projects[name]

    def save_projects(self):
        for project in self.__projects.values():
            self.save_project(project)

    def save_project(self, project):
        self.__project_service.save_project(project)
