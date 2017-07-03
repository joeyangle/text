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
客户端与服务端一一对应
isfile 判断的是否是文件，而不是directory
'''
import os
import sys
import socketserver
import json
import re
import hashlib
import time

addr =os.path.dirname(os.path.abspath(__file__))
sys.path.append(addr)#配置环境
root_address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Myhandler(socketserver.BaseRequestHandler):
    '''
    这个类继承BaseRequestHandler框架，其中有setup，handle，finish三个函数，
    分别对应开始，处理，结束，此处仅对handle进行重构
    '''
    log_in = False
    account_name = ''
    all_address = ''
    present_address = ''

    def handle(self):
        while True:#循环接收命令
            try:
                self.data = self.request.recv(1024).decode('utf-8')
                if len(self.data) == 0:
                    break
                print("{} wrote:".format(self.client_address[0]))
                #print(self.data)
                #新建一个类包含各种指令，通过反射来调用这些功能
                cmd_dic = json.loads(self.data)
                action = cmd_dic['action']
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
                # else:#没有这种方法,-----没必要，客户端与服务器端同步，而方法在客户端已经进行了筛选
                #     self.request.send('003\nno such action!')#服务端不存在该中方法
            except ConnectionResetError as e:
                print('err',e)
                break

    @classmethod
    def file_set(self):#初始化地址，
        root_file_address = root_address + '\data\%s\\file' % Myhandler.account_name
        Myhandler.all_address = root_file_address

    @classmethod
    def decrease_file_address(cls,address):
        '''
        将地址的最后一位去掉，即\address
        :param address: 
        :return: 去除后的地址
        '''
        pattern = re.compile(r'\\.*?$',re.S)
        address = re.sub(pattern,'',address)
        return address

    def file_level(self,data):
        '''
        control file address level
        :param data: 
        :return: 
        '''
        root_file_address = root_address + '\data\%s\\file' % Myhandler.account_name
        up_or_down = data['level']
        file_name = data['file_name']
        try:
            if up_or_down == 'up':#返回上一层
                #把最后一层删除
                Myhandler.present_address = self.decrease_file_address(Myhandler.present_address)
                is_up_down = '601'
                error = '成功返回上一层'
            elif up_or_down == 'down':#前往下一层
                present_address = Myhandler.present_address + '\%s'%file_name
                #print(555,present_address)
                all_address = root_file_address + present_address
                #print(all_address)
                if os.path.isdir(all_address):#判断该文件是否存在
                    Myhandler.present_address += '\%s'%file_name
                    is_up_down = '601'
                    error = '成功进入下一层'
                else:
                    is_up_down = '603'
                    error = '不存在该文件，使用lookfiles查看当前文件夹下文件'
            else:
                is_up_down = '605'
                error = '出问题了'
        except Exception as error:
            is_up_down = '603'
        send_data = {
            'is_up_down': is_up_down,
            'error' : error
        }
        Myhandler.all_address = root_file_address + Myhandler.present_address
        #print(Myhandler.all_address)
        self.send_dict(send_data)
        pass

    def put(self,data):
        '''
        client's data put in ftp serve 客户端上传的数据，
        包括文件名，文件大小
        错误 框架很重要，先想清楚一步一步怎么走，思路清晰
        :param data: data from client
        :return: 
        '''
        file_address = Myhandler.all_address
        file_name = data['file_name']
        file_size = data['file_size']
        address =  file_address + '\%s'%file_name
        if Myhandler.log_in:#保证登录
            if os.path.isfile(address):#文件重名
                is_put_file = '407'
                error = '您的文件夹中已经存在该文件'
                self.request.send('rname'.encode())#假如重名则返回值
            else:#接收文件
                self.request.send('ok'.encode())
                try:
                    get_size = 0
                    file = open(address,'wb')
                    hash_getfile = hashlib.md5()
                    #print(file_size)
                    while get_size < file_size:
                        reve_data = self.request.recv(1024)
                        hash_getfile.update(reve_data)
                        file.write(reve_data)
                        get_size += len(reve_data)
                        #print(get_size)
                    file.close()

                    self.request.send('done'.encode())
                    hash_file = self.request.recv(1024).decode()#16进制哈希值
                    if hash_getfile.hexdigest() == hash_file:
                        is_put_file = '401'
                        error = '成功上传文件'
                    else:
                        is_put_file = '403'
                        error = '文件漏传'
                except Exception as error:
                    is_put_file = '405'
            send_data = {
                'is_put_file' : is_put_file,
                'error' : error
            }
            self.send_dict(send_data)
        pass

    def get(self,data):
        '''
        将server端发送给用户端
        :param data: 
        :return: 
        '''
        file_name = data['file_name']
        file_address = Myhandler.all_address + '\%s'%file_name
        if not os.path.isfile(file_address):
            send_data = {
                'file_exist': 'false',
            }
            self.send_dict(send_data)
            file_get = '307'
            error = '不存在该文件'
        else:
            #该文件存在
            file_size = os.stat(file_address).st_size
            send_data = {
                'file_exist' : 'true',
                'file_size' : file_size
            }
            self.send_dict(send_data)
            is_send = self.request.recv(1024).decode()
            if is_send == 'true':
                # 开始发送文件
                hash_get = hashlib.md5()
                try:
                    with open(file_address, 'rb') as file:
                        for line in file:
                            hash_get.update(line)
                            # print('开始上传文件...1')
                            self.request.sendall(line)
                        is_done = self.request.recv(1024).decode()
                        if is_done == 'done':
                            self.request.sendall(str(hash_get.hexdigest()).encode())  # 将文件哈希值发送出去
                            file_get = '301'
                            error = 'success send file %s'%file_name
                        else:
                            print('这个错误应该不可能发生')
                except Exception as error:
                    file_get = '305'#文件发送出错
        data_answer = {
            'file_get' : file_get,
            'error' : error
        }
        self.send_dict(data_answer)
        pass

    def lookfiles(self,data):
        '''
        查看账户的文件目录
        :return: 
        '''
        address =Myhandler.all_address
        try:
            list_file = os.listdir(address)
            is_get = '501'
            error = 'success get file list'
        except Exception as error:
            is_get = '503'
            list_file = ''
        data = {
            'is_get' : is_get,
            'list_file' : list_file,
            'error' : error
        }
        #print(data)
        self.send_dict(data)
        pass

    def authentiate(self,data):
        '''
        check account，the style of data is json
        :return: send bool to client
        data = {
            'action' : 'authentiate',
            'name' : check_name,
            'password' : check_password
        }
        '''
        log_in = 'False'
        check_name = data['name']
        check_password = data['password']
        address = root_address + '\data\%s\\account.json'%check_name
        print(os.path.isfile(address),address)
        if os.path.isfile(address):#设立一个类变量，确认登录
            with open(address,'r',encoding='utf-8') as acc_file:
                acc_data = json.load(acc_file)
            if check_password == acc_data['password']:
                log_in = 'True'
                error = 'right log in'
                Myhandler.log_in = True
                Myhandler.account_name = check_name
            else:
                error = 'wrong password'
        else:
            #返回客户端，无此账号
            error = 'no such account name'
        send_data = {
            'log_in' : log_in,
            'error' : error
        }
        print(send_data)
        self.file_set()
        self.send_dict(send_data)
        pass

    def set_new_account(self,data):
        '''
        set new account, set all account need directory for ftp
        :param data: client sent data
        :return: 
        '''
        #print(data)
        name = data['name']
        password = data['password']
        account_address = '\data\%s\\account.json' % name
        account_address = root_address + account_address  # 环境配置找不到相应的数据，此处直接设立根目录来完成地址定位
        dic_address = '\data\%s' % name
        dic_address = root_address + dic_address
        print(os.path.isfile(account_address),account_address)
        if os.path.isfile(account_address):
            if_set = '103'
            error = 'this name of %s has exist\ntry again!'%name
        else:
            file_address = dic_address + '\\file'
            os.mkdir(dic_address)#j建立账户文件目录
            os.mkdir(file_address)  # ftp的目录文件
            # 打开文件，并将这些数据写入
            account_data = {
                'name': name,
                'password': password
            }
            try:
                with open(account_address, 'w', encoding='utf-8') as f:
                    json.dump(account_data, f)
                if_set = '101'
                error = 'success set new account'
                Myhandler.log_in = True
                Myhandler.account_name = name
            except Exception as wrong:
                if_set = '105'
                error = wrong
        send_data = {
            'if_set' : if_set,
            'error' : error
        }
        print(send_data)
        self.file_set()
        self.send_dict(send_data)
        pass

    def log_record(self):
        pass

    def send_dict(self,data):
        '''
        将传给server端的数据转化为json并且发给客户端
        :param data: data
        :return: none
        '''
        send_json = json.dumps(data)
        self.request.sendall(send_json.encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 6969 #监视该端口号
    # Create the server, binding to localhost on port 9999 监控本地9999端口
    server = socketserver.ThreadingTCPServer((HOST, PORT), Myhandler)#多进程
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print('start waiting...')
    server.serve_forever()#一直监听
