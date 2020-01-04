import os
import json


def getfileinfolder(path):
    directory = path
    for root, dirs, files in os.walk(directory):
        if files.__len__() != 0:
            for file in files:
                if file.endswith('_annotated.json'):
                    yield root + '/' + file


def readfile(path):
    with open(path, mode='r', encoding='utf8') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    work_dir = './data/data_extracted'
    files = getfileinfolder(work_dir)
    for file in files:
        readfile(file)
