import sys
# 查看操作系统
print(sys.platform)
# 查看当前python 版本信息
print(sys.version)
# 返回模块搜索路径
print(sys.path)
# 直接在终端中往脚本传参数
# python3 /Applications/python/gitPython/newStudyPython/sys模块/sys模块.py jim 123
ret = sys.argv
name = ret[1]   #jim
pasd = ret[2]   #123
print(name)
print(pasd)
# 退出程序,0正常退出，1不正常退出
#sys.exit()