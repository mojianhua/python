# 作用域
print(locals()) #返回本地作用域中的所有名字
print(globals()) #返回全局作用域中的所有名字
# global 变量 # 全局变量
# nolocal 变量 # 邻近可调用变量


# 迭代器
# 迭代器.__next__() == next(迭代器)
# 迭代器 = iner(可迭代) == 迭代器.__irer__()

# dir() 查看一个变量拥有的方法

#是否函数，callable(func),如果是函数则返回True,否则是False

#print('1,2,3,4,5,6',end='结束标准',sep='分割标识',file='输出文件路径')

# 打印进度条
# progress Bar,打印进度条用
# import time
# count = '*'
# for i in range(1,1010000000000000000000000):
#     time.sleep(0.1)
#     count = count + '*'
#     if i == 100:
#         res = '\r'+str(i) + '%：' + count + '\n'
#     else:
#         res = '\r' + str(i) + '%：' + count
#     print(res,end='',flush=True)


# exec 和 eval可以执行字符串类型的代码，exec 没返回值，eval有返回值
# compile('要执行的代码','','type') type有，exec,执行流程类代码
# eval执行计算类代码，single执行交互类代码

#abs绝对值
# divmod(9,5),除法取余，用于分页
a = divmod(100,15)
print(a)

# round(3.1231323,2),取小数点后保留值
# pow幂运算用的,pow(2,3,3),2的三次方，除以三余2

# 数据类型：int,bool....
# 数据结构，list--列表，dict---元祖，tuple---字典，set---集合

# 切片
l = [1,23,4,5,6,7]
sli = slice(1,5,2)
print(l[sli])

# bytes转换成bytes类型
# 将字符串通过bytes编码从成GBK
print(bytes('你好',encoding='GBK'))
# 再用GBK解码
print(bytes('你好',encoding='GBK').decode('GBK'))

# 网络编程，只传二进制
# 照片视频也是以二进制储存
# html网页爬取到也是编码


# bytearray

# zip() 拉链
l = [1,2,3,4,5]
l1 = ['a','n','c']
for i in zip(l,l1):
    print(i)


# filter(函数,需要传的值),最后返回True的值
# filter执行了filter之后的结果集合《=执行之前的个数
# filter只管筛选，不会改变原来的值
def is_str(s):
    if type(s) is str:
        return True

ret = filter(is_str,[1,2,3,'aa',0,'dd'])
for i in ret:
    print(i)

# map(自定义函数，数据)
# 逐个循环数据放入函数里面执行
def is_abs(s):
    return abs(s)

ret = map(is_abs,[1,-1,2,-2])
for i in ret:
    print(i)

#排序
l = [1,-2,-30,34,2]
l.sort(key=abs)
print(l)

# sorted() 也是排序可原列表不改变，可会占内存
print(sorted(l,key=abs,reverse=False))
print(sorted(l,reverse=True))    # desc排序
print(sorted(l,reverse=False))    # asc排序
print(l)



# 匿名函数lambda 接收值:返回值
# 下列输出结果
d = lambda p:p*2
t = lambda p:p*3
x = 2
x = d(x)
print(x)
x = t(x)
print(x)
x = d(x)
print(x)

# 两个元祖(('a'),('b'),('b'),('d')),利用匿名函数生成列表[('a':'c'),('b':'d')]
ret = zip((('a'),('b')),(('b'),('d')))
# def func2(tup):
#     return {tup[0]:tup[1]}
res = map(lambda tup:{tup[0]:tup[1]},ret)
# 强制将字典转成list
print(list(res))



# 内置函数55个
# 带key的 max , min, filter,map,sorted
# 匿名函数
# lambda 参数1,参数2 : 返回表达，可迭代


# 下列列表通过内置函数添加_abc
name = ['anc','sss']
def func2(s):
    return s+'_abc'
ret = map(func2,name)
print(list(ret))


# 用filter函数处理数字列表，将来偶数赛选出来
num = [1,2,3,4,5,6,7]
def fun3(x):
    if x % 2 == 0:
        return True
ret = filter(fun3,num)
print(list(ret))

# 匿名函数
ret = filter(lambda x:x%2 == 0 ,num)
print(list(ret))

# 每页显示2条数据
with open('./file.txt',encoding='utf-8') as r1:
    l = r1.readlines()

# page_num  = int(input('请输入页码'))
# pages,mod = divmod(len(l),3)        #求多少页，页数加一
# if mod:
#     pages += 1                      #一共有多少页
# if page_num > pages or pages <= 0:
#     print('输入有错误')
# elif page_num == pages and mod !=0:   #如果是最后一页，且之前有过剩余的行数
#     print(l[3*(page_num-1):])
#     #print(3*(page_num-1))
# else:
#     print(l[(3 * (page_num - 1)):((page_num * 3))])
#
#
# # 字典name对应股票名，shares代表股数目，price代表单价，计算总价
# pro = [
#     {'name':'IBM','shares':100,'price':91},
#     {'name':'IBM2','shares':101,'price':111},
#     {'name': 'IBM3', 'shares': 1111, 'price': 11111},
# ]
#
# # round 保留两个小数
# ret = map(lambda dit:{dit['name']:round(dit['shares'] * dit['price'],2)},pro)
# print(list(ret))
#
# # file 获取大于100的单价股票数
# ret = filter(lambda dit:dit['price'] > 100,pro)
# print(list(ret))

from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    # @property 把一个方法伪装成一个属性，不能传任何参数
    @property
    def perimeter(self):
        return 2*pi*self.r

    # @property 把一个方法伪装成一个属性，不能传任何参数
    @property
    def area(self):
        return self.r**2*pi

c1 = Circle(9)
print(c1.area)
print(c1.perimeter)

class Goods:
    __discount = 0.8
    def __init__(self,name,price):
        self.name = name
        self.__price = price


    # 将一个'类中的方法'变成一个属性调用
    @property
    def price(self):
        return self.__price * Goods.__discount

    # 将一个'类中的方法'变成一个属性的方式修改
    # 其中@price.setter 里面的 @price是可以修改的。对应下面要调用的下面price方法
    @price.setter
    def price(self,newPrice):
        self.__price = newPrice

    # 将一个'类中的方法'变成一个属性的方式删除
    # 其中@price.setter 里面的 @price是可以修改的。对应下面要调用的下面price方法
    # @price.deleter
    # def name(self):
    #     del self.name

    # 把一个方法变成一个类中方法，这个方法可以直接调用，不需要依托任何对象
    @classmethod
    def change_discount(cls,new_discount):
        cls.__discount = new_discount

    #静态方法
    @staticmethod
    def goods_desc():
        goods_name = input('请输入产品名称')
        goods_price = input('请输入产品价格')
        Goods(goods_name,goods_price)


apple = Goods('苹果',5)
# 将一个'类中的方法'变成一个属性调用
print(apple.price)
# 将一个'类中的方法'变成一个属性的方式修改
apple.price = 9
print(apple.price)
# 将一个'类中的方法'变成一个属性的方式删除
# del apple.price
# print(apple.price)

# 直接调用change_discount
Goods.change_discount(0.1)
print(apple.price)

# Goods.goods_desc()
