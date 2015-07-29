# -*- coding: utf-8 -*-

"""
example of Queue
"""

__author__ = 'guti'


from random import randint
from time import sleep
from Queue import Queue
from MyThread import MyThread


def write_queue(queue):
    queue.put('xxx', 1)
    print 'producing object for queue...size now:', queue.qsize()


def read_queue(queue):
    queue.get(1, timeout=5)
    print 'consumed object from queue...size now:', queue.qsize()


def writer(queue, loops):
    for i in range(loops):
        write_queue(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        read_queue(queue)
        sleep(randint(2, 5))


funcs = [reader, writer]


def main():
    nloops = randint(2, 5)
    nfuncs = range(len(funcs))
    q = Queue(32)

    threads = list()
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'ALL DONE!'

if __name__ == '__main__':
    main()