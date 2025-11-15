import shutil
from src.commands import pathes 

print(pathes.getManyPathes('-r tests/TestDir ..'))
shutil.copytree('tests/TestDir', 'src/TestDir')
# print(pathes.FileOrDir('tests/file3.txt'))
# print(os.path.split('tests'))