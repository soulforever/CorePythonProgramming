# -*- coding: utf-8 -*-
__author__ = 'guti'

from operator import add, sub, mul, div
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/': div}
MAXTRIES = 2


def doprob():
    op = choice(ops.keys())
    nums = gen_num(op)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct!'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect ...try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input ...try again'


def gen_num(operator):
    if operator in '+-':
        nums = [randint(1, 100)] * 2
        nums.sort(reverse=True)
        return nums
    elif operator == '*':
        return [randint(10, 100), randint(1, 10)]
    else:
        num = randint(2, 10)
        return [num * randint(2, 10), num]


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except (EOFError, KeyboardInterrupt):
            break

if __name__ == '__main__':
    main()