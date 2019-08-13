# 查看源文件
# f = open('./打开文件1.txt',mode='r+',encoding='utf-8')
# for i in f:
#     print(i)

# mode换成wb的话变成bype类型写入
# open方法里面不需要添加编码，可是写的内容需要加上编码
# f = open('./打开文件1.txt',mode='wb')
# f.write('aaa啊啊啊'.encode('utf-8'))
# f.close()

# 打开文件
# f = open('打开文件1.txt',mode='r',encoding='utf-8')
# 读文件,read方法将byte --> str
# content = f.read()
# print(content)
# 关闭文件
# f.close()

# 如果非文字类打开，或者上传或下载文件打开方式
# f = open('img.png',mode='rb')
# content = f.read()
# print(content)
# f.close()

# 写文件,如果不存在的新增文件，覆盖的
# f = open('./打开文件123.txt',mode='w',encoding='utf-8')
# f.write('1111111ssss三生三世')
# f.close()

# 内容追加
# f = open('./打开文件1.txt',mode='a',encoding='utf-8')
# f.write("22222222柔柔弱弱若999999")
# f.close()

# 以byte 方式追加
# f = open('./打开文件1.txt',mode='ab')
# f.write("22222222柔柔弱弱若999999".encode('utf-8'))
# f.close()

# 先读后写文件,内容追加
# f = open('./打开文件1.txt',mode='r+',encoding='utf-8')
# print(f.read())
# f.write('gaodaddad')
# print(f.read())

# 先写后读文件,前面内容覆盖
# f = open('./打开文件1.txt',mode='r+',encoding='utf-8')
# f.write('gaodaddad')
# print(f.read())

# f.read('字符数'),按照字符数来搞读取文件字符数

# 按照光标来读如
# f.tell() 告诉你光标的位置
# f.seek('3') 从第三个字节开始读，seek是按照字节来找
# f.readable()是否可读
# f.readline() 只读一行，一行一行读取
# f.readlines() 将来个文本每行数据当成列表中的一个元素，添加到列表中
# f.truncate('截取数'),对源文件进行取，

# 查看源文件
# f = open('./打开文件1.txt',mode='r+',encoding='utf-8')
# for i in f:
#     print(i)

# 忘记close,自动关闭
# with open('./打开文件1.txt',mode='r+',encoding='utf-8') as obj,open('./打开文件123.txt',mode='r+',encoding='utf-8') as obj1:
#     obj1.read()
#     obj.read()

# 修改文件内容
lts = []
with open('./账号密码1.txt',mode='r',encoding='utf-8') as r1:
    for v in r1:
        if 'jim' in v:
            lts.append(v.replace('jim','USB'))
        else:
            lts.append(v)
    with open('./账号密码1.txt', mode='w', encoding='utf-8') as w1:
        for lv in lts:
            w1.write(lv)

# 删除文件
import os
os.remove('./账号密码1.txt')
# 重命名文件
os.rename('./就文件.txt','./新文件.txt')
