#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/23'
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
反射
    hasattr(obj,name_str)， 判断一个对象obj里是否有name_str对应的字符串对应的方法
    getattr(obj,name_str), 根据字符串去获取obj对象里的对应的方法的内存地址，调用
    setattr(x, 'y', v) setattr(x, 'y', v) is equivalent to ``x.y = v''给一个x对象添加新的属性y对应外部的v
    delatter(obj,name_str), 删除obj对象中的name_str字符串对应的方法
'''

#hasattr(d,choice) 判断输入的choice（字符串）是否存在d中

#getattr(d,choice)() 调用该函数
def talk(self):
    print('%s is studying'%self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def say(self):
        print('%s is saia...'%self.name)

    def eat(self):
        print('%s is eating...'%self.name)

d = Dog('jiang')
choice = input('---->').strip()
print(hasattr(d,choice))#如果有则返回为Ture
#getattr(d,choice)()#调用该方法

if hasattr(d,choice):
    func = getattr(d,choice)
    func("jiang")
    delattr(d,choice)#把这个类方法删除
else:
    # setattr(d,choice,talk)#setattr(x, 'y', v) is equivalent to ``x.y = v''
    # d.talk(d)#相当于把class外的函数关联到该class中
    setattr(d,choice,None)#静态属性直接把值返回
    print(getattr(d,choice))
'''


'''