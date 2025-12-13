import os
from src.commands import log, undo
import shutil
from typing import Union

@undo.add_undo
@log.get_mistake
def rm(command: str, PathList: list, OptionList: list) -> Union[True, False]:
    """
    Удаление указанного файла или директории.

    Аргументы:
        PathList - список адресов. Первый адрес - адрес источника (source)
        OptionList - список опций. В работе используется только опция '-r'.
    
    Удаление файлов/каталогов происходит через их перемещение в директорию .trash/. Для удаления каталога требуется письменное подтверждение пользователя. 
    Удаление родительского и корневого каталогов не допускается.
    """
    # Определение наличия опции
    option=False
    for opt in OptionList:
        # Опция найдена
        if opt=='-r':
            option=True
        else:
            return f'ls: invalid option -- "{option[1:]}"'
    
    # Не был указан путь
    if PathList==[]:
        return "rm: missing operand"
    
    WorkList = PathList.copy()

    # Поочерёдная обработка путей
    for path in WorkList:
        # Не допускается к удалению
        if path=='..': return "rm: refusing to remove '.' or '..' directory: skipping '..'"
        if path[0]=='/': return "rm: it is dangerous to operate recursively on '/'"
        # Удаление файла
        if os.path.isfile(path):
            shutil.move(path, os.path.join('.trash', os.path.basename(path)))
        # Удаление директории
        else:
            # Для удаления директории необходимо наличие опции '-r'
            if option==False: 
                return f"rm: cannot remove {path}: Is a directory"
            # Не допускается удаление родительского каталога
            if path in os.getcwd(): return f"rm: cannot remove {path}: Родительский каталог"

            # Запрос на подтверждение удаления
            print(f"You want to delete direstory {path}. Do you want to continue? Y/n")
            line=input().strip()
            # Операция  не была одобрена пользователем
            if line=='n': return "Operation aborted."
            # Операция одобрена
            shutil.move(path, os.path.join('.trash', os.path.basename(path)))
            print('Successfully removed')

    return True
            
    