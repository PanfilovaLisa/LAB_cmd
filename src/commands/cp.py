import shutil
import os
from src.commands import log, pathes

@log.get_mistake
def cp(PathList, OptionList):
    """
    Копирование файла из источника в назначение.

    Аргументы:
        PathList - список адресов. Первый адрес - адрес источника (source)
        OptionList - список опций. В работе поддерживается только опция -r для реккурсивного копирования каталога.
    
    Вывод:
        1) В случае успешного выполнения ничего не выводит.

    shutil.copytree() по умолчанию выдаёт ошибку FileExistsError. При установлении dirs_exist_ok=True, копируются только файлы внутри 
    каталога источника, поэтому перед копированием вручную создаётся каталог назначения с помощью os.mkdir().
    """
    # Ошибка если не было передано ни одного адреса
    if PathList==[]:
        return 'cp: missing file operand'
    # Определение источника копирования
    source = PathList.pop(0)
    # Ошибка, если был передан только один адрес (источник)
    if PathList==[]:
        return f"cp: missing destination file operand after {source}"
    
    # Определение опции
    option=False
    for opt in OptionList:
        if opt=='-r':
            option=True 
        # Ошибка, если был передана любая другая опция кроме '-r'
        else:
            return f"cp: invalid option -- '{opt}'"
    
    # Поочерёдное копирование в назначения
    for destination in PathList:
        match pathes.FileOrDir(source):
            # Обычно копирование, если источник является файлом
            case 'file':
                shutil.copy(source, destination)
            # Если источник является каталогом
            case 'dir':
                # Необходима опция '-r' для рекурсивного копирования каталога
                if option==False: return f"cp: -r not specified; omitting directory {source}"
                # Ошибка, если назначение является файлом, а не директорией.
                if os.path.isfile(destination): return f"cp: cannot overwrite non-directory {destination} with directory {source}"
                # Создание папки назначения для копирования файлов
                destination_dir = os.path.join(destination, os.path.basename(source))
                os.mkdir(destination_dir)
                shutil.copytree(source, destination_dir, dirs_exist_ok=True)

        return True
