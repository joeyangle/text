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
互斥锁 同时只允许一个线程更改数据，
而Semaphore是同时允许一定数量的线程更改数据 ，
比如厕所有3个坑，那最多只允许3个人上厕所，
后面的人只能等里面有人出来了才能再进去。
'''
import time,threading

def run(n):
    semaphore.acquire()#允许多个进程获得资源使用权
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:#正在运行的线程数
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)