#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Home work of chapter 8.
"""

__author__ = 'guti'


def print_range():
    """
    Problem 8-2, print sequence with param from, to and increment
    :return: None
    """
    f = int(raw_input('input from: '))
    t = int(raw_input('input to: ')) + 1
    i = int(raw_input('input increment: '))
    for i in range(f, t, i):
        print i,


def is_prime(num):
    """
    Problem 8-4, check if a number is prime
    :param num: int
    :return: bool
    """
    from math import sqrt
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True


def get_factors(num):
    """
    Problem 8-5, get factors of a num, include 1 and itself
    :param num: int
    :return: list
    """
    return [i for i in range(1, num+1) if num % i == 0]


def get_prime_factors(num):
    """
    Problem 8-6, get prime factors
    :param num: int
    :return: list
    """
    # import should be moved to module
    from operator import mul
    # should change p_list by check prime and factor the same time
    p_list = [i for i in get_factors(num) if is_prime(i)]
    mul_num = reduce(mul, p_list)
    if mul_num == num:
        return p_list
    else:
        p_list.extend(get_prime_factors(num/mul_num))
        p_list.sort()
        return p_list


def is_perfect(num):
    """
    Problem 8-7, check if a num is perfect number
    :param num: int
    :return: bool
    """
    if sum(get_factors(num)[:-1]) == num:
        return True
    else:
        return False


def factorial(num):
    """
    Problem 8-8, calculate the factorial of number
    :param num: int
    :return: int
    """
    fac = 1
    for i in range(1, num+1):
        fac *= i
    return fac


def fib(n):
    """
    Problem 8-9, get number of fibonacci array
    :param n: index of fibonacci array
    :return: value of the index in fibonacci array
    """
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def name_list(times):
    """
    Problem 8-11, name fixing
    :param times: int, name list length
    :return: None
    """
    print 'Enter total number of names:', times
    wrong_time = 0
    n_list = list()
    for i in range(times):
        name = raw_input('Please enter name %d: ' % i)
        if ' ' not in name or len(name.split()) != 2:
            print '>>Wrong format... should be Last, First. Try again.'
            continue
        if not name.istitle():
            name = name.title()
        if ', ' not in name:
            print '>>Wrong format... should be Last, First.'
            n_list.append(name.split())
            wrong_time += 1
            print 'You have done this %d time(s) already, Fixing input...' % wrong_time
        else:
            n_list.append(name.split(', '))
    n_list.sort()
    print 'The sorted list (by last name) is:'
    for name in n_list:
        print '%s, %s' % tuple(name)


def print_num(start, end):
    """
    Problem 8-12, print number table in different format
    :param start: int
    :param end: int, start <= end
    :return: None
    """
    assert start <= end
    if end < 32 or start > 127:
        print '%-20s%-20s%-20s%-20s' % ('DEC', 'BIN', 'OCT', 'HEX')
        for i in range(start, end+1):
            print '%-20d%-20s%-20o%-20x' % (i, bin(i)[2:], i, i)
    else:
        print '%-20s%-20s%-20s%-20s%-20s' % ('DEC', 'BIN', 'OCT', 'HEX', 'ASC')
        for i in range(start, end+1):
            if i < 32 or start > 127:
                print '%-20d%-20s%-20o%-20x' % (i, bin(i)[2:], i, i)
            else:
                print '%-20d%-20s%-20o%-20x%-20s' % (i, bin(i)[2:], i, i, chr(i))


if __name__ == '__main__':
    print __doc__