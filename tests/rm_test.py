import unittest
from src.commands import rm

class rmCommandTestCase(unittest.TestCase):
    def test_delFile(self):
        self.assertTrue(rm.rm('tests/TestRM/file3.txt', None))

    
    def test_delDir(self):
        self.assertFalse(rm.rm('tests/TestRM', None))
        self.assertFalse(rm.rm('tests/TestRM', '-e'))
        self.assertTrue(rm.rm('tests/TestRM', '-r'))


if __name__ == '__main__':
    unittest.main()