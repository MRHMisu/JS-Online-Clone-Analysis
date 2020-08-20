import zipfile
import sys


def execute():
    dir_Path = sys.argv[1]
    output_dir_Path = sys.argv[2]

    with zipfile.ZipFile(dir_Path, 'r') as zip_ref:
        zip_ref.extractall(output_dir_Path)
        sys.exit()

execute()