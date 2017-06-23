#!/usr/bin/python
#_*_coding:utf-8_*_

import socket
import struct
import json
import os

class MYTCPClient:
    address_family = socket.AF_INET #定义网络协议
    socket_type = socket.SOCK_STREAM #定义流式协议
    allow_reuse_addree = False
    max_packet_size = 8192 #最大字节
    coding='utf-8' #编码
    request_queue_size=5 #队列请求长度

    def __init__(self,server_address,connect=True):
        self.server_address=server_address #服务端地址
        self.socket=socket.socket(self.address_family, #网络协议流式协议
                                  self.socket_type)

        if connect:
            try:
                self.client_connect() #开启客户端链接
            except:
                self.client_close() #关闭客户端链接
                raise #抛出异常

    def client_connect(self):   #定义客户端链接
        self.socket.connect(self.server_address) #客户端链接服务地址

    def client_close(self): #定义关闭客户端链接
        self.socket.close() #关闭链接

    def run(self):  #定义运行
        while True:
            inp=input('>>:').strip()
            if not inp:continue
            l=inp.split()
            cmd=l[0]

            if hasattr(self,cmd):   #self是否有cmd属性或者cmd方法
                func=getattr(self,cmd) #获取self的cmd属性或者方法
                func(l) #获取self的l属性或者方法
    def put(self,args): #定义推送
        cmd=args
        filename=args[1]
        if not os.path.isfile(filename): #如果filename不是一个存在的文件
            print('file:%s is not exists' %filename) #输出文件名
            return
        else: #如果filename是个存在的文件
            filesize=os.path.getsize(filename) #获取filename的大小

        head_dic={'cmd':cmd,'filename':os.path.basename(filename),'filesize':filesize} #定义报头字典
        print(head_dic) #打印报头字典
        head_json=json.dumps(head_dic) #序列化报头字典
        head_json_bytes=bytes(head_json,encoding=self.coding) #bytes序列化后的报头字典

        head_struct=struct.pack('i',len(head_json_bytes)) #用i方法struct报头长度为4字节
        self.socket.send(head_struct) #发送报头长度
        self.socket.send(head_json_bytes) #发送bytes报头
        send_size=() #定义一个空元祖
        with open(filename,'rb') as f: #rb方式打开filename
            for line in f: #循环每一行
                self.socket.send(line) #发送每一行数据
                send_size+=len(line) #将发送的每一行数据长度加到空元祖中
                print(send_size) #打印空元祖总长度
            else:
                print('upload successful') #循环结束打印上传成功

client=MYTCPClient(('127.0.0.1',8080)) #定义IP+PORT

client.run() #执行run方法
