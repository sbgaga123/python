#!/usr/bin/python
# -*- coding:utf-8 -*-

# class Foo:
#     '''文档注释'''
#     pass


#类是一系列对象共有的特征（变量的定义）与技能（函数的定义）的结合体
# class Chinese:
#     country='China'
#
#     # Chinese.__init__(p1,'egon','18','male')
#     def __init__(self,name,age,sex):
#         #p1.Name=name；p1.Age=age,p1.Sex=sex
#         self.Name=name
#         self.Age=age
#         self.Sex=sex
#
#
#     def talk(self):
#         print('talking',self)


#属性的引用
# print(Chinese.country)
# print(Chinese.talk)
# Chinese.talk(123)
# Chinese.x=1
# print(Chinese.x)
# Chinese.country=123123123123123
# print(Chinese.country)

#实例化
class Chinese:
    country = 'China'

    # Chinese.__init__(p1,'egon','18','male')
    def __init__(self, name, age, sex):
        # p1.Name=name；p1.Age=age,p1.Sex=sex
        self.Name = name
        self.Age = age
        self.Sex = sex
    def talk(self):
        print('%s is talking' %self.Name)
# p1=Chinese('egon','18','male') #Chinese.__init__(p1,'egon','18','male')
# p2=Chinese('alex','9000','female') #Chinese.__init__(p1,'egon','18','male')

#对象的使用：只有一种，就是属性引用
# print(p1.Name)
# print(p1.Age)
# print(p1.Sex)
# print(p2.Name)

# print(p1.country)
# print(p2.country)


# p1.talk()
# p2.talk()
country = 'aaaaaaaaaa'
class Chinese:
    country = 'China'
    def __init__(self, name, age, sex):
        # self.country=123123123123123123
        self.Name = name
        self.Age = age
        self.Sex = sex
    def talk(self):
        print('%s is talking' %self.Name)
#类名称空间
# print(Chinese.__dict__)


#对象的空间
p1=Chinese('egon','18','male') #Chinese.__init__(p1,'egon','18','male')
p2=Chinese('alex','180','male')


# print(p1.__dict__)
# print(p1.Age) #p1.__dict__['Age']
# print(p1.country,id(p1.country))
# print(p2.country,id(p2.country))

# print(Chinese.talk)
# print(p1.talk)
# p1.talk() #Chines.talk(p1)
# print(p2.talk)
# p2.talk()#chinese.talk(p2)
print(type(p1))

