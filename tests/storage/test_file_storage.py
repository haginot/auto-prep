import unittest

from autoprep.storage.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    fs = FileStorage('/home')

    def instance_file_storage(self):
        print(self.fs.input_path)


if __name__ == '__main__':
    unittest.main()
