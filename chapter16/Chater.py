# -*- coding: utf-8 -*-

"""
Homework for chapter 16, Problem 16-7
"""

__author__ = 'guti'

from socket import *
import threading
from Queue import Queue


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
    try:
        while True:
            msg = raw_input('client>>> ')
            if not msg:
                break
            client_socket.send(msg)
            data = client_socket.recv(buf)
            if not data:
                break
            print 'server>>> %s' % data
    except (EOFError, KeyboardInterrupt):
        client_socket.close()


#######################################################################################################################
# SERVER
#######################################################################################################################
condition = threading.Condition()
queue = Queue(32)


def server(host='', port=9087, buf=1024):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        name = conn.recv(buf)
        print 'connection with', addr
        queue.put('Welcome ' + name)
        threads = list()
        threads.append(threading.Thread(target=server_data_in, args=(conn, name, buf)))
        threads.append(threading.Thread(target=server_data_out, args=(conn,)))

        for t in threads:
            t.start()


def server_data_in(conn, name, buf=1024):
    while True:
        try:
            data = conn.recv(buf)
            if data == name + ': exit':
                conn.close()
            queue.put(data, True)
        except (EOFError, KeyboardInterrupt):
            queue.put(name+'left...', True)
            conn.close()
            break


def server_data_out(conn):
    while True:
        try:
            data = queue.get(True)
            conn.send(data)
        except (EOFError, KeyboardInterrupt):
            return


#######################################################################################################################
# CLIENT
#######################################################################################################################

out_str = ''
in_str = ''


def client(host='localhost', port=9087, buf=1024):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))
    name = raw_input('YOUR NAME:')
    s.send(name)
    threading.Thread(target=client_data_in, args=(s,)).start()
    threading.Thread(target=client_data_out, args=(s, name)).start()


def client_data_in(conn, buf=1024):
    global in_str
    while True:
        in_str = conn.recv(buf)
        if not in_str:
            return
        if in_str != out_str:
            print in_str


def client_data_out(conn, name):
    global out_str
    while True:
        out_str = raw_input('U SAY:')
        out_str = name + ':' + out_str
        conn.send(out_str)


if __name__ == '__main__':
    # server()
    client()

