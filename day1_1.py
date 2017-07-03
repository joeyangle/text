#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
大致思路：三级目录
dict对路径经行保存,用if语句对输入值经行判断，提取对应字典
'''
'''quanguo = {
    'zhongguo':['jiangxi','hunan','zhejiang'], 'riben':['1','2']
}
countyr_name = input('please put the country:')
print(countyr_name.)
江西财经 = {
        '蛟桥':['统计','会计'],
        '麦庐':['软件','公共管理']
    }
中国 = {
        '江西':['宜春','南昌'],
        '湖南':['长沙','洞庭湖']
    }
南昌 = {
    '青山湖' : ['江西财经','江西农大'],
    '谣湖' : ['师大','火车站']
}

def cheek_address():
    name = str(input('your address:'))
    if name not in ['江西','湖南']:
        print('please write your address!')
    print(中国[name])
    cheek_address()
cheek_address()
#print(中国['江西'])
for i in range(3):
    if i == 1:
        address = 中国
    if i == 2:
        address =  '''


'''def if_ture(address_ , addr):
    if address_ in addr:
        pass
    else:
        print('please input true address!')
        check_address()
def check(ad,addr):
    if_ture(ad,addr)
    for i in addr:
        print(i)
def check_address():
    address_name = input('your address:')
    check(address,address)
    check(address,address[address_name])
    address_name2 = input('your address:')
    check(address[address_name],address[address_name][address_name2])
while True:
    check_address()'''

address = {
    '湖南':{'长沙':['湖南大学','国防科技大学'],
          },
    '江西':{'南昌':{'谣湖':['师大', '火车站'],
                 '昌北':['江西财大','江西农大'],},
                 '宜春':['水江','袁州区']}
}
def downlevel(address):
    for one in address:
        print(one)

zhiling1 =address
count = 1
back = 'b'
esc = 'q'

while True:
    zhiling = input('%d the address you want:'%count)
    zhiling1 = address
    if zhiling == back:
        address = zhiling1
        downlevel(address)
        continue
    elif zhiling == esc:
        break
    elif zhiling in address:
        downlevel(address)
        address = address[zhiling]

