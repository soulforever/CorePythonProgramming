# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'


class MoneyFmt(object):
    """
    Problem 13-3, convert float to str
    """
    def __init__(self, value=0.0):
        self.value = float(value)

    def update(self, value=None):
        if value is not None:
            self.value = float(value)

    def __nonzero__(self):
        return int(self.value)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        is_neg = (self.value < 0)
        str_value = str(round(abs(self.value), ndigits=2))
        (int_part, dig_part) = tuple(str_value.split('.'))
        int_list = list()
        for i in range(len(int_part)-3, 0, -3):
            part = int_part[i:]
            int_list.insert(0, part)
            int_part = int_part[:i]
        int_list.insert(0, int_part)
        str_value = '$' + ','.join(int_list) + '.' + dig_part
        return str_value if not is_neg else '-' + str_value


if __name__ == '__main__':
    mf = MoneyFmt(-23456789.8191)
    print mf