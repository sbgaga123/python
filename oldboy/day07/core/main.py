#!/usr/bin/python
#_*_coding:utf-8_*_

msg_f="""
###############################
####欢迎来到老男孩管理平台####
##############################
"""
msg_s="""
请选择序号并进行相关身份操作
1.学员，2.讲师，3.管理员
"""
msg_x="""
###欢迎登录老男孩学员管理界面###
请选择序号并进行对应操作
1.学员注册，2.交学费，3选择班级
"""
msg_j="""
###欢迎登录老男孩讲师管理界面###
请选择序号并进行对应操作
1.管理班级，2.选择上课的班级，3.查看班级成员列表，4.修改学员成绩
"""
msg_g="""
###欢迎登录老男孩管理员管理界面###
请选择序号并进行对应操作
1.创建讲师，2.创建班级，3.创建课程
"""


# dict_msg={
#     '1':
#
#
# }

print(msg_f)
print(msg_s)
while True:
    user_in = input('序号>>:').strip()
    # if len(user_in) == 0 or user_in in menu_dic:continue
    # if user_in == '4':break
    if int(user_in) == 1:
        print(msg_x)
    elif int(user_in) == 2:
        print(msg_j)
    elif int(user_in) == 3:
        print(msg_g)
    elif int(user_in) == 4:
        exit()

