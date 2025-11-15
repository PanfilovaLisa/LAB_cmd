import os
from src.commands import pathes, log
import sys 
import colorama

def getPermission():
    ...

def clearTrash():
    ...

def savePath(ctlg, file):
    with open('.undo', 'w') as save:
        save.write('rm' + file + ' ' + ctlg + '\n')


    # Функция очистки корзины рекурсивно проходится по файлам и каталогам и удаляет.
    # Функция удаления каталога
    # Обычное удаление переносит в папку корзины


    # Что если ответ - нет
    # Удаление родительских каталогов - CRITICAL в логе

def rm(path, option):
    ctlg, file = os.path.split(path)
    match pathes.FileOrDir(path):
        # Определяем, что удалять - файл или каталог
        case 'file':
            savePath(ctlg, file)
            # Удаление файла - перенос в каталог .trash
            os.rename(path, os.path.join('.trash', file))
            return True
        
        case 'dir':
            # Удаление каталога требует наличия опции -r
            if option=='-r':
                print(f'Это действие приведёт к удалению каталога {path} и содержащихся в нём файлов. Продолжить? y/n')
                
                # Подтверждение удаления
                for line in sys.stdin:
                    if line.rstrip() == 'y':
                        savePath(ctlg, file)
                        # Перенос каталога в .trash
                        os.rename(path, os.path.join('.trash', file))
                        return True
                    else:
                        print(colorama.Fore.GREEN + 'Отменено.' + colorama.style.RESETALL)
                        log.log_in('CANCELED')
                        return False 
                    
            # Команда на удаление каталога без опции -r
            elif option == 'None':
                RESULT = f'rm: cannot remove "{path}": Is a directory'
                log.log_in('ERROR: ' + RESULT)
                return False
            else:
                RESULT = f'rm: invalid option -- "{option}"'
                log.log_in('ERROR: ' + RESULT)
                return False
            

       # for file in os.listdir(path):
                        #     print(f'{file} ----- ' + colorama.Fore.RED + 'deleted' + colorama.Style.RESET_ALL)
                        #     os.rename(file, os.path.join('.trash', os.path.split(path)[-1], file))
                        #     os.remove(os.path.join(path, file))
                        # os.rmdir(path)            