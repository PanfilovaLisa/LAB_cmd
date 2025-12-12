import os

def get_mistake(func):
    def wrapper(*args):
        RESULT = func(*args)
        if RESULT!=True:
            print(RESULT)
            # log.log_in('ERROR: ' + RESULT)
            return False 
        return
    return wrapper

@get_mistake
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

    return True


print(
    cd(['lala', 'klala'], [])
)