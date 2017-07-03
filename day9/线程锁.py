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
线程锁用于解决多线程下多个线程访问同一份数据的问题
上锁以后该对象只能被先上锁的线程修改，其它线程要调用改对象只有等待
'''
'''
多线程的不安全：
假如我们先创建了10个线程，一开始运行的很流畅，但是结果就是不对
你不知道什么情况啊，一直查代码也没有发现什么问题
其实多线程在执行时由于其并行，可能出现调用混乱的情况
但是python3并不会发生这种情况，所以也不用去管理啦
'''
import time
import threading

def addNum():
    global num  # 在每个线程中都获取这个全局变量
    print('--get num:', num)
    time.sleep(1)
    num -= 1  # 对此公共变量进行-1操作

num = 100  # 设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)

#以上在Python2.7x上可能会出现结果不为0的情况
#可以看到取到的每个值均为100，那返回值不应该是99嘛，但是在这结果就是0
#可以认作在Python3中自动加了线程锁

'''
counter_lock = threading.Lock() #只是定义一个锁,并不是给资源加锁,你可以定义多个锁,像下两行代码,
当你需要占用这个资源时，任何一个锁都可以锁这个资源 
counter_lock2 = threading.Lock()  
counter_lock3 = threading.Lock() 
锁是一个标记，表示这部分资源已经被占用
RLock递归锁
lock.acquire()加锁
lock.release()解锁
'''

'''
还有一种奇葩“死锁”
如果多个线程要调用多个现象，而A线程调用A锁占用了A对象，
B线程调用了B锁占用了B对象,A线程不能调用B对象，B线程不能
调用A对象，于是一直等待。这就造成了线程“死锁”。

Threading模块中，也有一个类，RLock，称之为可重入锁。
该锁对象内部维护着一个Lock和一个counter对象。counter对象
记录了acquire的次数，使得资源可以被多次require。最后，
当所有RLock被release后，其他线程才能获取资源。在同一个线程中，
RLock.acquire可以被多次调用，利用该特性，可以解决部分死锁问题。
'''
import threading, time

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire(timeout=1)#假如一秒之内还没有释放锁住的内容，则自动释放
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.RLock()#先创建一把锁，递归锁
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)





