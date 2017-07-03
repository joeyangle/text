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
进程池
http://www.cnblogs.com/kaituorensheng/p/4465768.html 这一篇解释的很详细
进程池，执行完一个进程后添加新的进程进去，直至没有
进程池中有两个方法：
apply    阻塞的,变成串行，下一个进程运行必须等待上一个进程执行完成
apply_async    非阻塞的，不必等待，只要规定进程数未满即可执行新进程
close()    关闭pool，使其不在接受新的任务。不再添加新的任务进去
terminate()    结束工作进程，不再处理未完成的任务。
join()    主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用
'''
from  multiprocessing import Process,Pool
import time

def Foo(i):
    print('nice')
    time.sleep(2)
    return i + 100

def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':#这个也必须？没有报错，为什么
    pool = Pool(processes=3)
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)#callback回调函数，进程执行完后运行的函数，和前进程无关
        # pool.apply(func=Foo, args=(i,))
    print('end')
    pool.close()
    pool.join()#放后面，先close，否则出错(?执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束)
    # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    print('done')
