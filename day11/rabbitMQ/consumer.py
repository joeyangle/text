#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/20'
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
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
    )  #建立连接
channel = connection.channel()  #建立管道

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
# 确认queue被声明，但是现在未知是生产者先运行还是消费者先运行
channel.queue_declare(queue='hello')  #声明从哪个队列中收取信息，相当于新建一个queue


def callback(ch, method, properties, body):
    '''
    处理消息的函数
    :param ch: 管道的内存对象
    :param method: = =一般不用  
    :param properties: 以后再讲
    :param body: 
    :return: 
    '''
    print(" [x] Received %r" % body)
    time.sleep(30)

channel.basic_consume(callback,  #消费消息#如果收到消息就调用callback函数来处理消息
                      queue='hello',  #声明从哪个队列收取消息
                      no_ack=False)  #先不用管？ 不管消息是否处理完都不给服务器端确认
#假如no_ack设置为False就会将未处理完的消息给下一个consumer，Ture则默认consumer返回的消息服务器端不care
#不会转给其它consumer，服务器端亦不会有任何反应

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()