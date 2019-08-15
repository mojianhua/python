# 第n个斐波那契数列
# 1,1,2,3,5,8

def fib(key):
    if key == 1 or key == 0:
        return 1
    return fib(key - 1) + fib(key - 2)