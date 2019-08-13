# sorce = int(input("请输入分数"))
# if sorce > 90:
#     print("A")
# elif sorce > 60:
#     print("B")
# else:
#     print("DDD")

# sorce = 100000000000000
# while sorce > 0:
#     sorce = sorce - 1000000000
#     print(sorce)

# i = 0
# while i < 3:
#     name = input("请输入姓名")
#     password = int(input("请输入密码"))
#     if name == 'Jim' and password == 123:
#         print("登录成功")
#         break;
#     else:
#         print("登录失败")
#         i += 1

#格式化输出其中 %代表占位符
# name = input("请输入姓名：")
# age = int(input("请输入年龄："))
# height = int(input("请输入身高："))
# msg = "我叫 %s 今年 %s 身高 %s" %(name,age,height)
# print(msg)

# name = input("请输入姓名：")
# age  = input("请输入年龄：")
# job  = input("请输入工作：")
# hobbie = input("你的爱好：")
#
# msg = '''--------!!----------------
#     Name  : %s
#     Age   : %d
#     job   : %s
#     Hobbie: %s
# -----------------------!!----------''' %(name,int(age),job,hobbie)
# print(msg)

# while,当while没被break打断的时候执行else
# i = 0
# while i <= 5:
#     if i == 3:
#         pass
#     print(i)
#     i += 1
# else:
#     print('out')

# n = 0
# username = 'Jim'
# userpassword = '123'
# while n < 3:
#     name = input('请输入姓名：')
#     password = input('请输入密码：')
#     if name == username and password == userpassword:
#         print('登录成功')
#         break
#     else:
#         print("还剩下" + str(int(2 - n)) + '次')
#         if n == 2:
#             res = input('是否再试试？Y / N :')
#             if res == 'Y':
#                 n = 0
#                 continue
#             else:
#                 print("退出！")
#                 break
#     n += 1
# else:print("3次用晒重新输入")

# n = 1
# sum = 1
# while n < 100:
#     if n == 88:
#         n = n + 1
#         continue
#     elif n % 2 == 0:
#         sum = sum - n
#     else:
#         sum = sum + n
#     n = n + 1
# print(sum)

# n = 3
# username = 'Jim'
# password = '123'
# while n > 0:
#     name = input('请输入用户姓名：')
#     inputpassword = input('请输入密码：')
#     if name == username and inputpassword == password:
#         print('登录成功')
#         break
#     else:
#         n = n - 1
#         print('还剩下' + str(int(n)) + '次')
#         if  n == 0:
#             res = input('还要试试？Y/N ：')
#             if res == 'Y':
#                 n = 3
#                 continue
#             else:
#                 print('结束输入！')
# else:print("3次错误，退出登录！")

# 数据类型

# int
# str
# bool
# list [1,2,3]
# 元祖只读 (1,2,3)
# 字典 {'aji':[23,23],'jin2':['age':'132']}

# i = 6
# #二进制位数
# print(i.bit_length())

# s
# if s:
#     print("空")
# else:
#     pass

#字符串的索引与切片
s = 'ADFSFSFDFFSF'
# print(s[2])
##且第一到第5个
# print(s[0:4])
# print(s[-1])
# print(s[2:])
# #从第一个开始截，截到第六个，相隔1隔字符串截取[首:尾:步长]
# print(s[2:6:2])

sd = 'fsfADF'
#去大写
sd1 = sd.upper()
#全小写
sd2 = sd.lower()
#验证码不区分大小写
# s_str = 'ABC123'
# input_str = input('请输入验证码，不区分大小写！')
# if s_str.lower() == input_str.lower():
#     print('登录成功')
# else:
#     print('请重新输入！')

# 首字母大写
sd4 = sd.capitalize()
# 大小写翻转
sd5 = sd.swapcase()
# print(sd5)

# 按照特殊字符（包括空格或者特殊符号，如*）分割，首字母大写
sd_str = 'my namme abc'
# sd6 = sd_str.title()
# print(sd6)

#文本长度，和居中，并且填充
# sd7 = sd_str.center(20,'*')
# print(sd7)

#字符串长度
# l = len('啊a')
# print(l)

#是否指定字符串存在,startswith('指定字符串',起始位置,结尾位置)
# sd7 = sd_str.startswith('my123')
# print(sd7)

#find会寻找字符串，find('指定字符串','起始位置','结束位置'),找不多返回-1

# 去除左右空格字符串空格,默认删除空格，如果输入值的话，就删除指定字符串,则从前往后没被卡主的可以删除
# 删除左边空格，rstrip,右面是rstrip
a = '   adfsdd      '
# a1 = a.strip()
# print(a1)

# a1 = '%%%sff%%%**aaaaa***'
# print(a1.strip('%*'))

# 去除输入空格
# username = input('请输入名称').strip()
# if username == 'Jim':
#     print('OK')

# 统计字符串里面出现指定字符串个数
# print(a.count('d'))

# 字符串分割,默认以空格分割，如果在里面输入指定字符串，则以为指定字符串元素
# s = 'a dadfs qew asop'
# sl = s.split()
# print(sl)

# 格式化输出
# s = '我叫{},今年{},性别{}'.format('aji',23,'boy')
# print(s)

# s = '我叫{0},今年{1},性别{2},我叫{0}'.format('aji',23,'boy')
# # print(s)

# s = '我叫{name},今年{age},性别{sex},我叫{name}'.format(name='aji',age=23,sex='boy')
# print(s)

#字符串代替,replace('需要搜索的字符串','要代替的字符串',代替次数)
# s = '1321fsaf舒服法萨芬舒服舒服1321'
# s11 = s.replace('舒服','shufu')
# print(s11)

# 循环字符串
# s = '123sfsaffsfs111'
# for i in s:
#     print()

# 判断字符串是否包含222。not in，不包含
# s = 'aaabbbddd222'
# if '222' in s:
#     print('存在222')

# 取反切片
# s = 'abcdefghijk'
# s1 = s[2::-2]
# print(s1)

# 判断是否全部数字字符串组成的，isdigit() 返回bool,isalpha(),判断是否字符串和数字组成


#s = 'appleacdfd'
# for i in s:
#     print(i)

# index = 0
# while 1:
#     print(s[index])
#     index += 1
#     if index == len(s):
#         break

# content = input("请输入内容：")
# res = content.split('+')
# rnum = 0
# for num in res:
#     rnum = rnum + int(num)
# print(rnum)

# 列表
l = [1,2,3,4,5,6]
# 在列表最后增加一个元素
l.append('a')
print(l)

l1 = ['a','b','c']
# 在列表中添加一个列表进去
l.extend(l1)
print(l)

# 把 x 插入到索引值为n的地方中去，l.insert(n,x)
l.insert(2,'ooo')
l.insert(4,'ooo')
l.insert(6,'ooo')
print(l)

# 从列表中删除第一次出现的元素
l.remove('ooo')
print(l)

# 删除列表中最后一个元素,或删除指定数量的元素（从最后算起）
l.pop(2)
print(l)

#根据下标删除元素
del l[2]
print(l)

# 清空列表
l.clear()

# 字符串根据指定标识符连接连接
s = 'abcdf23'
s1 = '--'.join(s)
print(s1)

# 将列表以指定标识拼接成字符串
l = ['123','23','123','sss','3333','fffdd','111323','rrrr']
s2 = '++++'.join(l)
print(s2)
# 将字符串变成数组
s3 = s2.split('++++')
print(s3)

# range,按数字排序的列表，估头不顾尾，例如rangd(3,10),只能保存，3到9
# 能添加步长，range(0,10,2),结果0,3,5,8
# 结果什么都不输出
for i in range(0,10,-1):
    print()

# 列表排序
s3.sort()
print(s3)

# 列表里翻转排序
s3.reverse()
print(s3)

# 列表中元素出现次数
s4 = l.count('123')
print(s4)

# 元素第一次出现的位置
s5 = l.index('123')
print(s5)

# 元祖
# 只读的，儿子不能变，孙子能变
tp = (1,5,3,5,7,4,3,2,4,9,)

# 字典
die = {'name':'Jim'}
print(die)

# 如果不存在则新增
die.setdefault('age',12)
print(die)

# 按照键值删除有返回值
# die.pop('age')
# print(die)

# 按照键值删除，没返回值
del die['age']

# update,使用d2的内容更新到d的相同内容
die2 = {'name':'jim2'}
die.update(die2)
print(die)

# 查找字段中所有的值
die.values()

# 查找字典中所有的keys
die.keys()

# 字典根据key取出相应的value
die.get('name')

# 打印所有的键值对
d1 = die.items()
print(d1)
# 随机删除
die.popitem()

# 清空字典
die.clear()

li = ['手机','电脑','鼠标垫','游艇']
# 生成下标
# while 1:
#     for i, k in enumerate(li):
#         print(str(i+1),k)
#
#     pid = input('请输入商品商品id或输入Q或q退出')
#     if pid.isdigit():
#         if int(pid) > len(li) or int(pid) <= 0:
#             print('请输入有效数字！')
#         else:print(li[int(pid) - 1])
#     elif pid.upper() == 'Q':break
#     else:print('请输入数字')


# 一个等号是赋值，是同一内存地址，==是否等于，is比较内存地址，id(内容)，查看内存
# 如果
a = [1,2,3,4,5]
# b = a
# print(a)
# print(b)
# a.append(6)
# print(a)
# print(b)

# 上述本目的只想添加a列表的值，结果变成b也添加值了，解决如下
# b = a.copy()
# print(a)
# print(b)
# a.append(6)
# print(a)
# print(b)

# 小数据池，数字 -5 到 256一样的内存地址
# 字符串也有小数据池，1、不能有特殊字符；2、s*20同一地址，超过就不同内存地址
# 文件的传输不能是unicode,因为容量大
# py3的str是用unicode
s1 = 'jim'
# str 转换成 bytes,encode,编码，encode('指定编码')
s11 = s1.encode('utf-8')
print(s11)

s2 = '啊啊'
# utf8中1个中文3个字节，gbk中1个中文2个字节
# s22 = s2.encode('utf-8')
# print(s22)

# 集合是无序不重复的，如果想要将来列表去重，则将列表转换成集合，再把集合重新转换成列表达成去重
set1 = {1,2,3,4,56}

# 添加集合数据
# set1.add('Jim')
# set1.update('Jim11')
# print(set1)

# 删除集合数据
# set1.pop()    #随机删除有返回值
# set1.remove('Jim') #按元素删除
# set1.clear() # 清空元素

# 查集合
# for i in set1:
#     print(i)

# 查集合交集
set2 = {1,2}
# print(set1 & set2)
#
# print(set1.intersection(set2))

# 查集合并集
# set2 = {111111,222222}
# print(set1 | set2)
# print(set1.union(set2))

# 集合反交集
# print(set1 ^ set2)
# print(set1.symmetric_difference(s2))

# 集合差集
# print(set1 - set2)
# print(set1.difference(set2))


# 列表去重
li = [1,1,2,2,2,3,3,4,5,6,1,1,2,4]
# set1 = set(li)
# print(set1)
# li = list(set1)
# print(li)

#将来字符串变成集合,去重循环打印
# set3 = frozenset('zhuzhuyihao')
# for i in set3:
#     print(i)

lis = [11,22,33,44,55]
lis2 = []
for i in range(len(lis)):
    if i % 2 == 0:
        pass
    else:
        lis2.append(lis[0])
# print(lis2)

# 字典中不能直接删除字典
die = {'k1':'v1','k2':'v2','a3':'v3'}
# die2 = {}
# for i in die:
#     if 'k' in i:
#         pass
#     else:
#         die2.setdefault(i,die[i])
# print(die2)
# print(die)

# 能通过列表删除字典
# l = []
# for i in die:
#     if 'k' in i:
#         l.append(i)
# for j in l:
#     del die[j]
# print(die)

# li2 = []
# for i in li:
#     if i not in li2:
#         li2.append(i)
# print(li2)

# 元祖、字典，字符串，列表只有一个元素，并且没逗号则返回int类型，反之才是自身元素