import re
from urllib.request import urlopen
# search 从前往后，找到第一个就返回
ret = re.search('e','ead abcd')
# 调用group才能找打到结果，如果找不到会报错
if ret:
    print(ret.group())

# match从头开始匹配，如果正则规则从头开始匹配上就返回一个变量，也需要group
# 调用group才能找打到结果，如果找不到会报错
ret = re.match('e','ead abcd')
if ret:
    print(ret.group())

# findall是找所有,返回所有满足匹配条件的结果放到列表中
ret = re.findall('[a-z]+','aaafrfdddd123')
print(ret)

# split，分割,一下是通过ab分割
# 先按a分割，得到''和bcd,再对''和'bcd'分别按'b'分割，得到['','','cd']
ret = re.split('[ab]','abcd')
print(ret)

# sub替换
# 将数字替换成@
ret = re.sub('\d','@','aafdsf123fsfsf12313sfsf')
print(ret)

# subn替换并且返回替换次数
# 将数字替换成@,保存到元祖中
ret = re.subn('\d','@','aafdsf123fsfsf12313sfsf')
print(ret)

#将正则表达式编译成一个正则表达式对象，以下例子是要匹配3个数字
obj = re.compile('\d{3}')
ret = obj.search('aaad123fsff')
print(ret.group())

# finditer 返回一个存放匹配结果的迭代器,返回数据很多，节约内存用
ret = re.finditer('\d','da1dd2aa3dd1f2ff313')
for i in ret:
    #print(i.group())
    pass

# 注意点，group能根据分组取数据,第一组取数字，第二组取字母，通过（）分开
ret = re.search('([0-9]+)([a-z]+)','123456789sfsf123sff')
print(ret.group(2))

# 取消分组优先
ret = re.findall('www.(baidu|abc).com','www.abc.com')
# 因为findall会返回结果到数组里面
print(ret)

# 取消分组优先，在分组里面添加?:
ret = re.findall('www.(?:baidu|abc).com','www.abc.com')
print(ret)


# 抓取豆瓣豆瓣电影 Top 250内容
def getpage(url):
    return urlopen(url).read().decode('utf-8')

# 密码组合
# ^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$

'''
1. ```?=``` ： 询问后面跟着的东西是否等于这个    /b(?=a)/.test('bab')

2. ```?<=``` ： 询问是否以这个东西开头  /(?<=a)b/.test('ab')

3. ```?!``` : 询问后面跟着的东西是否不是这个  /b(?!a)/.test('bb')

4. ```?<!=``` ：询问是否不是以这个东西开头  /(?<!=a)b/.test('bb')
'''

def parsePage(s):
    # return re.findall('<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
    #                  '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>',s,re.S)
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+)</em>.*?<span class="title">.*?(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>\d+)人评价</span>',re.S)
    ret = com.finditer(s)
    for i in ret:
        yield {
            "id":i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
       }

def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    html = getpage(url)
    ret = parsePage(html)
    for i in ret:
        print(i)

for i in range(10):
    main(i * 25)