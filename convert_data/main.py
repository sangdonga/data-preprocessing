import json
from convert_data.features import extractfile, features


def writedata(file, data):
    with open(file, mode='r', encoding='utf8') as f:
        obj = json.load(f)
        f.close()
    obj["data"].append(data)
    with open(file, mode='w', encoding='utf8') as f:
        json.dump(obj, f, ensure_ascii=False)
        f.close()


def processed(file):
    with open('./data/processed', mode='r', encoding='utf8') as f:
        for line in f:
            if file == line.rstrip():
                return True
        f.close()
    return False


def main():
    print("=====Begin extract files=====")
    extractfile.extractfile()
    print("=====Finish extract files====\n")
    print("====Begin data processing====")
    work_dir = './data/data_extracted'
    data_file = './data/vimrc.json'
    files = features.getfileinfolder(work_dir)

    for file in files:
        if not processed(file):
            print("\t(+) Processing \'" + file + '\'...')
            with open('./data/processed', mode='a', encoding='utf8') as f:
                f.write(file + '\n')
                f.close()
            data = features.readfile(file)
            writedata(data_file, data)
        else:
            print('\t(e) \''+file + '\' be added!')
    print("============FINISH===========")


if __name__ == '__main__':
    main()
