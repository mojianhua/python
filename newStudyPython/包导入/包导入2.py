# import os
# os.makedirs('./glance/api')
# os.makedirs('./glance/cmd')
# os.makedirs('./glance/db')
# l = []
# l.append(open('./glance/__init__.py','w'))
# l.append(open('./glance/api/__init__.py','w'))
# l.append(open('./glance/api/versions.py','w'))
# l.append(open('./glance/api/policy.py','w'))
# l.append(open('./glance/cmd/__init__.py','w'))
# l.append(open('./glance/cmd/manage.py','w'))
# l.append(open('./glance/db/model.py','w'))
# l.append(open('./glance/db/__init__.py','w'))
# map(lambda f:f.close,l)

# # 导入包方式1
# import glance.api.policy as policy
# policy.get()

# 因为导入包默认会执行__init__.py文件
# 所以减少导入层先在glance里面__init__.py导入一部分包
import glance
glance.api.policy.get()
from 包导入 import glance
glance.db.model.register_models('mysql')


# __all__是用于控制 from 包 import *
glance.manage.main()


