# -*- coding: utf-8 -*-

"""
example of Thread
"""

__author__ = 'guti'

import threading
from time import ctime, sleep

loops = [2, 4]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self):
        return self.func(*self.args)


def loop(nloop, nesc):
    print 'start loop', nloop, 'at', ctime()
    sleep(nesc)
    print 'end loop', nloop, 'at', ctime()


def main():
    print 'start at:', ctime()
    threads = list()
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
