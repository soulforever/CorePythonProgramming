#!/usr/bin/env python

"""
Home work of chapter 2.
"""

__author__ = 'guti'
from time import sleep


def input_print_a():
    """
    problem 2-4 (a)
    """
    s = raw_input('>>>')
    print s


def input_print_b():
    """
    problem 2-4 (b)
    """
    num = int(raw_input('>>>'))
    print(num)


def loop_number():
    """
    problem 2-5 (a) and (b)
    """
    # (a)
    i = 10
    while i >= 0:
        print(i)
    # (b)
    for i in range(0, 11):
        print(i)


def sign():
    """
    problem 2-6
    """
    num = int(raw_input('>>>'))
    if num > 0:
        print('%d is a positive number' % num)
    elif num < 0:
        print('%d is a negative number' % num)
    else:
        print('input is 0')


def print_chars_a():
    """
    problem 2-7 (a), need to import sleep from module time
    """
    s = raw_input('>>>')
    i = 0
    while i < len(s):
        sleep(3)
        print(i)


def print_chars_b():
    """
    problem 2-7 (b), need to import sleep from module time
    """
    s = raw_input('>>>')
    for char in s:
        sleep(3)
        print(char)


def sum_list():
    """
    problem 2-8
    """
    li = []
    while True:
        num = float(raw_input('>>>'))
        li.append(num)
    s = 0
    for i in li:
        s += i
    print s


def avg_list(li):
    """
    problem 2-9
    :param li: list with only numbers
    :return: average of numbers in list
    """
    return float(sum(li)) / len(li)


def input_check():
    """
    problem 2-10
    """
    while True:
        print('Input a num between 1100')
        num = int(raw_input('>>>'))
        if 0 < num < 101:
            print('Your input is %d' % num)
            break
        else:
            continue


def text_menu():
    """
    problem 2-11
    """
    li = [1, 2, 3, 4, 5]
    print(li)
    while True:
        print('(S)um')
        print('(A)vg')
        print('e(X)it')
        s = raw_input('>>>').lower()
        if s == 's':
            print(sum(li))
        elif s == 'a':
            print(float(sum(li)) / len(li))
        elif s == 'x':
            break
        else:
            print 'can not understand'


def sort(length):
    """
    problem 2-15
    :param length: the length of list to be sorted
    :return: None
    """
    li = []
    for i in range(0, length):
        num = float(raw_input('%d >>>' % i))
        li.append(num)
    print 'before sort', li
    for i in range(0, length - 1):
        for j in range(i, length - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print 'after sort', li


if __name__ == '__main__':
    print __doc__