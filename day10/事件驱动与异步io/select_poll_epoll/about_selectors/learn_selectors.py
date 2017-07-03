#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/19'
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

import selectors
import socket

sel = selectors.DefaultSelector()#建立一个实例

def accept(sock, mask): #
    conn, addr = sock.accept()  # Should be ready一个新连接
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)#非阻塞模式
    sel.register(conn, selectors.EVENT_READ, read) #新连接注册read回调函数
    # 新注册的链接加入到sel中，然后调用read函数

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)#建立实例
#来了新连接就调用accept

while True:
    events = sel.select()#可能是select，可能是epoll（默认），默认阻塞，有活动链接就返回活动的链接列表
    for key, mask in events:
        callback = key.data # 掉accept
        callback(key.fileobj, mask) #key.fileobj = fd文件句柄

#第一次建立连接，调用accept将该连接加入到注册表中
#第二次监控到该连接活动，调用read函数处理