#!/usr/bin/python
#_*_coding:utf-8_*_

import socket
import struct
import json
import subprocess
import os

class MYTCPServer:
    address_family = socket.AF_INET #ipv4套接字
    socket_type = socket.SOCK_STREAM #有保障套接字类型
    allow_reuse_address =False #允许地址再调用默认FALSE
    max_packet_size = 8192 #最大套接字长度字节
    coding='utf-8' #编码类型
    request_queue_size = 5 #请求队列长度
    server_dir = 'D:/gitfile/oldboy/day08/server/' #服务端目录

    def __init__(self,server_address,bind_and_activate=True):
        """Constructor. May be extended, do not override."""
        self.server_address=server_address #服务端地址
        self.socket = socket.socket(self.address_family,self.socket_type) #网络协议流式协议

        if bind_and_activate: #如果bind_and_activate为True
            try:
                self.server_bind() #调用server_bind()
                self.server_activate() #调用server_activate()
            except:
                self.server_close() #bind_and_activate为Flase，调用close()
                raise #抛出异常

    def server_bind(self): #定义bind函数
        """Called by constructor to bind the socket"""
        if self.allow_reuse_address: #如果地址再调用为True
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #设置可以reuser addr
        self.socket.bind(self.server_address) #设置bind方法
        self.server_address = self.socket.getsockname() #设置server_address为当前套接字地址

    def server_activate(self): #定义activate函数
        """Called by constructor to activate the server"""
        self.socket.listen(self.request_queue_size) #开启TCP监听，请求队列长度默认为5

    def server_close(self): #定义server_close函数
        """Called to clean-up the server"""
        self.socket.close() #关闭链接

    def get_request(self): #定义get_request函数
        """Get the request and client address from the socket"""
        return self.socket.accept() #返回被动接受TCP客户的链接

    def close_request(self, request): #定义request的链接关闭
        """Called to clean up an individual request."""
        request.close() #关闭request链接

    def run(self): #定义run函数
        while True:
            self.conn,self.client_addr=self.get_request() #开启TCP被动链接
            print('from client',self.client_addr) #打印客户端地址
            while True:
                try:
                    head_struct = self.conn.recv(4) #接受报头
                    if not head_struct:break

                    head_len = struct.unpack('i', head_struct)[0] #获取报头长度
                    head_json = self.conn.recv(head_len).decode(self.coding) #获取报头信息
                    head_dic = json.loads(head_json) #反序列化报头信息

                    print(head_dic) #打印报头信息
                    cmd=head_dic['cmd']
                    if hasattr(self,cmd): #判断self是否有cmd方法或属性
                        func=getattr(self,cmd) #获取self的cmd方法或属性
                        func(head_dic) #获取self的head_dic方法或属性

                except Exception:
                    break

    def put(self,args):#定义put函数
        file_path=os.path.normpath(os.path.join( #拼接文件路径
            self.server_dir,
            args['filename']
        ))

        filesize=args['filesize'] #获取文件大小
        recv_size=0 #定义空值
        print('----->',file_path) #打印文件路径
        with open(file_path,'wb') as f: #wb方式打开文件
            while recv_size < filesize:
                recv_data=self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size+=len(recv_data)
                print('recvsize:%s filesize:%s' %(recv_size,filesize))

tcpserver1=MYTCPServer(('127.0.0.1',8080))
tcpserver1.run()