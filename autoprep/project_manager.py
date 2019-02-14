from autoprep.project import Project
from autoprep.service.project_service import ProjectService
from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.train_storage_mixin import TrainStorageMixin


class ProjectManager:
    def __init__(self,
                 project_service: ProjectService,
                 default_train_storage: TrainStorageMixin,
                 default_model_storage: ModelStorageMixin):
        self.projects = {}
        self.project_service = project_service
        self.projects = self.project_service.load_projects()
        self.default_train_storage = default_train_storage
        self.default_model_storage = default_model_storage

    def add_project(self, name):
        self.projects.update({
            name: Project(
                name = name,
                train_storage=self.default_train_storage,
                model_storage=self.default_model_storage
            )
        })

    def save_projects(self):
        for project in self.projects.values():
            self.save_project(project)

    def save_project(self, project):
        self.project_service.save_project(project)
