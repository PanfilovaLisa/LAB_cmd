import os, shutil
from src.commands import pathes, log



def add_undo(func):
    def warpper(*args):
        RESULT = func(*args)
        if RESULT==True:
            file = open('.undo', 'w')

            for argument in args:
                # print(argument, type(argument))
                try:
                    file.write(argument + ' ')
                except:
                    for opt in argument:
                        file.write(opt + ' ')
            file.close()
        return 
    return warpper

def edit_command(line: str) -> list:
    CommandsLine=line.split()

    # Определение команды
    command = CommandsLine.pop(0)

    # Обнаружение команды history
    if command == 'history':
        return {'com': command, 'opt': CommandsLine, 'path': []}

    # Определение опций
    OptionsList = [option for option in CommandsLine if pathes.getOption(option)]
    CommandsLine = [string for string in CommandsLine if (string not in OptionsList)]
    # Нахождение путей
    PathList = []
    for path in CommandsLine:
        PathList+=[path]
    
    return [command, PathList, OptionsList]


@log.get_mistake
def undo():
    with open('.undo', 'r+') as file:
        line=file.read().strip()

        if line=='': return 'undo: nothing for undo'
        # Обработка пути. Проверка на handle==True не требуется, т.к. это уже выполненная программа
        command, PathList, OptionList = edit_command(line)
        file.seek(0)
        WorkList = PathList.copy()
        # Отмена команды копирования
        if command == 'cp':
            
            source = WorkList.pop(0)

            file_for_delete = os.path.basename(source)
            # Поочерёдно удаляет скопированный файл/каталог из назначений
            for path in WorkList:
                path = os.path.join(path, file_for_delete)
                if os.path.isfile(path): 
                    os.remove(path)
                else:
                    shutil.rmtree(path)
                
                file.truncate()
                file.close()
                return True
        
        # Отмена команды перемещения
        if command == 'mv':
            destination = WorkList.pop()
            for source in WorkList:
                source, file_for_move = os.path.split(source)
                destination = os.path.join(destination, file_for_move)

                shutil.move(destination, source)

            file.truncate()
            file.close()
            return True


        # Отмена команды удаления
        if command == 'rm':
            for path in PathList:
                source, file_for_move = os.path.split(path)
                shutil.move(os.path.join('.trash', file_for_move), source)

            file.truncate()
            file.close()
            return True
