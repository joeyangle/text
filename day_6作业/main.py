#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/16'
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
角色：学校，学员，课程，讲师
要求：
1.创建北京，上海两所学校
2.创建Linux，Python，go3个课程，Linux\py在北京开，go在上海开
3.课程包含，周期，价格，通过学校创建课程（创建class类）
4.通过学校创建班级，班级关联课程、讲师（继承学校）
5.创建学员时，选择学校，关联班级
6.创建讲师的角色时要关联学校
7.提供两个角色接口
7.1学员视图，可以注册，交学费，选择班级
7.2讲师视图，讲师可管理自己的班级，上课时选择班级，查看班级学生列表，修改所管理的学院成绩
7.3管理视图，创建讲师，创建班级，创建课程
8.上面的操作产生的数据都通过pickle序列化保存到文件里
混乱了，感觉类没有分清楚
'''
# import pickle
# import json
# linwei = {'a':1,'b':'2'}
# print(pickle.dumps(linwei))
# with open('fei.json','w') as ff:
#     json.dump(linwei,ff)
#
# fei = open('fei.json','r')
# print(json.load(fei))
#
# with open('feiyong.pk','wb') as f:
#     pickle.dump(linwei,f)
#
# fei = open('feiyong.pk','rb')
# print(pickle.load(fei))

import student
#学生
def students_start():
    '''
    学生部分的主函数，包括注册，登录，缴纳学费，选择班级等
    :return: 
    '''
    Student_log = False  # 全局变量，用户是否通过登录验证
    #登录或者注册
    while not Student_log:#已经登录则略过该模块
        print('=' * 50)
        log_rgs = input('1.登录\n2.注册\n ---other key is out---')

        if log_rgs == '1':#登录
            while True:
                print('=' * 50)
                account_name = input('your account name:\n-->')
                if len(account_name) == 0:
                    print('none name! again!')
                    continue
                check_student = student.Student(account_name)
                while check_student.check_accout():
                    Student_log = True
                    print('welcome! have a nice day!')
                    break
                break

        elif log_rgs == '2':#注册
            while True:
                print('=' * 50)
                account_name = input('q is out\nyour account name:\n-->')
                if account_name == 'q':
                    break
                if len(account_name) == 0:
                    print('none name! again!')
                    continue
                new_student = student.Student(account_name)#注册账户过程，注册后直接登录
                #new_student.register()
                while new_student.register():#注册
                    Student_log = True#改变全局变量
                    #print('123',Student_log)
                    break
                print('=' * 50)
                break
        else:
            break

    while Student_log:#已经登录,先判断是否交学费，再选择班级，查看自身情况，分数，改密码什么的
        #是否已交学费加入到个人信息中
        ch_money_class = input('1.缴费\n2.选择班级')
        if ch_money_class == '1':
            #缴费函数，显示所有课程及费用等相关信息，选择课程后显示费用然后缴费
            pass
        break


#主函数
def main_start():
    while True:
        print('welcome to oldboy!')
        print('please choose who you are:')
        main_ch = input('1.student\n2.teacher\n3.administrators\nq is out\n-->')
        if main_ch == '1':#学生
            students_start()
        elif main_ch == '2':#老师
            pass
        elif main_ch == '3':#管理员
            pass
        elif main_ch == 'q':#退出
            print('thanks for your coming!\nsee you again!')
            break
        else:
            print('please input right choose!')
            continue

if __name__ == '__main__':
    main_start()


