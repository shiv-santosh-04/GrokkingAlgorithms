from os import listdir
from os.path import isfile, join
from collections import deque

def print_names(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)

print_names(r"D:\GrokkingAlgorithms\Data-Structures")
