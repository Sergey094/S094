'''
import os

# create a directory
os.mkdir("test_folder")

# list directories in current folder
for item in os.listdir():
    if os.path.isdir(item):
        print(item)

'''