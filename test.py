import os
import shutil
#path = input('path: ')
path1 = 'D:\Загальне'
t = os.listdir(path1)
print(t[1])
filename, file_extension = os.path.splitext(t[0])
print(file_extension)

shutil.move(f'{path1}\\{filename}{file_extension}', f'{path1}\\manual')