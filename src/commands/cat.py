import os
from src.commands import log

@log.get_mistake
def cat(PathList, OptionList):
    """
    Переход в указанный каталог.

    Аргументы:
        PathList - список, содержаащий путь перехода. 
        OptionList - список с опциями. В работе для команды cat не используются опциии.
        При передачи опции выводится ошибка:    cat: invalid option -- '<Передаваемая опция>'

    Вывод:
        1) Выводит путь к файлу и его содержимое (поочерёдно для нескольких файлов);
        2) Ошибка:  cat: invalid option -- '<Передаваемая опция>'   если была передана опция;
        3) Ошибка:  f'cat: <переданный путь>: Is a directory'   если адрес указывает на директорию, а не файл;
        4) Ошибка:  'Невозможно открыть .pdf'   если был передан PDF файл.

    В работе не поддерживается вывод файло с расширением .pdf
    """
    # Проверка на наличие опций
    if OptionList != []:
        return f"cat: invalid option -- '{OptionList[0]}'"
    
    for path in PathList:
        # Проверяет на что указывает путь - на файл или на папку
        if os.path.isdir(path):
            return f'cat: {path}: Is a directory'
        base, exst = os.path.splitext(path)
        if exst == '.pdf':
            return 'Невозможно открыть .pdf'
        print(path + '\n')
        file=open(path)
        for line in file:
            print(line.rstrip())
    
    return True
