# -*- coding: utf-8 -*-

"""
Homework for chapter 16, Problem 16-4
"""

__author__ = 'guti'
from socket import *
from time import ctime


def udp_server(host='', port=9087, buf=1024):
    udp_server_socket = socket(AF_INET, SOCK_DGRAM)
    udp_server_socket.bind((host, port))
    try:
        while True:
            print 'waiting for connection...'
            data, addr = udp_server_socket.recvfrom(buf)
            udp_server_socket.sendto('[%s] %s' % (ctime(), data), addr)
            print '...received from and return to:', addr
    except (EOFError, KeyboardInterrupt):
        udp_server_socket.close()


def udp_client(host='localhost', port=9087, buf=1024):
    addr = (host, port)
    udp_client_socket = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = raw_input('>>>')
        if not data:
            break
        udp_client_socket.sendto(data, addr)
        data, addr = udp_client_socket.recvfrom(buf)
        if not data:
            break
        print data
    udp_client_socket.close()


if __name__ == '__main__':
    udp_client()