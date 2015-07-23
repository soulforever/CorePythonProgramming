# -*- coding: utf-8 -*-

"""
Home work of chapter 10.
"""

__author__ = 'guti'


def mod_open(name, mode='r', buffering=-1):
    """
    Problem 10-6, mod the built-in function open
    :param name: str, name of file
    :param mode: str, mode to operate the file
    :param buffering: int, buffer
    :return: file
    """
    try:
        f = open(name, mode, buffering)
        return f
    except IOError:
        return None


def safe_input():
    """
    Problem 10-8, mode the raw_input for float input
    :return: float
    """
    try:
        num = float(raw_input('input float >>>'))
        return num
    except (TypeError, ValueError, EOFError, KeyboardInterrupt):
        return None


def mod_sqrt(x):
    """
    mod the sqrt function to make it support complex
    :param x: num, int or float
    :return: num, float or complexs
    """
    import math
    import cmath
    try:
        return math.sqrt(x)
    except ValueError:
        return cmath.sqrt(x)


if __name__ == '__main__':
    print __doc__