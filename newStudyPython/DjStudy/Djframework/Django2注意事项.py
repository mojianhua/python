# 1、django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11
# 屏蔽base.py文件里面的
'''
if version < (1, 3, 3):
    raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
'''

# 2、链接数据库mysql\operations.py"报错
'''
把：
query.decode(errors='replace')
改成：
query = query.encode('utf-8').decode(errors='replace')
'''