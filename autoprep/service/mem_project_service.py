from autoprep.project import Project
from autoprep.service.project_service import ProjectService


class MemProjectService(ProjectService):
    """
    This Class is just a stub for testing.
    """
    def __init__(self):
        self.projects = {}

    def get_projects(self):
        return self.projects

    def get_project(self, name):
        return self.projects.get(name)

    def save_project(self, project: Project):
        self.projects.update({
            project.get_name(): project
        })

