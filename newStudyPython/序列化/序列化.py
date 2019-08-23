import json
dic = {'k1':'vi'}
# 序列化
str_d = json.dumps(dic)
print(str_d)
# json.dumps参数
data = {'username':['jim111','jim222'],'sex':'male','age':16}
# sort_keys 字典键盘值按照从小到大排序
# indext字典每个键值缩进排序
# separators 分割符
json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=True)
print(json_dic2)
#反序列化
dic_d = json.loads(str_d)
print(dic_d)

# 将数据以为json格式写入文件
dic = {"国家":"中国",'1':1}
# 这是json格式写入
f = open('./file1.txt','w',encoding='utf-8')
json.dump(dic,f)
f.close()
# json格式取回数据
f = open('./file1.txt',encoding='utf-8')
res = json.load(f)
f.close()
print(res)

# 防止中文写入变成ascii,所以屏蔽ascii写入方法
dic = {'国家':'中国11','1':2}
f = open('./file2.txt','w',encoding='utf-8')
json.dump(dic,f,ensure_ascii=False)
f.close()
f = open('./file2.txt',encoding='utf-8')
res = json.load(f)
f.close()
print(res)

# json多行文件写入和读取
# 写入
f = open('./file3.txt','w',encoding='utf-8')
dit = [{"lang1":"python"},{"lang2":'php'},{'lang3':'shell'}]
for i in dit:
    str = json.dumps(i)
    f.write(str + '\n')
f.close()

# 读取
f = open('./file3.txt',encoding='utf-8')
l = []
for i in f:
    l.append(json.loads(i.strip()))
f.close()
print(l)


# pickle
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
# 序列化
str_dic = pickle.dumps(dic)
print(str_dic)
# 反序列化
dic2 = pickle.loads(str_dic)
print(dic2)

import time
str_time = time.localtime(100000000)
print(str_time)
#支持多行文件写入和读取
str_time2 = time.localtime(200000000)
print(str_time2)
# 按pickle_file写入文件
f = open('./pickle_file','wb')
pickle.dump(str_time,f)
pickle.dump(str_time2,f)
f.close()
# 按pickle_file读取文件
f = open('./pickle_file','rb')
res = pickle.load(f)
print(res.tm_year)
res2 = pickle.load(f)
print(res2.tm_year)
f.close()


# shelve
import shelve
f1 = shelve.open('./shelve')
# 写入
f1['key1'] = {'int':10,'float':9.4,'string':'aa到底'}
f.close()

# 读取
f1 = shelve.open('./shelve')
res = f1['key1']
f1.close()
print(res)

# 添加值
f2 = shelve.open('./shelve',writeback=True)
f2['key1']['newkeyval'] = 'afsadf佛挡杀佛三123'
f2.close()

f1 = shelve.open('./shelve')
res = f1['key1']
f1.close()
print(res)
