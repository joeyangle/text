#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/5/19'
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
#ftp客户端，支持文件上传下载

import socket
import sys
import json
import hashlib
import os


class MyClient(object):
    '''
    客户端类，文件的上传下载，进度条
    '''

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sk_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def help(self):
        help_str = '''
        download        >>
        upload          >>
        authentiate     >>
        
        '''
        print(help_str)
        pass

    def handle(self):
        '''
        负责socket的主要函数，通过 指令 + 参数 来控制socket运行
        :return: 
        '''

        try:
            self.sk_client.connect((self.host,self.port))#接受由tuple组成的地址
            print('success connect to server')
        except Exception as erro:
            print(erro)
            return
        while True:
            cmd = input('>>').strip()
            if cmd == 'exit':
                break
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]#通过人工输入命令来运行ftp
            if hasattr(self,"cmd_%s" % cmd_str):#反射：判断这个类中是否有输入的命令
                func = getattr(self,"cmd_%s" % cmd_str)#如果有则运行
                func(cmd)
            else:
                print('错误的命令，以下为帮助文件：')
                self.help()#假如没有该命令就打印帮助列表
        pass

    def cmd_authentiate(self):
        '''
        认证account，简单处理account后发送给server端，判断后返回bool
        :return: bool
        '''
        check_name = input('your account name:\n>>')
        check_password = input('your account password:\n>>')
        data = {
            'action': 'authentiate',
            'name': check_name,
            'password': check_password
        }
        self.send_dict(data)
        # 将数据发送出去后接受服务端返回的json,包括log_in,及error组成的字典
        check_account_answer = self.sk_client.recv(1024).decode()
        bool_account = json.loads(check_account_answer)
        # print(bool_account)
        if bool_account['log_in'] == 'True':
            print(bool_account['error'])
            return True
        elif bool_account['log_in'] == 'False':
            print(bool_account['error'])
            return False
        else:
            print('some where wrong!')

    def cmd_download(self, *args):
        print('xiazai')
        pass

    def cmd_upload(self, *args):
        print('upload')
        pass

    def send_dict(self,data):
        '''
        将传给server端的数据转化为json并且发给服务端
        :param data: data
        :return: none
        '''
        send_json = json.dumps(data)
        self.sk_client.sendall(send_json.encode())

    def vew_bar(self,num,total):
        '''
        进度条
        :param num:当前值 
        :param total: 总值
        :return: none
        '''
        rate = num / total
        rate_num = int(rate * 50)
        r = '\r%s%d%%' % ("$" * rate_num, rate_num*2)
        sys.stdout.write(r)
        sys.stdout.flush()

    def parse_reve(self):
        '''
        获取服务器返回值，遵循自创协议对返回值进行解释说明
        创建用户部分
        101 成功设立新账户
        103 账户名已存在
        105 服务器端发生未知错误，无法设立新账户

        账户认证部分
        201 账户验证成功
        203 账户验证错误
        205 服务器发生未知错误，稍后重试

        文件下载部分
        301 成功传输文件
        303 文件下载失败
        305 服务器未知错误

        文件上传部分
        401 成功上传文件
        403 文件上传失败
        405 服务器未知错误
        :return: 
        '''
        myftp_reve = {
            '001': '成功建立连接',
            '101': '成功设立新账户',
            '103': '账户名已存在',
            '105': '服务器未知错误，无法设立新账户',
            '201': '账户验证成功',
            '203': '账户验证错误',
            '205': '服务器发生未知错误，稍后重试',
            '301': '成功传输文件',
            '302': '服务器端正在准备发送文件',
            '303': '文件下载失败',
            '305': '服务器未知错误',
            '401': '成功上传文件',
            '402': '服务器端正在准备接收文件',
            '403': '文件上传失败',
            '405': '服务器未知错误',
        }
        # 各种接受异常没有处理
        serve_reve = self.sk_client.recv(1024).decode('utf-8')
        #print(serve_reve)  # 测试用
        if serve_reve in myftp_reve:
            print(serve_reve, myftp_reve[serve_reve])

if __name__ == '__main__':
    host, port = 'localhost', 10000
    client = MyClient(host,port)
    client.handle()
