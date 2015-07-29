# -*- coding: utf-8 -*-

"""
Home work for 16-6
"""

__author__ = 'guti'


import socket
from time import ctime
from UDP import udp_client


def udp_server(host='', port=9087, buf=1024):
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind((host, port))
    try:
        while True:
            print 'waiting for connection...'
            data, addr = udp_server_socket.recvfrom(buf)
            udp_server_socket.sendto('[%s] %s' % (ctime(), socket.getservbyname('daytime', 'udp')), addr)
            print '...received from and return to:', addr
    except (EOFError, KeyboardInterrupt):
        udp_server_socket.close()


if __name__ == '__main__':
    udp_server()
    # udp_client()
