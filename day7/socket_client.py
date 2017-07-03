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
#客户端
import socket

client = socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))#连接端口
while True:
    shuru = input('>:')
    if len(shuru) == 0:
        continue
    client.send(shuru.encode('utf-8'))#发送数据，只接收b类型，encode将识别数据编译成字节型
    daxiao = client.recv(1024)#将要接收数据的大小
    print(daxiao)
    client.send(('wozhuanbeihaole').encode())#此处发送以避免粘包
    daxiao = int(daxiao)
    print(daxiao)
    print('将要收到的结果大小:%s'%daxiao)
    data_size = 0
    received_data = b''
    while data_size < daxiao:
        data = client.recv(1024)

        #print(len(data))
        #print(data.decode())
        data_size += len(data)
        #print(33,data_size)
        received_data += data
        #print(received_data.decode('utf-8'))
        #print(1)
        if len(data) < 1024:
            break

    print(received_data.decode('utf-8'),len(received_data))#decode将字节型编码成可识别
    print("收完了",data_size)
    #data = client.recv(1024)#接受服务器返回的数据，此处只收1024字节
    #print("recv:",data.decode())
print('关闭')
client.close()#关闭