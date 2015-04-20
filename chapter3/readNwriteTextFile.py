#!/usr/bin/env python
"""
choose to read or write a text file with python
"""
__author__ = 'guti'

import os


def read_file():
    """
    read and display text file
    """
    # problem 3-10, use file exists to check read file
    fname = ''
    while True:
        fname = raw_input('Enter filename: ')
        if not os.path.exists(fname):
            print 'Error: %s already exists' % fname
        else:
            break
    print
    fobj = open(fname, 'r')
    line_num = 1
    for eachline in fobj:
        # problem 3-11, use strip method and remove comma
        print line_num, eachline.strip()
        line_num += 1
    fobj.close()


def write_file():
    """
    write input into text file
    """
    # problem 3-9
    # in windows ls = '\r\n', in linux ls = '\n'
    ls = os.linesep
    fname = raw_input('Enter filename: ')
    lines = []
    line_num = 1
    print "\nEnter lines (. by itself to quit)."
    while True:
        entry = raw_input('%d ' % line_num)
        line_num += 1
        if entry == '.':
            break
        else:
            lines.append(entry)
    # problem 3-10, use exception handling
    try:
        fobj = open(fname, 'w')

    except IOError, e:
        print '*** file open error: ', e
    else:
        fobj.writelines(['%s%s' % (x, ls) for x in lines])
        fobj.close()
        print 'DONE!'


def usr_interface():
    """
    problem 3-12
    """
    while True:
        print '\n(R)ead a text file'
        print '(W)rite a text file'
        print 'e(X)it'
        s = raw_input('Choice: ').lower()
        if s == 'r':
            read_file()
        elif s == 'w':
            write_file()
        elif s == 'x':
            break
        else:
            print('Cannot understand...')

if __name__ == '__main__':
    print __doc__