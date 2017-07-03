#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/7'
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

from threading import Timer
def hello():
    print("hello, world")

t = Timer(30.0, hello)#线程自带的时间控制指令，从start后开始计时
t.start()  # after 30 seconds, "hello, world" will be printed
t.cancel()#删除这个时间指令
#详细看文档说明
'''
队列queue
class queue.Queue(maxsize=0) #先入先出
class queue.LifoQueue(maxsize=0) #last in first out 
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列(priority number, data)


生产消费者模型

多线程
边生产边消耗即生产消费者模型
基于 queue队列

put()将对象置入队列中
get()从队列中取出一个对象
join()直至队列中所有的对象被取走
qsize()队列中对象的多少
task_done()  告知这个任务执行完了??
'''
#block组织，阻塞
import queue
import threading
import time
import random

q = queue.Queue()
q.join()#直至队列为空，否则一直等待队列被取空
q.put('1')
q.put('2')
print(q.get())

def producer():
    for i in range(10):
        q.put("骨头 %s" % i)
    print("开始等待所有的骨头被取走...")
    q.join()
    print("所有的骨头被取完了...")

def consumer(n):
    while q.qsize() > 0:
        time.sleep(random.randrange(3))
        print("%s 取到" % n, q.get())
        q.task_done()  # 告知这个任务执行完了

q = queue.Queue()
p = threading.Thread(target=producer, )
p.start()

c1 = consumer("李闯")