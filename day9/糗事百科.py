#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/5'
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
需求：
1.多线程
2.设立图片url池，抓取图片
3.实现刷新翻页
4.文字一同爬取，将结果以HTML格式表示，有图片与文字
'''
import requests
import re

#图片url管理池
class Photourl(object):
    '''
    图片url管理
    '''
    new_urls = set()
    old_urls = set()

    def __init__(self,url):
        self.url = url

    def is_new(self):
        if self.url in self.old_urls:
            return False
        else:
            self.new_urls.add(self.url)

    def get_url(self):
        if len(self.new_urls) > 0:
            new_url = self.new_urls.pop()
            return new_url
        else:
            return False

