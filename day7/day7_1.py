#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/22'
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
静态方法
类的工具包，没有变量关联，但是功能有共同的特性，比较清楚思路
只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性

'''
class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod#静态方法，实际上跟该类没什么关系了，只是名义上属于该类
    def eat(self,food):#不会传self了
        print("%s is eating %s"%(self.name,food))

d = Dog("ChenRonghua")
d.eat(d,'包子')#自己传自己，这样没什么意思

'''
类方法@classmethod
    使该方法只能访问类变量，不能访问实例变量
    保证调用本地地址，确保安全性？固定不变的东西？ 
'''
class Dog(object):
    #n = 333
    name = "huazai"#实际调用的是类变量，要是仅有实例变量会报错
    def __init__(self,name):
        self.name = name


    #@staticmethod#静态方法，实际上跟类没什么关系了
    @classmethod#类方法
    def eat(self):#不会传self了
        print("%s is eating %s"%(self.name,'food'))

d = Dog("ChenRonghua")#实例变量传入，但是没有调用
#d.eat(d,'包子')#自己传自己，这样没什么意思
d.eat()

'''
属性方法@property 
'NoneType'空类型，不能调用
    把一个方法变成一个静态属性，不要括号了
    d.eat<--这样
    不能传参数了吗？
应用场景
把实现细节隐藏了
'''
class Dog(object):

    def __init__(self,name):
        self.name = name
        self.__food = None#先新建一个对象

    @property#把一个方法变成一个属性
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))#del之后没有self.__food就报错了

    @eat.setter#实例化时先建立了一个对象，就相当于把想要应用的参数引用进来，然后就能赋值了
    def eat(self,food):#可以改成大写
        print('set to food:',food)
        self.__food = food#通过这里调入

    @eat.deleter#删除属性化方法引入的参数
    def eat(self):
        del self.__food#实际是在此处删除了要调用的__food
        print('删完了')

d = Dog("ChenRonghua")
d.eat#一个属性
d.eat = '包子'#通过.setter给属性参数
d.eat
# aa = 'aa'
# del aa#删除一个变量
del d.eat
d.eat#再调用就报错了，还是调用原来的