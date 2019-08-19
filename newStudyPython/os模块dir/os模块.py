import os
# 当前文件路径
print(os.getcwd())
# 改变当前工作目录
#print(os.chdir(r'/Applications/python/gitPython/newStudyPython/操作文件'))
#print(os.getcwd())
#返回当前目录
print(os.curdir)
print(os.getcwd())
#返回返回上一层目录
print(os.pardir)
print(os.getcwd())
# 创建文件夹多个
# os.makedirs('abc1/abc2')
# 删除文件夹，递归删除
#os.removedirs('abc1/abc2')
# 创建1个文件夹
#os.mkdir('abc2')
# 删除文件夹
#os.remove('abc2')
# 列出文件
#print(os.listdir(r'/Applications/python/gitPython/newStudyPython'))
# 获取文件信息
#print(os.stat('/Applications/python/gitPython/newStudyPython/os模块dir/os模块dir.py'))

#输出分隔符,python跨平台用的
print(os.sep)

# 直接在控制台执行命令没返回值
# os.system('ls -all')
# 直接在py执行命令有返回值的
ret = os.popen('ls -all').read()
print(ret)

#获取系统环境变量
print(os.environ)
# 返回路径和当前文件夹保存在元祖中
print(os.getcwd())
print(os.path.split(os.getcwd()))

# 判断目录是否存在
#os.path.exists(path)

# 判断文件是否存在
# os.path.isfile(path)

# 判断文件夹是否存在
# os.path.isdir(path)

# 如果path是绝对路径则返回True
# os.path.abspath(path)

# 拼接目录
print(os.path.join('/Applications/python/gitPython/newStudyPython/os模块dir','test.py'))

# 获取文件最后返回时间
# os.path.getatime()

# 获取文件最后修改时间
# os.path.getmtime()

# 获取文件大小
# os.path.getsize()