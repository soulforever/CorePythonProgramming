# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'

import os


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return repr(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def writelines(self, lines, linebreak=False):
        """
        Problem 13-16
        :param lines: seq of line
        :return:
        """
        for line in lines:
            if linebreak:
                line += os.linesep
            self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)


if __name__ == '__main__':
    f = CapOpen('test', 'w')
    f.write('hello' + os.linesep)
    f.writelines(['you are not', 'the one'], linebreak=True)