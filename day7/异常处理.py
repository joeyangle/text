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
异常处理
'''

# class Dog(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def say(self):
#         print('%s is saia...'%self.name)
#
#     def eat(self):
#         print('%s is eating...'%self.name)
#
# d = Dog('jiang')
# choice = input('---->').strip()

# try:
#     getattr(d,choice)
# except KeyError as aa:
#     print(aa)

qinshi = ['jiang','liu','pen']

try:
    qinshi[3]
except KeyError as aa:
    print('出错了',aa)
#except...
except Exception:#其它所有错误
    print('未知错误')
else:#没有任何错误时
    print('一切正常')
finally:
    print("不管有没有错，都执行")

#raise keyvalue 使自己写的异常执行

#断言
assert type(qinshi) is list
#检查是否正确，假如后面的程序非常重要，不能出错，上一层保险
