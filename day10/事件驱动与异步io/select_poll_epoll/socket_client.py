#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/15'
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
import sys
#两个client，分别发送三句话
messages = ['This is the message. ',
            'It will be sent ',
            'in parts.',
            ]
server_address = ('localhost', 10000)

# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         ]#地址

# Connect the socket to the port where the server is listening
print(sys.stderr, 'connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)#先连接上

for message in messages:#开始发送了

    # Send messages on both sockets
    for s in socks:
        print(sys.stderr, '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode())

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print(sys.stderr, '%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname())
            s.close()