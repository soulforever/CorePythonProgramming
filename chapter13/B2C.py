# -*- coding: utf-8 -*-

"""
Homework for chapter 13
"""

__author__ = 'guti'


class User(object):
    """
    Problem 13-11, B2C
    """
    def __init__(self, name):
        self.name = name
        self.carts = dict()
        self.add_cart(Cart('default', {}))

    def add_cart(self, cart):
        if cart.name not in self.carts:
            self.carts[cart.name] = cart

    def buy(self, item, cart_name='default'):
        if item.name not in self.carts[cart_name].data:
            self.carts[cart_name].data[item.name] = item
        else:
            self.carts[cart_name].data[item.name].num += item.num


class Item(object):
    def __init__(self, name, num=1):
        self.name, self.num = name, num

    def __str__(self):
        return '(%s, %s)' % (self.name, self.num)

    __repr__ = __str__


class Cart(object):
    def __init__(self, name, data):
        self.name, self.data = name, data

    def __str__(self):
        return '<%s: %s>' % (self.name, str(self.data))

    __repr__ = __str__


if __name__ == '__main__':
    guti = User('guti')
    guti.buy(Item('apple'))
    print guti.carts['default']
    guti.buy(Item('banana'))
    print guti.carts['default']
    guti.buy(Item('apple'))
    print guti.carts['default']
