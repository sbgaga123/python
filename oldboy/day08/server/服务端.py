#!/usr/bin/python
#_*_coding:utf-8_*_

import socket,struct,json
import subprocess

FTP=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #指定网络套接字，指定流式协议
FTP.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

FTP.bind(('127.0.0.1',8080)) #绑定IP，端口

FTP.listen(5) #tcp半连接池挂起

while True:
    conn,addr=FTP.accept() #conn三次握手链接，addr客户端地址
    while True:
        filedetails=conn.recv(4)
        if not filedetails:break
        x=struct.unpack('i',filedetails)[0]
        head_bytes=conn.recv(x)
        print(head_bytes.decode('utf-8'))
        # print(filedetails.decode('utf-8'))
        # res=subprocess.Popen(filedetails.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # err=res.stderr.read()
        # print(err)
        # if err:
        #     back_msg=err
        #     print(back_msg)
        # else:
        #     back_msg=res.stdout.read()
        #     print(back_msg)



conn.close()