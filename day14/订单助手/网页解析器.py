#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/8/6'
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
from bs4 import BeautifulSoup
import re
import json
import socket
'''
对爬取到的订单页面进行解析
    - 需要解决的问题
        1.对商品按照店铺---卖家id进行分类并按照这种框架对商品id和图片url进行分类
        2.

通过以下字典方式建立数据结构
{店铺1：{订单1:[商品1，商品2...]，订单2:[...]...},店铺2:{}...}
商品包含的信息为 本地图片地址 商品名 

查看网页知各层级结构class属性不同，通过该区别对店铺分类，订单分类
    店铺class属性为：class="batch_tb_shop"
    订单class属性为：class="packageItem "
    
问题：数据结构不够清晰
    确立订单的数据结构，便于之后的操作
    买家订单
        -- 备注
        -- 每个商品
            -- 商品的属性
                -- 数量
                -- 标题
                -- 详细信息
                -- 图片url
    {order1:{good1:{num:shu,photo_url:url,detail:xiangqing,title:tit},good2:{}...},order2...}
    以上再依据beautifulsoup的分析结构重新对数据进行解析
'''


with open("C:\\Users\joeya\Desktop\批量打印.html",encoding='utf-8') as f:
    file_html = f.read()

class Html_parser(object):
    '''
    将下载好的网页进行解析处理
    提供两种输出选择
        一种为分订单输出
        一种会汇总输出
    建立一个url与url存储地址的字典，存储地址含有title信息，以上用josn格式保存
    设立打印订单数量机制，避免过多订单影响拣货
    '''
    def __init__(self,parser_html,parser_number = 7):
        '''
        :param parser_html:对应解析的html文件 
        :param parser_number: 需要解析的订单数量
        '''
        self.parser_html = BeautifulSoup(parser_html,'lxml')
        self.parser_number = parser_number
        self.goods_num = 0

    def each_order_get(self):
        '''
        获取每一个order并对order进行解析
        返回格式如下：
        {order1:
        {good1:{number:shu,photo_url:url,detail:xiangqing,title:tit},
        good2:{},
        wangwangid:duiyingid,massage:duiiying...},
        order2...}
        :return: 如上格式的数据
        '''
        #以下为各目标tag所对应的class
        order_class = 'packageItem'
        wangwang_id_class = "wangwangHover"
        total_number_class = "align_c totalBuyNum"
        true_name_class = "align_c togetherReceiverContainer"
        order_address_class = 'addrItem'
        order_massage_class = 'flagMeoItem'
        photo_url_class = 'goodsDetailTrigger'
        order_goods_class = "prod_list_sml"

        order_list_tag = self.parser_html.find_all(class_ = order_class)
        order_list_tag = order_list_tag[:self.parser_number]#控制解释的订单量
        all_order_list = []
        s = 1
        for order_tag in order_list_tag:
            each_order_list = []
            print(order_tag)
            wangwang_id = order_tag.find(class_ = wangwang_id_class).string
            total_number = order_tag.find(class_ = total_number_class).string
            true_name = order_tag.find(class_ = true_name_class).string
            order_address = order_tag.find(class_ = order_address_class).string
            order_massage = order_tag.find(class_ = order_massage_class).string
            #photo_url = order.find_all(class_ = photo_url_class)
            order_goods = order_tag.find_all(class_ = order_goods_class)
            i = 1
            for each_order_good in order_goods:
                good_title = each_order_good.dt.img['data-title']
                photo_url = each_order_good.dt.img['data-url']
                good_detail = each_order_good.dd.span.string
                good_number = each_order_good.dd.span.next_sibling.string
                good_list = [("title",good_title),("photo_url",photo_url),("detail",good_detail),("number",good_number)]
                good_list_dict = dict(good_list)
                each_order_list.append(('good%s'%i,good_list_dict))
                i += 1
            each_order_dict = dict(each_order_list)
            order_dict = dict([("goods",each_order_dict),("wangwang_id",wangwang_id),("total_number",total_number),("true_name",true_name),("order_address",order_address),("order_massage",order_massage)])
            all_order_list.append(('order%s'%s, order_dict))
            s += 1
        all_order_dict = dict(all_order_list)
        return all_order_dict

    # def get_wangwangHover_BuyNum(self):
    #     '''
    #     get the ID of wangwang and the number of buyer get goods
    #     tip: you buy same good as number of 2 is 2 not 1
    #     :return: a list of all order's wangwang and number present
    #     '''
    #     id_nums = []
    #     num = []
    #     wangwang_ids = self.parser_html.find_all(class_="wangwangHover")
    #     totalBuyNums = self.parser_html.find_all(class_=re.compile("totalBuyNum"))
    #     for wangwang_id in wangwang_ids:
    #         wangwang_list = []
    #         wangwang_list.append(wangwang_id.string)
    #         id_nums.append(wangwang_list)
    #     for totalBuyNum in totalBuyNums:
    #         num.append(totalBuyNum.string)
    #     for i in range(len(id_nums)):
    #         id_nums[i].append(num[i])
    #     id_nums = id_nums[:self.parser_number]
    #     for id_num in id_nums:
    #         self.goods_num += int(id_num[1])
    #     return id_nums
    #
    # def get_photourl_title_orderdetail(self):
    #     '''
    #     获取订单页商品url、商品标题、购买商品的详细信息
    #     :return: 返回当前操作的订单url及详细信息组成的有序列表
    #     '''
    #     goods = self.parser_html.find_all(class_="prod_list_sml")  # 每一个商品的描述区块
    #     goods_list = []
    #     goods_num_infact = 0
    #     for each_good in goods:
    #         good_photo_url = each_good.dt.img['data-url']
    #         good_title = each_good.dt.img['data-title']
    #         self.add_url(good_photo_url,good_title)
    #         good_orderdetail = each_good.dd.span.string
    #         good_ordernum = each_good.dd.find_all('span')[1].string#订单中每一件商品的数量
    #         goods_list.append(good_photo_url)
    #         goods_list.append(good_orderdetail)
    #         goods_list.append(good_ordernum)
    #         goods_num_infact += int(good_ordernum)
    #         if goods_num_infact == self.goods_num:
    #             return goods_list[:self.goods_num * 3]

    def add_url(self,url,title):
        '''
        验证本地的url池是否含有该商品，否则添加到url池并且新建本地图片文档，是则不做操作
        url池以josn数据保存
        :param url: 该商品的图片链接
        :param title: 该商品的标题
        :return: 
        '''
        pass

test = Html_parser(file_html, 7)
print(test.each_order_get())

def handle_html(html,orlist):
    '''
    将html模板进行数据填充
    :param html: html模板
    :param orlist: 数据
    :return: 填充好的html文件
    '''

    buyers_html = ''
    for k_buyer,v_orlist in orlist.items():
        buyer_html = '<div style="font-size:50px;color:green" > %s </div>'%k_buyer
        buyers_html += buyer_html
        print(len(v_orlist))
        #print(v_orlist)
        for i in range(0,int(len(v_orlist)),3):
            xunhuan = '''
                  <div style="font-size:50px; background-color:#FF0000">
                    @@good_title
                </div>
                <div style="font-size:100px; background-color:#FFFF00;width: 35%;float:right">
                    @@good_num
                </div>
                <div width: 60%;float:left>
                    <img src="@@good_photo_url" style="width:500px;height:500px">
                </div>
                
                '''
            if v_orlist[i+1] == None:
                xunhuan = xunhuan.replace('@@good_title','no choose')
            else:
                xunhuan = xunhuan.replace('@@good_title',v_orlist[i+1])
            xunhuan = xunhuan.replace('@@good_num',v_orlist[i+2])
            xunhuan = xunhuan.replace('@@good_photo_url',v_orlist[i])
            buyers_html += xunhuan
            print(xunhuan)

    html = html.replace('@@@all_good_list',buyers_html)
    return html


def handle_request(client):
    buf = client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    with open('order_list.html',encoding='utf-8') as f:
        html_file = f.read()
    html_file = handle_html(html_file,all_order).encode()#对html模板进行填充
    client.send(html_file)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8080))
    sock.listen(5)
    print('可以访问了，地址为：%s:8079'%ip)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

main()