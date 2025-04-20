import os
import unittest
from pathlib import Path
from h_version_provider import HVersionProvider
import shutil
from unittest.mock import Mock

# The code under test that you will import
# For example, if your code is in a file called 'calculator.py':
# from calculator import add, subtract

class TestMyFunctionality(unittest.TestCase):
    def setUp(self):
        self.original_dir = os.getcwd()
        os.chdir(Path(__file__).parent)  # change to /tests

    def tearDown(self):
        os.chdir(self.original_dir)

    def test_get_version(self):
        # Arrange
        file_source = Path() / 'VersionOld.h'
        file = Path() / 'Version.h'
        provider = HVersionProvider(config=Mock())
        shutil.copy(file_source, file)

        # Act
        version = provider.get_version()

        # Assert
        self.assertEqual(version, '1.2.3', 'Version is incorrect')

    def test_set_version(self):
        # Arrange
        provider = HVersionProvider(config=Mock())
        file_source = Path() / 'VersionOld.h'
        file = Path() / 'Version.h'
        file_correct = Path() / 'VersionNew.h'
        shutil.copy(file_source, file)

        # Act
        version = provider.set_version('4.5.6')

        # Assert
        self.assertEqual(file_correct.read_text(), file.read_text(), 'Version is incorrect')

if __name__ == '__main__':
    unittest.main()