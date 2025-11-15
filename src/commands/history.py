import os
from src.commands import pathes
history_path = os.path.join('.history')

def getHistory():
    history_mass = []
    with open(history_path, 'r') as his:
        for rec in his:
            history_mass+=[rec.rstrip()]
    return history_mass

def printHistory(N):
    history_mass=getHistory()
    start=1
    if N:
        start=len(history_mass)-N
        history_mass = history_mass[-N:]
    for rec in enumerate(history_mass, start=start):
        print(*rec)
    return ("SUCCESS")

def MakeRecord(line):
    with open(history_path, 'a') as his:
        his.write(line + '\n')
    return


def undo():
    with open('.undo', 'r') as undofile:
        command=undofile.readline()
    