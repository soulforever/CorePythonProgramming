# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'


class Stack(list):
    """
    Problem 13-8
    """
    def push(self, obj):
        self.append(obj)

    def peek(self):
        return self[-1]

    def isempty(self):
        return len(self) == 0


class Queue(list):
    """
    Problem 13-9
    """
    def enqueue(self, obj):
        self.append(obj)

    def dequeue(self):
        return self.pop(0)


class Array(list):
    """
    Problem 13-10
    """
    def shift(self):
        return self.pop(0)

    def unshift(self, obj):
        self.insert(0, obj)

    def push(self, obj):
        self.append(obj)


if __name__ == '__main__':
    # # ********Stack test********
    # s = Stack([1, 2, 3, 4, 5, 6])
    # print s.peek(), s.isempty(), s.pop()
    # s.push('test')
    # print s[:2]
    # # ********Queue test********
    # q = Queue([1, 2, 3, 4, 5, 6])
    # q.enqueue('a')
    # print q
    # q.dequeue()
    # print q
    # ********Array test********
    a = Array([1, 2, 3, 4, 5, 6])
    a.shift()
    print a
    a.unshift('a')
    print a
    a.push('b')
    print a
    a.pop()
    print a