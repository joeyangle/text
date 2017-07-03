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
'''
通过gevent实现socket多并发
只要在server端修改就可以啦
'''
import socket
import gevent

from gevent import socket,monkey
monkey.patch_all()#相当于声明要查看所有io

def server(port):
    ss = socket.socket()
    ss.bind(('0.0.0.0',port))#绑定
    ss.listen(100)
    while True:
        cli,addr = ss.accept()
        gevent.spawn(handle_request,cli)#将每一个请求

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:
        conn.close()

if __name__ == '__main__':
    server(8001)

