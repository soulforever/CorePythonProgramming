# -*- coding: utf-8 -*-

"""
Home work of chapter 11.
"""

__author__ = 'guti'


def max2(x, y):
    """
    Problem 11-3 (a), built-in function max
    :param x: obj
    :param y: obj
    :return: max of x and y
    """
    return x if x > y else y


def my_max(*args):
    """
    Problem 11-3(b), use max2 to build the function of max
    :param seq: seq
    :return: obj
    """
    args_len = len(args)
    if args_len == 0:
        assert 'max expected 1 arguments, got 0'
    try:
        if args_len == 1:
            return reduce(max2, args[0])
        elif args_len > 1:
            return reduce(max2, args)
    except TypeError:
        raise TypeError('args is not iterable')


def get_time_exp(str_min):
    """
    Problem 11-4, extension of 5-13
    :param str_min: str or int, minute
    :return: str, hour:minute
    """
    hour, minute = divmod(int(str_min), 60)
    return '%02d:%02d' % (hour, minute)


def sales_tax(income, tax_rate=0.05):
    """
    Problem 11-5, extension of 5-7
    :param income:
    :return: float, sales tax
    """
    if income < 30000:
        return 0
    else:
        return round(income * tax_rate, 2)


def printf(format_str, *args):
    """
    Problem 11-6, use python implement printf
    :param format_str: str
    :param args: tuple
    :return: None
    """
    print format_str % args


def map_using(a_list, b_list):
    """
    Problem 11-7, using map to implement the built-in function zip()
    :param a_list: list
    :param b_list: list, same length as the a_list
    :return: list
    """
    assert len(a_list) == len(b_list), 'list to be zipped must be the same length.'
    return map(lambda x, y: (x, y), a_list, b_list)


def filter_leap_year(y_list):
    """
    Problem 11-8, extension of 5-4
    :param y_list: list
    :return: list
    """
    def is_leap_year(year):
        """
        Problem 5-4, test if a year is leap
        :param year: int
        :return: True if it is leap, false otherwise
        """
        if (year % 4 == 0 and year % 100 != 0) or\
                (year % 4 == 0 and year % 100 == 0):
            return True
        else:
            return False
    year_list = [y for y in y_list if type(y) is int]
    return filter(is_leap_year, year_list)
    # #
    # return [y for y in year_list if is_leap_year(y)]


def average(*args):
    """
    Problem 11-9, use map() to implement average function
    :param args: tuple
    :return: float
    """
    return reduce(lambda x, y: x+y, args) / float(len(args))


def file_strip(filename, mode='NEW'):
    """
    Problem 11-11, use map() to strip each line of a file
    :param filename:
    :param mode:
    :return:
    """
    import os
    if mode not in ['NEW', 'COVER']:
        return
    with open(filename) as f_in, open(filename+'.new', 'w') as f_out:
        map(lambda line: f_out.write(str.strip(line)+os.linesep), f_in)
    if mode == 'NEW':
        pass
    elif mode == 'COVER':
        os.remove(filename)
        os.rename(filename+'.new', filename)


def timeit(func, *args, **kwargs):
    """
    Problem 11-12, calculate the execute time of func
    :param func: function
    :param args: parameter
    :param kwargs: parameter
    :return: time delta
    """
    from time import time
    time_start = time()
    func(*args, **kwargs)
    time_end = time()
    return time_end - time_start


def factorial(n):
    """
    Problem 11-13, factorial of n
    :param n: int
    :return: int
    """
    assert type(n) is int and n > 0, 'Input must be int and greater than zero'
    mult = lambda x, y: x * y
    print reduce(mult, range(1, n+1))


def fib(n):
    """
    Problem 11-14, add to Problem 8-9
    get number of fibonacci array, iterator
    :param n: int
    :return: int
    """
    a = 1
    b = 1
    for i in range(2, n):
        a, b = b, a+b
    return b


def print_char(s):
    """
    Problem 11-15, print str
    :param s: str
    :return: None
    """
    if len(s) == 0:
        return
    else:
        print s[0],
        print_char(s[1:])

if __name__ == '__main__':
    print __doc__
