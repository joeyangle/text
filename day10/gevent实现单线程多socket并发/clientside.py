#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import socket

HOST = 'localhost'
PORT = 8001
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    if msg == b'exit':
        break
    ss.sendall(msg)
    data = ss.recv(1024)
    # print(data)
    print('Received', repr(data))

ss.close()


