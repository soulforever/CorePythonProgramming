# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'


class HideX(object):
    """
    Problem 13-21
    """
    def __init__(self, x):
        self.x = x

    @staticmethod
    @property
    def x():
        def fget(self):
            return ~self.__x

        def fset(self, x):
            assert isinstance(x, int), '"x" must be a integer'
            self.__x = ~x
        return locals()

if __name__ == '__main__':
    h = HideX(8)
    print h.x