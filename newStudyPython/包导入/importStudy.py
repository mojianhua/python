import demo
import sys
# 调用模块里面的方法
demo.demo1()
# 调用模块里的变量
demo.test_momny
# 先从sys.modules里面查看是否已经被导入
# 如果没有被导入，就依据sys.path路径寻找模块
# 再到导入
# 创建这模块的命名空间
# 执行文件，把文件中的名字都放到命名空间里面
print(sys.modules.keys())
print(sys.path)

# 帮模块起别名,as
import time as t
print(t.time())

# 单独引入某个模块里面的某个方法
from time import time
print(time())

from demo import demo1
demo1()


# 引入包里面的所有东西,包括方法和变量
# 如下，当调用 import * 时候会受__all__影响，如果__all__没定义会报错
from demo import *
print(test_momny)
demo1()

# import 多个模块
# import re,sys
# from demo import test1,test2
    #导入多个变量名
    # 如果本文件中项目的变量名会发生
# 如果本文件中项目的变量名会发生
# from demo import *
    #将来模块中所有的变量名都保存到内存中
    # 如果本文件中项目的变量名会发生
# from 模块名 import * 和 __all__是一对
  # 没有这个变量，就会导入所有名字
  # 如有有all只导入all列表中的名字


# 在模块中有一个变量__name__
    # 当我们执行这个模块的时候，__name__ == '__mian__'
    # 当在其他模块，引用这模块的时候会__name__会变成自己的模块名