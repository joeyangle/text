#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/7'
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
#执行文件
import os, sys
#os.path.dirname()返回上一级目录
#os.path.abspath()相对路径返回为绝对路径
#__file__当前相对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#返回到该程序的总目录
sys.path.append(BASE_DIR)#添加到环境变量
from core import main
main.atm_shop()
