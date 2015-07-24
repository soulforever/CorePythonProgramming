# -*- coding: utf-8 -*-

"""
Homework for chapter 16, Problem 16-7
"""

__author__ = 'guti'

from socket import *


def server_v1(host='', port=9087, buf=1024):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    try:
        while True:
            print 'waiting for connection...'
            client_socket, addr = server_socket.accept()
            print 'connected from', addr
            while True:
                data = client_socket.recv(buf)
                if not data:
                    break
                print 'client>>> %s' % data
                msg = raw_input('server>>> ')
                client_socket.send(msg)
            client_socket.close()
    except (EOFError, KeyboardInterrupt):
        server_socket.close()


def client_v1(host='localhost', port=9087, buf=1024):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((host, port))
    while True:
        msg = raw_input('client>>> ')
        if not msg:
            break
        client_socket.send(msg)
        data = client_socket.recv(buf)
        if not data:
            break
        print 'server>>> %s' % data


if __name__ == '__main__':
    server_v1()

