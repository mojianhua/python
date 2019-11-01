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
3、多个app合并到一个apps目录下
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
4、UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: illegal multibyte sequence
打开django/views下的debug.py文件，转到line331行：
　　　with Path(CURRENT_DIR, 'templates', 'technical_500.html').open() as fh:
　　将其改成：
　　　with Path(CURRENT_DIR, 'templates', 'technical_500.html').open(encoding="utf-8") as fh:
就成功了。
'''