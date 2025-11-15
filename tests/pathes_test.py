import unittest
import os
from src.commands import pathes

class PathesTestCase(unittest.TestCase):
    
    def test_wrongPath(self):
        self.assertFalse(pathes.getPath('cd tests/testing'))

    def test_AddOption(self):
        self.assertEqual(pathes.getPath('ls -l'), ('ls', None, '-l'))

    
    def test_IsDir(self):
        self.assertEqual(pathes.FileOrDir('tests/TestDir'), 'dir')

    def test_IsFile(self):
        self.assertEqual(pathes.FileOrDir('tests/TestDir/file_for_pathes.txt'), 'file')
    
    def test_AddPath(self):
        # Relative
        self.assertEqual(pathes.getPath('ls tests'), ('ls', 'tests', None))
        # Absolute
        self.assertEqual(pathes.getPath('ls tests/TestDir'), ('ls', os.path.join('tests', 'TestDir'), None))

    def test_getOption(self):
        self.assertTrue(pathes.getOption('-l'))
        self.assertFalse(pathes.getOption('pre-l'))
        self.assertFalse(pathes.getOption('-lpost'))

    
    def test_commandHistory(self):
        self.assertTrue(pathes.getPath('history'))
        self.assertTrue(pathes.getPath('history 12'))
        self.assertFalse(pathes.getPath('history line'))

        self.assertFalse(pathes.getPath('ls history'))
    
if __name__ == '__main__':
    unittest.main()