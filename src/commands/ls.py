import os
import tabulate
import datetime
import colorama
from src.commands import pathes, log


def MakeAnswer(path, option: bool):
    """
    Формирование ответа для вывода

    Аргументы:
        path - путь, ведущий к каталогу
        option - наличие опции для подробного отображения

    Вывод:
        result - таблица, сформированная с помощью библиотеки tabulate
    """
    # Содержимое текущей директории. type: list
    listdir = os.listdir(path)
    data=[]
    # Сбор подробной информации при наличие опции
    if option:
        for link in listdir:
                inf = os.lstat(path + '/' + link)
                time = datetime.datetime.fromtimestamp(inf.st_mtime)
                data+=[[link, inf.st_size, time.isoformat(timespec='minutes', sep=' '), inf.st_mode]]
    
    # Обычный вывод содержимого каталога
    else:
        # Создание таблицы
        data = [[]]
        for dir in listdir:
            way = os.path.join(path, dir)
            # Если рассматривается каталог => окрасит фон текста зелёным
            if os.path.isdir(way):
                data[-1]+=[colorama.Back.GREEN + colorama.Fore.BLUE + dir + ' ']
                data[-1]+=[colorama.Style.RESET_ALL]
            
            # Если рассматривается папка => окрасит сам текст зелёным
            else:
                data[-1]+=[colorama.Fore.GREEN + dir + ' ']
                data[-1]+=[colorama.Style.RESET_ALL]
            # Форматирование таблицы
            if len(data[-1]) == 8:
                data+=[[]]
    # Преобразование в красивую таблицу
    result = tabulate.tabulate(data)
    return result

def ls(PathList, OptionList):
    """
    Отображение списка файлов и каталогов в текущем рабочем.

    Аргументы:
        PathList: список, содержащий переданные пути. Допускается PathList = [].
        OptionList: опция команды
            -l  Подробное отображение (имя, рамзер, дата изменения, права доступа)
        
    Вывод:
        1) Выводит таблицу, сформированную в MakeAnswer в консоль и передаёт в main значение True.
        2) В случае неверно указанной опции - запись в лог, возвращает False в main.
    
    В работе рассматривается только опция -l, остальные опции выдадут ошибку:
    ls: invalid option -- '<переданная опция>'

    """
    # Определение наличия и правильности опции
    # Опции нет
    if OptionList==[]:
        option=False
    else:
        # Опции есть
        for option in OptionList:
            if option=='-l':
                option=True 
            # Была передана неизвестная опция
            else:
                RESULT = f'ls: invalid option -- "{option[1:]}"'
                print(RESULT)
                log.log_in('ERROR: ' + RESULT)
                return False
            
    # Путь не указан -> отображает список файлов и каталогов в текущем раблочем каталоге (path=None)
    if PathList==[]:
        path = os.getcwd()
        print(MakeAnswer(path, option))
        return True
    
    for path in PathList:
        print(path)
        print(MakeAnswer(path, option))
    
    return True