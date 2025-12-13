import unittest
from src.commands import ls
from unittest.mock import Mock, patch
import os

class lsCommandTestCase(unittest.TestCase):
    """
    Тесты для команды ls.

    Проверки:
        1) Поддержка пустого PathList - функция должна вернуть True;
        2) Отображение списка файлов директории - функция должна вернуть True;
        3) При передаче файла функция возвращает True
        4) Проверка поддержки опции -l - функция должна вернуть True;
        5) Передача опций, отличных от -l - функция должна вернуть False.
    """
    
    # Поддержка пустого PathList
    @patch('builtins.print')
    @patch('src.commands.ls.log.get_mistake')
    def test_empty_PathList(self, mock_print, mock_getmistake):
        self.assertTrue(ls.ls([], []))

    # Передача директории
    @patch('builtins.print')
    @patch('src.commands.ls.log.get_mistake')
    def test_getLSdir(self, mock_print, mock_getmistake):
        self.assertTrue(ls.ls([os.path.join('src', 'commands')], []))

    # Передача файла
    @patch('builtins.print')
    @patch('src.commands.ls.log.get_mistake')
    def test_getLSdir(self, mock_print, mock_getmistake):
        self.assertTrue(ls.ls([os.path.join('src', 'main.py')], []))

    # Проверка поддержки опции -l
    @patch('builtins.print')
    @patch('src.commands.ls.log.get_mistake')
    def test_option_l(self, mock_print, mock_getmistake):
        self.assertTrue(ls.ls([os.path.join('src', 'commands')], ['-l']))

    # Передача опций, отличных от -l
    @patch('builtins.print')
    @patch('src.commands.ls.log.get_mistake')
    def test_option_wrong(self, mock_print, mock_getmistake):
        self.assertFalse(ls.ls([os.path.join('src', 'commands')], ['-e']))



if __name__ == '__main__':
    unittest.main()