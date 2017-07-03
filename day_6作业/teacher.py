#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/20'
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
class Teacher(object):
    '''
    老师，讲师可管理自己的班级，上课时选择班级，查看班级学生列表，修改所管理的学员成绩
    '''
    def __init__(self,name,class_name= None):
        self.name = name
        self.class_name = class_name

    #加入新老师
    def new_teacher(self):
        pass
    #查看班级学生列表
    def check_students(self):
        pass


    #录入学生成绩
    def input_score(self):
        pass

    #修改学生成绩
    def revise_score(self):
        pass
