import os
import tabulate
import datetime
import colorama
from src.commands import pathes, log


def ls(path, option):
    """
    Отображение списка файлов и каталогов в текущем рабочем.

    Аргументы:
        path: путь федущий к каталогу
        option: опция команды
            -l  Подробное отображение (имя, рамзер, дата изменения, права доступа)
        
        Входные данные: path, option
        Выходные данные:
            1) Имя файла, если на вход был подан файл
            2)


    """
    RESULT='SUCCESS'
    # Путь был указан неверно
    if path==False:
        return False
    
    # Путь не указан -> отображает список файлов и каталогов в текущем раблочем каталоге (path=None)
    if path==None:
        path = os.getcwd()
    # Был задан путь
    else:
        # Определение к чему ведёт путь - к файлу или к каталогу
        catalog = pathes.FileOrDir(path)
        if catalog=='file':
            ctlg, file = os.path.split(path)
            result = colorama.Fore.GREEN + file + colorama.Style.RESET_ALL
            return result
        if catalog=='dir':
            ...

    listdir = os.listdir(path)
    data=[]
    if option=='-l':
        for link in listdir:
            inf = os.lstat(path + '/' + link)
            time = datetime.datetime.fromtimestamp(inf.st_mtime)
            data+=[[link, inf.st_size, time.isoformat(timespec='minutes', sep=' '), inf.st_mode]]
  
    elif option==None:
        data = [[]]
        for dir in listdir:
            if pathes.FileOrDir(dir)=='dir':
                data[-1]+=[colorama.Back.GREEN + colorama.Fore.BLUE + dir + ' ']
                data[-1]+=[colorama.Style.RESET_ALL]
            else:
                data[-1]+=[colorama.Fore.GREEN + dir + ' ']
                data[-1]+=[colorama.Style.RESET_ALL]
            if len(data[-1]) == 8:
                data+=[[]]
    else:
        RESULT = f'ls: invalid option -- "{option[1:]}"'
        print(RESULT)
        log.log_in('ERROR: ' + RESULT)
        return False
    result = tabulate.tabulate(data)
    return result