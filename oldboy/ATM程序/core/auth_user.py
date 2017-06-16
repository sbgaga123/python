#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,time,logging


#用户登录函数
def user_login():
    user_login_dict = {}
    user_login_list = []
    with open(os.path.join(BS_ATM, 'db\\user_msg').strip(), 'r') as f:
        for line in f:
            line = eval(line)
            user_login_list.append(line['name'])
            user_login_dict.setdefault(line['name'], line['pwd'])
    while True:
        user_in = input('请输入用户名:')
        user_pwd = input('请输入密码:')
        user_pwd = int(user_pwd)
        if user_in in user_login_list:
            if user_pwd == user_login_dict.get(user_in):
                print('登陆成功')
                logging.debug('用户 %s 成功登录系统',user_in)
                break
            else:
                print('密码错误请重新输入')
        else:
            print('用户名不存在，请重新输入')

