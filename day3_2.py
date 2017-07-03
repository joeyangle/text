#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/3'
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
global       
        log 127.0.0.1 local2
        daemon
        maxconn 256
        log 127.0.0.1 local2 info
defaults
        log global
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        option  dontlognull

listen stats :8888
        stats enable
        stats uri       /admin
        stats auth      admin:1234

frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.oldboy.org
        use_backend www.oldboy.org if www

backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000

原配置文件
'''
'''
1、查
    输入：www.oldboy.org
    获取当前backend下的所有记录

2、新建
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

3、删除
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

需求
'''
# a = 'abandon'忘记了，可以这样直接判断，做一个小实验
# b = 'o'
# if b in a:
#     print('dui')
'''
目标：修改haproxy文件
需求如上所示
新建和删除模板已经建好
路径
首先只读打开文件，逐行读出
此处print目录‘1.查询2.新建；3.删除；’
1.查询：用户输入目标（判断输入是否符合规范）
遍历文件找到目标
获取该纪录‘server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000’可能多行，全部导出，此处加判断
2.新建：追加模式打开，用户按照‘'bakend'；'server'；'weight'；'maxconn'；’输入，以以上模板形式组合
3.删除：write模式打开
'''


#建立一个函数打开文件，两参数，1.地址；2.读写方式;返回为文件内存位置
#我靠 这函数不行，返回内存位置，文件最后还是要关闭，位置就不存在了
#这样就不能采用一行行在内存遍历的方式了
#真的是一点用都没有，只能返回个值，不能追加，不能写，毛用没有
def openfile(address ,style = 'r'):
    f = open(address,style,encoding='utf-8')
    f1 = f.readlines()
    f.close()
    return f1
def write_add(set1,address):
    f = open(address,'a',encoding='utf-8')
    f.write('\nbakend %s\n'%set1['bakend'])
    f.write(' '*(len('bakend')+1))
    f.write('server %s '%set1['record']['server'])
    f.write('weight %s ' % set1['record']['weight'])
    f.write('maxconn %s ' % set1['record']['maxconn'])

while True:
    f_address = 'haproxy'
    address_list = ['www.oldboy.org', 'smgui']
    print('all address:\n%s'%address_list)
    ha_data = openfile(f_address)
    print('welcome!')
    choose_1 = input('choose option:\n1.查询\n2.新建\n3.删除\nq leave\nyour option:')
    choose_1_option = ['1','2','3','q']
    if choose_1 not in choose_1_option:
        print('wrong opition! please try again!')
        continue
    if choose_1 == 'q': #退出
        break
        # 1、查
        # 输入：www.oldboy.org
        # 获取当前backend下的所有记录
        # .strip()方法去除字符的前后空格
    while choose_1 == '1': #查询
        inquire_add = input('the address you want to inquire?\nthe same input q to leave\n--->')
        if len(inquire_add) == 0:#再次重申input方法判断为None不适合用于此处判断？？？为什么？？？
            continue
        if inquire_add == 'q':
            break
        f_or_t = 0
        if inquire_add in address_list:#此处定义避免错误输入导致奇怪情况发生，应设定一个模板，避免错误输入
            for line in ha_data:
                line.split()
                if f_or_t == 1:
                    print(line.strip())
                    if line[0] != ' ':
                        f_or_t == 0
                if inquire_add in line and "backend" in line:
                    f_or_t = 1
                    print(inquire_add)
        else:
            print('please input right address!')
    # 2、新建
    # 输入：
    # arg = {
    #     'bakend': 'www.oldboy.org',
    #     'record': {
    #         'server': '100.1.7.9',
    #         'weight': 20,
    #         'maxconn': 30
    #     }
    # }
    if choose_1 == '2': #新建
        while True:
            arg ={}
            print('now, please input one by one!')
            address = input('the address:')
            serve = input('the serve:')
            weight = input('the weight:')
            maxconn = input('the maxconn:')
            address_list.append(address)
            arg = {
                'bakend': address,
                'record': {
                    'server': serve,
                    'weight': weight,
                    'maxconn': maxconn
                }
            }#定义一个追加的函数把这个格式化写入
            write_add(arg,f_address)
            panduan = input("go on? y/n\n")
            if panduan == 'n':
                break
    if choose_1 == '3': #删除
        while True:
            write_list = []
            cut_add = input('the address you delete\nq is leave\n--->')
            if cut_add == 'q':
                break
            if cut_add in address_list:
                f_or_t = 0
                print('-' * 15, 'you delete', '-' * 15)
                for line in ha_data:
                    line = line.rstrip()
                    if f_or_t == 1:
                        print(line.strip())
                        if line.startswith('   ') != ' ':
                            f_or_t == 0
                        continue
                    if cut_add in line and "backend" in line:
                        f_or_t = 1
                        print(line)
                        continue
                    write_list.append(line)
                while True:
                    choose_2 = input('sure to delete?y/n\nq leave\n--->')
                    if choose_2 == 'q':
                        break
                    if choose_2 == 'y':
                        address_list.remove(cut_add)
                        f = open(f_address,'w',encoding='utf-8')
                        for line in write_list:
                            f.write(line+'\n')
                        f.close()
                    if choose_2 == 'n':
                        continue
                    else:
                        print('wrong import!again!')