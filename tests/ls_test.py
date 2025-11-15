import unittest
from src.commands import ls

class lsCommandTestCase(unittest.TestCase):
    def test_getFile(self):
        self.assertIn('main.py', ls.ls('src/main.py', None))
    

    def test_getLSdir(self):
        self.assertTrue(ls.ls('tests/TestDir', None))


    def test_option_l(self):
        self.assertTrue(ls.ls('tests/TestDir', '-l'))


    def test_option_wrong(self):
        self.assertFalse(ls.ls('tests/TestDir', '-e'))



if __name__ == '__main__':
    unittest.main()