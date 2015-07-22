# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'

import time


class Date(object):
    """
    Problem 13-7, time interface
    """
    def __init__(self, t=time.time()):
        self.__time = t
        self.__time_str_dict = {
            'MDY': '%m/%d/%y',
            'MDYY': '%m/%d/%Y',
            'DMY': '%d/%m/%y',
            'DMYY': '%d/%m/%Y',
            'MODYY': '%a %d, %Y',
        }

    def update(self, t=time.time()):
        self.__init__(t)

    def display(self, time_format='MDY'):
        time_format = time_format.upper()
        if time_format in self.__time_str_dict:
            print time.strftime(self.__time_str_dict[time_format], time.gmtime(self.__time))
        else:
            print time.ctime(self.__time)

if __name__ == '__main__':
    d = Date()
    d.display()
