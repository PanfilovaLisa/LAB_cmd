import shutil
import os

def cp(path, option):
    if option==None:
        shutil.copy2(*path)
        return True
    elif option=='-r':
        shutil.copytree(*path)
        return True 
    return False