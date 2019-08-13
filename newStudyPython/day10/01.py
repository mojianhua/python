# 写个函数获取列表中获取奇数位
def a(l):
    return l[1::2]
print(a([1,2,34,5,6,7,8]))

# 判断用户传入的对象（字符串，列表，元祖）长度是否大于5
def b(d):
    print(d)
    if len(d) > 5:
        return 1
    else:
        return 0
print(b({1,2,3,4,5,6}))

# 检查列表长度，如果大于2，那么只保留前两个长度的内容，并把新内容返回调用用者
def d(d):
    return d[:2]
print(d([1]))

# 写函数，计算传入字符串中【数字】【字母】【空格】以及[其他]的个数
def e(d):
    dic = {'n':0,'z':0,'k':0,'q':0}
    for v in d:
        if v.isdigit():
            dic['n'] += 1
        elif v.isalpha():
            dic['z'] += 1
        elif v.isspace():
            dic['k'] += 1
        else:
            dic['q'] += 1
    return dic
print(e('123adc         +_)'))

# 判断字符串，列表，元素是否有空内容
def f(d):
    if type(d) is str and d:
        for v in d:
            if v == '':
                return True
    elif type(d) is list or type(d) is tuple:
        for v in d:
            if not v:
                return True
    elif not d:
        return True
print(f([]))

# 检查自定的每一个value的长度，如果大于2，那么只保存前2个长度的内容，并把内容返回调用者
def g(d):
    for v in d:
        if len(d[v]) > 2:
            d[v] = d[v][:2]
    return d
print(g({'d':'123','d1':[1,2,3,4,5]}))

# 三元运算
a = 10
b = 9
# True结果 if 条件 else False结果
c = a if a > b else b
print(c)

# 写函数，用户传入修改文件名，与修改内容，执行函数，完成整改文件的修改
def h(filename,old,new):
    with open(filename,encoding='utf-8',mode='r') as r1:
        data = []
        for l in r1:
            if old in l:
                data.append(l.replace(old,new))
            else:
                data.append(l)
    with open(filename, encoding='utf-8', mode='w') as w1:
        for lv in data:
            w1.write(lv)
h('./file.txt','123','222')