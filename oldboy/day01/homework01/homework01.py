
# 作业：
#     1. 基于文件存储的用户登录程序（3次登录失败，锁定用户）
#         先补充示例

#思路
#两个文件分别存放正常用户和被锁定用户
#用户登录先遍历被锁定用户名单，有就提示锁定，并退出
#没有被锁定继续遍历正常用户名单，先找是否存在用户，不存在提示用户不存在，并退出
#用户存在且没被锁定，循环密码，输入正确，提示登陆成功，输入错误重新输入，错误达到三次锁定
#被锁定用户写入被锁定用户名单，并从正常用户名单删除

#代码实现
import sys
count = 0
name_list = []
while count < 3:
    name = input("请输入用户名：")
    lock_file = open('name_pwd_lock.txt','r+')
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        lock_line = lock_line.strip('\n')
        if name == lock_line:
            sys.exit('用户 %s 已经被锁定,请联系管理员解锁.' %  name)
    user_file = open('name_pwd.txt','r')
    user_list = user_file.readlines()
    for user_line in user_list:
        (user,password) = user_line.strip('\n').split('|')
        name_list.append(user_line)
        if name == user:
            i = 0
            while i < 3:
                passwd = input('请输入密码：')
                if passwd == password:
                    print('欢迎 %s 登录' % name)
                    sys.exit()
                else:
                    if i < 2:
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会.' % (name,2 - i))
                i += 1
            else:
                lock_file.write(name + '\n')
                sys.exit('用户 %s 输错密码三次，用户将被锁定并退出，请联系管理员解锁.' % name)
        else:
            pass
    else:
        if count < 2:
            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (name,2 - count))
    count += 1
else:
    sys.exit('用户 %s 不存在，退出' % name)

lock_file.close()
user_file.close()