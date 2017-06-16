import time
staff_head = ['staff_id','name','age','phone','dept','enroll_date']
with open('table1.txt','r') as user:
    staff_table = []
    for us_line in user:
        sta_line = us_line.strip('\n').split(',')
        staff_table.append(sta_line)  #staff_table 列表
def staff_table_get():     #打印staff_table函数
    print('STAFF_TABLE'.center(60,'='))
    print('\033[34;0m【staff_id】【name】【age】【phone】【dept】【enroll_date】\033[0m')
    for i in staff_table:
            print(i)
def input_get():           #input order函数
    print('ORDER'.center(60,'='))
    add_order = 'add name=\033[1;31;0mLaay\033[0m age=\033[1;31;0m18\033[0m phone=\033[1;31;0m13563630129\033[0m dept=\033[1;31;0mIT\033[0m'
    del_order = 'del \033[1;31;0m1\033[0m'
    upd_order = 'update staff_table set \033[1;31;0mdept\033[0m = Market where dept = \033[1;31;0mIT\033[0m'
    sel_order_1 = 'select \033[1;31;0mname,age\033[0m from staff_table where \033[1;31;0mage > 22\033[0m'
    sel_order_2 = 'select  \033[1;31;0m*\033[0m from staff_table where \033[1;31;0mdept = IT\033[0m'
    sel_order_3 = 'select  \033[1;31;0m*\033[0m from staff_table where \033[1;31;0menroll_date like 2013\033[0m'
    print('增加=>  ',add_order)
    print('删除=>  ',del_order)
    print('修改=>  ',upd_order)
    print('查询=>  ',sel_order_1)
    print('查询=>  ',sel_order_2)
    print('查询=>  ',sel_order_3)
    print('退出=>  ','\033[1;32;0mq\033[0m')
    print('INPUT ORDER'.center(60, '='))
    input_order = input('\033[31;0m Input your order:\033[0m' )
    return input_order
def func_sel(input_ord):  #查询函数
    input_list = input_ord.split()
    judge = ' '.join(input_list[5:])
    out_list = []
    for i in staff_table:
        staff_id = i[0]
        name = i[1]
        age = int(i[2])
        phone = int(i[3])
        dept = i[4]
        enroll_date = i[5]
        if 'like' in judge:
            if input_list[7] in i[staff_head.index(input_list[5])] and input_list[1] == '*':
                out_list.append(i)
            elif input_list[7] in i[staff_head.index(input_list[5])]  and input_list[1] != '*':
                input_list_mix = input_list[1].split(',')
                out_mix = []
                for j in input_list_mix:
                    out_mix.append(i[staff_head.index(j)])
                out_list.append(out_mix)
        elif '=' in judge:
            if input_list[7]  ==  i[staff_head.index(input_list[5])] and input_list[1] == '*':
                out_list.append(i)
            elif input_list[7]  ==  i[staff_head.index(input_list[5])]and input_list[1] != '*':
                input_list_mix = input_list[1].split(',')
                out_mix = []
                for j in input_list_mix:
                    out_mix.append(i[staff_head.index(j)])
                out_list.append(out_mix)
        else:
            if eval(judge) and input_list[1] == '*':
                out_list.append(i)
            elif eval(judge) and input_list[1] != '*':
                input_list_mix = input_list[1].split(',')
                out_mix = []
                for j in input_list_mix:
                    out_mix.append(i[staff_head.index(j)])
                out_list.append(out_mix)
    if len(out_list)>0:
        print('查询结果'.center(60,'='))
        for z in out_list:
            print('\033[36;3m%s\033[3m'%(z))
        print('共计有\033[35;3m{}\033[3m条数据'.format(len(out_list)))
    else:
        print('wrong ,please try again!')
def func_upd(input_ord): #更改函数
    input_list = input_ord.split()
    if input_list[3] in staff_head:
        j = staff_head.index(input_list[3])
        i_j = []
        for i in staff_table:
            i_j.append(i[j])
        if input_list[9] in i_j:
            for z in staff_table:
                if z[j] == input_list[9]:
                    z[j] = input_list[5]
                    print('修改成功')
                else:
                    continue
        else:
            print('wrong input ,please try again!')
    else:
        print('wrong input,please try again!')
#add name=bb age=22 phone=13563636541 dept=Sales
def func_add(input_ord): #增加函数
    input_list = input_ord.split()
    i_j = []
    for i in staff_table:
        i_j.append(i[3])
    if input_list[3].split('=')[1] not in i_j:
        staff_add = []
        # staff_add[0] = str(len(staff_table)+2)
        # staff_add[1] = input_list[1].split('=')[1]
        # staff_add[2] = str(input_list[2].split('=')[1])
        # staff_add[3] = str(input_list[3].split('=')[1])
        # staff_add[4] = input_list[4].split('=')[1]
        # staff_add[5] = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        staff_add.append(str(int(staff_table[-1][0])+1))
        staff_add.append(input_list[1].split('=')[1])
        staff_add.append(str(input_list[2].split('=')[1]))
        staff_add.append(str(input_list[3].split('=')[1]))
        staff_add.append(input_list[4].split('=')[1])
        staff_add.append(str(time.strftime('%Y-%m-%d',time.localtime(time.time()))))
        staff_table.append(staff_add)
        print('增加成功')
    else:
        print('这个号码已经在表中了')
def func_del(input_ord):
    input_list = input_ord.split()
    i_j = []
    for i in staff_table:
        i_j.append(i[0])
    if input_list[1] in i_j:
        for j in staff_table:
            if input_list[1] == j[0]:
                staff_table.remove(j)
                print('\033[34;0m删除成功\33[0m')
            else:
                continue
    else:
        print('wrong staff_id')
def judge_get():         #输入判断函数
    while 1:
        staff_table_get()
        input_order = input_get()
        if 'select' in input_order and len(input_order.split()) == 8:
            func_sel(input_order)
        elif 'update' in input_order and len(input_order.split()) == 10:
            func_upd(input_order)
        elif 'add' in input_order and len(input_order.split()) == 5:
            func_add(input_order)
        elif 'del' in input_order and len(input_order.split()) == 2:
            func_del(input_order)
        elif input_order.strip() == 'q':
            break
        else:
            print('Wrong input，please try again')
            continue
def wrt_op():
    with open('user.txt','r') as old_us , open('user_back.txt','w') as back_user:
        for l_b in old_us:
            back_user.write(l_b)
    with open('user.txt', 'w') as new_us :
        for n_b in staff_table:
            wrt = n_b[0]+','+n_b[1]+','+n_b[2]+','+n_b[3]+','+n_b[4]+','+n_b[5]+'\n'
            new_us.write(wrt)
judge_get()
wrt_op()