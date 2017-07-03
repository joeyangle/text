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
class Dog(object):
    '''
    描述 描述 描述 狗
    '''
    aa = 'aa'
    def __init__(self,name,food):
        self.food = food
        self.name = name

    def talking(self):
        print('%s is eating %s'%(self.name,self.food))

    def __str__(self):#使内存地址变的具象化，便于识别
        return '<obj:%s>'%self.name

d = Dog('jingmao','gutou')
print(d)
print(Dog.__doc__)#打印类描述信息

#__modele__ 表示当前操作的对象在哪个模块,位置，返回这个类是从哪里导入过来的
#__class__ 表示当前操作的对象的类是什么，还有从哪导入过来的

print(Dog.__dict__)#__dict__ 打印类里的所有实例属性(可以被实例调用)，不包括类属性


class Foo(object):#字典，字典，字典
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):#获取key对应的value
        print('__getitem__',key)
        return self.data.get(key)

    def __setitem__(self, key, value):#将一组值加入到字典中
        print('__setitem__',key,value)
        self.data[key] = value

    def __delitem__(self, key):#删除key
        print('__delitem__',key)
        del self.data[key]

obj = Foo()
obj['name'] = 'alex'#调用__setitem__创建
obj['food'] = 'gutou'
print(obj['name'])#调用__getitem__显示key对应value
print(obj.data)
del obj['food']#调用__delitem__删除字典中的key
print(obj.data)
#可以用于通过字典控制各种功能的调用
#反射大概就是这样吧？

# result = obj['k1'] #自动
# obj['k2'] = 'alex'
# del obj['k1']

#__call__()方法，
# Foo()()--》执行__call__()方法


'''
既然一切皆为对象，那每个对象是具体的实体，
那么一个类也就是一个实例，那么这个类（实例）是谁？
创建类有两种方式，一种是普通的
class 类：
另一种装逼方式
type: 类的类，牛逼了，一切的起源

'''
class Moo(object):
    def __init__(self,name):
        self.name = name

f = Moo('alex')

print(type(f))
print(type(Moo))#Moo这个类就是来自type，type是类的始祖

#另一种装逼方式
def func(sel):
    print('nice day!joey')

Noo = type('Noo',(object,),{'talk':func})#新建了类，第二项继承的类是元组的形式
print(type(Noo))
aaa = Noo()#实例化
aaa.talk()
print(type(aaa.talk))

'''
__new__是用来创建实例的，默认已经写好了，会自动执行
__mataclass__原始类的调用？该板块水深
'''
