#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,time,logging

def logging_func():
#日志配置
    BS_ATM=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BS_ATM_LOG=os.path.join(BS_ATM,'log\\atm.log')
    logging.basicConfig(filename=BS_ATM_LOG, format='%(asctime)s - %(name)s ' \
                                                    '- %(levelname)s - %(module)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %p', level=10)

logging_func()