#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/12'
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
同步与异步的区别
同步，必须完成上一件才能进行下一件
异步，当一个异步调用发出后，调用者不能立刻得到结果，但是程序继续往下运行

下面有个例子挺好玩的
'''
'''
 同步和异步的区别
 举个例子：普通B/S模式（同步）AJAX技术（异步）
同步：提交请求->等待服务器处理->处理完毕返回 这个期间客户端浏览器不能干任何事
异步: 请求通过事件触发->服务器处理（这是浏览器仍然可以作其他事情）->处理完毕
同步就是你叫我去吃饭，我听到了就和你去吃饭；如果没有听到，你就不停的叫，直到我告诉你听到了，才一起去吃饭。
异步就是你叫我，然后自己去吃饭，我得到消息后可能立即走，也可能等到下班才去吃饭。
所以，要我请你吃饭就用同步的方法，要请我吃饭就用异步的方法，这样你可以省钱。
举个例子 打电话时同步 发消息是异步
'''

import gevent

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]#
    gevent.joinall(threads)#阻塞直至gevent.spawn中所有执行完毕

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()

'''
上面程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。 
初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 函数，
后者阻塞当前流程，并执行所有给定的greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。　　
'''