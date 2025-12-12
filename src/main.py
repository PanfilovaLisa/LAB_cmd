import sys 
import re
import os
from src.commands import pathes, ls, cd, cat, rm, history, log, mv, cp, home
import colorama


def main():
    # Определение домашней директории
    home.HomeAddress()
    print(colorama.Fore.BLUE + os.getcwd()+'>' + colorama.Style.RESET_ALL)
    for line in sys.stdin:
        line=line.rstrip()

        log.make_log()
        history.MakeRecord(line)

        log.log_in(line)
        RESULT_LOG=False
        handle = pathes.getPath(line)

        if handle:
            command, OptionList, PathList = handle.values()
        else:
            continue
        
        
        if command=='ls':
            if result:=ls.ls(PathList, OptionList):
                RESULT_LOG=True

        elif command=='cd':
            RESULT_LOG=cd.cd(PathList, OptionList)

        elif command=='cat':
            if (cat.cat(PathList, OptionList)):
                RESULT_LOG=True            

        if command=='cp':
            if cp.cp(PathList, OptionList):
                RESULT_LOG=True

        elif re.search(r'^mv\b', line):
            mv.mv(PathList)

        elif command=='rm':
            if rm.rm(PathList, OptionList):
                RESULT_LOG=True

        elif command=='history':
            if history.printHistory(OptionList):
                RESULT_LOG = True

        elif command=='undo':
            if history.undo():
                RESULT_LOG==True

        elif command=='exit':
            log.log_in('SUCCESS')
            break

        print(colorama.Fore.BLUE + os.getcwd()+'>' + colorama.Style.RESET_ALL)
        if RESULT_LOG:
            log.log_in('SUCCESS')
    


if __name__ == '__main__':
    main()