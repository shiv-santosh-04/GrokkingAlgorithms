from os import listdir
from os.path import isfile, join

def print_names(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            print_names(fullpath)
    return 0
print_names(r"C:\Users\Gads\PycharmProjects\GrokkingAlgorithms\Data-Structures")