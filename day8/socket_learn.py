#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/26'
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
#粘包，缓冲区的存在缓冲区文件一起发出去的数据在一起被发送出去
#防止粘包，设置sleep使超时隔开数据，其实没有什么用
'''
sk.bind(address) 必会

　　s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。
在AF_INET下，以元组（host,port）的形式表示地址。

sk.listen(backlog) 必会

　　开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。

      backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept
      进行处理的连接个数最大为5
      这个值不能无限大，因为要在内核中维护连接队列

sk.setblocking(bool) 必会

　　是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。

sk.accept() 必会

　　接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。

　　接收TCP 客户的连接（阻塞式）等待连接的到来

sk.connect(address) 必会

　　连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。

sk.connect_ex(address)

　　同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061

sk.close() 必会

　　关闭套接字

sk.recv(bufsize[,flag]) 必会

　　接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。

sk.recvfrom(bufsize[.flag])

　　与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。

sk.send(string[,flag]) 必会

　　将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。

sk.sendall(string[,flag]) 必会

　　将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。

      内部通过递归调用send，将所有内容发送出去。

sk.sendto(string[,flag],address)

　　将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。

sk.settimeout(timeout) 必会

　　设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）

sk.getpeername()  必会

　　返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。

sk.getsockname() 

　　返回套接字自己的地址。通常是一个元组(ipaddr,port)

sk.fileno() 

　　套接字的文件描述符

socket.sendfile(file, offset=0, count=None)

     发送文件 ，但目前多数情况下并无什么卵用。
'''