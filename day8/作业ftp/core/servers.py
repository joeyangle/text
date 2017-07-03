#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/28'
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
class Servers(object):
    '''
    该类以实现server端各功能，通过反射方法调用该类中的函数
    '''
    def __init__(self,order):
        self.order = order

    def servers_main(self):
        '''
        通过反射调用该类中函数
        :return: 
        '''
        if hasattr(self, "cmd_%s" % self.order):  # 反射：判断这个类中是否有输入的命令
            func = getattr(self, "cmd_%s" % self.order)  # 如果有则运行
            func(self.order)
        else:
            return '3'#指令错误
    def help(self):
        introduce = '''
        introduce abount class of Servers
        帮助信息服务器与用户端同步
        此处仅返回一个指令给客户端，显示指令错误即可
        ...
        '''
        return introduce