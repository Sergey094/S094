'''
import os

# create a directory
os.mkdir("test_folder")

# list directories in current folder
for item in os.listdir():
    if os.path.isdir(item):
        print(item)


import shutil

# move file.txt into test_folder
shutil.move("file.txt", "test_folder/file.txt")
'''