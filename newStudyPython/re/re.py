import re
# search 从前往后，找到第一个就返回
ret = re.search('e','ead abcd')
# 调用group才能找打到结果，如果找不到会报错
print(ret.group())