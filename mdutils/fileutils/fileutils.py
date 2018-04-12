# Python
#
# This module implements a main class that allows to create markdown files, write in them or read.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# (C) 2018 Dídac Coll
#
# SPDX-License-Identifier:   BSD-3-Clause


class NewFile(object):
    """NewFile class creates a new file of MarkDown extension.

    Features available are:
    - Create a file.
    - Rewrite all the file with new data.
    - Write at the end of the file."""

    def __init__(self, name):
        self.file_name = name + '.md'
        self.file = open(self.file_name, 'w+', encoding='UTF-8')
        self.file.close()

    def rewrite_all_file(self, data):
        """Rewrite all the data of a Markdown file by ``data``.

        :param data: is a string containing all the data that is written in the markdown file."""
        with open(self.file_name, 'w', encoding='utf-8') as self.file:
            self.file.write(data)

    def append_end(self, data):
        """Write at the last position of a Markdown file.

        :param data: is a string containing all the data that is written in the markdown file."""
        with open(self.file_name, 'a', encoding='utf-8') as self.file:
            self.file.write(data)

    def append_after_second_line(self, data):
        """Write after the file's first line.

        :param data: is a string containing all the data that is written in the markdown file."""
        with open(self.file_name, 'r+', encoding='utf-8') as self.file:
            file_data = self.file.read()                        # Save all the file's content
            self.file.seek(0, 0)                                # Place file pointer at the beginning
            first_line = self.file.readline()                   # Read the first line
            second_line = self.file.readline()                  # Read the second line
            self.file.seek(len(first_line + second_line), 0)    # Place file pointer at the end of the first line
            self.file.write(data)                               # Write data
            self.file.write('\n' + file_data[len(first_line + second_line):])

if __name__ == '__main__':
    new_file = NewFile('Example')
    new_file.rewrite_all_file(data="# Some Text Example")
