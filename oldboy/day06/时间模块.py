#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
#时间戳
# print(time.time())

#结构化的时间
# print(time.localtime())
# print(time.localtime().tm_year)
# print(time.gmtime())

#格式化的字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %X'))

#
# print(time.localtime(13211123))
# print(time.localtime(time.time()))
#
# print(time.mktime(time.localtime()))

# print(time.strftime('%Y %X',time.localtime()))

# print(time.strptime('2017-06-04 11:59:59','%Y-%m-%d %X'))

# print(time.ctime(123123132))

# print(time.asctime(time.localtime()))
# import time
# #--------------------------我们先以当前时间为准,让大家快速认识三种形式的时间
# print(time.time()) # 时间戳:1487130156.419527
# print(time.strftime("%Y-%m-%d %X")) #格式化的时间字符串:'2017-02-15 11:40:53'
#
# print(time.localtime()) #本地时区的struct_time
# print(time.gmtime())    #UTC时区的struct_time
#--------------------------按图1转换时间
# localtime([secs])
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
time.localtime()
time.localtime(1473525444.037215)

# gmtime([secs]) 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

# mktime(t) : 将一个struct_time转化为时间戳。
print(time.mktime(time.localtime()))#1473525749.0


# strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个
# 元素越界，ValueError的错误将会被抛出。
print(time.strftime("%Y-%m-%d %X", time.localtime()))#2016-09-11 00:49:56

# time.strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
#time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6,
#  tm_wday=3, tm_yday=125, tm_isdst=-1)
#在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。