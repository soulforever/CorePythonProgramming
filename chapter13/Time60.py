# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'


class Time60(object):
    """
    Problem 13-20
    """
    def __init__(self, *args):
        if not args:
            self.hr, self.mi = 0, 0
        elif isinstance(args[0], str):
            self.hr, self.mi = tuple(map(int, args[0].split(':')))
        elif isinstance(args[0], tuple):
            self.hr, self.mi = args[0]
        elif isinstance(args[0], dict):
            self.hr = args[0]['hr']
            self.mi = args[0]['min']
        elif isinstance(args, tuple):
            self.hr, self.mi = args
        # simplified time
        self.__simplified()

    def __simplified(self):
        if self.mi >= 60:
            self.hr += self.mi / 60
            self.mi %= 60

    def __str__(self):
        return '%02d:%02d' % (self.hr, self.mi)

    def __repr__(self):
        return "Time60('%s')" % self.__str__()

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.mi + other.mi)

    def __iadd__(self, other):
        self.hr += other.hr
        self.mi += other.mi
        self.__simplified()
        return self

if __name__ == '__main__':
    a = Time60(5, 60)
    print a
    a = Time60('5:6')
    print a
    a = Time60((10, 30))
    print a
    a = Time60({'hr': 7, 'min': 11})
    print a
    b = Time60(4, 49)
    print a + b
    a += b
    print repr(a)