# name = 'alex'
# # v = name[0:2]
# # v = name.strip('x')
# # print(v)
# # print(name)
# # v = name[3:1]
# # print(v)
# for i in name:
#     print(i)
# content = input('请输入内容：')
# v = content.partition('+')
# v1 = int(v[0]) + int(v[2])
# print(v1)

# while True:
#     def check_code():
#         import random
#         checkcode = ''
#         for i in range(4):
#             current = random.randrange(0,4)
#             if current != i:
#                 temp = chr(random.randint(65,90))
#             else:
#                 temp = random.randint(0,9)
#             checkcode += str(temp)
#         return checkcode
#
#     code = check_code()
#
#     print(code)
#     code1 =code.lower()
#     v = input("请输入验证码：")
#     v1 = v.lower()
#     if v1 == code1:
#         print("欢迎登陆")
#         break
#     else:
#         print("验证码错误，请重新输入")

# v = input("请输入内容：")
# i = ['苍老师','东京热']
# for item in i:
#     if item in v:
#         v = v.replace(item,'***')
#
# print(v)
#
# while True:
#     v1 = input("请输入用户名：（不可超过20个字符）")
#     v2 = input("请输入密码：")
#     v3 = input("请输入邮箱：")
#
#     v = [v1,v2,v3,]
#     v4 = "\t".join(v)
#     v5 = v4.expandtabs(40)
#
#     print(v5)
#     exit()

# li = ['alex','eric','rain']
# # v = li.insert(0,'Tony')
# # print(li)
# li = ['eric','alex','tony']
# for i,ele in enumerate(li,100):
#     print(i,ele)

# v = input('请输入商品序号：')
# v = int(v)
# item = li[v-1]
# print(item)
# tu = ('alex',[11,22,{'k1':'v1','k2':['age','name'],'k3':(11,22,33)},44])
#
# v = tu[1][2].get('k2')
# v1 = v.append('Seven')
# print(tu)
dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
    for i in dic:
        print(i)
