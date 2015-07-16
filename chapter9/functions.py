#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Home work of chapter 9.
"""
__author__ = 'guti'

import os


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
    pass


def copy_file(file_a, file_b):
    """
    Problem 9-15, copy file
    :param file_a: str
    :param file_b: str
    :return: None
    """
    with open(file_a) as fa, open(file_b, 'w') as fb:
        for la in fa:
            fb.write(la)


def break_line(filename):
    """
    Problem 9-16, handle the line longer than 80
    :param filename: str
    :return: None
    """
    with open(filename, 'r+') as f, open('temp.txt', 'w+') as f_temp:
        for line in f:
            if len(line) > 80:
                while len(line) > 80:
                    point = line[:80].rfind(' ')
                    f_temp.write(line[:point] + os.linesep)
                    line = line[point:].lstrip()
                f_temp.write(line)
            else:
                f_temp.write(line)
        f.seek(0, 0)
        f_temp.seek(0, 0)
        for line in f_temp:
            f.write(line)
        os.remove('temp.txt')


def search_file(filename, byte):
    """
    Problem 9-18, search char in file
    :param byte: int 0-255
    :param filename: str
    :return: int, times that char occur
    """
    char = chr(byte)
    total = 0
    with open(filename) as f:
        for line in f:
            total += line.count(char)
    return total


def create_file(byte, times, length):
    """
    Problem 9-19, create a file with random info
    :param byte: int 0-255
    :param times: int, times char(byte) occur
    :param length: int, file length
    :return: None
    """
    from random import randint, randrange
    from time import time
    pos_list = list()
    for i in range(times):
        pos = randrange(length)
        if pos in pos_list:
            continue
        else:
            pos_list.append(pos)
    filename = 'random' + str(int(time())) + '.txt'
    with open(filename, 'w') as f:
        for i in range(length):
            if i in pos_list:
                f.write(chr(byte))
            else:
                r = randint(0, 255)
                if r != byte:
                    f.write(chr(r))
                else:
                    continue


def file_gzip(filename):
    """
    Problem= 9-20, create gzip a file
    :param filename: str
    :return: None
    """
    import gzip
    with open(filename) as f_in, gzip.open(filename + '.gz', 'wb') as f_out:
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()


def file_zip(filename, zippath, mode='OPEN'):
    """
    Problem= 9-21, using zipfile
    :param filename: file name or path
    :param zippath: zip path
    :param mode: OPEN or ADD
    :return:
    """
    import zipfile

    def zip_open(file_name, zip_path):
        f = zipfile.ZipFile(zip_path)
        f.extract(file_name, os.path.dirname(zip_path))
        f.close()

    def zip_add(file_path, zip_path):
        f = zipfile.ZipFile(zip_path, 'a')
        f.write(file_path, os.path.basename(file_path), zipfile.ZIP_DEFLATED)
        f.close()

    def zip_create(file_path, zip_path):
        f = zipfile.ZipFile(zip_path, 'w')
        f.write(file_path, os.path.basename(file_path), zipfile.ZIP_DEFLATED)
        f.close()

    f_dict = {'OPEN': zip_open, 'ADD': zip_add, 'CREATE': zip_create}
    f_dict[mode](filename, zippath)


def ls_zip(filename):
    """
    Problem= 9-22, list the file of zip
    :param filename: file name of zip
    :return:
    """
    import zipfile
    import datetime
    zip_file = zipfile.ZipFile(filename)
    for info in zip_file.infolist():
        print '%-20s%-20s' % (info.filename, info.compress_size),
        if info.file_size == 0:
            print '%.2f%%' % 100,
        else:
            print '%.2f%%' % (float(info.compress_size) * 100 / info.file_size),
        date_time = datetime.datetime(*info.date_time)
        print date_time.strftime('%40c')


def ls_tar(filename):
    """
    Problem= 9-23, list the file of tar
    :param filename: file name of tar
    :return:
    """
    import tarfile
    import datetime
    tar_file = tarfile.TarFile.open(filename, 'r:*')
    for info in tar_file.getmembers():
        # # can see the info details and tailor...
        # print info.get_info(encoding='UTF-8', errors='strict')
        info_dict = info.get_info(encoding='UTF-8', errors='strict')
        print '%-80s%-20s%40s' % (info_dict['name'], info_dict['size'],
                                  datetime.datetime.utcfromtimestamp(info_dict['mtime']).strftime('%40c'))


if __name__ == '__main__':
    print __doc__