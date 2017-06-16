#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
# print(os.path.abspath('a/b/c.txt')) #E:\wupeiqi\s17\day06\a\b\c.txt
# print(os.path.abspath('/a/b/c.txt')) #E:\a\b\c.txt

# print(os.path.split('E:\\a\\c.txt'))
# print(os.path.dirname('E:\\a\\c.txt'))
# print(os.path.dirname('E:\\a'))
# print(os.path.basename('E:\\a\\a,txt'))

# print(os.path.exists('E:\\a'))
# print(os.path.exists('E:\wupeiqi\s17\day06'))

# print(os.path.isabs('E:\\day06'))
# print(os.path.isabs('day06'))

# print(os.path.getsize(r'E:\wupeiqi\s17\day06\test.py'))

# print(os.path.join('a','E:\\b','c.txt'))
# print(os.path.join('a','/b','c.txt')) #/b/c.txt

# print(os.path.normcase('c:/wIndows\\system32\\') )

# print(os.path.normpath('c://windows\\System32\\../Temp/'))




# os路径处理
#方式一：推荐使用
import os
#具体应用
import os,sys
possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir, #上一级
    os.pardir,
    os.pardir
))
sys.path.insert(0,possible_topdir)


#方式二：不推荐使用
os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))