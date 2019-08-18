import time
#time.sleep(1)  #睡眠时间以秒为单位
print(time.time())    #时间截

#格式化时间
print(time.strftime('%Y-%m-%d %a %X'))
print(time.strftime('%Y-%m-%d %H:%M:%S'))

#结构化时间
str_time = time.localtime()
print(str_time)
#获取格式化时间指定下标
print(str_time.tm_hour)

# 时间戳和结构化时间转换
t = time.time()
#通过时间戳转换结构化时间
print(time.localtime(36000000000))
print(time.localtime(t))
#查看格力位置时间
print(time.gmtime(t))

# 结构化时间转换成时间戳
print(time.mktime(time.localtime()))

# 格式化时间转换成结构化
print(time.strptime('2019-12-21 12:12:12','%Y-%m-%d %H:%M:%S'))
# 结构化时间转换成格式化
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(3088)))

print(time.asctime())
# 结构化时间格
print(time.asctime(time.localtime(3990)))
print(time.ctime())