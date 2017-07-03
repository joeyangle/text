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
Events manage a flag that can be set to true with the set() method and reset
to false with the clear() method. The wait() method blocks until the flag is
true.  The flag is initially false.

通过这来可以实现线程之间简单逻辑关系

.isSet()相当于线程中的一个全局变量
clear()将flag设为FALSE
set()将flag设为TRUE
wait()等待一直到flag转为TRUE
'''
import threading,time
import random
def light():
    if not event.isSet():
        event.set() #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:#一个线程中一直循环产生车辆
        time.sleep(random.randrange(10))#随机取10以内的任意整数值
        #print(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()#先建立一个对象，事件锁
    Light = threading.Thread(target=light)#灯的线程
    Light.start()
    for i in range(3):#生成三辆车
        t = threading.Thread(target=car,args=(i,))
        t.start()