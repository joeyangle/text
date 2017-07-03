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
import threading
import time

def sock_conn():
    client = socket.socket()

    client.connect(("localhost",8001))
    count = 0
    while True:
        time.sleep(0.4)
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        client.send( ("hello %s" %count).encode("utf-8"))

        data = client.recv(1024)

        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果 get_ident返回当前线程的标识符
        count +=1

for i in range(100):
    t = threading.Thread(target=sock_conn)#同时跑一百个线程请求server端
    t.start()