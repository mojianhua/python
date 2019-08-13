import time
# 时间截
print(time.time())
# 休眠
# time.sleep(5)
print('123')

# def b():
#     time.sleep(0.01)
#     print('jim123')
#
# def a(f):
#     start = time.time()
#     f()
#     end = time.time()
#     return end - start
#
# print(a(b))

# 装饰器函数
# def timer(f):
#     def inner():
#         start = time.time()
#         ret = f()             # 被装饰器函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timer  #语法糖,@装饰器名 = func = timer(func)
# def func():
#     print('JIM123')
#     return 'Ok'
#
# #func = timer(func)
# res = func()
# print(res)

# 装饰器是对扩展是开发的，对修改是封闭的
# 语法糖

# 装饰带参数的装饰器
# def timer(f):
#     def inner(a):
#         start = time.time()
#         ret = f(a)             # 被装饰器函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timer  #语法糖,@装饰器名 = func = timer(func)
# def func(a):
#     print('JIM12333333----' + str(a))
#     return 'Ok'
#
# #func = timer(func)
# a = 1
# res = func(a)
# print(res)



# def timer(f):
#     def inner(*args,**kwargs):
#         start = time.time()
#         ret = f(*args,**kwargs)             # 被装饰器函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timer  #语法糖,@装饰器名 = func = timer(func)
# def func(a):
#     print('JIM12333333----' + str(a))
#     return 'Ok'
#
# @timer  #语法糖,@装饰器名 = func = timer(func)
# def func(a,b):
#     print('JIM12333333----' + str(a) + str(b))
#     return 'Ok'
#
# #func = timer(func)
# res = func(1,b = 123)
# print(res)

# 装饰器的固定模式
# def warpper(f):      #装饰器的名词，f是被装饰的函数
#     def inner(*args,**kwargs):
#         # 在被装饰函数之前要做的事
#         print('在被装饰函数之前要做的事')
#         ret = f(*args,**kwargs)   #被装饰函数
#         # 在被装饰函数之后要做的事
#         print('在被装饰函数之后要做的事')
#         return ret
#     return inner
#
# @ warpper       # 语法糖 func = warpper(func)
# def func(*args,**kwargs):
#     print('111111')
#     print(args)
#     print(kwargs)
#     print('jim12ddddddddddd3')
#     return 'oK1111'
#
# print(func(1,2,3,4,a = 1 ,c =1)) # 实际上是执行 inner

def wrapper(function):
    def inner(*args,**kwargs):
        print('函数调用前执行')
        ret = function(*args,**kwargs)
        print('函数调用后执行')
        return ret
    return inner

@wrapper # === function = warrper(function)
def function(*args,**kwargs):
    print('旧函数执行前执行')
    print(args)
    print(kwargs)
    print('JIM123')
    return '最后修改'

print(function(1,2,3,4,a = 1,b = 2))



# 如果想跳过装饰器，直接调用旧的function的函数，不想调用装饰器的warpper
# from functools import wraps
# def wrapper(function):
#     @wraps(function)
#     def inner(*args,**kwargs):
#         print('函数调用前执行')
#         ret = function(*args,**kwargs)
#         print('函数调用后执行')
#         return ret
#     return inner
#
# @wrapper # === function = warrper(function)
# def function(*args,**kwargs):
#     '''
#     :param args:
#     :param kwargs:
#     :return: 旧的function
#     '''
#     print('旧函数执行前执行')
#     print(args)
#     print(kwargs)
#     print('JIM123')
#     return '最后修改'
#
# print(function.__name__)   # 打印方法名
# print(function.__doc__)    # 打印函数里面的注释
# print(function(1,2,3,4,a = 1,b = 2))


#带参数装饰器,又称为带参数装饰器
from functools import wraps
STATUS = False
def timerStatus(STATUS):
    def timer(func):
        # 完美装饰器添加的
        @wraps(func)
        def inner(*args,**kwargs):
            if STATUS:
                start = time.time()
                ret = func(*args,**kwargs)
                end = time.time()
                print(end - start)
            else:
                ret = func(*args, **kwargs)
            return  ret
        return inner
    return timer

@timerStatus(STATUS)  # 1、timer = timeStatus(STATUS)；2、timer = timer(a)
def a():
    time.sleep(0.01)
    print('aaaaaaaaaaaaaaaaaaaaaaaa')

# 1、timer = timeStatus(STATUS);2、timer = timer(b)
@timerStatus(STATUS)
def b():
    time.sleep(0.01)
    print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

a()
b()