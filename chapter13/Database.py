# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'

import pickle as p


class Database(object):
    """
    Problem 13-4, personal database
    """
    def __init__(self, filename=None):
        self.filename = filename
        if self.filename is not None:
            with open(self.filename, 'r') as f:
                self.__data = p.load(f)
        else:
            self.__data = dict()

    def login(self, username, password):
        if self.__data[username]['password'] == password:
            self.__data[username]['authorization'] = True
        else:
            print 'Username or password incorrect.'

    def update(self, username, password='123456', authorization=False):
        u_dict = {'password': password, 'authorization': authorization}
        self.__data[username] = u_dict

    def __del__(self):
        filename = 'data.pkl' if self.filename is None else self.filename
        with open(filename, 'w') as f:
            p.dump(self.__data, f)
