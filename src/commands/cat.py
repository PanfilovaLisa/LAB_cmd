import os
from src.commands import pathes, log

def cat(path):
    for ctlg in path:
        if pathes.checkRightPath(pathline=ctlg):
            match doc:=pathes.FileOrDir(ctlg):
                case 'dir':
                    RESULT = f'cat: {ctlg}: Is a directory'
                    print(RESULT)
                    log.log_in('ERROR: ' + RESULT)
                    return False
                case 'file':
                    base, exst = os.path.splitext(ctlg)
                    if exst == '.pdf':
                        print('Невозможно открыть .pdf')
                        return False
                    file=open(ctlg)
                    for line in file:
                        print(line.rstrip())
        else:
            return False
    return True