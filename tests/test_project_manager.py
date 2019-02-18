import unittest

from autoprep.project import Project
from autoprep.project_manager import ProjectManager
from autoprep.service.mem_project_service import MemProjectService
from autoprep.storage.file_storage import FileStorage


class TestProjectManager(unittest.TestCase):
    def setUp(self):
        file_storage = FileStorage(train_path='input/', model_path='output/')
        self.pm = ProjectManager(
            project_service=MemProjectService(),
            default_train_storage=file_storage,
            default_model_storage=file_storage)

    def test_add_project(self):
        self.pm.add_project('test_project')
        self.assertEqual(self.pm.get_projects(), ['test_project'])
        self.assertIsInstance(self.pm.get_project('test_project'), Project)


if __name__ == '__main__':
    unittest.main()
