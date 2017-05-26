#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
作业要求：
1.查
    输入：www.oldboy1.org
    获取当前backend下的所有记录

2.新建
    输入：
        arg = {
            'bakend': 'www.oldboy1.org'
            'record':{
                'server': '100.1.7.9',
                'weight':20,
                'maxconn':30
            }
        }

3.删除
    输入：
        arg = {
                'bakend': 'www.oldboy.org',
                'record':{
                    'server':'100.1.7.9',
                    'weight':20,
                    'maxconn':30
                }
        }
"""


def fetch(data):
    print(1)
def add(data):
    pass
def remove(data):
    pass

if __name__ == '__main__':
    msg="""
    1.查询
    2.添加
    3.删除
    4.退出  
    """
    menu_dic={
        '1':fetch,
        '2':add,
        '3':remove,
        '4':exit,
    }
while True:
    print(msg)
    user_in = input('操作>>:').strip()
    #if len(user_in) == 0 or user_in in menu_dic:continue
    #if user_in == '4':break
    data = input("数据>>:").strip()

    menu_dic[user_in](data)