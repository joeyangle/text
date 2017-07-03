#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/10'
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
未知原因，运行假如有函数名test+num形式，则会进入测试模式？？

greenlet
设定了前位置，转换后位置，并以此保存，将运行顺序串联起来
此处仍需要人工设置好跳转的操作，且无法避免io操作切换
'''
from greenlet import greenlet

def tet1():
    print(12)
    gr2.switch()#暂停转换，到gr2目标
    print(34)
    gr2.switch()

def tet2():
    print(56)
    gr1.switch()#再次转换
    print(78)
    gr1.switch()#不能回调到已经执行过的步骤

gr1 = greenlet(tet1)#目标tet1，类似作为一个指令标
gr2 = greenlet(tet2)#目标tet2
gr1.switch()#启动