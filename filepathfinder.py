import argparse
import os

DIRECTORY = os.getcwd()

class FilePathFinder:
    
    def __init__(self):
        self.directory = ''
        self.filename = ''
        self.paths = []

    def get_dictionary(self):
        return self.directory

    def get_filename(self):
        return self.filename

    def get_paths(self):
        return self.paths

    def find_paths(
        self,
        directory: str,
        filename: str,
        absolute: bool = False
    ):
        for root, _, files in os.walk(top=directory):
            if filename in files:
                path = f'{root}/{filename}'
                if absolute:
                    path = f'{DIRECTORY}/{path[2:]}'
                self.paths.append(path)


def main():
    parser = argparse.ArgumentParser(
        prog='FILE PATH FINDER',
        description=("Look if the given filename is present in a tree with "
                     "the given directory as root and return all paths "
                     "to that file")
    )
    parser.add_argument(
        '-d', '--root-directory', dest='directory', default='.',
        help='define root directory into looking file'
    )
    parser.add_argument(
        '-f', '--filename', dest='filename', required=True,
        help='define file name'
    )
    parser.add_argument(
        '-a', '--absolute', dest='absolute', action='store_true', default=False,
        help='show all paths as absolute'
    )
    arguments = parser.parse_args()

    path_founder = FilePathFinder()
    path_founder.find_paths(
        directory=arguments.directory,
        filename=arguments.filename,
        absolute=arguments.absolute
    )
    print(path_founder.get_paths())


if __name__ == '__main__':
    main()
