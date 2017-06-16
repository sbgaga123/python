#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,auth_user
BS_ATM=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#查看商品列表
def shoplistdict():
    shoplist_dict = {}
    with open(os.path.join(BS_ATM, 'db\\shoplist').strip(), 'r',encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('|')
            shoplist_dict.setdefault(line[0],line[1])
        return shoplist_dict
#购买商品，加入购物车
def buyshoplist():
    buyshoplist_li=[]
    print(shoplistdict())
    comm=input('请输入想购买的商品名：')
    yeorno=input('是否确认购买？ yes or no?')
    if yeorno == 'yes':

        print(buyshoplist_li)




buyshoplist()