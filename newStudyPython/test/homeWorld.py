dic = {'name': 1,'id': 0,'age': 2,'phone': 3,'job': 4}
# 读取文件 ---将文件中的内容整理到内存中
def get_line(filename):
    with open(filename,encoding='utf-8') as r1:
        for line in r1:
            line = line.strip()
            lts = line.split(',')
            yield lts

# 筛选
def conditionfilter(condtion):
    '''条件筛选'''
    condtion = condtion.strip()
    if '>' in condtion:
        col,val = condtion.split('>')
        g = get_line('./test.txt')
        for line_lst in g:
            if int(line_lst[dic[col.strip()]]) > int(val):
                yield line_lst


def views(vie_list,staff):
    #print(dic[vie_list[0]])
    for staff in staff:
        #print(vie_list)
        # print(dic[vie_list[0]])
        # exit(2222)
        print(staff[dic[vie_list[0]]],staff[dic[vie_list[1]]])

# 接收用户信息 --- 分析信息，获取字段和 条件
ret = 'select name,age where age > 22'
# 根据where拆分
view,condtion = ret.split('where')
#print(view,condtion)
# 将select代替成空格，并且去掉空格
view = view.replace('select','').strip()
#print(view)
# 根据，号隔开保存查询字段,保存到列表中
view = view.split(',')
#print(view,condtion)

g = conditionfilter(condtion)
views(view,g)