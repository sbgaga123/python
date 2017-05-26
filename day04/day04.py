#!/usr/bin/python
# -*- coding:utf-8 -*-

# def select(sql):
#     print('select')
# def insert(sql):
#     print('insert')
# def delete(sql):
#     print('delete')
# def update(sql):
#     print('update')
#
#
# func_dic = {
#     'select':select,
#     'update':update,
#     'insert':insert,
#     'delete':delete
# }
#
# def main():
#     while True:
#         sql = input('sql>').strip()
#         if not sql:continue
#         l = sql.split()
#         cmd=l[0]
#         if cmd in func_dic:
#             func_dic[cmd](l)
# main()
#
# from urllib.request import urlopen
# #
# # def index(url):
# #     def get():
# #         return urlopen(url).read()
# #     return get
# #
# # oldboy=index('http://www.baidu.com')
# #
# # print(oldboy().decode('utf-8'))
#

#无参装饰器
# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#         return res
#     return  wrapper
#
# @timmer
# def index():
#     time.sleep(3)
#     print('welcome to index')
#     return 1
#
#
# @timmer
# def foo(name):
#     time.sleep(1)
#     print('from foo')
#
# res=index()
# print(res)
#
# res1=foo('egon')
#
# print(res1)



# import time
#
# def longin(func):
#     def wrapper(*args,**kwargs):
#         u_in=input('请输入用户名')
#         pw_in=input('请输入密码')
#         if u_in == '123' and pw_in == '123':
#             print('登陆成功')
#         res =func(*args,**kwargs)
#         return res
#     return wrapper
#
#
# @longin
# def index():
#     time.sleep(1)
#     print('welcome to index')
#     return 1
#
# res = index()
# print(res)


#有参装饰器
# login_user={'user':None,'status':False}
# def auth(driver='file'):
#     def auth2(func):
#         def wrapper(*args,**kwargs):
#             if driver == 'file':
#                 if login_user['user'] and login_user['status']:
#                     res=func(*args,**kwargs)
#                     return res
#                 else:
#                     name=input(">")
#                     password=input(">")
#                     if name == '123' and password == '123':
#                         login_user['user']='123'
#                         login_user['status']='123'
#                         print('\33[45mlogin successful\33[0m')
#                         res=func(*args,**kwargs)
#                         return res
#                     else:
#                         print('\033[45mlogin err\033[0m')
#             elif driver == 'ldap':
#                 print('======ldap')
#             elif driver == 'mysql':
#                 print('======mysql')
#             else:
#                 print('=======未知')
#
#         return wrapper
#     return auth2
#
# @auth('file')
# def index():
#     print('welcome to index page')
#
# res=index()
# print(res)

def foo():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3
    print('fourth')
    yield 4
    print('fifth')

g=foo()
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopAsyncIteration:
    print('err')