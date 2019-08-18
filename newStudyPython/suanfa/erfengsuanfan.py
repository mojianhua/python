# a 比b 大2岁
# b 比c 大2岁
# c 比d 大2岁
# d 是40 岁，求a,b,c,d
def age(x):
    if x == 4:
        return 40
    elif x > 0 and x < 4:
        return age(x+1) + 2

#print(age(2))

# 二分算法
#print(l)
def find(l,aim,start = 0,end = None):
    end = len(l) if end is None else end;
    mid_index = (end - start) // 2 + start
    if start <= end:
        if l[mid_index] < aim:
            return find(l,aim,start = mid_index + 1,end = end)
        elif l[mid_index] > aim:
            return find(l,aim,start = 0,end = mid_index - 1)
        else:
            return  mid_index
    else:
        return '找不到！！'

l = [2,3,4,5,6,7,7,8,9,11,12,14,12,15,17,21,22,23,24,25,33,32,32,41,41,42,45,47,45,51,51,55,52,53,52,55,56,57,58,60,61,62,63,64,65,66,67,68,69,79,76,88]
# 先从小到大排序
l.sort()
#print(find(l,4))

# 斐波拉西,1,1,2,3,5,8,13
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#print(fib(7))

def fib2(n,l = [0]):
    l[0] += 1
    print(l[0])
    if n == 1 or n == 2:
        l[0] -= 1
        return 1,1
    else:
        a,b  = fib2(n - 1)
        l[0] -= 1
        print(l[0])
        if l[0] == 0:
            return a+b
        return b,a+b
print(fib2(3))