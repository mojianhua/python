# -*- coding: utf-8 -*-
import re
import urllib
#找到imooc字符串
def find_start_str(filename):
    f = open(filename)
    for line in f:
        #打印以immooc开头的数据
        if line.startswith('imooc'):
            print(line)
#find_start_str('/Applications/PythonStudy/imoooc.txt')

#找到以为imooc开头和结束的语句
def find_start_end_star(filename):
    f = open(filename)
    for line in f:
        #py文件每行是以\n结束
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print(line)
#find_start_end_star('/Applications/PythonStudy/imoooc.txt')

#初始化字符串
str10 = 'imooc pyton'
#定位规则，以imooc开头的字符串，用pa保存起来
pa = re.compile(r'imooc')
#利用pa规则，匹配str字符串
ma = pa.match(str10)
#保存匹配结果到ma1变量中
res = ma.group()
#print(res)

#匹配忽略大小写
str1 = 'imOoc python'
#匹配规则加上re.I,忽略大小写,r后面加上（）,返回方式以组的方式返回，打印用groups
pa1 = re.compile(r'(imooc)', re.I)
ma1 = pa1.match(str1)
res1 = ma1.groups()
#print(res1)

#直接忽略大小写
ma2 = re.match(r'imoon',str1)
res2 = ma.group()
#print(res2)

#匹配所有字符串,用'.'代表
ma3 = re.match(r'.',str1)
res3 = ma3.group()
#print(res3)

#匹配{}里面任何字符,如果一个'.'则只匹配一个字符，如果n个'.'，则匹配n个字符
ma3 = re.match(r'{.}','{a}')
#print(ma3.group())

#[..]代表字符集,下面是匹配a-zA-Z0-9的字符串，单里面也有中括号的时候，要转意
#ma4 = re.match(r'{[a-zA-Z0-9]}','{I}')
#ma4 = re.match(r'\[[\w]\]','{I}')
#\d / \D 匹配数字/非数字，\s / \S 匹配空白/非空白字符，\w / \W 匹配单词字符 /非单词字符
#print(ma4.group())

#大写字母开头，后面跟着小写字母或者没小写字母,到小写字母，*表示前一个字符0次到无限次，+表示前一个字符1次到无限次,？表示前一个字符1次到0次 ,
ma5 = re.match(r'[A-Z][a-z]*','Asss21ssss')
#print(ma5.group())

ma6 = re.match(r'[_a-zA-Z]+[\w]*','1')
#print(ma6.group())

#{}加数字表示次数，{6}表示只有6个字符，{6，10}表示匹配6到10个字符串

#匹配qq邮箱
ma7 = re.match('[0-9]+.qq.com','1123@qq.com')
#print(ma7.group())

#匹配163邮箱
ma8 = re.match('[\w]{4,10}.163.com$','safsadf@163.com')
#print(ma8.group())

#匹配以为mo开头，cn结尾的邮箱
ma9 = re.match('^mo[\w]{4}.cn','1mo1234.cn')
#print(ma9)

#\A 以为 字符串开头 ，\Z 以字符串结尾
ma10 = re.match('\Amo[\w]*.com\Z','mo13.com1')
#print(ma10)

# |表示或
ma11 = re.match('[1-9]?\d$|100','100')
#print(ma11)

#()表示分组,例子：查询163或者是126的邮箱
ma12 = re.match('[\w]{4,10}@(163|126).com','abc22@226.com')
#print(ma12)

#/表示规则别名,要加r在前头
ma13 = re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
#print(ma13)

#（？P<name>）分组起一个别名，（?P=name）引用别名为name的分组匹配字符串
ma14 = re.match(r'<(?P<test>[\w]+>)[\w]+</(?P=test)','<abc>afds</abc>')
#print(ma14)

#search,查找字符串第一次出现的数据
str2 = 'imooc videwos num = 101111100'
ma15 = re.search(r'\d+',str2)
#print(ma15.group())

#findall 找到匹配并且返回列表中
str3 = 'c++=1111,php=22222,java=55555'
ma16 = re.findall(r'\d+',str3)
#print(ma16)

#print(sum([int(n) for n in ma16]))

#sub匹配带替换,例子是查询到数字全部替换成200
str4 = 'misfsf 21'
ma17 = re.sub(r'\d+','200',str4)
#print(ma17)

def add1(match):
    val = match.group()
    num = int(val)+1
    return str(num)

# ma18 = re.sub(r'\d+',add1,str4)
# print(ma18)

#split分隔字符串
str5 = 'abc:123 0999 sfsffsf.1230?sfsf'
ma18 = re.split(r':| |\?|,',str5)
#print(ma18)
#print(1)
#抓取图片到本地，（练习）
#抓网页内容
req = urllib.urlopen('https://www.imooc.com/course/list/')
#读取内容
content = req.read()
#print(content)
#匹配规则
list = re.findall(r'src=.+?\.jpg',content)
#print(list)
#nums = 1
# for url in list:
#     f = open('/Applications/PythonStudy/'+str(nums)+'.jpg','w')
#     #print(url)
#     new_url = url.replace('src="//','http://')
#     #print(new_url)
#     req = urllib.urlopen(new_url)
#     img = req.read()
#     f.write(img)
#     nums+=1
