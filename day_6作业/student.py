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
'''
global语句是适用于当前整个代码块的声明。它是全局变量的标识符。
如果某名字在局部名字空间中没有定义, 就自动使用相应的全局名字.
没有global是不可能手动指定一个名字是全局的.在 global 中出现
的名字不能在global 之前的代码中使用.在 global 中出现的名字不
能作为形参, 不能作为循环的控制对象, 不能在类定义, 函数定义,
import语句中出现.
'''
'''
学生的信息储存方式
{真实姓名，账户名，账户密码，班级}
通过姓名去班级分数储存调用分数
'''
import pickle

class Student(object):
    def __init__(self,name,grade=None):
        self.name = name
        self.grade = grade

    def tell(self):
        print('''
        -----info of Student:%s -----
        Name: %s
        Grade: %s
        '''%(self.name,self.name,self.grade))

    def register(self):
        while True:
            address = 'stu_info/%s.pk' % self.name
            real_name = input('your real name:\n-->')
            acc_new_password = input('your account password:\n-->')
            aacc_new_password = input('again account password:\n-->')
            if len(real_name) == 0 or len(acc_new_password) ==0:
                print('somewhere is none!\ntry again!')
                continue
            elif aacc_new_password != acc_new_password:
                print('first password not same as second!')
                continue
            #还可以加是否账号名已被占用
            else:
                data = {
                    'name': real_name,
                    'account_name' : self.name,
                    'account_pass' : acc_new_password
                }
            try:
                with open(address,'wb') as f:
                    pickle._dump(data,f)
                print('well!anway!\nwelcome join oldboy')
                # global Student_log不行，全局变量不能这样用
                # Student_log = True
                # print(Student_log)
                return True
            except:
                print('somewhere wrong!')
                return False

    def check_accout(self):#验证登录账号
        while True:
            check_name = self.name
            check_password = input('account password:\n-->')
            if len(check_password)==0:
                print('password is none! again!')
                continue
            address = 'stu_info/%s.pk' % self.name
            with open(address,'rb') as f_stu_data:
                stu_data = pickle.load(f_stu_data)
            print(stu_data)
            if stu_data['account_name'] == check_name:
                if stu_data['account_pass'] == check_password:
                    return True
                else:
                    print('wrong password! again!\nforget password?\nq is out\nother key go on')#可以设置每日尝试次数
                    go_out = input('-->')#退出接口
                    if go_out == 'q':
                        break
                    else:
                        continue

    def check_money(self):
        address = 'stu_info/%s.pk' % self.name
        with open(address, 'rb') as f_stu_data:
            stu_data = pickle.load(f_stu_data)
        try:
            if stu_data['money'] == True:
                return True
        except:
            print('='*23,'缴费','='*23)
            #调用课程名，课程费用



# jiang = Student('jiang',3)
# jiang.register()