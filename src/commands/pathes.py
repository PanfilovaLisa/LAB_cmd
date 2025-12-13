import os
import re
from src.commands import log
from typing import Union, Optional
    
def getOption(line: str) -> Optional[str]:
    if option:= re.findall(r'\-\w\b', line):
        return option
    return None


def EditPath(path: str) -> str:
    slash = ''
    # Если путь в системе Linux
    if ('/' in path):
        # Если путь, начинается с / => чтобы не было '' после path.split('/')
        if path[0]=='/':
            path=path[1:]
        slash = '/'
    elif ('\\' in path):
        slash = '\\'
    if len(slash)>0:
        path = path.split(slash)
        return os.path.join(*path)
    return path


def getPathWithSpace(line: str) -> Union[dict, False]:
    # Выражение файла, в названии которого есть пробел
    fileWithSpace = r'[\'"]{1}[\w+\s*]*.\w+[\'"]{1}'
    # Составление пути файла, в названии которого есть пробел
    pathWithSpace = rf'(\w+[/\\])+{fileWithSpace}'

    # Пути
    PathList=[]

    # Пока в строке находится файл с пробелом
    while re.search(fileWithSpace, line):
        # Сначала ищем путь для файла с пробелом
        if re.search(pathWithSpace, line):
            path = max([name.group() for name in re.finditer(pathWithSpace, line)], key=len)
        # Если указано только название файла 
        else:
            path = max([name.group() for name in re.finditer(fileWithSpace, line)], key=len)
        
        # Исключаем найденный файл/путь из строки
        line = ''.join(line.split(path))
        # Добавляем путь в список путей
        path=''.join(path.split("'"))
        if checkRightPath(path):
            PathList+=[EditPath(path)]
        else:
            return False

    # Если в строке были файлы с пробелами
    if PathList:
        if line:
            CommandsLine = line.strip().split()
            # Определение команды
            command, CommandsLine=CommandsLine[0], CommandsLine[1:]
            # Нахождение опций
            OptionsList = [option for option in CommandsLine if getOption(option)]
    return {'com': command, 'opt': OptionsList, 'path': PathList} if PathList else False

@log.get_mistake
def checkRightPath(path: str) -> Union[True, False]:
    if os.path.exists(path) or path == '~':
        return True
    else:
        # Не существующий путь
        return f"Cannot access '{path}': No such file or directory"


def getPath(line: str) -> Union[dict, False]:   
    """
    Обработка введённой команды.

    Аргументы:
        line: str - строка команды

    Вывод:
        1) Словарь вида:
            dict = {
                'com' : <Команда для выполнения: str>,
                'opt': <Список переданных опций: list>,
                'path': <Список переданных адресов: list>,
            };
        2) False - если был обнаружен несуществующий путь.
    """     
    # Проверка на наличие файлов с пробелами
    if CommandDict:=getPathWithSpace(line):
        return CommandDict
    
    CommandsLine=line.split()
    # Определение команды
    command, CommandsLine = CommandsLine[0], CommandsLine[1:]

    # Обнаружение команды history
    if command == 'history':
        return {'com': command, 'opt': CommandsLine, 'path': []}

    # Определение опций
    OptionsList = [option for option in CommandsLine if getOption(option)]
    CommandsLine = [string for string in CommandsLine if (string not in OptionsList)]
    # Нахождение путей
    PathList = []
    for string in CommandsLine:
        
        # Подгон пути под ОС
        path = EditPath(string)
        # Проверка правильный ли путь
        if checkRightPath(path):
            PathList+=[path]
        else:
            return False
    return {'com': command, 'opt': OptionsList, 'path': PathList}


def FileOrDir(line):
    if os.path.isdir(line):
        return ('dir')
    if os.path.isfile(line):
        return ('file')