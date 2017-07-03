#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/2'
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
文件属性的一些方法
oneset = set([5,6,5,2,4,65,2,3])
twoset = set([54,21,35,4,5,2])
print(oneset.intersection(twoset))#取交集
print(oneset.union(twoset))#取并集
print(oneset.difference(twoset))#差集 我这有，你那没有in oneset not in twoset
print(oneset.issubset(twoset))#oneset 是不是twoset的子集
print(oneset.issuperset(twoset))#oneset是不是twoset的父集
print(oneset.symmetric_difference(twoset))#对称差集 把两者都没有的取出来
#oneset.pop#随机删除一个元素并把该元素返回
oneset.discard('100')#删除集合中一个元素，如果在该集合中存在则删去，不存在也不报错
oneset.isdisjoint(twoset)#如果两者没有交集则返回为Ture
print(oneset.remove(2))
print(oneset & twoset)#交集
print(oneset | twoset)#并集
print(oneset - twoset)#差集 在一中不在二中
print(oneset ^ twoset)#对称差集
oneset.add()#添加
oneset.update({[2,3,4]})#添加多项
oneset.remove()#删除指定一项
#in 方法适用列表 字典 集合 字符串

#######文件操作#######
#f = open('address','r/w/a',encoding='utf-8')#文件句柄，内存中的一个对象
'''
'''
f = open('chart_goods','r',encoding='utf-8')
f1 = f.read()
f2 = f.read()
print(f1)
print('-------%s--'%f2)
#read()从开始时有相当于光标，第二次read从末尾开始，故“没有”读出来
#直接采用
for line in f:#f在这充当迭代器
    pass#节省内存方法
注意以上的光标的作用，read方法均适用
'''

'''
#####文件的一些方法
f.strip(rm)方法去除开头结尾的换行符空格和rm序列处的字符
enumerate()函数可以同时获得索引和值 for index, item in enumerate(list1):index索引 item值 可接受第二个参数指定索引开始值
f.tell()方法 计数已读 光标现在的位置 
f.seek()方法 将光标回到输入位置
f.detach()方法 文件编辑到一半转换格式（？从gbk到utf-8）
f.encoding 文件的编码
f.fileno() 方法返回整数的底层实现使用请求从操作系统的I / O操作的文件描述符
f.name 返回文件名
f.isatty()方法 看这是不是终端设备
f.seekable()方法 判断该文件的光标是否可以移动
f.readable()方法 判断文件是否可写
f.writeable() 同上
f.flush()方法 一般为在内存建立一个缓存，默认缓存满了再写入硬盘
现在使用该方法直接强制刷新写入硬盘,一个一个蹦出来
f.closed 判断文件是否关闭
f.truncate()方法 无参数默认清空文件 参数为截断位置，如10即为从第十个字符处截断，后面全部删除
'''

'''
#######文件的修改
'a'  追加方法，加在后面，不覆盖原文件
'w'  写方法 会覆盖以前的文件
'r'  只读，不可修改
'r+' 读写 可读可写，不覆盖写从最后开始写
'w+' 写读 可读可写， 先覆盖，再读出来
'a+' 追加读，可以读了
'rb' 以二进制文件格式读文件
'wb' 以二进制格式写文件
f. write("hello world\n".encode())告诉你现在是什么格式，便于转换成二进制
'ab' 以二进制格式追加
'rU' 'r+U' 可以将\r\n \n\r自动转换成\n (为了保证Windows和Linux一致)
'''
'''
import sys, time
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()#强制写入，进度条就是这样,确保已经写入了硬盘
    time.sleep(0.1)    
'''

'''
########文件的修改
1.vim式读取文件，全部读出来
2.找到修改的地方修改，然后写到另一个文件
字符串有replace方法 line.replace
whit open('address','r',encoding = 'utf-8') as f:#自动关闭文件，并且可同时打开多个
    pass
'''
'''
#########字符编码与转码
Windows默认bgk编码
import sys:
print(sys.getedfaultencoding())打印系统默认编码
解码前告知原编码为什么
decode告诉原编码  encode告诉转码成什么 先转码再编码 .decode('gbk').encode('utf-8')示例为gbk转utf-8
ASCII码只存英文 Unicode扩展包可升缩性utf-8英文一个字节中文三个字节
Unicode兼容GB2312兼容bgk，gbk兼容GB*****，但是还是需要转码
uncode 可以直接在utf-8 中打印
python2.x默认ASCII
Python3.x默认utf-8
先转码，再编码，先decode转成Unicode，再encode编成目标代码
转码
'''
'''
#######函数
1.面向对象  class
2.面向过程  def
3.函数式编程  def
import time
def logger():#日志函数，添加时间
    time_format = '%Y-%m-%d %X'#时间格式 年-月-日-小时分钟秒#0format：构成版式
    time_current = time.strftime(time_format)#按照格式输出时间 #current：现在的；
    with open('address','a+') as f:
        f.write('%s end action\n'%time_current)

没有return 即为None
return 返回一个tuple，return 1, 'hello', [] ,{'1':'2'}任意可行

def test(*args):#接受n个位置参数，参数不固定，传多个参数为一个多个参数组成的tuple，关键是前面有一个*
    print(args)
test(1,2,3,4,5)  输出就是(1,2,3,4,5)
test(*[1,2,3,4,5])  args = tuple([1,2,3,4,5]) 输出为：[1,2,3,4,5]
def test2(**kwargs):#接受n个关键字参数，把n个关键字参数转换成字典形式
    print(kwargs)
test2(name = 'Alex',age = 8, sex = 'F')
test2(**{"1":"2",})
'''
#global shool 可以改全局变量！！！别用，自己搞不清楚    Ctrl+ / 所选中前都加#

