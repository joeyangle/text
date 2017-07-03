#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/6'
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
# def shengch():
#     for x in range(4):
#         yield x*x
# f = shengch()
# print(f.__next__())
# f.__next__()
# print(f.__next__())
# print(f.__next__() ,'bb')
'''
yield 生成器
生成器函数在Python中与迭代器协议的概念联系在一起。
简而言之，包含yield语句的函数会被特地编译成生成器。当函数被调用时，他们返回一个生成器对象，
这个对象支持迭代器接口。函数也许会有个return语句，但它的作用是用来yield产生值的。

不像一般的函数会生成值后退出，生成器函数在生成值后会自动挂起并暂停他们的执行和状态，
他的本地变量将保存状态信息，这些信息在函数恢复时将再度有效
'''
import time
def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield#nice此处可以终止函数调用，再用send方法使函数继续调用
        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))

def producer(name):
    c = consumer('A')#生成器A
    c2 = consumer('B')#生成器B
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")