import os
import re
from src.commands import log

def getPathWithSpace(line):
    fileWithSpace = r'[\'"]{1}[\w+\s*]*.\w+[\'"]{1}'
    pathWithSpace = rf'(\w+[/\\])+{fileWithSpace}'

    pathes=[]
    while re.search(fileWithSpace, line):
        if re.search(pathWithSpace, line):
            path = max([name.group() for name in re.finditer(pathWithSpace, line)], key=len)
        else:
            path = max([name.group() for name in re.finditer(fileWithSpace, line)], key=len)
        
        line = ''.join(line.split(path))
        path=''.join(path.split("'"))
        pathes+=[path]
    if pathes:
        if line:
            pathes+=[line.strip()]
    return pathes if pathes else False


def checkRightPath(pathline=None, file=None):
    if pathline!=None:
        path=pathline 
    else:
        path=file
    if os.path.exists(path):
        return pathline if pathline!=None else file
    else:
        # Не существующий путь
        RESULT = f"Cannot access '{path}': No such file or directory"
        print(RESULT)
        log.log_in('ERROR: ' + RESULT)
        return False    


def getOption(line):
    if option:= max([x.group() for x in re.finditer(r'\-\w\b', line)], key=len):
        return option
    return None
    # return True if  else False
    

def getManyPathes(line):
    option = getOption(line)
    print(option)
    if option!=None:
        line=''.join(line.split(option)).strip()
    if pathes := getPathWithSpace(line):
        withoutspace = pathes.pop()
        pathes+=withoutspace.split()
    else:
        pathes=line.split()
    return pathes, option



def commandHistory(line):
    commands=line.split()

    option = 0
    command=commands[0]

    if len(commands)==2:
        print(commands)
        try:
            option=int(commands[-1])
        except:
            RESULT = f'history: {option}: numeric argument required'
            print(RESULT)
            log.log_in('ERROR: ' + RESULT)
            return False
    return (command, None, option)

  

def getPath(line):
    if re.search(r'^history\b', line):
        return commandHistory(line)

    for comand in [r'^cat\b', r'^mv\b', r'^cp\b']:
        if re.search(comand, line):
            result = getManyPathes(re.split(comand, line)[-1].strip())
            return (comand[1:-2], *result)
        
    
    # Если в названии файла содержится пробел, например "название файла с пробелом.pdf"
    if result:=getPathWithSpace(line):
        return result if checkRightPath(pathline=result[1]) else False
    
    commands = line.split()
    command = commands[0]
    way=None
    option=None 

    for rec in commands[1:]:
        # Определение абсолютного пути
        if ('/' in rec):
            if rec[0]=='/':
                rec=rec[1:]
            path = rec.split('/')
            way = os.path.join(*path)
            if checkRightPath(pathline=way):
                continue
            else:
                return False
        # Определение опции
        elif option:=getOption(rec):
            continue
        # Определение относительного пути
        elif way := checkRightPath(file=rec):
            continue
        else:
            print('ERRRRRRRRR')
            return False
    
    return (command, way, option)


def FileOrDir(line):
    if os.path.isdir(line):
        return ('dir')
    if os.path.isfile(line):
        return ('file')