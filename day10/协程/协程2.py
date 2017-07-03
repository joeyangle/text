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
#greenlet是一个用c实现的协程模块
#非自带
'''
gevent
学习一个直接封装好的协程模块，一定意义上实现自动切换
将程序通过gevent进行调用，gevent通过程序是否io阻塞来自动切换任务
很方便，不用greenlet进行人工设置


引入monkey，在python中，由于大量库的存在使得程序的编写更加便捷，但是
库是封装好的，所以往往程序不能直接识别其是否在执行io操作，此处调用
monkey，可以通过其来识别程序是否在执行io操作
'''
#如下，实现
from gevent import monkey

monkey.patch_all()
import gevent
from  urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
    gevent.spawn(f, 'https://www.baidu.com'),#spawn大量生产
    gevent.spawn(f, 'http://www.cnblogs.com/alex3714/articles/5248247.html'),
    gevent.spawn(f, 'https://github.com/'),
])
