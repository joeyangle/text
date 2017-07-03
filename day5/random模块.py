#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/9'
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
import time
import random
puke = []
huase = ['红心','梅花','黑桃','方块']
for one in range(0,4):
    aa = []
    for i in range(1,14):
        i = huase[one] + str(i)
        puke.append(i)
puke.append('大王')
puke.append('小王')
print(puke)
print(len(puke))
for num in range(10):
    print(random.sample(puke,17))
'''
'''
while True:
    beilv = 1
    person = random.shuffle(puke)
    person1 = puke[0:17]
    print(len(person1),person1)
    person2 = puke[17:34]
    print(len(person2),person2)
    person3 = puke[34:51]
    print(len(person3),person3)
    choose = puke[51:55]
    #现在把扑克牌分发显示给各位玩家
    #玩家反馈是否叫地主，由随机庄家开始叫地主，如果抢地主则倍率*2
    #将底牌加入地主的牌库
    #现在设立一个监视器，判断出牌是否符合规则，并且监视每一位的手牌数
    #一局结束后，询问是否go on？
    break
print(puke)
'''
'''
import os
#help(os)
import sys
print(sys.path)#查看当前环境路径
print(__file__)#查看当前文件相对路径
#所谓相对路径，例如：/pytext/python_days/random模块.py 这就是相对路径
#将相对路径修改为绝对路径
print()#现在输出的就是绝对路径
#通过下面的方法返回上一级文件，例如，返回一层
print()
#依次类推,就能找到所需要添加的环境变量
#找到后如下添加到环境路径中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#一般要用到的话至少返回两层以上，此处简写了
'''
import time
#help(time)
# time() -- return current time in seconds since the Epoch as a float
#     clock() -- return CPU time since process start as a float
#     sleep() -- delay for a number of seconds given as a float
#     gmtime() -- convert seconds since Epoch to UTC tuple
#     localtime() -- convert seconds since Epoch to local time tuple
#     asctime() -- convert time tuple to string
#     ctime() -- convert time in seconds to string
#     mktime() -- convert local time tuple to seconds since Epoch
#     strftime() -- convert time tuple to string according to format specification
#     strptime() -- parse string to time tuple according to format specification
#     tzset() -- change the local timezone
#print(time.time())
#print(time.clock())
#print(time.localtime())
#import random
#help(random)
aa = ['1','2','3','4','5','6','7']
#先来做一个装饰器，将函数值输出
#print(random.random()) #0到1中的一个浮点数
#print(random.choice(aa))  #在aa中随机取一个值
#print(random.randrange(0,20,4))  #在range(0,20,4)中随机取一个值
#print(random.sample(aa,4))  #在aa中随机取4个值
#random.shuffle(aa)  #将aa打乱
#print(aa)
#有没有什么有意思的操作。。。
#现在看看能不能画图来判断一下这个伪随机数的随机性
#import matplotlib
