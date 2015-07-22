# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'

import math


class Point(object):
    """
    Problem 13-5, class of geometry point
    """
    def __init__(self, x=0.0, y=0.0):
        try:
            self.x, self.y = float(x), float(y)
        except ValueError:
            self.x = self.y = 0.0

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    __repr__ = __str__


class Line(object):
    """
    Problem 13-6, a class of Line
    """
    def __init__(self, point_a=Point(), point_b=Point()):
        self.point_a, self.point_b = point_a, point_b

    def __str__(self):
        return '(%s, %s)' % (str(self.point_a), str(self.point_b))

    __repr__ = __str__

    def length(self):
        return math.hypot(self.point_b.x - self.point_a.x, self.point_b.y - self.point_a.y)

    def slope(self):
        try:
            return (self.point_b.y - self.point_a.y) / (self.point_b.x - self.point_a.x)
        except ZeroDivisionError:
            return None


if __name__ == '__main__':
    l = Line(Point(1, 2), Point(3, 7))
    print l, l.length(), l.slope()