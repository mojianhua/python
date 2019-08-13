username = input('请输入用户名：')
password = input('请输入密码：')
with open('./账号密码.txt',mode='w',encoding='utf-8') as w1:
    w1.write('{}\n{}'.format(username,password))

n = 0
lis = []
while n < 3:
    usr = input('请输入登录用户名：')
    pas = input('请输入登录密码：')

    with open('./账号密码.txt','r',encoding='utf-8') as r1:
        for link in r1:
            lis.append(link)
    # str.strip能去除空格和换行符
    if lis[0].strip() == usr and lis[1].strip() == pas:
        print('登录成功')
        break
    else:print('账号密码错误')
    n = n + 1