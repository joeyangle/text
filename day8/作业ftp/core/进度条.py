#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/1'
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
import os,sys,string
import time

# def view_bar(num=1, sum=100, bar_word=":"):
#     rate = float(num) / float(sum)
#     rate_num = int(rate * 100)
#     print('\r%d%% :'%(rate_num)),
#     for i in range(0, num):
#         os.write(1, bar_word.encode())
#     sys.stdout.flush()

def view_bar(num, total):
     # rate = float(num) / float(total)
     rate = num / total
     rate_num = int(rate * 100)
     r = '\r%s%d%%' % ("+" * rate_num, rate_num)
     sys.stdout.write(r)
     sys.stdout.flush()

if __name__ == '__main__':
    for i in range(0, 100):
        time.sleep(0.5)
        view_bar(i, 100)