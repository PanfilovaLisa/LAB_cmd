import os
import src.commands.pathes as pathes

def cd(path):
    """
    Переход в указанный каталог.
        Аргументы:
            line: введённая команда
            path: путь перехода, полученный в 
    """
    if path==None:
        return False
    match pathes.FileOrDir(path):
        case 'file':
            RESULT = f'ERROR: cd: {path} : Not a directory'
            print(RESULT)
            return RESULT
        case 'abs':
            os.chdir(os.path.join(*path))
        case _:
            os.chdir(path)
    
    return 'SUCCESS'