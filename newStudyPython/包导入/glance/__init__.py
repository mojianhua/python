# 然后在从各自包里面的__init__.py文件再导入各自的包


# 包导入使用绝对路径的分析
# 使用决定路径，不管包内还是外包外都能用
# 可不能挪动，可很直观
from glance import api
# from glance import cmd
# from glance import db

# 使用相对路径分析
# 可以移动包，只有能找到包的位置，就可以使用包的模块
# 包里的模块如果想使用模块的内容只能使用相对路基，使用了相对路径不能再包里执行
# 按照相对路径导入
# from . import api
# from . import cmd
from . import db


# from 包结合import * 结合 __all__ 使用
from .cmd import *