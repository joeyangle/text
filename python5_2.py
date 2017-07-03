#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/14'
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
5.开发一个简单的python计算器
实现加减乘除及拓号优先级解析
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) 
- (-4*3)/ (16-3*2) )等类似公式后，
必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
运算后得出结果，结果必须与真实的计算器所得出的结果一致
建立一个函数，迭代，如果内部有括号则优先运算
'''
# import re
# aaa = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# def jisuan(shuru):
#     pattern = re.compile(r'\(.*\)',re.S)
#     aa = re.findall(pattern,shuru)
#     aa = aa[1:-1]
#     print(aa)
#     for one in aa:
#         one1 = one[1:-1]
#         if '(' not in one1 and ')' not in one1:#先把第一层括号中的值计算出来，然后用replace进行替换
                #此处开始计算其中的值，将符号转换
                    #计算其中的加减乘除通过字典形式进行转换,这种方法不行
                    #还是必须通过if进行判断,先把乘除找出来算完
        #     pattern1 = re.compile(r'\d+\*\d+',re.S)
        #     oneout = re.findall(pattern1,one1)
        #     print(oneout)
        # pattern2 = re.compile(r'%s'%one,re.S)
        # out = re.sub(pattern2,jieguo_one1,aaa)
        # jisuan(out)
#jisuan()
# def biaozhunchuli(shuru):
#     for i in shuru:
#         if i in
# def kuohao(shuru):
#     if '(' not in shuru:
#
#         return
# aa = input()
# print(int(aa))
#无法int(含小数的数)
# aa = '2.3'
# aa = float(2.3)
# print(aa)
# 查询float可用
#print(str(2.333333))
#abc = '-7'
#print(float(abc))
#主函数

# shuru= '1 - 2 * ((60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# shuru = shuru.replace(' ','')
# pattern = re.compile(r'\([^()]+\)',re.S)#nice
# kuohao_pipei = re.findall(pattern,shuru)
# print(kuohao_pipei)
# for eachone in kuohao_pipei:
#     kuohao_answer = kuohao_jisuan(eachone)


# import re
# shuru= '1 - 2 * ((60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# shuru = shuru.replace(' ','')
# pattern = re.compile(r'\([^()]+\)',re.S)#nice
# kuohao_pipei = re.findall(pattern,shuru)
# print(kuohao_pipei)
# while True:
#     for i, one in enumerate(kuohao_pipei):
#         one1 = one[1:-1]
#         print(one1)
#         pattern2 = re.compile(r'\d+[*/]+\d+',re.S)
#         chenchu_pipei = re.findall(pattern2,one1)
#         print(chenchu_pipei)#判断没有乘除后进行加减运算
#         answer = str(jisuan(chenchu_pipei[0]))
#         print(answer)
#         print(i)
#         one.replace(chenchu_pipei[0],answer)
#         print(one)
#
#         while True:
#             for each in chenchu_pipei:
#                 pattern3 = re.compile(r'\d+[*/]\d+',re.S)
#                 jisuan_pipei = re.findall(pattern3,each)
#                 print(jisuan_pipei)
#             break
#     break

# def kuo_h_jisuan(string):或许更好
#     '''
#     本函数上面的优化版，将内部转化为列表形式，格式如[数字符号数字符号。。。]
#     :param string:去除括号没有
#     :return:返回该结果
#     '''
#     ti_h_zz = re.compile(r'/d+',re.S)
#     string = re.sub(ti_h_zz,'')
import re

def fuhao_chuli(string):
    if '--' in string:
        string = string.replace('--','+')
    if '+-' in string:
        string = string.replace('+-','-')
    if '-+' in string:
        string = string.replace('-+','-')
    return string

def jisuan(string):
    '''
    :param string:格式化后的计算式 ，形式如：A+B，仅含三项，数字+运算符+数字
    :return: 计算结果
    '''
    # 先把运算符取出来
    pattern = re.compile(r'\d([*+/-])-?\d', re.S)
    fuhao = re.findall(pattern, string)[0]
    pattern1 = re.compile(r'(.*\d)[*+/-](-?\d.*)')
    num = re.findall(pattern1,string)
    num1 = float(num[0][0])
    num2 = float(num[0][1])
    if fuhao == '+':
        jieguo = num1 + num2
    elif fuhao == '-':
        jieguo = num1 - num2
    elif fuhao == '*':
        jieguo = num1 * num2
    elif fuhao == '/':
        if num2 == 0:
            print('分母不可为0')
            jieguo = 'wrong'
            return jieguo
        jieguo = num1 / num2
    jieguo = round(jieguo,7)
    return jieguo
#一直在正则匹配出问题，需要再熟悉
def kuohao_jisuan(string):#本来以为已经解决问题，但是在浮点数处遇到问题，不能以string，太麻烦
    '''
    该函数将最底层含括号进行运算，思路，先乘除，后加减
    :param string: 内部无括号的计算式，字符形式
    :return: 计算结果
    '''
    if '*' in string or '/' in string:
        #pattern = re.compile(r'\d+[*/][*/0-9]+',re.S)#'1+2*3*4'
        # pattern = re.compile(r'\d[*/0-9.]+\d')#换一种匹配规则：加减中间含乘除的匹配项
        # chen_chu = re.findall(pattern,string)#'2*3*4'
        # #print(chen_chu)
        # for ch_ch_one in chen_chu:
        #print(string)
        pattern_ch_ch = re.compile(r'[0-9.]+[*/]-?[0-9.]+',re.S)#取出乘除的第一项
        zu_chen_chu = re.findall(pattern_ch_ch,string)#'2*3'
        answer = str(jisuan(zu_chen_chu[0]))
        string = string.replace(zu_chen_chu[0],answer)
        return kuohao_jisuan(string)
    else:
        try:
            string = fuhao_chuli(string)
            float(string)
            return string
        except:
            string = fuhao_chuli(string)
            pattern_j_j = re.compile(r'-?[0-9.]+[+-][0-9.]+',re.S)
            zu_jia_jian = re.findall(pattern_j_j,string)
            answer = str(jisuan(zu_jia_jian[0]))
            string = string.replace(zu_jia_jian[0], answer)
            return kuohao_jisuan(string)
#print(kuohao_jisuan('-6-2*3/4-4*2'))
#主函数，现将最底层括号匹配，然后计算后返回替代
def all_jisuan(string):
    string = string.replace(' ','')
    if '(' not in string and ')' not in string:
        string = kuohao_jisuan(string)
        return string
    else:
        pattern = re.compile(r'\([^()]+\)', re.S)#括号开始括号结束，中间没有括号
        base_kh_list = re.findall(pattern,string)
        for base_kh in base_kh_list:
            base_kh1 = base_kh[1:-1]#base_kh为去除括号的算式
            kuohao_out = kuohao_jisuan(base_kh1)
            string = string.replace(base_kh,kuohao_out)
            string = fuhao_chuli(string)
        return all_jisuan(string)
    return string
        #替换之后可能出现*- +- -- /-这样的情况，所以这时候就需要处理
def start():
    while True:
        shuru = str(input('\033[1;31;47m q is out\ninput:\n\033[0m'))
        if shuru == 'q':
            break
        answer = all_jisuan(shuru)
        if '+' in answer:
            answer = answer[1:]
        print(answer)

if __name__ == '__main__':
    start()