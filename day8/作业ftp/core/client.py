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
import socket
import os
import json
import hashlib
import sys

class FtpClient(object):
    '''
    该类为ftp用户端，实现用户端的各种功能，主要功能如下：
    1.判断本地文件是否存在
    2.将获取文件置入到目的文件中
    3.与服务端连接
    4.实现人工命令输入并完成相应命令    
    '''
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        introduce = '''
        introduce 
        各种指令的帮助信息
        lookfiles
        查看ftp中所有的文件
        get file_name
        从ftp下载指定的文件，file_name为文件名
        put file_address
        将本地文件上传到ftp,file_address 为文件的本地地址
        '''
        print(introduce)
        #将这个类解释，说明

    def connect(self,ip,port):#连接
        '''
        荒废了
        :param ip: 
        :param port: 
        :return: 
        '''
        self.client.connect((ip,port))

    def send_dict(self,data):
        '''
        将传给server端的数据转化为json并且发给服务端
        :param data: data
        :return: none
        '''
        send_json = json.dumps(data)
        self.client.sendall(send_json.encode())

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

    def reve_all(self,data_size):
        '''
        收集分多次来自客户端的数据，然后组成完整的数据
        用于文件的接收
        :return: 完整的字节码格式数据
        '''
        data_size = int(data_size)
        reve_data = 0
        all_data = b''
        while reve_data < data_size:
            data = self.client.recv(1024)
            reve_data += len(data)
            all_data += data #可能会陷入死循环
        return all_data

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
            '001' : '成功建立连接',
            '101' : '成功设立新账户',
            '103' : '账户名已存在',
            '105' : '服务器未知错误，无法设立新账户',
            '201' : '账户验证成功',
            '203' : '账户验证错误',
            '205' : '服务器发生未知错误，稍后重试',
            '301' : '成功传输文件',
            '302' : '服务器端正在准备发送文件',
            '303' : '文件下载失败',
            '305' : '服务器未知错误',
            '401' : '成功上传文件',
            '402' : '服务器端正在准备接收文件',
            '403' : '文件上传失败',
            '405' : '服务器未知错误',
        }
        #各种接受异常没有处理
        serve_reve = self.client.recv(1024).decode('utf-8')
        print(serve_reve)#测试用
        if serve_reve in myftp_reve:
            print(myftp_reve[serve_reve])

    def authentiate(self):
        '''
        认证account，简单处理account后发送给server端，判断后返回bool
        :return: bool
        '''
        check_name = input('your account name:\n>>')
        check_password = input('your account password:\n>>')
        data = {
            'action' : 'authentiate',
            'name' : check_name,
            'password' : check_password
        }
        self.send_dict(data)
        #将数据发送出去后接受服务端返回的json,包括log_in,及error组成的字典
        check_account_answer = self.client.recv(1024).decode()
        bool_account = json.loads(check_account_answer)
        #print(bool_account)
        if bool_account['log_in'] == 'True':
            print(bool_account['error'])
            return True
        elif bool_account['log_in'] == 'False':
            print(bool_account['error'])
            return False
        else:
            print('some where wrong!')

    def set_new_account(self):
        '''
        set new account，the size as:
        see check_account
        :return: None
        '''
        while True:
            name = input('exit is break\nyour name:\n>>')
            if name == 'exit':
                break
            password = input('your password:\n>>')
            again_password = input('again your password:\n>>')
            if not len(name) or not len(password):
                print('no name input! again!')
                continue
            elif password != again_password:
                print('the first password is not same as the second!again!')
                continue
            else:#set new account
                data = {
                    'action' : 'set_new_account',
                    'name' : name,
                    'password' : password
                }
                self.send_dict(data)
                new_account_answer = self.client.recv(1024).decode('utf-8')
                bool_new_account = json.loads(new_account_answer)
                #print(bool_new_account)
                #print(bool_new_account['if_set'])
                if bool_new_account['if_set'] == '101':#101成功建立新账户
                    print('hello %s\n'%name,bool_new_account['error'])
                    return True
                elif bool_new_account['if_set'] == '103':#103账户名已存在
                    print(bool_new_account['error'])
                    continue
                elif bool_new_account['if_set'] == '105':#105服务器问题，账户创建失败
                    print(bool_new_account['error'])
                    return False
                else:
                    print('...什么地方错了')
                    return False

    def interactive(self):
        '''
        实现命令的输入并且执行输入命令
        :return: 
        '''
        while True:#反复输入命令
            cmd = input(">:").strip()
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

    #必要的操作，使数据传递标准化
    #写一套标准请求码
    def cmd_lookfiles(self,*args):
        '''
        查看当前文件夹所有文件
        :return: 
        '''
        print('lookfiles......')
        data = {
            'action' : 'lookfiles'
        }
        self.send_dict(data)
        file_list_reve = self.client.recv(1024).decode('utf-8')
        data = json.loads(file_list_reve)
        #print(data)
        if data['is_get'] == '501':
            print(data['error'])
            print(data['list_file'])
        elif data['is_get'] == '503':
            print('未知错误未获取文件目录')
            print(data['error'])
        pass

    def cmd_up_level(self,data):
        '''
        第一个参数up or down 第二个参数 前往的文件名，仅在down时有用
        :param data: 
        :return: 
        '''
        data = {
            'action' : 'file_level',
            'level' : 'up',
            'file_name' : ''
        }
        self.send_dict(data)
        level_reve = self.client.recv(1024).decode('utf-8')
        level_sure = json.loads(level_reve)
        if level_sure['is_up_down'] == '605':
            print(level_sure['error'])
        self.cmd_lookfiles()
        pass

    def cmd_down_level(self,data):

        file_name = data.split()[1]
        data = {
            'action': 'file_level',
            'level': 'down',
            'file_name': file_name
        }
        self.send_dict(data)
        level_reve = self.client.recv(1024).decode('utf-8')
        level_sure = json.loads(level_reve)
        if level_sure['is_up_down'] == '603':
            print(level_sure['error'])
        elif level_sure['is_up_down'] == '605':
            print(level_sure['error'])
        self.cmd_lookfiles()
        pass

    def cmd_put(self,*args):
        '''
        该函数执行将数据读取并且发送到服务端       
        :return: 
        '''
        self.cmd_lookfiles()
        while True:
            print('-' * 50)
            file_name_address = input('q is out\nthe file you want to put in ftp:\n>>').strip()
            if file_name_address == 'q':
                break
            elif len(file_name_address) == 0:continue
            elif os.path.isfile(file_name_address):
                #文件存在的话开始上传文件
                file_size = os.stat(file_name_address).st_size
                #print(type(file_size))
                file_name = os.path.basename(file_name_address)
                put_data = {
                    'action' : 'put',
                    'file_name' : file_name,
                    'file_size' : file_size
                }
                self.send_dict(put_data)#将数据发送给服务端
                reve2 = self.client.recv(1024).decode()
                if reve2 == 'rname':
                    pass
                elif reve2 == 'ok':#错误就会有返回值
                    #开始发送文件
                    put_size = 0
                    hash_put = hashlib.md5()
                    #while not put_size > file_size:
                    try:
                        # 这里要做一个进度条,怎么做？
                        print('打开文件了')
                        with open(file_name_address,'rb') as file:
                            print('_'*50)
                            for line in file:
                                hash_put.update(line)
                                #print('开始上传文件...1')
                                #传得很慢，怀疑是不是逐行读取的原因
                                self.client.sendall(line)
                                put_size += len(line)
                                self.vew_bar(put_size,int(file_size))
                                # if put_size > int(file_size)/20 :#进度条
                                #     print('$$')
                                #     #print(put_size,int(file_size)/20)
                                #     put_size = put_size - int(file_size)/20
                            #print(end='\n')
                            is_done = self.client.recv(1024).decode()
                            if is_done == 'done':
                                self.client.sendall(str(hash_put.hexdigest()).encode())#将文件哈希值发送出去
                            else:
                                print('这个错误应该不可能发生')
                    except Exception as aa:
                        print('文件传输出错',aa)
                reve3 = self.client.recv(1024).decode()#解析发回的结果
                put_answer = json.loads(reve3)
                if put_answer['is_put_file'] == '407':
                    print(put_answer['error'])
                if put_answer['is_put_file'] == '401':
                    print(put_answer['error'])
                if put_answer['is_put_file'] == '403':
                    print(put_answer['error'])
                if put_answer['is_put_file'] == '405':
                    print(put_answer['error'])
            else:
                print('no such file,please make sure then try again!')
                continue

    def cmd_get(self,*args):
        '''
        获取文件从ftp
        :return: 
        '''
        print('now get...')
        self.cmd_lookfiles()#先把所有文件列出来
        while True:
            print('-' * 50)
            file_name = input('q is out\nthe file you want to load in ftp:\n>>').strip()
            if file_name == 'q':
                break
            data = {
                'action' : 'get',
                'file_name' : file_name
            }
            self.send_dict(data)
            #服务端返回是否存在及若存在则返回文件大小
            is_file = self.client.recv(1024).decode('utf-8')
            is_file = json.loads(is_file)
            if is_file['file_exist'] == 'true':
                file_size = is_file['file_size']
                choose = input('sure load? input yes is sure\n>>').strip()
                if choose == 'yes':
                    self.client.send('true'.encode())#返回确认下载
                    save_address = input('the address:') + '\%s'%file_name#输入保存地址，此处未判断地址是否存在
                    #self.reve_all(is_file)#下载文件，可以文件保存地址
                    get_size = 0
                    file = open(save_address, 'wb')
                    hash_getfile = hashlib.md5()
                    #print(file_size)
                    while get_size < file_size:
                        reve_data = self.client.recv(1024)
                        hash_getfile.update(reve_data)
                        file.write(reve_data)
                        get_size += len(reve_data)
                        # print(get_size)
                        print('_'*50)
                        self.vew_bar(get_size,file_size)
                    file.close()
                    self.client.send('done'.encode())
                    hash_file = self.client.recv(1024).decode()
                    if hash_getfile.hexdigest() == hash_file:
                        print('成功下载文件')
                    else:
                        print('文件漏传')
                else:
                    print('out! now, choose again')
                    continue
            elif is_file['file_exist'] == 'false':
                print('不存在该文件，请确认后重新输入')
                continue
            self.client.send('file_get_answer'.encode())
            get_answer = self.client.recv(1024)#其实这一步没有必要


def start(HOST, PORT):
    log_in = False
    user_client = FtpClient()  # 建立实例
    try:
        user_client.connect(HOST, PORT)  # 建立连接
    except:
        print('wrong')
        return
    while True:
        print('Welcome'.center(50, '-'))
        choose = input('q is out\n1.login\n2.set new account\n>>')
        if choose == 'q':
            break
        elif choose == '1':
            if user_client.authentiate():#账户验证
                log_in = True
        elif choose == '2':#设立新账户
            if user_client.set_new_account():
                log_in = True
        else:
            print('input right choose!again')
            continue

        while log_in:
            user_client.interactive()
            break

if __name__ == '__main__':
    HOST, PORT = "localhost", 6969
    start(HOST, PORT)


