# -*- coding: utf-8 -*-

"""
Homework for chapter 16, Problem 16-4
"""

__author__ = 'guti'

from socket import *
from time import ctime


def tcp_server(host='', port=9087, buf=1024):
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind((host, port))
    tcp_server_socket.listen(5)
    try:
        while True:
            print 'waiting for connection...'
            tcp_client_socket, addr = tcp_server_socket.accept()
            print 'connection from:', addr
            while True:
                data = tcp_client_socket.recv(buf)
                if not data:
                    break
                tcp_client_socket.send('[%s] %s' % (ctime(), data))
            tcp_client_socket.close()
    except (EOFError, KeyboardInterrupt):
        tcp_server_socket.close()


def tcp_client(host='localhost', port=9087, buf=1024):
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect((host, port))
    while True:
        data = raw_input('>>>')
        if not data:
            break
        tcp_client_socket.send(data)
        data = tcp_client_socket.recv(buf)
        if not data:
            break
        print data
    tcp_client_socket.close()


if __name__ == '__main__':
    tcp_server()
