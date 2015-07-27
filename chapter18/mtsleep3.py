# -*- coding: utf-8 -*-

"""
example of Thread
"""

__author__ = 'guti'


import threading

from time import ctime, sleep


loops = [4, 2]


def loop(nloop, nesc):
    print 'start loop', nloop, 'at', ctime()
    sleep(nesc)
    print 'end loop', nloop, 'at', ctime()


def main():
    print 'start at:', ctime()
    threads = list()
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at:', ctime()

if __name__ == '__main__':
    main()