#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
#读取商品列表
goods_list = open('商品列表.txt','r',encoding="utf-8")
open_goods_list = goods_list.readlines()
goods_list.close()
#读取用户名密码
user_all = open('用户列表.txt','r',encoding="utf-8")
open_user_all = user_all.readlines()
user_all.close()
#提取用户名密码表
dic = {}
for i in open_user_all:
    v = i.strip().split('|')
    dic_list = dic.setdefault(v[0],v[1])
# dic_k =  dic.get()
#dic_all = {}
list_all = []
for qa in open_user_all:
    vp = qa.strip().split('|')
    #dic_alm = dic_all.setdefault(vp[0],[vp[1],vp[2]])
    list_all.extend([vp[0],vp[1],vp[2]])
#用户登录
t = 0
while t < 3:
    user_in = input("请输入用户名：")
    pwd_in = input("请输入密码：")
    if user_in in dic.keys():
        i_pwd = dic.get(user_in)
        if i_pwd == pwd_in:
            print('欢迎登录购物系统！')
            user_status = '1'
            break
        else:
            print('密码不正确，请重新输入：')
            t += 1
    else:
        print('用户不存在，请重新输入：')
        t += 1

if user_status == '1':
    x = 0
    while x < 50:
        user_doo = input('请进行操作:1.查看用户余额，2.查看商品列表，3.查看购物记录，4.退出购物系统')
        user_do = int(user_doo)
    # 查看用户余额
        dic_money = {}
        for op in open_user_all:
            v_money = op.strip().split('|')
            dic_m = dic_money.setdefault(v_money[0],v_money[2])
        i_money = dic_money.get(user_in)
        if user_do == 1:
            print('您当前的账户余额为：',i_money)
            x += 1
    #查看商品列表
        elif user_do == 2:
            # while x < 50:
            dic_goods = {}
            # p = int(input('请输入页码,返回上一级请输入q'))
                # if p == q:
                #     x = 50
                # else:
                #     start = (p - 1) * 10
                #     end = p * 10
                #     int(start)
                #     int(end)
                #     pate_open_goods_list = open_goods_list[start:end]
                #     print(pate_open_goods_list)
            for pd in open_goods_list:
                v_goods = pd.strip().split('|')
                dic_g = dic_goods.setdefault(v_goods[0], v_goods[1])
            #     v1 = v_goods[start:end]
            #         # for i in v_list:
            #     print(v1)
            print(dic_goods)
            user_buy = input("请输入要购买的商品，返回上一级请输入q")
            i_goods = dic_goods.get(user_buy)
            if user_buy == 'q':
                x += 1
            else:
                i_now_money = int(i_money) - int(i_goods)
                if i_now_money < 0:
                    print('购买失败！您当前的余额不足')
                    x += 1
                else:
                    print('购买成功!您当前的余额为',i_now_money)
                    goods_hist = [user_buy]
                    f =open('购物记录.txt','w',encoding="utf-8")
                    f.writelines(goods_hist)
                    f.close()
                    #dic_fin = dic_all.update({user_in:[pwd_in,i_now_money]})
                    vpj = list_all.index(user_in)
                    #vpj = '|'.join(dic_all)
                    vpjj = int(vpj) + 2
                    list_all[vpjj] = i_now_money
                    # list_all_change = "|".join('%s' %id for id in list_all)
                    # f_money = open('用户列表.txt', 'w', encoding="utf-8")
                    # f_money.writelines(list_all_change)
                    # f_money.close()
    #查看购物记录
        # 读取购物记录
        elif user_do == 3:
            goods_history = open('购物记录.txt','r', encoding="utf-8")
            open_goods_history = goods_history.readlines()
            goods_history.close()
            print(open_goods_history)
    #退出购物系统
        elif user_do == 4:
            sys.exit('欢迎您下次光临！')

