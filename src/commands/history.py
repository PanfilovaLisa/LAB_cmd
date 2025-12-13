import os
from src.commands import log
from typing import Union, Optional

history_path = os.path.join('.history')

def getHistory() -> list:
    history_mass = []
    with open(history_path, 'r') as his:
        for rec in his:
            history_mass+=[rec.rstrip()]
    return history_mass

@log.get_mistake
def printHistory(OptionList: list) -> Union[True, False]:
    """
    Выводит последние введённые N команд с их номерами.
    
    :param OptionList: Description
    :type OptionList: list
    :return: Description
    :rtype: Any
    """
    # Массив введённых команд
    history_mass=getHistory()

    # Если в команду было передано несколько значений
    if len(OptionList)>1: return 'history: too many arguments'

    # Если не было передано дополнительных аргументов -> выводит всю историю
    if OptionList==[]:
        start=1
    else:
        # Определение переданного аргумента
        opt = OptionList[0]
        try:
            # На вход принимаются только числа
            N = int(opt)
            if N:
                # Формирование массива последних N команд
                start=len(history_mass)-N
                history_mass = history_mass[-N:]
        except:
            # Если была введена строка
            return f"history: invalid argument '{opt}'"
        
    # Выводит истории в терминал
    for rec in enumerate(history_mass, start=start):
        print(*rec)
    return True


def MakeRecord(line: str):
    """
    Заносит команду в историю
    """
    with open(history_path, 'a') as his:
        his.write(line + '\n')
    return


def undo():
    with open('.undo', 'r') as undofile:
        command=undofile.readline()
    