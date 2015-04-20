# -*- coding: utf-8 -*-

"""
Home work of chapter 5.
"""

__author__ = 'guti'


def multi(a, b):
    """
    Problem 5-2 (a)
    :param a: number, int or float
    :param b: number, int or float
    """
    return a * b


def grade(score):
    """
    Problem 5-3, give the grade by score
    :param score: int type and in [0, 101]
    :return: str
    """
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


def least_coins(money):
    """
    Problem 5-5, give the solution of exchange least coins for money less than 1$
    :param money: float, represent dollar
    :return: dict about amount for each type of money
    """
    assert 0 <= money < 1
    dict_money = {}
    money = int(money * 100)
    for cents in [25, 10, 5, 1]:
        dict_money[cents] = money / cents
        money %= cents
    return dict_money


def calc(expr):
    # TODO use re module
    """
    Problem 5-6, calculate expression with only two positive operands and one operator
    :param expr: str, illegal expression, otherwise raise illegal expression exception
    :return: float, result of expression
    """
    from operator import add, sub, pow, div, mod, mul
    symbols = {'+': add, '**': pow, '-': sub, '/': div, '%': mod, '*': mul}
    # the list should have a proper order to handle '-'
    for k in ['**', '*', '%', '/', '+', '-']:
        li = expr.replace(' ', '').split(k)
        if len(li) == 2:
            try:
                return symbols[k](float(li[0]), float(li[1]))
            except ValueError:
                raise Exception('Not illegal expression.')
    else:
        raise Exception('Not illegal expression.')


def sales_tax(income):
    """
    Problem 5-7, calculate the sales tax
    :param income:
    :return: float, sales tax
    """
    if income < 30000:
        return 0
    else:
        return round(income * 5 / float(100), 2)


def geometry(shape, param):
    """
    Problem 5-8, calculate some geometry problem
    :param shape: str, 'square', 'cube', 'circle' or 'sphere'
    :param param: float or int, border or radius
    :return:
    """
    from math import pi

    def square(border):
        return border ** 2

    def cube(border):
        return border ** 3

    def circle(radius):
        return pi * (radius ** 2)

    def sphere(radius):
        return pi * (radius ** 3) * float(4) / 3

    g_dict = {'square': square, 'cube': cube, 'circle': circle, 'sphere': sphere}
    assert shape in g_dict, 'Not illegal shape.'
    assert param > 0, 'Not illegal param'
    return g_dict[shape](param)


def c_to_f(f_degree):
    """
    Problem 5-10, convert Celsiur to Fahrenheit
    :param f_degree: int or float, F
    :return: float, C
    """
    # use true division by add this at the beginning of file
    # from __future__ import division
    return round((f_degree - 32) * (float(5) / 9), 2)


def get_even():
    """
    Problem 5-11, a example of get even from 0 to 20
    :return: list
    """
    # change x % 2 == 1 to get odd
    return [x for x in range(21) if x % 2 == 0]


def boundary_info():
    # TODO complex information
    """
    Problem 5-12, get sys information about int, long, float and complex
    :return: dict, about their information
    """
    import sys
    b_dict = dict()
    b_dict['int'] = (-sys.maxint - 1, sys.maxint)
    b_dict['float'] = (sys.float_info.min, sys.float_info.max)
    b_dict['long'] = (sys.long_info.bits_per_digit, sys.long_info.sizeof_digit)
    return b_dict


def get_minute(time):
    """
    Problem 5-13, convert time.
    recommend to use time module
    :param time: str, '%H:%M'
    :return: int, minutes
    """
    t_list = [int(x) for x in time.split(':')]
    return t_list[0] * 60 + t_list[1]


def annual_interest(daily_interest):
    """
    Problem 5-14, calculate annual_interest, assume 365 days a year
    :param daily_interest: float, daily interest
    :return:
    """
    b_daily = 1
    for i in range(0, 365):
        b_daily += b_daily * daily_interest
    return b_daily - 1


def com_div(x, y):
    """
    Problem 5-15 (a), get greatest common divisor
    :param x: int, >= 0
    :param y: int，>= 0
    :return: int, greatest common divisor
    """
    # # iterator
    # # ------------------
    # for i in range(min(x, y), 0, -1):
    #     if x % i == 0 and y % i == 0:
    #         return i
    # # ------------------
    # recursion
    if y == 0:
        return x
    else:
        return com_div(y, x % y)


def com_mul(x, y):
    """
    Problem 5-15 (b), get lease common multiple
    :param x: int, >= 0
    :param y: int, >= 0
    :return: int, lease common multiple
    """
    # # iterator
    # # ------------------
    # for i in range(max(x, y), x * y + 1):
    #     if i % x == 0 and i % y == 0:
    #         return i
    # # ------------------
    return x * y / com_div(x, y)


def finance(balance, monthly_payment):
    """
    Problem 5-16, print the family finance
    :param balance: int or float,balance at the beginning
    :param monthly_payment: int or float
    :return: None, print the result
    """
    print '%20s' % 'Amount Remaining'
    print '%-10s%-10s%-10s' % ('Pymt#', 'Paid', 'Balance')
    print '-' * 30
    month = 0
    while balance > 0:
        print '%-10d%-10s%-10s' % (month, '$'+str(monthly_payment), '$'+str(balance))
        balance -= monthly_payment
        month += 1
    print '%-10d%-10s%-10s' % (month, '$'+str(monthly_payment+balance), '$'+str(0))


def random_list():
    """
    Problem 5-17, generate a random list and choose some element to generate another one
    :return: list, sorted random list
    """
    from random import randint, choice
    r_list = list()
    s_list = list()
    num = randint(1, 100)
    for i in range(num):
        r_list.append(randint(0, 2e31-1))
    for i in range(randint(1, num)):
        s_list.append(choice(r_list))
    s_list.sort()
    return s_list

if __name__ == '__main__':
    print __doc__