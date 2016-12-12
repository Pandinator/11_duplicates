import os
import sys


def сrawl_directories(directoryToCrawl):
    output = []
    for path, dirnames, filenames in os.walk(directoryToCrawl):
        for filename in filenames:
            output.append(os.path.join(path,filename))
    return output


def are_files_duplicates(file_path1, file_path_2):
    pass


if __name__ == '__main__':
    directory_path = input()

