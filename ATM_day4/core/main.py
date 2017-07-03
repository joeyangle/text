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
from core import controller, user
import time
from logs import logs_do

#账户所有的信息以字典形式存储
account_list ={
    'account' : '',
    'password' : '',
    'bakance' : '',
    'debt' : '',
    'date' : ''
}
#货物列表的字典存储格式
goods_list = {
    'good' : '',
    'price' : '',
    'num' : '',
}
#日志格式，只有用户登录成功日志才会被保存
log_list = {
    'account': '',
    'start_time' : '',
    'do_what' : {},
    'end_time' : ''
}
T_or_F = False #初始定义状态---未登录
def atm_shop():
    time_start = time.time()
    log_list['start_time'] = time_start
    while True:
        f_ch_input = input('1.I am user;\n2.I am controller\nq is out\n--->')
        f_choose = {
            '1' : user.user_do ,
            '2' : controller.controller_do
        }
        if f_ch_input == 'q':
            break
        elif f_ch_input in f_choose:
            f_choose[f_ch_input]()
        else:
            print('wrong input!\ntry again1')
    time_end = time.time()
    log_list['end_time'] = time_end
    time_spend = time_end - time_start
    #此处调用日志函数，将日志写入保存
    if logs_do.write_logs():
        print('记录已保存')
    print('thanks for your coming!\ntime spend:%s'%time_spend)

def start():
    if __name__ == '__main__':
        atm_shop()
start()
