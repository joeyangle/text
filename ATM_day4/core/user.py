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
import time
#写了假代码，思路不够清晰，现在推到重做
# def user_shop():
#     shopper_T_F = False
#     address = 'user_accounts'
#     f = open(address, 'r+', encoding='utf-8')
#     @check_account
#     def account_putin():  # 输入账号密码
#         name = input('your account:')
#         password = input('your password:')
#         if name or password is None:
#             print('your account or password is None!\nplease try again')
#         return name, password
#         if shopper_T_F == False:
#             print('wrong account! try again!')
#         return
#
# def user_atm():
#     pass
#
# def check_account(func):#装饰器，判断account是否准确
#     def check():
#         user_input = func()
#         global shopper_T_F
#         for line in f:
#             line = line.split()
#             if line[0] == user_input[0] and line[1] == user_input[1]:
#                 shopper_T_F = True
#     return  check
#
#
# def user_log(func):#装饰器，保存登录信息到用户日志
#     def user_log_():
#         func()
#         if shopper_T_F == True:
#             pass
#
# def account_putin():#输入账号密码
#     name = input('your account:')
#     password = input('your password:')
#     if name is None or password is None:
#         print('your account or password is None!\nplease try again')
#         return None
#     return name,password
#
# def user_do():
#     while True:
#         f_u_input = input('please choose!\n1.SHOP\n2.ATM_day4\n--->')
#         f_u_choose = {
#             '1': user_shop,
#             '2': user_atm
#         }
#         if f_u_input == 'q':
#             break
#         elif f_u_input in f_u_choose:
#             f_u_choose[f_u_input]()
#         else:
#             print('wrong input!\ntry again1')
'''
在这一部分，首先实现登录验证,
登录函数，希望可以和controller耦合
'''

def check_acc_bendi(function):
    '''
    装饰器，用来验证输入的账号密码是否准确，若准确则将全局变量T_or_F修改为Ture
    :param function: 用来装饰的函数
    :return: 无
    '''
    def check_account():
        log_in()
        try:
            u_acc_address = '/logs/user_accounts/%s'%account[0]
            f = open(u_acc_address,'r',encoding='utf-8')
            pass#不写了，没营养这个地方
        except:
            pass

def log_in():
    '''
    该函数实现用户的账号密码输入,当style为本地时
    :return: 账号 密码
    '''
    name = input('your account:')
    password = input('your password:')
    if len(name)== 0 or len(password)== 0:
        print('your account or password is None!\nplease try again')
    else:
        account.append(name)
        account.append(password)


def user_do():
    '''
    该函数调用其它函数完成用户操作的功能
    :return: 
    '''
    wrong_count = 3
    while T_or_F is not True and wrong_count >=0:
        account = []
        style = input('which style you want?\n1.本地 2.QQ ...')
        if style == '本地'
            log_in()
        #...此处可加各种登录方式
        else:
            print('please choose right!')
    while T_or_F is True:
        #开始选择各种功能
        pass