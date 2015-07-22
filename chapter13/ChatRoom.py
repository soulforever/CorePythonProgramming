# -*- coding: utf-8 -*-

"""
Homework for chapter 13, problem 11-12
"""

__author__ = 'guti'

users_form = {}
rooms_form = {}


class User(object):
    def __init__(self, user_name):
        self.name = user_name
        self.mailbox = list()
        self.rooms = list()

    def add_room(self, room):
        if room.name not in rooms_form:
            self.rooms.append(room.name)
            rooms_form[room.name] = room
            room.users.append(self.name)
        else:
            print 'Room has been exist...'

    def invite(self, user_name, room_name):
        if room_name in self.rooms:
            users_form[user_name].rooms.append(room_name)
            rooms_form[room_name].users.append(user_name)
        else:
            print 'Sorry %s, you do not have room named %s' % (self.name, room_name)

    def send_msg(self, msg):
        msg.from_name = self.name
        if not msg.str_msg:
            return
        if msg.user_name:
            users_form[msg.user_name].mailbox.append(msg)
        elif msg.room_name:
            if msg.room_name in self.rooms:
                for user_name in rooms_form[msg.room_name].users:
                    if user_name != self.name:
                        users_form[user_name].mailbox.append(msg)
            else:
                print 'Sorry %s, you do not have room named %s' % (self.name, msg.room_name)


class Message(object):
    def __init__(self, str_msg, user_name=None, room_name=None):
        self.str_msg, self.user_name, self.room_name = str_msg, user_name, room_name
        self.from_name = None

    def __str__(self):
        if self.user_name or self.room_name:
            to_name = self.user_name if self.user_name is not None else self.room_name
            return '<FROM: %s, TO: %s, CONTENT: %s>' % (self.from_name, to_name, self.str_msg)
        else:
            return 'BAD MESSAGE!'

    __repr__ = __str__


class Room(object):
    def __init__(self, room_name):
        self.name = room_name
        self.users = list()


if __name__ == '__main__':
    name_list = ['lily', 'nancy', 'cole', 'laowang']
    for name in name_list:
        users_form[name] = User(name)
    print users_form
    users_form['lily'].add_room(Room('travel'))
    print rooms_form
    users_form['lily'].invite('cole', 'travel')
    users_form['lily'].invite('nancy', 'travel')
    print users_form['lily'].rooms
    print rooms_form['travel'].users
    users_form['lily'].send_msg(Message('love SA!', room_name='travel'))
    users_form['cole'].send_msg(Message('Me too...', room_name='travel'))
    print users_form['lily'].mailbox
    print users_form['cole'].mailbox
    users_form['lily'].send_msg(Message('Get out!', user_name='laowang', room_name='travel'))
    print users_form['laowang'].mailbox