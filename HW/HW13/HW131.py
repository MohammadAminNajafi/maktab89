import os
import argparse

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        # print(filenames)
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def x(y):
    size = 0
    for current_path, directories, files in os.walk(y.directory):
        for file in files:
            PATH = os.path.join(current_path, file)
            if os.path.splitext(PATH)[1][1:] == y.filetype2:
                size += os.path.getsize(PATH)
    return f'{size / 1024} kb'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate size of files in a directory')
    parser.add_argument('-d', '--dir', dest='directory', type=str, help='directory to calculate file size')
    parser.add_argument('-f', '--filetype1', type=str, help=' one file type to calculate size')
    parser.add_argument('-F', '--filetype2', type=str, help='files type to calculate size')
    args = parser.parse_args()



    if args.filetype1 and args.directory:
        print('Error')
        exit()

    if args.directory and not args.filetype2:
        print(get_size(args.directory))
    print(args)
    if args.filetype2:
        print(x(args))

    if args.filetype1 and not args.directory:
        print(os.path.getsize(args.filetype1))
