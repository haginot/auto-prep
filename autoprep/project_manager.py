from autoprep.project import Project
from autoprep.service.project_service import ProjectService
from autoprep.storage.base.model_storage_mixin import ModelStorageMixin
from autoprep.storage.base.training_storage_mixin import TrainingStorageMixin


class ProjectManager:
    def __init__(self,
                 project_service: ProjectService,
                 default_training_storage: TrainingStorageMixin,
                 default_model_storage: ModelStorageMixin):
        self.projects = {}
        self.project_service = project_service
        self.projects = self.project_service.load_projects()
        self.default_training_storage = default_training_storage
        self.default_model_storage = default_model_storage

    def add_project(self, name):
        self.projects.update({
            name: Project(
                name = name,
                training_storage=self.default_training_storage,
                model_storage=self.default_model_storage
            )
        })

    def save_projects(self):
        for project in self.projects.values():
            self.save_project(project)

    def save_project(self, project):
        self.project_service.save_project(project)
