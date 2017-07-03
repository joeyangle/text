#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/16'
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
类
    属性
        实例变量
        类变量，相同的属性
        私有属性__var
    方法
        构造方法，初始化实例
        析构函数，实例在销毁释放的时候执行，不管写不写都会执行，写了相当于重构了它
        私有方法
        
对象：实例化一个类之后得到的对象


封装
    把一些功能的实现细节不对外暴露
继承
    继承，组合(就和另一个类关联起来了)
    代码的重用
    单继承
    多继承
        2.7 经典类，深度优先， 新式类，广度优先
        3.x 都是广度优先  
        super(Teacher,self).__init__(name,age,sex)继承
        基类的主要功能是作为父类继承给子类，不应该出现继承两个父类之间还有交集的情况
        
多态
    接口重用，一种接口，多种实现
    多种类似的接口只需要调用一个接口
    类名.方法(实例)
'''
'''
类= =
？在类中只能调用其内部的参数
__init__传参数
面向对象三大属性
封装
继承
多态
'''

#class Role:经典类
class Role(object): #新式类
    n = 123 #类变量，先找实例变量，再找类变量
    #__init__构造函数
    #在实例化时做一些类的初始化的工作
    #self将
    def __init__(self, name, role, weapon, life_value=100, money=15000):#传参数
        self.name = name#实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value#私有属性，仅在内部可以访问
        self.money = money

    def shot(self):#类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name))


r1 = Role('Alex', 'police', 'AK47') #生成一个角色,实例化（初始化一个类，造了一个对象）
r2 = Role('Jack', 'terrorist', 'B22')  #把一个类变成一个具体对象的过程叫实例化
r1.buy_gun('b22')

'''
类变量的用途？
类中所需要共用的属性，节省代码
'''

'''
析构函数： 在实例释放或销毁的时候执行的，通常用于做一些收尾工作，
关闭一些数据框链接，打开的临时文件
'''
def __del__(self):
    print('%s彻底死了》》-《《'%self.name)

'''
私有方法，私有属性
类的封装
内部可以访问，通过这样就可以把私有变成非私有
'''
##继承##
'''
经典类与新式类的区别主要就在继承上
查询策略
Python2.X 经典类深度优先，新式类广度优先
Python3.X 都是广度优先
广度优先：先把横向策略遍历，继承遵照该方法
深度优先：先把纵向策略遍历
'''
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('%s is eating...'%self.name)
    def talk(self):
        print('%s is talking...'%self.name)
    def sleep(self):
        print('%s is sleeping...'%self.name)


class Realation(object):
    def make_friends(self, obj):
        print('%s is making friends with %s' % (self.name, obj.name))


class Man(People,Realation):#继承父类People
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)这两种方法相同，推荐下面那种
        super(Man,self).__init__(name,age)#从父类继承，新式类写法
        self.money = money
        print('%s 一出生就有%s money'%(self.name,self.money))
    def piao(self):
        print('%s is piaoing....'%self.name)


##多态##
#一种接口，多种实现，实现接口的重用




