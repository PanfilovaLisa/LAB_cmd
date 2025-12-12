import shutil
import os 

# print(os.path.basename(os.path.join('tests', 'TestDir')))
# # os.mkdir(os.path.join('src', 'TestDir'))
# shutil.copytree(os.path.join('tests', 'TestDir'), os.path.join('src', 'TestDir'))
# shutil.move(os.path.join('tests', 'TestDir'), os.path.join('tests', 'TestDir', 'test'))
print(os.path.join('tests', 'TestDir') in os.path.join('tests', 'TestDir', 'test'))