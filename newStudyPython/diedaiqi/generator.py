# # 生成器
# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#
# # 原理就是迭代器，每个yield断点
# g = generator()
# print(g.__next__())
# print(g.__next__())
# def tail(filename):
#     f = open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             yield line.strip()
#
# g = tail('./file.txt')
# for i in g:
#     # 如果包含abc输出
#     #if 'abc' in i:
#     print('****',i)


# def func():
#     for i in range(200):a
#         yield 'func%s'%i
#
# f = func()
# print(list(f)) #列表取值
# # 分次取词
# print(f.__next__())
# print(f.__next__())
# print(f.send('abc'))  # 能获取yield并且返回指定值给yield，要先f.__next__()
# for i in f:
#     print('func',i)



# 生成器实现，有一个文件，从文件分段读取内容
# readline
# read(10) # 按字节读取
# 再读文件内容加上'***'，返回调用者
# def b(filename):
#     f = open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             yield line
#
# bs = b('./file.txt')
# for i in bs:
#     print(i)

# 移动平均值
# def avger():
#     count = 0
#     sum = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#
# avg_g = avger()
# avg_g.__next__()
# avg1 = avg_g.send(10)
# print(avg1)
# avg1 = avg_g.send(20)
# print(avg1)


# 完美移动平均值
# 装饰器
# def init(func):
#     def inner(*args,**kwargs):
#         g = func(*args,**kwargs)
#         g.__next__()
#         return g
#     return inner
#
# @init # avger2 = init(avger2) = inner
# def avger2():
#     sum = 0
#     avg = 0
#     count = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#
# avg2 = avger2()
# res2 = avg2.send(10)
# print(res2)
# res2 = avg2.send(13)
# print(res2)


def init(func):      #func = avg3()
    def inner(*args,**kwargs):
        g = func(*args,**kwargs)
        g.__next__()
        return g
    return inner


@init #avg3() = init(avg3) = inner()
def avg3():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum/count

avg_g3 = avg3()
res3 = avg_g3.send(10)
print(res3)
res3 = avg_g3.send(130)
print(res3)


# 列表推导式
res_list = ['鸡蛋%s' %i for i in range(10)]
print(res_list)

#生成器推导式
res_list2 = ('鸡蛋%s' %i for i in range(10))
for i in res_list2:
    print(i)

# 取平方生成器
res_list3 = ((i*i) for i in range(10))
# for i in res_list3:
#     print(i)
print(res_list3.__next__())
print(res_list3.__next__())
print(res_list3.__next__())


# 列表推导式
# 30以内能被30整除
res_list4 = [i for i in range(30) if i % 3 == 0]
print(res_list4)

# 30 以内能被30整除的平方
res_list5 = [i * i for  i in range(30) if i % 3 == 0]
print(res_list5)

res_list_list6 = [['Tom','bibly','Toms','bin','Tomss','binbs'],['Tom','bibly','Toms','bin','Tomss','binbs']]
res_list6 = [i2 for i in res_list_list6 for i2 in i if i2.count('b') >=2]
print(res_list6)


# 字典推导式
# 字典的值和key互换
t = {'a':10,'b':20}
t1 = {t[i] : i for i in t}
print(t1)

# 合并大小写对应的value值，将k统一成小写
t2 = {'a':1,'A':12,'b':23,'Z':3}
# 结果是{'a':1+12,'b':23,'Z':3}
t2r = {k.lower():t2.get(k.lower(),0) + t2.get(k.upper(),0) for k in t2}
print(t2r)

# t.get用法,t.get('key',默认值)
t3r = {'a':2}
print(t3r.get('a'))
print(t3r.get('v','bu'))

# 集合推导式，结果自带去重
sq = {x*x for x in {1,2,3,1}}
print(sq)

# 总结
# 迭代器和生成器
# 迭代器
# 可迭代的 包含__iner__的方法
# 迭代器 包含__iner__和__next__的方法
# 特点，节省内存空间，方便迭代器中能取一次
# 生成器----都是迭代器
# 生成器函数，含有yield关键字的函数都是生成器函数
    # 生成器函数的特点
    # 每从生成器中取一个值就会执行一段代码，遇见yield就停止，
    # 如何从生成器中取值；
    # for ：如果没用break会一直到取完
    # next：每次只取一个
    # send：不能第一个调用，取下一个值的时候给上一个位置传一个新的值
    # 数据类型强制转换：会一次性把所有数据都存到内存到
# 生成器表达式：（条件成立在生成器中的值 for in in if 条件）


# def tail(filename):
#     f = open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             yield line.strip()
#
# g = tail('./file.txt')
# for i in g:
#     # 如果包含abc输出
#     #if 'abc' in i:
#     print('****',i)

# 处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出屏幕
def check_file(filename,ami):
    with open(filename,encoding='utf-8') as f:
        for i in f:
            if ami in i:
                yield i

filename = input('请输入文件')
str = input('请输入要查找内容')
g = check_file(filename,str)
for i in g:
    print(i.strip())