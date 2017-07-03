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
'''
通过两种办法建立新线程
1 join方法的作用是阻塞主进程无法执行join以后的语句,专注执行多线程,必须等待多线程执行完毕之后才能执行主线程的语句。
2 多线程多join的情况下,依次执行各线程的join方法,前一个结束之后,才能执行后一个。
3 无参数,则等待到该线程结束,才开始执行下一个线程的join。
4 设置参数后,则等待该线程N秒之后不管该线程是否结束，就开始执行后面的主进程。
通过join以确认线程结束
设置join(2)等同于join(timeout = 2)

守护进程
m.setDaemon(True) #将main线程设置为Daemon线程,它做为程序主线程的守护线程,
当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务

一般来说，线程之间并没有父子关系，线程都是相互独立的，就算“父线程”结束也对“子线程”没有丝毫影响
'''
import threading
import time

def said(name):
    print('my name is %s'%name)
    time.sleep(1)

#直接定义
n1 = threading.Thread(target=said,args=('peng',))
n2 = threading.Thread(target=said,args=('xin',))

n1.start()
n1.join(timeout=1)
n2.start()
n2.join(timeout=1)

print(n1.getName())
print(n2.getName())

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('my name is %s'%self.name)

threads = []

t1 = time.time()
for i in range(5):
    t = MyThread(i)
    t.start()
    threads.append(t)
    print(t.getName())

def main():
    for i in threads:
        i.join()
        print(time.time()-t1)

print(time.time()-t1)

m = threading.Thread(target=main,args=[])
m.setDaemon(True) #将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
m.start()
m.join(timeout=2)#由于主线程退出而导致m线程直接退出
print("---main thread done----")