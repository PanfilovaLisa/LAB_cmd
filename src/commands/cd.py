import os
from src.commands import log, pathes, home

@log.get_mistake
def cd(PathList, OptionList):
    """
    Переход в указанный каталог.

    Аргументы:
        PathList - список, содержаащий путь перехода. 
        OptionList - список с опциями. В работе для команды cd не используются опциии.
        При передачи опции выводится ошибка:    -bash: cd: too many arguments
    """
    if len(PathList)>1 or len(OptionList)>0:
        return '-bash: cd: too many arguments'

    path = PathList[0]
    if os.path.isfile(path):
        return f'-bash: cd: {path}: Not a directory'

    match path:
        case '..': 
            os.chdir(path)
        case '~': 
            os.chdir(home.HomeDir)
        case _:
            os.chdir(path)
    
    return True

    # match os.path.isdir:
    #     case 'file':
    #         RESULT = f'ERROR: cd: {PathList} : Not a directory'
    #         print(RESULT)
    #         return RESULT
    #     case 'abs':
    #         os.chdir(os.path.join(*PathList))
    #     case _:
    #         os.chdir(PathList)
    
    # return 'SUCCESS'