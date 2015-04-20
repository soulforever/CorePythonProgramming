# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 7-5
"""

__author__ = 'guti'


from time import ctime

db = {}


def newusr(name=None):
    if not name:
        prompt = 'login name:'
        while True:
            name = raw_input(prompt).lower()
            if name in db:
                prompt = 'name taken, try another:'
                continue
            else:
                break
    else:
        print 'User name is %s' % name
    pwd = raw_input('password:')
    time = ctime()
    db[name] = [pwd, time]


def oldusr():
    name = raw_input('login:').lower()
    if name not in db:
        is_new = raw_input('User %s is not exist, create a new user?(Y/N)' % name).strip()[0].lower()
        if is_new not in 'yn' or is_new == 'y':
            newusr(name)
    else:
        pwd = raw_input('password:')
        password = db[name][0]
        if password == pwd:
            db[name][1] = ctime()
            print 'welcome back %s (at %s)' % (name, db[name][1])


def manage():
    prompt = '''
Choose the manage command:
(D)el
(L)ist
(Q)uit
    '''
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (IOError, KeyboardInterrupt):
                choice = 'q'
            print 'You picked : [%s]' % choice

            if choice not in 'dlq':
                print 'Invalid option, try again'
            else:
                chosen = True

            if choice == 'q':
                done = True
            if choice == 'd':
                name = raw_input('The list is' + str(db) +
                                 '\nEnter the user name need deleted: ')
                if name not in db:
                    print 'Delete user failed, user is not exist.'
                else:
                    del name
            if choice == 'l':
                print db


def showmenu():
    prompt = '''
(N)ew User
(L)ogin
(M)anage
(Q)uit
Enter choice:
    '''

    done = False

    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (IOError, KeyboardInterrupt):
                choice = 'q'
            print 'You picked : [%s]' % choice

            if choice not in 'mnlq':
                print 'Invalid option, try again'
            else:
                chosen = True

            if choice == 'q':
                done = True
            if choice == 'n':
                newusr()
            if choice == 'l':
                oldusr()
            if choice == 'm':
                manage()


if __name__ == '__main__':
    showmenu()
