#!/usr/bin/python
# -*- coding:utf-8 -*-



import os
def fetch(data):
    dict_all = {}
    backend_list = []
    dict_server = {}
    with open('haproxy.conf','r',encoding='utf-8') as read_f:
        i = 0
        hapro_list = read_f.readlines()
        for line in hapro_list:
            if data in line:
                print(line)
                line_list = hapro_list[i+1]
                dict_server['name'] = line_list.strip().split()[1]
                dict_server['IP'] = line_list.strip().split()[2]
                dict_server['weight'] = line_list.strip().split()[4]
                dict_server['maxconn'] = line_list.strip().split()[6]
                print(dict_server)
            i += 1





def add(data):
    data = data.strip().split()
    data = data[2] + data[3]
    data1 = eval(data)
    list_dic = []
    list_dic1 = []
    with open('haproxy.conf','a+',encoding='utf-8') as read_f:
        for k in data1:
             if k == 'backend':
                 read_f.write(k + ' ' + data1.get(k) + '\n')
             elif k == 'record':
                 data2 = data1.get(k)
                 for k,v in data2.items():
                     list_dic.append(k)
                     list_dic.append(v)

                 for i in list_dic:
                     i = str(i)
                     list_dic1.append(i)
                 list_dic1.insert(1,list_dic1[1])
                 vs = " ".join(list_dic1)
                 read_f.write('\t'+ vs + '\n')


def remove(data):
    list_dic = []
    data = data.strip().split()
    data = data[2] + data[3]
    data1 = eval(data)
    for k in data1:
         if k == 'backend':
             bac = data1.get(k)
         elif k == 'record':
             data2 = data1.get(k)
             for k,v in data2.items():
                 list_dic.append(k)
                 list_dic.append(v)
             ser = list_dic[0]
    with open('haproxy.conf','r',encoding='utf-8') as read_f:
        i = 0
        hapro_list = read_f.readlines()
        for line in hapro_list:
            if bac in line and ser in hapro_list[i+1]:
                bac_line = line
                ser_line = hapro_list[i+1]
                hapro_list.remove(bac_line)
                hapro_list.remove(ser_line)
            i += 1
            hapro_list1 = "".join(hapro_list)
    with open('.haproxy.conf.swp','w',encoding='utf-8') as write_f:
        write_f.write(hapro_list1)
    os.remove('haproxy.conf')
    os.rename('.haproxy.conf.swp','haproxy.conf')

if __name__ == '__main__':
    msg="""
    1.查询
    2.添加
    3.删除
    4.退出
    """
    msg_fetch = """
    1.查
        输入：www.oldboy1.org
        获取当前backend下的所有记录
    """
    msg_add = """
    2.新建
        输入：
            arg = {'backend':'www.oldboy1.org', 'record':{'server':'100.1.7.9','weight':20,'maxconn':30}}
    """
    msg_del = """
    3.删除
        输入：
            arg = {'backend':'www.oldboy1.org', 'record':{'server':'100.1.7.9','weight':20,'maxconn':30}}
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
    if int(user_in) == 1:
        print(msg_fetch)
    elif int(user_in) == 2:
        print(msg_add)
    elif int(user_in) == 3:
        print(msg_del)
    elif int(user_in) == 4:
        exit()
    data = input("数据>>:").strip()

    menu_dic[user_in](data)



