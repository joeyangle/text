#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/24'
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

#服务器端
import os,time
import socket
server = socket.socket()
server.bind(('localhost',6969))#绑定要监听端口
while True:
    server.listen() #监听
    print('开始等待。。。')

    conn,addr = server.accept() #等电话打进来，返回两个值，conn对方电话打过来的实例，addr就是个地址
    #conn就是客户端连过来而在服务端为其生成的一个连接实例
    print(conn,addr)
    print('有电话。。。')
    while True:
        data = conn.recv(1024)
        #cmd_ipconfig = os.popen(data.decode()).read()
        shuju = b''
        shuju += data
        if len(data) == 0:
            cmd_ipconfig = 'cmd not output...'
        #print('recv:',data.decode())
        if len(data) == 0: break
        #fanhui = input('>>')
        # daxiao =str(len(str(cmd_ipconfig).encode()))
        # if daxiao == 0:
        #     continue
        # else:
        #     conn.send(daxiao.encode())#先发大小给客户端
        # #缓冲区的建立提升了I/O效率
        # conn.send('>>>'.encode())
        # haole = conn.recv(1024)#据说在此插入一个接受可以避免粘包
        # print(haole)
        conn.send(b'shoudao')#返回去,有一个缓冲区，直到缓冲区全部发送出去
    print('用户已断开')

server.close()