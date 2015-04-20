#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Home work of chapter 9.
"""
__author__ = 'guti'


def note_ignore(filename):
    """
    Problem 9-1, ignore the note of a file
    :param filename: str
    :return: None
    """
    f = open(filename)
    for line in f:
        # # ------------------------
        # # handle line start with #
        # if not line.startswith('#'):
        #     print line.strip()
        # # ------------------------
        l_list = line.split('#')
        if l_list[0]:
            print(l_list[0])
    f.close()


def show_lines(filename, row):
    """
    Problem 9-2, print lines of previous row
    :param filename: str, file name
    :param row: int, the row number
    :return: None
    """
    f = open(filename)
    for i, line in enumerate(f):
        if i >= row:
            break
        print i, line.strip()
    f.close()


def show_line_num(filename):
    """
    Problem 9-3, show the total number of lines of a text file
    :param filename: str
    :return: None
    """
    f = open(filename)
    print len(f.readlines())
    f.close()


def show_lines_step(filename):
    """
    Problem 9-4, show 25 lines each time, press any key to continue
    :param filename: str
    :return: None
    """
    with open(filename) as f:
        for i, line in enumerate(f):
            if i != 0 and i % 25 == 0:
                raw_input()
            print i, line.strip()


def change_grade(filename):
    """
    Problem 9-5, change the score to grade
    using the function in 6-4
    :param filename: str
    :return: None
    """

    import os

    def grade(score):
        assert 0 <= score <= 100
        if 90 <= score <= 100:
            return 'A'
        elif 80 <= score < 90:
            return 'B'
        elif 70 <= score < 80:
            return 'C'
        elif 60 <= score < 70:
            return 'D'
        else:
            return 'F'

    g_list = list()
    with open(filename, 'r') as f:
        for line in f:
            item = line.split(':')
            g_list.append(item)

    with open(filename, 'w') as f:
        for item in g_list:
            f.write('%s:%s%s' % (item[0], grade(int(item[1])), os.linesep))
    print 'finish....'


def compare_file(file_a, file_b):
    """
    Problem 9-6, compare text file, return the first different position
    :param file_a: str
    :param file_b: str
    :return: (int, int) or None
    """
    with open(file_a) as fa, open(file_b) as fb:
        row = 0
        for la, lb in zip(fa, fb):
            if la != lb:
                col = 0
                for ca, cb in zip(la, lb):
                    if ca != cb:
                        return row, col
                    col += 1
            row += 1


def read_config(filename):
    """
    Problem 9-7, resolve config file
    :param filename: str
    :return: dict
    """
    c_dict = dict()
    with open(filename) as f:
        for line in f:
            if '=' in f:
                c_list = line.strip().split()
                c_dict[c_list[0]] = c_list[1]
    return c_dict


def family_finance():
    # TODO use TK to solve
    pass




if __name__ == '__main__':
    print compare_file('test.txt', 'test1.txt')