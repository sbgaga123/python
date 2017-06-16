#!/usr/bin/python
# -*- coding:utf-8 -*-
# import random
# proxy_ip=[
#     '1.1.1.1',
#     '1.1.1.2',
#     '1.1.1.3',
#     '1.1.1.4',
# ]
#
# print(random.choice(proxy_ip))


# import random
# print(random.sample([1,'23',[4,5]],2))

# import random
# # item=[1,3,5,7,9]
# #
# # random.shuffle(item)
# # print(item)
#
#
# def v_code(n=5):
#     res=''
#     for i in range(n):
#         num=random.randint(0,9)
#         s=chr(random.randint(65,90))
#         add=random.choice([num,s])
#         res+=str(add)
#     return res
#
# print(v_code(6))

# import random
#
# print(random.random())  # (0,1)----float    大于0且小于1之间的小数
#
# print(random.randint(1, 3))  # [1,3]    大于等于1且小于等于3之间的整数
#
# print(random.randrange(1, 3))  # [1,3)    大于等于1且小于3之间的整数
#
# print(random.choice([1, '23', [4, 5]]))  # 1或者23或者[4,5]
#
# print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合
#
# print(random.uniform(1, 3))  # 大于1小于3的小数，如1.927109612082716
#
# item = [1, 3, 5, 7, 9]
# random.shuffle(item)  # 打乱item的顺序,相当于"洗牌"
# print(item)

import random

def v_code():

    code = ''
    for i in range(5):

        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code += str(add)
    return code

print(v_code())

# 生成随机验证码