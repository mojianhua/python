# def 多个return,如果只有一个变量则保存到元祖上，多个变量保存则保存到不同变量上去,每个值用逗号隔开
def abc():
    return 1,[2,34,5,6]
abc1= abc()
print(abc1)

# 动态参数（带*args），不规定参数数量，以元祖保存,如果
def a(*args):
    r = 0
    for v in args:
        r = r + v
    return r

print(a(1,2,3,4,5,6))
print(a(2,3))
print(a(1,2))


# 动态参数（带*args），不规定参数数量，以元祖保存,如果关键子传参，知道数量的
def b(*args,bs):
    print(*args)
    print(bs)

b(1,2,3,4,5,6,bs = [1,2,3,4])


# 动态参数（带*args），不规定参数数量，如果关键子传参，不数量的,通过字典保存
def c(**kwargs):
    print(kwargs)

c(a = 1,b = {2,3},bs = [1,2,3,4])
c(a = 1,b = {2,3})
c(a = 1)

# 动态参数永远不会报错的方法，1、先按位置传，2、再按关键词传,注意不能传字典
def d(*args,**kwargs):
    print(args,kwargs)

d(123,12,312,31,2312,3,a = 1,b =[1,2,3],c = {1,232,3,4})

# 动态参数之传列表，当需要函数里面的参数为列表时
def e(*e1):
    print(e1)
e1 = [1,2,3,4,5,6,7]
e(*e1)

# 动态参数之传列表，当需要函数里面的参数为字典时
def f(**f1):
    print(f1)

f1 = {'a':1,'b':2}
f(**f1)

def g(g1 = []):
    g1.append(1)
    print(g1)

g()
g([])
g()
g()

# 如果默认参数的值是一个可变数据类型，如果每一次调用函数的时候，
# 如果不传值就公用这个数据类型

# globals() 打印全局变量
# locals() 在函数内能打印函数里变量，如果在函数外会打印全局变量

def max(a,b):
    # 三元运算
    return  a if a > b else b

def the_max(x,y,z):
    c = max(x,y)
    return max(c,z)

print(the_max(1,4,-1))