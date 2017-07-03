#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/8'
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
multiprocessing多进程    [英]多重处理
当一个任务设立多个进程
此时由于进程与进程之间内存是独立的，不能直接调用其它进程的数据
那么当一些地方需要进程与进程之间互相协调时，就面临进程间的通讯问题
'''
from multiprocessing import Process,Queue
import os

#Queues方法
'''
进程间的队列与线程间队列的设置并没有很大的区别
把相同的队列实例传入多个进程中即可实现多个进程对该队列的修改
即一定意义上实现了进程之间的通讯
'''
def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()#先生成一个队列实例
    p = Process(target=f, args=(q,))#建立了一个新进程，传参数和thread一样
    p.start()#线程启动
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()#结束线程

#Pipes管道
'''
作为一个管道实现两个进程之间的数据传递
parent_conn, child_conn = Pipe()此处生成端口的两端
这连个端口是互相平等的，通过
send()
recv()
实现信息的互传
'''
from multiprocessing import Pipe

def f(conn):
    conn.send([42, None, 'hello'])#
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()#pipe生成两个端口
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()

#managers
'''
该方法支持基本所有类型python对象的传输，如下：
types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore,
Condition, Event, Barrier, Queue, Value and Array.
挺不错的，通过manager建立的对象在进程间可以互相修改
其实以上三种都是同样的实现方式，都是实时copy，看似相同，其实也是占用了双份的内存？
但是，我们知道进程是并行的，那么如何避免多个进程同时修改同一个
数据而造成错误呢？依旧老样子，加锁使得进程同步
以上
'''
from multiprocessing import Manager

def f2(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f2, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)



