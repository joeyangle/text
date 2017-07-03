#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
all_chart =[['毛巾','21'],['自行车','989'],['手机','1200'],['桌子','488']]
salary = int(input('please input your salary:'))
count = 1
print('your salary is %d'%(salary))
for each in all_chart:
    print('-'*10,'chat','-'*10)
    print('%d:'%(count),each)
    count = count + 1
print('-'*10,'chat','-'*10)
buy_chart = []
while True:
    shuru = input('please input you want to buy:')
    #print(shuru,type(shuru))
    if shuru == 'q':
        break
    if int(shuru) < 1 or int(shuru) > 4:
        print('out of shop list!')
        continue
    salary = salary - int(all_chart[int(shuru)-1][1])
    while salary >= 0:
        print('-'*10,'your buy','-'*10)
        print(all_chart[int(shuru)-1])
        buy_chart.append(all_chart[int(shuru)-1])
        break
    while salary < 0:
        salary = salary + int(all_chart[int(shuru)][1])
        print('you money to less and your money is %d'%salary)
        break


print('-'*10,'your chat','-'*10)
for each in buy_chart:
    print(each)
print('-'*10,'your money','-'*10)
print('NOW,YOUR MONEY IS %d'%salary)
'''
'''
购物车优化
要求：
商品信息存储在文件
已购记录 余额
添加商品 修改价格
需求：
记录商品信息的文本文件
文件的读取与修改
账户信息的记录文件
后台与前台的不同登录
'''


#定义一个确认密码函数make_sure 三个参数 1.账号 2.密码 3.账户存放地址
#增加一需求：读取salary
def make_sure(name,password,address):
    '''
    :param name: 账户的名字
    :param password: 账户密码
    :param address: 账户密码存放地址
    :return: 该账户是否正确 是否存在salary，如有则返回,第一项为账户是否真确，第二为是否有工资，有则返回
    '''
    f1 = open(address,'r')
    f = f1.readlines()
    f1.close()
    for line in f:
        out_list = []
        line = line.split()
        if len(line)==0 :
            continue
        #print(line)
        if line[0] == name and line[1] == password:
            out_list.append(True)
            try:
                salary = line[2]
            except:
                salary = None
            if salary is None:
                out_list.append(None)
            else:
                try:
                    salary = int(salary)
                    out_list.append(salary)
                except:
                    out_list.append('wrong')
            return out_list
        else:
            out_list.append(None)
        return out_list
#定义一个函数chat_out取出文件中的货架数据,一参数，文件地址，返回货物数据
def chat_out(address,p = 'f'):
    '''
    :param address: 货物信息存放地址
    :return: 货物信息
    '''
    f = open(address, 'r',encoding='utf-8').readlines()
    goods_out = []
    for line in f:
        if len(line) == 0:
            continue
        eachone = line.split()
        if p == 't':
            print(eachone)
        goods_out.append(eachone)
    return goods_out
#定义一个函数对chart进行输出，一参数为总体货物列
def print_chart(chart):
    count = 1
    for eachone in chart:
        print('-'*10,count,'-'*10)
        count = count + 1
        print(eachone)
#定义一个购买函数，三参数，总体货物，用户选择，salary
def buy_good(chart,choose,salary):
    '''
    :param chart:所有货物 
    :param choose: 用户输入的编号
    :param money: 用户salary
    :return: 
    '''
    buy_good_out = []
    salary = salary - int(chart[int(choose) - 1][1])
    while salary >= 0:
        print('-' * 10, 'your buy', '-' * 10)
        print(chart[int(choose) - 1])
        shopper_chart.append(chart[int(choose) - 1])
        break
    while salary < 0:
        salary = salary + int(chart[int(choose)][1])
        print('you money to less and your money is %d' % salary)

    buy_good_out.append(salary)
    return salary
'''
#定义一个简单的判断函数，参数为panduan，输出为Turn或者False
def panduan():
    panduan = input('would you want to go on?\n"q"is no\n"g"is yes')
    if panduan == 'q':
        return False
    elif panduan == 'g':
        return True
    else:
        print('wrong!please try again!\n"q"is no\n"g"is yes\n')
        panduan(panduan)
'''
#定义一个函数写入文件
def writefile(chart,salary,address1,address2):
    '''
    :param chart:买到的货物 
    :param salary: 还剩多少钱
    :param address1: 存储购买记录目录
    :param address2: 存储个人信息目录
    :return: 状况
    '''
    change = open(address2,'r',encoding='utf-8')
    jilu = open(address1,'a',encoding='utf-8')
    jilu.write('-' * 10 +'%s'%s_name+ '-' * 10 + '\n')
    jilu.write('-' * 10 + 'salary'+ '-' * 10 + '\n')
    jilu.write('%d'%salary + '\n')
    jilu.write('-' * 10 + 'chart' + '-' * 10 + '\n')
    for each in chart:
        print(each)
        jilu.write('%s'%each + '\n')
    jilu.close()
    change_xinxi = []
    for line in change.readlines():
        line = line.split()
        if len(line) == 0:
            continue
        if line[0] == s_name and line[1] == s_password:
            line[2] = salary
        change_xinxi.append(line)
    change.close()
    change2 = open(address2, 'w', encoding='utf-8')
    for each in change_xinxi:
        change2.write('\n')
        for eachone in each:
            change2.write(' %s '%eachone )
    change2.close()
#定义一个写入货物函数，两参数，一写入货物列表，二写入地址
def add_chart(lists,address,style = 'a'):
    f = open(address,style,encoding='utf-8')
    for eachone in lists:
        if len(eachone) == 0:
            continue
        for one in eachone:
            f.write('%s '%one)
        f.write('\n')
    f.close()

s_address = 'shopper'
c_address = 'controller'
g_address = 'chart_goods'
jilu_address = 'goumaijilu'

while True:
    print('please choose:\n1.I am controller\n2.I am shopper\n3.get out\n')
    choose = input('please choose:')
    if choose == '3':
        print('see you naxt time')
        break
    if choose == '2':
        s_name = input('your name:')
        s_password = input('your s_password:')
        if len(s_name) == 0 or len(s_password) == 0:
            print('please input!')
            continue#先判断，避免调用下一个函数
        make_sure_out = make_sure(s_name,s_password,s_address)
        if make_sure_out[0] == None:
            print('wrong account!please try again!')
            continue
        if make_sure_out[0] == True:
            print('right name and password')
            if make_sure_out[1] == 'wrong':
                print('some salary is wrong!\nplease link controller!')
                break
            elif make_sure_out[1] == None:
                salary = int(input('please input your salary:'))
            else:
                salary = make_sure_out[1]
            print('-'*10,'salary:%d'%salary,'-'*10)
            goods_chart = chat_out(g_address)
            #print(goods_chart)
            print_chart(goods_chart)
            shopper_chart = []
            while True:
                shuru = input('please choose goods you want:')
                if shuru == 'q':
                    break
                if int(shuru) < 1 or int(shuru) > len(goods_chart):
                    print('out of shop list!')
                    continue
                salary = salary - int(goods_chart[int(shuru) - 1][1])
                if salary >= 0:
                    print('-' * 10, 'your buy', '-' * 10)
                    print(goods_chart[int(shuru) - 1])
                    shopper_chart.append(goods_chart[int(shuru) - 1])
                elif salary < 0:
                    salary = salary + int(goods_chart[int(shuru)-1][1])
                    print('you money to less and your money is %d' % salary)
                    break
            print('-' * 10, 'your chat', '-' * 10)
            for each in shopper_chart:
                print(each)
            writefile(shopper_chart,salary,jilu_address,s_address)
            print('-' * 10, 'your money', '-' * 10)
            print('NOW,YOUR MONEY IS %d' % salary)
        else:
            print('mabey somewhere wrong!\nplease input again!')
            continue
    elif choose == '1':
        c_name = input('your name:')
        c_password = input('your password:')
        if len(c_name) == 0 or len(c_password) == 0:
            print('please input!')
            continue  # 先判断，避免调用下一个函数
        make_sure_out = make_sure(c_name, c_password, c_address)
        if make_sure_out[0] == None:
            print('wrong account!please try again!')
            continue
        if make_sure_out[0] == True:
            print('right name and password')
            while make_sure_out[1] == 'wrong':
                print('data wrong!')
                break
            #查看商品
            while True:
                chat_out(g_address,p = 't')
                c_price_add = input('1.增加商品\n2.修改价格\n3.leave\n')#此处还应该有货物下架
                if c_price_add == '3':
                    break
                elif c_price_add == '1':#增加商品
                    add_goods = []
                    while True:
                        print('you can add good one by one\nleave: Q\n go on: G  ')
                        add_more = input('choose:')
                        if add_more == 'Q':
                            break
                        if add_more == 'G':
                            add_good = []
                            good_name = input("the good's name:")
                            good_price = input("the good's price:")
                            add_good.append(good_name)
                            add_good.append(good_price)
                            add_goods.append(add_good)
                        else:
                            print('please input right!')
                            continue
                    add_chart(add_goods,g_address)
                elif c_price_add == '2':#修改价格
                    name_c_price = input("input good's name you want to change name:")
                    c_price = input('the price you want to change:')
                    f1 = open(g_address,'r',encoding = 'utf-8')
                    f2 = f1.readlines()
                    f1.close()
                    goods_c_price = []
                    for eachone in f2:
                        eachone = eachone.split()
                        if len(eachone) == 0:
                            continue
                        if eachone[0] == name_c_price:
                            eachone[1] = c_price
                        goods_c_price.append(eachone)
                    add_chart(goods_c_price,g_address,style= 'w')

                else:
                    print('please input right!= =')
                    continue
    else:
        print('please input right choose!')
