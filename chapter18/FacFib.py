# -*- coding: utf-8 -*-

"""
example of Thread
"""

__author__ = 'guti'


from MyThread import MyThread
from time import ctime, sleep


def fib(x):
    assert isinstance(x, int), 'input must be type int'
    sleep(0.005)
    if x < 2:
        return 1
    else:
        return fib(x-2) + fib(x-1)


def fac(x):
    assert isinstance(x, int), 'input must be type int'
    sleep(0.1)
    if x < 2:
        return 1
    else:
        return x * fac(x-1)


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    else:
        return x + sum(x-1)


funcs = [fib, fac, sum]
n = 12


def main():
    nfuncs = range(len(funcs))

    print '*** SINGLE THREAD'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:', ctime()

    print '\n***MULTIPLE THREADS'
    threads = list()
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()

    print 'ALL DONE!'

if __name__ == '__main__':
    main()