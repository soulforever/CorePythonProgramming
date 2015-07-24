# -*- coding: utf-8 -*-

"""
Problem 9-17, ignore the note of a file
"""

__author__ = 'guti'

import os


def create_file_wrapper():
    def create_file(filename, text):
        """
        Function for Problem 9-17 1), create a file
        :param filename: str
        :return: None
        """
        with open(filename, 'w') as f:
            f.write(text + os.linesep)

    while True:
        s = raw_input('input the file name: ')
        if os.path.isfile(os.path.join(os.getcwd(), s)):
            print 'file exist, change the file name.'
        else:
            t = raw_input('input the text if you want to: ')
            create_file(s, t)
            break


def print_file(filename):
    """
    Function for Problem 9-17 2), print a text file
    :param filename: str
    :return: None
    """
    with open(filename) as f:
        print '\n'.join((30*'-', filename, 30*'-'))
        for i, line in enumerate(f):
            print '%-2s%s' % (i, line.strip())


def print_file_wrapper():
    while True:
        s = raw_input('input the file name: ')
        if not os.path.isfile(os.path.join(os.getcwd(), s)):
            print 'file not exist, please check'
        else:
            print_file(s)
            break


def edit_file_wrapper():
    # noinspection PyUnboundLocalVariable
    def edit_file(filename, temp, line_num, text):
        """
        Function for Problem 9-17 3),edit file
        :param filename: str, file name
        :param line_num: str, temp file name
        :param text: str
        :return: None
        """
        with open(filename) as f, open(temp, 'w') as f_temp:
            for i, line in enumerate(f):
                if i == line_num:
                    f_temp.write(text + os.linesep)
                else:
                    f_temp.write(line)
            if i <= line_num:
                f_temp.write(text + os.linesep)

    while True:
        s = raw_input('input the file name: ')
        if not os.path.isfile(os.path.join(os.getcwd(), s)):
            print 'file not exist, please check'
        else:
            print_file(s)
            l = 0
            while True:
                try:
                    l = int(raw_input('input the line number you want to change: '))
                except ValueError:
                    print 'illegal input.'
                else:
                    break
            t = raw_input('input the text you want to change to: ')
            edit_file(s, s + '.temp', l, t)
            break


def save_file_wrapper():
    def save_file(filename, temp):
        """
        Function for Problem 9-17 4),save file
        :param filename: str, file name
        :param temp: str, temp file name
        :return: None
        """
        with open(filename, 'w') as f, open(temp) as f_temp:
            for l in f_temp:
                f.write(l)
        os.remove(temp)

    s = raw_input('input the file name: ')
    if not os.path.isfile(os.path.join(os.getcwd(), s)):
        print 'file not exist, please check'
    elif os.path.isfile(os.path.join(os.getcwd(), s + '.temp')):
        save_file(s, s + '.temp')


def main():
    m_dict = {'c': create_file_wrapper, 'p': print_file_wrapper,
              'e': edit_file_wrapper, 's': save_file_wrapper}
    while True:
        print ' '.join(('(C)reate', '(P)rint', '(E)dit', '(S)ave', '(Q)uit'))
        choice = raw_input().lower()
        if choice == 'q':
            break
        elif choice in 'pecs':
            m_dict[choice]()
        else:
            print 'input illegal.'

if __name__ == '__main__':
    main()