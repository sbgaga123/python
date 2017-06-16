
#增
def insert_into_value():
    pass

#删
def delete_where(input_ord):
    input_list = input_ord.split()
    i_j = []
    for i in test_table:
        i_j.append(i[0])
    if input_list[1] in i_j:
        for j in test_table:
            if input_list[1] == j[0]:
                test_table.remove(j)
                print('删除成功')
            else:
                continue
    else:
        print('wrong staff_id')
#改
def update_where(input_ord):
    input_list = input_ord.split()
    if input_list[3] in test_table_list:
        j = test_table_list.index(input_list[3])
        i_j = []
        for i in test_table:
            i_j.append(i[j])
        if input_list[9] in i_j:
            for z in test_table:
                if z[j] == input_list[9]:
                    z[j] = input_list[5]
                    print('修改成功')
                else:
                    continue
        else:
            print('wrong input ,please try again!')
    else:
        print('wrong input,please try again!')
#查
def select_from_where():
    pass




#用户登陆界面
test_table_list = ['test_id','name','age','phone','dept','enroll_date']
with open('table1.txt','r') as user:
    test_table = []
    for us_line in user:
        sta_line = us_line.strip('\n').split(',')
        test_table.append(sta_line)  #staff_table 列表
def test_table_get():     #打印staff_table函数
    print('Test_TABLE'.center(60,'='))
    print('【test_id】【name】【age】【phone】【dept】【enroll_date】')
    for i in test_table:
            print(i)
while True:
    user_in  = input('sql>')
    if 'insert' in user_in:
        insert_into_value()
    elif 'delete' in user_in:
        delete_where()
    elif 'update' in user_in:
        update_where()
    elif 'select' in user_in:
        select_from_where()
    elif 'exit' == user_in:
        exit()
    else:
        print('输入内容无效，请输入sql命令：')
