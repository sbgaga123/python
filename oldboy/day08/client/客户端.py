#!/usr/bin/python
#_*_coding:utf-8_*_

import socket
import hashlib
import os
import sys
import time

# class ProgressBar:
#     def __init__(self, count=0, total=0, width=50):
#         self.count = count
#         self.total = total
#         self.width =width
#     def move(self):
#         self.count +=1
#     def log(self,s):
#         sys.stdout.write('' * (self.width + 9)+ '\r')
#         sys.stdout.flush()
#         print(s)
#         progress = self.width * self.count / self.total
#         sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
#         sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
#         if progress == self.width:
#             sys.stdout.write('\n')
#         sys.stdout.flush()


client_dir = 'D:/gitfile/oldboy/day08/client/'
client = socket.socket()

client.connect(("127.0.0.1", 8080))

while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:
        continue
    #下载实现
    if cmd.startswith("download"):
        client.send(cmd.encode())    #客户端发送指令
        receive_file_size = client.recv(1024)
        print("server file size",receive_file_size.decode())
        client.send("准备好接收文件了".encode())   #客户端发送确认

        receive_size = 0
        file_total_size = int(receive_file_size.decode())
        filename = cmd.split()[1]
        filename_unpath=filename.split('/')
        filename_newpath=filename_unpath[-1]
        f = open(os.path.join(client_dir,filename_newpath), "wb")   #新文件，没有的话会创建
        m = hashlib.md5()       #生成md5对象

        while receive_size < file_total_size:

            if file_total_size - receive_size > 1024:  #要收不止一次
                size = 1024
            else:  #最后一次，剩多少收多少
                size = file_total_size - receive_size
                # print("最后一次收:", size)
            data = client.recv(size)

            receive_size += len(data)
            m.update(data)
            f.write(data)       #写到文件
        else:
            new_file_md5 = m.hexdigest() #根据收到文件生成的md5
            print("file recv done")
            print(receive_size, file_total_size)
            f.close()
        receive_file_md5 = client.recv(1024)
        print("server file md5:", receive_file_md5)
        print("client file md5:", new_file_md5)

# bar = ProgressBar(total=10)
# for i in range(10):
#     bar.move()
#     bar.log('aaaaaaaaa')
#     time.sleep(1)

client.close()