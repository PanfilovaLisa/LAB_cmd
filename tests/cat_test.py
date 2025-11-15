import unittest
from src.commands import cat

class catCommandTestCase(unittest.TestCase):
    def test_readFile(self):
        self.assertTrue(cat.cat('tests/TestDir/file_for_cat.txt'))


    def test_readDir(self):
        self.assertFalse(cat.cat('tests/TestDir'))

        
if __name__ == '__main__':
    unittest.main()