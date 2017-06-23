#!/usr/bin/python
#_*_coding:utf-8_*_

import time
import sys

f = sys.stdout
for i in range(1,101):
    s = ('#' * i ).ljust(100, '-')
    f.write(s)
    f.flush()
    time.sleep(0.3)
    f.write('\r')

f.write('\n')