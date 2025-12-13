import unittest
from unittest.mock import Mock, MagicMock, patch
from src.commands import cp
import os

class CpCommandTestCase(unittest.TestCase):
    """
    Тесты для команды cp.

    Проверки:
        1) При отсутствии переданных путей функция должна вернуть False;
    """
    # Не переданы адреса
    @patch('builtins.print')
    @patch('src.commands.cp.log.get_mistake')
    def test_empty_PathList(self, mock_print, mock_getmistake):
        mock_getmistake=True
        self.assertFalse(cp.cp([], []))

    # Был передан только один адрес
    @patch('builtins.print')
    @patch('src.commands.cp.log.get_mistake')
    def test_single_path(self, mock_print, mock_getmistake):
        PathList =  [os.path.join('tests', 'testfile.txt')]
        self.assertFalse(cp.cp(PathList, []))

    # Были переданы одинаковые адреса
    @patch('builtins.print')
    @patch('src.commands.cp.log.get_mistake')
    def test_same_path(self, mock_print, mock_getmistake):
        PathList =  [os.path.join('tests', 'testfile.txt'), os.path.join('tests', 'testfile.txt')]
        self.assertFalse(cp.cp(PathList, []))
    


if __name__ == '__main__':
    unittest.main()
