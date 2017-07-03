#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/21'
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
from os import mkdir
import pickle
class School(object):

    def __init__(self,city,class_name=None,stu_name = None):
        self.city = city
        self.class_name = class_name
        self.stu_name = stu_name

    #开设新课程,每一门课程专设一个pickle文件，管理员权限
    def new_class(self):
        '''
        开设新的课程，课程相关存储格式
        {'name':'',
        'cost':'',
        'time':'',
        'memember':[],
        'teacher':''
        }
        :return: 
        '''
        name = input('new_class:')
        cost = input('cost:')
        time = input('time:')
        teacher = input('teacher:')
        one_class = {'name':name,
         'cost':cost,
         'time': time,
         'memember': [],
         'teacher': teacher
         }
        add_class = 'class_info/%s/%s.pk' % (self.city,name)
        with open(add_class,'wb') as f:
            pickle.dump(one_class,f)

    #显示现在已经开设的课程，一个总文件，包括所有开设的课程
    def tell_class(self):
        add_class = 'class_info/%s' % self.city
        pass

    #创建一个新学校,管理员权限,调用os模块
    def new_school(self):
        new_school = ''
        mkdir('class_info/%s'%new_school)
        pass



class Grade(object):
    def __init__(self,name,st_name,tea_name,cost,city):
        self.name = name#课程名
        self.st_name = st_name#学生名
        self.tea_name = tea_name#老师名
        self.cost = cost#课程费用
        self.city = city

    @staticmethod #静态方法，与类没有什么关系了
    def tell_all():#把所有课程都罗列出来
        '''
        打印出所有课程及相关信息
        所有课程pickle格式为：
        aaa = {
        '江西': [['python', '费用:123','讲师：jiang'], ['linux', '费用：234', '讲师：Joey']],
        '深圳': [['python', '费用：113','讲师：ji'], ['go', '费用：212', '讲师：Joe']]
        }
        :return: 
        '''
        all_class_address = 'class_info/all_class.pk'
        with open(all_class_address,'rb') as f:
            all_class = pickle.load(f)
            for city in all_class:
                print(city)
                for cla in all_class[city]:
                    print(cla)

    def tell(self):#介绍一门课程
        print('''
        ============info of %s=============
        本次%s课程由精英讲师%s主讲
        开设于%s
        。。。
        。。。一大堆介绍什么的
        ===================================
        '''%(self.name,self.name,self.tea_name,self.city))

    @staticmethod
    def add_to_class(stu_name):#将学生加入到课程成员名单中
        all_class_address = 'class_info/all_class.pk'
        with open(all_class_address, 'rb+') as f:
            all_class = pickle.load(f)
            all_class['memember'].add(stu_name)

#Grade.tell_all()
#b = School('shanghai')
#b.new_class()
#bb = Grade('python','jiang','joey','123','jiangxi')
Grade.add_to_class('jiangjoey')
