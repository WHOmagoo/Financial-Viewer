from sys import argv
from os import listdir
from os import walk
from os import path

def get_files_in_folder(path):
    result = []

    for a in walk(path, False):
        print(a)

    for f in listdir(folder):
        print(f)


if __name__ == '__main__':
    folder = "finances"
    if argv is not None and len(argv) > 1:
        folder = argv[1]

    get_files_in_folder(folder)

