#!/usr/bin/python
#_*_conding:utf-8_*_

import pickle
import os
import sys
BS_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 两个角色接口
class Interface1:
    pass
class Interface2:
    pass
# 学校类
class School:
    def __init__(self,address):
        self.address=address
    def school_pickle(self,name):
        school_pic = pickle.dumps(self)
        BS_SCHOOL_t = 'db\\school_pickle\\{name}'
        BS_SCHOOL = BS_SCHOOL_t.format(name=name)
        f_course = open(os.path.join(BS_PATH, BS_SCHOOL), 'wb')
        f_course.write(school_pic)
        f_course.close()
# 班级类
class Class():
    def __init__(self,address):
        School.__init__(self,address)
        Course.__init__(self)
        Teacher.__init__(self)

# 学生类
class Student:
    def __init__(self,address):
        School.__init__(self,address)
        Class.__init__(self)

# 课程类
class Course:
    # 定义周期价格
    def __init__(self,price,period,address):
        self.price=price
        self.period=period
        # 调用学校类创建课程
        School.__init__(self,address)
    def course_pcikle(self,name):
        course_pic=pickle.dumps(self)
        BS_COURSE_t='db\\course_pickle\\{name}'
        BS_COURSE=BS_COURSE_t.format(name=name)
        f_course=open(os.path.join(BS_PATH,BS_COURSE),'wb')
        f_course.write(course_pic)
        f_course.close()
# 讲师类
class Teacher:
    def __init__(self,address):
        School.__init__(self,address)

# 实例化两个学校
School_beijing=School('北京')
School_shanghai=School('上海')
# 序列化两个学校
School_beijing.school_pickle('school_beijing')
School_shanghai.school_pickle('school_shanghai')

# 实例化三个课程
Course_python=Course(10000,24,'北京')
Course_linux=Course(8000,30,'北京')
Course_go=Course(15000,20,'上海')
# 序列化三个课程
Course_python.course_pcikle('course_python')
Course_linux.course_pcikle('course_linux')
Course_linux.course_pcikle('course_go')
# f=open(os.path.join(BS_PATH,'db\\course_pickle\\$s'),'rb')
# data=pickle.loads(f.read())
# print(data)