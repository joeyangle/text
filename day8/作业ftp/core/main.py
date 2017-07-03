#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/27'
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
ftp的主函数
用户接入，
控制用户端及服务端完成相应指令
'''
'''
大致框架
ftp类
用户端类建立
服务端建立
1.用户 登录
2.用户输入命令
3.显示该用户文件，它的下层再创建一个文件目录
通过控制文件访问来实现权限控制
问题？
在哪里
'''

import sys
import os
import json
import socketserver
addr =os.path.dirname(os.path.abspath(__file__))
sys.path.append(addr)#配置环境
root_address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import server
from client import FtpClient

class User(object):
    '''
    建立ftp类
    ftp账号登录，用户空间分配
    '''

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def check_account(self):
        '''
        数据以pickle储存在本地文件中，账户数据格式为
        {
        'name':'',
        'password':''
        ...待添加
        }
        check account is ture 
        :return: turn or false
        '''
        #先把数据拿出来
        address = '/data/%s/account.json' % self.name
        address = root_address + address
        try:
            with open(address,'r',encoding='utf-8') as f:
                account_data = json.load(f)
            if account_data['name'] == self.name and account_data['password'] == self.password:
                print('right account!')
                return True
        except:
            print('wrong account name!')
            return False

    @staticmethod
    def set_new_account():
        '''
        set new account，the size as:
        see check_account
        :return: None
        '''
        while True:
            name = input('your name:\n>>')
            password = input('your password:\n>>')
            again_password = input('again your password:\n>>')
            if not len(name) or not len(password):
                print('no name input! again!')
                continue
            elif password != again_password:
                print('the first password is not same as the second!again!')
                continue
            else:
                account_address = '/data/%s/account.json' % name
                account_address = root_address + account_address#环境配置找不到相应的数据，此处直接设立根目录来完成地址定位
                dic_address = '/data/%s' % name
                dic_address = root_address + dic_address
                file_address = dic_address + '/file'
                os.mkdir(dic_address)
                os.mkdir(file_address)#ftp的目录文件
                #打开文件，并将这些数据写入
                data ={
                        'name': name,
                        'password': password
                    }
                #try:
                with open(account_address,'w',encoding='utf-8') as f:
                    json.dump(data,f)
                print('na complete')
                return
                #except:
                   # print('error')

def main():

    #通过client类验证账号密码
    #可以通过调用其它api实现登录
    log_in = False

    while not log_in:#验证登录版块
        print('Welcome'.center(50, '-'))
        print('q is out')
        #读取账户数据
        log_set_choose = input('1.login\n2.set new account\n>>')
        if log_set_choose == 'q':
            break
        elif log_set_choose == '1':#登录接口
            while True:
                check_name = input('your account name:\n>>')
                check_password = input('your account password:\n>>')
                ftp = User(check_name, check_password)
                if not len(check_name) or not len(check_password):
                    print('maybe somewhere is None!')
                    continue
                elif ftp.check_account():#调用ftpserve类验证
                    log_in = True
                    break
                else:
                    choose_out = input('q is out!\n others go on!')
                    if choose_out == 'q':
                        break
                    else:
                        continue
                #没有设立break接口

        elif log_set_choose == '2':#设立新账号接口
            User.set_new_account()
            #此处设立自动登录
            log_in = True
        else:
            print('please choose 1 or 2 \n q is out')

    #登陆后开始ftp的操作
    '''
    ftp主要功能
    '''
    while log_in:
        print('kaishi ftp')
        client = FtpClient()
        client.interactive()
        print('jieshuluo')
        break



def start():
    if __name__ != '__main__':
        main()
#start()  # 程序开始运行

