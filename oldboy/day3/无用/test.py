# -*- coding:gbk -*-
#!/usr/bin/env python

s='��'
#unicode(str)-----encode---->utf-8(bytes)
#utf-8(bytes)-----decode---->unicode

s2=s.encode('utf-8')
# s.decode('utf-8') #����
# print(s)
print(s2)

# s2.encode('utf-8') #����