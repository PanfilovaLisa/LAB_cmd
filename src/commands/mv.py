import os 
import shutil
from src.commands import log, pathes

@log.get_mistake
def mv(PathList, OptionList):
    """
    Перемещение или переименование файла/каталога.

    Аргументы:
        PathList - список адресов. Первый адрес - адрес источника (source)
        OptionList - список опций. В работе не используются опции для работы с командой mv.
    
    Вывод:
        1) В случае успешного выполнения ничего не выводит.
    """
    # Ошибка если не было передано ни одного адреса
    if PathList==[]:
        return 'mv: missing file operand'
    
    # Определение назначения перемещения
    destination = PathList.pop()
    # Ошибка, если был передан только один адрес (источник)
    if PathList==[]:
        return f"mv: missing destination file operand after {destination}"
    
    # Если источников несколько назначение должно быть каталогом, а не файлом
    if len(PathList)>1 and os.path.isfile(destination):
        return f"mv: target {destination}: Not a directory"
    
    # Определение опции
    if OptionList != []:
        return f"mv: invalid option -- '{OptionList[0]}'"
    
    # Последовательный перебор источников перемещения
    for source in PathList:
        # Если источник и назначение - одно и то же
        if destination==source: return f"mv: {source} and {destination} are the same file"
        # Нельзя перемещать каталог собственный подкаталог
        if source in destination: return f"mv: cannot move {source} to a subdirectory of itself, {os.path.join(destination, os.path.basename(source))}"
        match pathes.FileOrDir(source):
            # Обычное перемещение/переименование, если источник является файлом
            case 'file':
                shutil.move(source, destination)
            # Если источник является каталогом
            case 'dir':
                # Ошибка, если назначение является файлом
                if os.path.isfile(destination): return f"mv: cannot overwrite non-directory {destination} with directory {source}"
                shutil.move(source, destination)

    return True
