#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time
# 读取login.py文件，将内容赋值给变量login_f1,并关闭
f1 = open('name_pwd.txt','r')
data = f1.read()
f1.close()

# 将变量login_f1的值，进行分片，分隔符为‘:‘
# 提取第0位元素，赋值给另一个变量ruser
ruser = data.strip().split("|")[0]
# 提取第1位元素，赋值给另一个变量rpwd
rpwd = data.split("|")[1]

# 读取黑名单文件lock.user，将内容赋值给变量lock_f2，并关闭
f2 = open("name_pwd_lock.txt", 'r')
data1 = f2.readlines()
f2.close()

# 定义一个变量，用于计数
t = 0

#当t小于3时，无限循环。
while t < 3:
    name = input("请输入帐号:")
    for a in data1:
        if name == a:
            print("抱歉!此帐号已被锁定。")
            exit()

for b in login_f1:
    if name == ruser:
        t = 0
        while t < 3:
            pwd = input("请输入密码:")
            if pwd == rpwd:
                print("Welcome!%s" %name)
                exit()
            else:
                print("Sorry!wrong password.")
            t += 1
        else:
            print("抱歉，错误次数达到3次，该账户被锁定!")
            f = open('name_pwd_lock.txt', 'w')
            f.write('%s' % name)
            f.close()
        exit()