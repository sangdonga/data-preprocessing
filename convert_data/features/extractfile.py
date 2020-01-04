import os

import patoolib
from pyunpack import Archive


def extractfile():
    try:
        path = input('\t==> Enter path to file: ')
        patoolib.extract_archive(path, outdir='./data/data_extracted') if os.path.exists(path) else print('\t(?) File ' + path + ' does not exists!')
        # Archive(path, backend='auto').extractall('./data/data_extracted', auto_create_dir=True) if os.path.exists(path) else print('\t(-) File ' + path + ' does not exists!')
    except:
        print("\t(o) Can not extract file!")


if __name__ == '__main__':
    extractfile()
