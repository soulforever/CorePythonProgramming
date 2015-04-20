#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Home work of chapter 6.
"""

__author__ = 'guti'


def sort_nums(num_str):
    """
    Problem 6-3, sort a number string
    :param num_str: number string, use space to split
    :return: list, sorted desc
    """
    # # ---------------------------
    # # Problem 6-3 (a)
    # num_list = [int(x) for x in num_str.split()]
    # # ---------------------------
    # Problem 6-3 (b)
    num_list = num_str.split()
    num_list.sort(reverse=True)
    return num_list


def list_grade(s_list):
    """
    Problem 6-4, use grade function in chapter 5
    :param s_list: a score list, element must be int and between 0 and 100
    :return: tuple with float and list: average score and grade of s_list
    """
    def grade(score):
        assert 0 <= score <= 100
        if 90 <= score <= 100:
            return 'A'
        elif 80 <= score < 90:
            return 'B'
        elif 70 <= score < 80:
            return 'C'
        elif 60 <= score < 70:
            return 'D'
        else:
            return 'F'
    return sum(s_list)/float(len(s_list)), [grade(x) for x in s_list]


def print_char():
    """
    Problem 6-5 (a), print char from middle of string
    :return: None
    """
    from time import sleep
    s = raw_input('>>>')
    s_for = s_back = ''
    index_for = index_back = len(s) / 2
    while True:
        if index_for >= 0:
            s_for = s[index_for:(len(s)/2)]
            index_for -= 1
        if index_back < len(s):
            s_back = s[len(s)/2:index_back]
            index_back += 1
        print '%8s%-8s' % (s_for, s_back)
        if index_for < 0 and index_back >= len(s):
            break
        sleep(2)


def scan_cmp(str_a, str_b):
    """
    Problem 6-5 (b), compare string by scanning chars
    :param str_a: str, compare with strB
    :param str_b:
    :return: bool, True if strA == strB
    """
    if len(str_a) != len(str_b):
        return False
    for (a, b) in zip(str_a, str_b):
        if a != b:
            return False
    else:
        return True


def is_palindrome(s):
    """
    Problem 6-5 (c), check if a string is palindrome
    :param s: str
    :return: bool， True if s is palindrome
    """
    import string
    li = [char for char in s.lower() if char in string.ascii_lowercase]

    # # use reverse to check
    # if len(li) <= 0:
    #     return False
    # else:
    #     s_for = li[:len(li)/2]
    #     s_for.reverse()
    #     s_back = li[len(li)/2:] if len(li) % 2 == 0 else li[len(li)/2+1:]
    #     return s_for == s_back
    # # --------------------
    # use recursion
    def is_pal(s_list):
        if len(s_list) <= 1:
            return True
        else:
            return s_list[0] == s_list[-1] and is_pal(s_list[1:-1])
    return is_pal(li)


def gen_palindrome(s):
    """
    Problem 6-5 (d), generate a palindrome by add reversed string
    :param s: str
    :return: str, palindrome
    """
    for i in range(len(s)-1, -1, -1):
        s += s[i]
    return s


def str_strip(s):
    """
    Problem 6-6, remove space in string at the beginning and end
    :param s: str
    :return: str, striped
    """
    if s == '' or s == ' ':
        return ''
    i = j = 0
    for i in range(len(s)):
        if s[i] != ' ':
            break

    for j in range(-1, -len(s)-1, -1):
        if s[j] != ' ':
            break
    return s[i:j+1] if j != -1 else s[i:]


def tran_int(number):
    """
    Problem 6-8, translate number to English
    can still extend to mega number
    :param number: int, between 0 and 1000
    :return: str, English expression
    """
    assert 0 <= number < 1000, 'just translate positive number'
    mp = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
          7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
          13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
          18: "eighteen", 19: "nineteen",
          20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
          70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
          1000: "thousand", 1e6: "million", 1e9: "billion", 1e12: "trillion"}

    def tan_tens(num):
        assert num < 100
        if num < 20:
            num_en = mp[num]
        else:
            num_en = mp[(num / 10) * 10]
            if num % 10 != 0:
                num_en += '-' + mp[num % 10]
        return num_en

    def tran_hundreds(num):
        assert num < 1000
        if num < 100:
            num_en = tan_tens(num)
        else:
            if num % 100 != 0:
                num_en = '%s %s and %s' % (mp[num / 100], mp[100], tan_tens(num % 100))
            else:
                num_en = mp[num/100] + ' ' + mp[100]
        return num_en

    return tran_hundreds(number)


def tran_minute(minutes):
    """
    Problem 6-9, transfer minute to '%H:%M'
    :param minutes: int
    :return: str, '%H:%M'
    """
    hour = minutes / 60
    minutes %= 60
    return '%02d:%02d' % (hour, minutes)


def print_swap():
    """
    Problem 6-10, use BIF to swap case of input string
    :return: None
    """
    s = raw_input('>>>')
    print s.swapcase()


def int_to_ipaddr(ip_int):
    """
    Problem 6-11 (a), translate int to ip address
    :param ip_int: int, int representation of ip address
    :return: str, string representation of ip address
    """
    ip_list = list()
    for i in range(4):
        ip_list.insert(0, ip_int % 256)
        ip_int /= 256
    return '%d.%d.%d.%d' % tuple(ip_list)


def ipaddr_to_int(ip_str):
    """
    Problem 6-11 (b), translate int ip address to int
    :param ip_str: str, string representation of ip address
    :return: int, int representation of ip address
    """
    ip_list = [int(x) for x in ip_str.split('.')]
    ip_list.reverse()
    total = 0
    for i, num in enumerate(ip_list):
        total += num * (256 ** i)
    return total


def findchr(s, char):
    """
    Problem 6-12 (a), find char in s
    :param s: str
    :param char: str, character
    :return: index of char in s, if not found return -1
    """
    for i, c in enumerate(s):
        if c == char:
            return i
    else:
        return -1


def rfindchr(s, char):
    """
    Problem 6-12 (b), find char in s from right hand
    :param s: str
    :param char: str, character
    :return: index of char in s from right hand, if not found return -1
    """
    index = -1
    for i, c in enumerate(s):
        if c == char:
            index = i
    return index


def subchar(s, origchar, newchar):
    """
    Problem 6-12 (c), replace new char in s
    :param s: str
    :param origchar: str, original char
    :param newchar: str, new char to replace
    :return: str, with char replaced
    """
    for i, c in enumerate(s):
        if c == origchar:
            new_s = s[:i] + newchar
            if i == len(s) - 1:
                return new_s
            else:
                return new_s + s[i+1:]


def atoc(c_str):
    """
    Problem 6-13, format a complex from str
    :param c_str: str
    :return: complex
    """
    if 'j' not in c_str:
        return complex(float(c_str), 0)
    index = 0
    for i, c in enumerate(c_str):
        if c in ('+', '-') and i != 0 and c_str[i-1] not in ('e', 'E'):
                index = i
                break
    if index == 0:
        real = 0
    else:
        real = float(c_str[:index])
    imag = float(c_str[index:-1])
    return complex(real, imag)


def rochambeau():
    """
    Problem 6-14, Rochambeau game
    :return: None
    """
    from random import choice
    c_list = ['stone', 'shear', 'paper']
    win_lose_dict = {('stone', 'stone'): 'draw', ('shear', 'shear'): 'draw', ('paper', 'paper'): 'draw',
                     ('stone', 'shear'): 'win ', ('shear', 'stone'): 'lose', ('paper', 'stone'): 'win',
                     ('stone', 'paper'): 'lose', ('shear', 'paper'): 'win', ('paper', 'shear'): 'lose'}
    while True:
        y_choice = raw_input('Your choice>')
        if y_choice not in c_list + ['.']:
            print 'Can not understand...0.0'
            continue
        if y_choice == '.':
            print 'Bye, my dear...'
            break
        c_choice = choice(c_list)
        print 'You just choose:', y_choice
        print 'Computer choose:', c_choice
        print 'Result:', win_lose_dict[(y_choice, c_choice)]


def days_diff(start, end):
    """
    Problem 6-15 (a), calculate the days between start and end
    :param start: str, format is MM/DD/YY
    :param end: str, format is MM/DD/YY
    :return: int, days
    """
    from datetime import datetime
    start_time, end_time = (datetime.strptime(x, '%m/%d/%Y') for x in (start, end))
    assert start_time < end_time
    return (end_time - start_time).days


def live_days(birthday):
    """
    Problem 6-15 (b), calculate the days from a person birth to today
    :param birthday: str, birthday
    :return: int, days
    """
    from datetime import datetime
    birthday_time = datetime.strptime(birthday, '%m/%d/%Y')
    assert birthday_time < datetime.today()
    return (datetime.today() - birthday_time).days


def next_birthday_days(birthday):
    """
    Problem 6-15 (b), calculate the days to next birthday
    :param birthday: str, birthday
    :return: int, days
    """
    from datetime import datetime
    birthday_time = datetime.strptime(birthday, '%m/%d/%Y')
    today = datetime.today()
    next_time = birthday_time.replace(year=today.year if birthday_time < today else today.year + 1)
    return (next_time - today).days


def matrix_add(matrix_a, matrix_b):
    """
    Problem 6-16(a), add two matrix
    matrix must be a list with list item, like [[...], [...],..., [...]]
    :param matrix_a: list, using list to represent matrix
    :param matrix_b: list
    :return: list
    """
    assert is_matrix(matrix_a) is True and is_matrix(matrix_b) is True,\
        'not illegal matrix'
    assert [len(a) for a in matrix_a] == [len(b) for b in matrix_b],\
        'length of two matrix must be the same'
    r_list = list()
    for i in range(len(matrix_a)):
        r_list.append([a + b for a, b in zip(matrix_a[i], matrix_b[i])])
    return r_list


def matrix_mul(matrix_a, matrix_b):
    """
    Problem 6-16 (b), multiply two matrix
    matrix must be a list with list item, like [[...], [...],..., [...]]
    :param matrix_a: list, using list to represent matrix
    :param matrix_b: list
    :return: list
    """
    if len(matrix_a) == 0 or len(matrix_b) == 0:
        return []
    assert is_matrix(matrix_a) is True and is_matrix(matrix_b) is True,\
        'not illegal matrix'
    assert len(matrix_a[0]) == len(matrix_b), 'col of matrix_a is not match row of matrix_b'
    r_list = list()
    for list_a in matrix_a:
        # use * to input args of zip function
        r_list.append([list_mul(list_a, list_b) for list_b in zip(*[i for i in matrix_b])])
    return r_list


def list_mul(list_a, list_b):
    """
    function for Problem 6-16 to calculate the row of a mul col of b
    :param list_a: list, col of a
    :param list_b: list, row of b
    :return: float or int
    """
    result = 0
    for a, b in zip(list_a, list_b):
        result += a * b
    return result


def is_matrix(matrix):
    """
    function Problem 6-16 to check if matrix illegal
    :param matrix: matrix to be checked
    :return: bool, True if matrix is illegal
    """
    col = len(matrix[0])
    if col == 0:
        return False
    for i in range(len(matrix)):
        if len(matrix[i]) != col:
            return False
    else:
        return True


def my_pop(in_list):
    """
    Problem 6-17, pop the newest item of list and return list
    :param in_list: list
    :return: list
    """
    out_list = in_list[:-1]
    return out_list


def get_list(container, col, direct):
    """
    function for Problem 6-19, get list for container
    :param container: list, string or tuple
    :param col: int
    :return: list
    """
    assert direct in ('row', 'col')
    p_list = list()
    length = len(container)
    if direct == 'row':
        for i in range(0, length, col):
            p_list.append(list(container[i:(i+col if i+col < length else length)]))
        if len(p_list) != 0:
            for i in range(col-len(p_list[-1])):
                p_list[-1].append('')
    if direct == 'col':
        t_list = get_list(container, (length / col if length % col == 0 else length / col + 1), 'row')
        p_list = zip(*[i for i in t_list])
    return p_list


def print_container(container, col=1, direct='row'):
    """
    Problem 6-19, print container
    :param container: list, string or tuple
    :param col: int
    :return: None
    """
    if direct not in ('row', 'col'):
        direct = 'row'
    p_list = get_list(container, col, direct)
    for i in p_list:
        for j in i:
            print '%10s' % str(j),
        print

if __name__ == '__main__':
    print __doc__
    print_container('')
