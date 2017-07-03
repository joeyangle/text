#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/8'
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
哈希算法用于对传输数据的加密及保证传输对象的完整性
'''
import hashlib

a = "a test string".encode()
print(hashlib.md5(a).hexdigest())
aa =hashlib.md5("a test string".encode())
aa.update('add bs name'.encode())
print(aa.hexdigest())
print(hashlib.sha1(a).hexdigest())
print(hashlib.sha224(a).hexdigest())
print(hashlib.sha256(a).hexdigest())
print(hashlib.sha384(a).hexdigest())
print(hashlib.sha512(a).hexdigest())


