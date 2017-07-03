
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/5'
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
什么时候使用进程呢？
就我来看，进程不过也是目录的一种而已，它将线程与资源结合，使得程序结构
更加的明确，简化了逻辑结构，便于梳理理解。
一定意义上来说清晰地结构规则设立使得人们在有限的智商下能够完成无限的创造

'''
# import multiprocessing
# from multiprocessing import Process
# import time
#
# def f(name):#子进程下的主函数
#     time.sleep(2)
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))#和建立线程一样的方法
#     p.start()
#     p.join()

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())#得到进程名
    print('process id:', os.getpid())
    print("\n\n")

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()


