# -*- coding: utf-8 -*-

"""
Home work of chapter 7.
"""
__author__ = 'guti'


def print_dict():
    """
    Problem 7-3, print dict keys and values in different order
    :return: None
    """
    d = {'host': '10.0.1.1',
         'port': 8080,
         'database': 'sqlite',
         'service': 'weather'}
    k_list = d.keys()
    k_list.sort()
    # Problem 7-3 (a)
    print '-' * 30, '\nsorted keys\n', '-' * 30
    for k in k_list:
        print k
    # Problem 7-3 (b)
    print '-' * 30, '\nsorted keys with value\n', '-' * 30
    for k in k_list:
        print '(%s: %s) ' % (str(k), str(d[k]))
    # Problem 7-3 (c)
    print '-' * 30, '\nsorted value with key\n', '-' * 30
    v_list = d.values()
    v_list.sort()
    for v in v_list:
        print '(%s: %s) ' % (str([k for k in k_list if d[k] == v][0]), str(v))


def gen_dict(k_list, v_list):
    """
    Problem 7-4, form dict by two list
    :param k_list: list
    :param v_list: list
    :return: dict
    """
    # try:
    #     [hash(k) for k in k_list]
    # except TypeError:
    #     return
    # else:
    return dict(zip(k_list, v_list))


def stock_dict():
    """
    Problem 7-6, use dict to record stock
    :return: None
    """
    s_list = list()
    input_list = ['id', 'name', 'state', 'in_hand', 'check_in_price']
    while True:
        row = raw_input('input the' + str(input_list) +
                        '\nusing space to split and "." to end.\n')
        if row == '.':
            break
        else:
            r_list = row.split(' ')
            try:
                r_list[0] = int(r_list[0])
                r_list[3] = int(r_list[3])
                r_list[4] = float(r_list[4])
                assert len(r_list) == 5
            except TypeError:
                print 'id should be int, and check_in_price should be number.'
            except AssertionError:
                print 'input length not illegal.'
            else:
                s_list.append(r_list)
    sort_col = 'id'
    while True:
        sort_col = raw_input('choose the col to be sort,' + str(input_list))
        if sort_col in input_list:
            break
        else:
            print 'input in not one of the column. try again.'
    s_list = [(item[input_list.index(sort_col)], item) for item in s_list]
    s_list.sort()
    print s_list
    s_dict = dict(s_list)
    print s_dict


def hr_dict():
    """
    Problem 7-8, using dict to manage employees
    :return: None
    """
    e_dict = dict()
    while True:
        row = raw_input('input the employee\'s id and name' +
                        '\nusing space to split and "." to end.\n')
        if row == '.':
            break
        else:
            e_list = row.split(' ')
            if len(e_list) == 2:
                try:
                    e_dict[int(e_list[0])] = e_list[1]
                except ValueError:
                    print 'id must be int.'
            else:
                print 'input length is not match.'
    k_list = e_dict.keys()
    k_list.sort()
    print '-' * 20 + '\nsort by the id\n' + '-' * 20
    for k in k_list:
        print '%-10d%-20s' % (k, e_dict[k])


def reverse_dict(in_dict):
    """
    Problem 7-7, reverse the keys and values relationship of a dict
    :param in_dict: dict, input dict
    :return: dict
    """
    return dict(zip(in_dict.values(), in_dict.keys()))


def tr(srcstr, desstr, string, is_case=False):
    """
    Problem 7-9, translate char, len(srcstr) >= len(desstr)
    :param srcstr: str, source char list
    :param desstr: str, destination char list
    :param string: str, operated string
    :return: str
    """
    # Problem 7-9 (b), extend src and des string for case sensitive
    if is_case:
        tr_dict = dict(zip(srcstr.lower(), desstr.lower()))
        tr_dict.update(dict(zip(srcstr.upper(), desstr.upper())))
    else:
        tr_dict = dict(zip(srcstr, desstr))
    # Problem 7-9 (c), dict will ignore the
    str_list = [(tr_dict[char] if char in tr_dict else char) for char in list(string)]
    return ''.join(str_list)


def rot13(en_str):
    """
    Problem 7-10, rot13 encrypt
    :param en_str: str, string to be encrypted
    :return: str, encrypted string
    """
    import string
    des_list = [chr((ord(c)+13-ord('a')) % (ord('z')-ord('a')+1) + ord('a'))
                for c in string.ascii_lowercase]
    return tr(string.ascii_lowercase, ''.join(des_list), en_str, True)


def random_set():
    """
    Problem 5-17, generate a random list and choose some element to generate another one
    :return: None
    """
    def get_random_set():
        from random import randint
        s = set()
        num = randint(1, 10)
        for i in range(num):
            s.add(randint(0, 9))
        return s
    a_set = get_random_set()
    b_set = get_random_set()
    print 'A   --> ', a_set
    print 'B   --> ', b_set
    print 'A|B --> ', a_set | b_set
    print 'A&B --> ', a_set & b_set


def set_compute():
    """
    Problem 5-18
    :return:
    """
    legal_opr = ('in', 'not in', '&', '|', '^', '<', '<=', '>', '>=', '==', '!=')
    while True:
        print '\nusing space to split and "." to end.'
        a_str = raw_input('input the A: ')
        if a_str == '.':
            break
        a_set = set(a_str.split(' '))
        b_str = raw_input('input the B: ')
        if b_str == '.':
            break
        b_set = set(b_str.split(' '))
        opr = legal_opr[0]
        while True:
            opr = raw_input('input operator:')
            if opr not in legal_opr:
                print 'legal operator:', legal_opr
            else:
                break
        print 'a  --> ', a_set
        print 'b  --> ', b_set
        print 'result:', eval(str(a_set) + opr + str(b_set))

if __name__ == '__main__':
    print set_compute()