import sys 
import re
import os
from src.commands import pathes, ls, cd, cat, rm, history, log, mv, cp
import colorama


def main():
    
    print(colorama.Fore.BLUE + os.getcwd()+'>' + colorama.Style.RESET_ALL)
    for line in sys.stdin:
        line=line.rstrip()

        log.make_log()
        history.MakeRecord(line)

        log.log_in(line)
        RESULT_LOG=False
        handle = pathes.getPath(line)

        if handle:
            command, path, option = handle 
        else:
            continue

        if command=='ls':
            if result:=ls.ls(path, option):
                print(result)
                RESULT_LOG=True

        elif command=='cd':
            RESULT_LOG=cd.cd(path)

        elif command=='cat':
            if (cat.cat(path)):
                RESULT_LOG=True            

        if command=='cp':
            if cp.cp(path, option):
                RESULT_LOG=True

        elif re.search(r'^mv\b', line):
            mv.mv(path)

        elif command=='rm':
            if rm.rm(path, option):
                RESULT_LOG=True

        elif command=='history':
            if history.printHistory(option):
                RESULT_LOG = True

        elif command=='undo':
            if history.undo():
                RESULT_LOG==True

        elif command=='exit':
            break

        print(colorama.Fore.BLUE + os.getcwd()+'>' + colorama.Style.RESET_ALL)
        if RESULT_LOG:
            log.log_in('SUCCESS')
    


if __name__ == '__main__':
    main()