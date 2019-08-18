# 元字符
# \s 数字字符下划线，\d 数字 ，\s 空格符
# \S 除了数字字符下划线 \D除了数字，\S除了空格
# .任意字符，re.S ,'.'可以匹配任何字符，包含换行符
import re
# 转义问题
# print(re.findall(r'\s',r'\s'))

# 匹配<h1>jim</h1>,匹配jim出来
ret = re.search(r'<(?P<tag_name>.*?)>(?P<name>.*?)</(?P<tab_name>.*?)>','<h1>jim</h1>')
print(ret.group('name'))
print(ret.group('tag_name'))

# 匹配整数
ret = re.findall('\d+\.\d+|(\d+)','123+11.21+123-42')
print(ret)
ret.remove('')
print(ret)
