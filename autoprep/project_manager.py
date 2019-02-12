from autoprep.service.project_service import ProjectService


class ProjectManager:
    def __init__(self,
                 project_service: ProjectService):
        self.projects = {}
        self.project_service = project_service

    def load_projects(self):
        self.project_service.get_projects()

    def save_projects(self):
        for project_name, project in self.projects.items():
            self.save_project()

    def save_project(self, project_obj):
        self.project_service.save_project(project_obj)
