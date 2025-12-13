import unittest
from unittest.mock import patch
from src.commands import cat
import os

class CpCommandTestCase(unittest.TestCase):

    #Была передана опция
    @patch('builtins.print')
    @patch('src.commands.cp.log.get_mistake')
    def test_empty_PathList(self, mock_print, mock_getmistake):
        PathList=[os.path.join('src', 'main.py')]
        self.assertFalse(cat.cat(PathList, []))

    # Была передана директория
    @patch('builtins.print')
    @patch('src.commands.cp.log.get_mistake')
    def test_single_path(self, mock_print, mock_getmistake):
        PathList=[os.path.join('src', 'commands')]
        self.assertFalse(cat.cat(PathList, []))

if __name__ == '__main__':
    unittest.main()
