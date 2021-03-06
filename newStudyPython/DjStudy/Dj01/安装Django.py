# 安装指定Dj版本
# pip install django==1.11.17
# Django命令
  # python3 manage.py runserver ip:端口—->指定的ip和端口运行
  # python3 manage.py runserver 端口—>指定运行端口
  # python3 manage.py runserver —>默认在本机的8000端口运行

#2.配置相关，项目名settings.py文件，
#  1、Templates,指定Django在哪里找到模板文件
#  2、静态文件
#     STATIC_URL = '/static/'
#  3、所有静态文件（css/js/图片）都放在以下配置文件夹中
#     STATICFILE_DIRS = [
#     	 os.path.join(BASE_DIR,”staticv”)
#     ]
#3.当出现403令牌报错，注释掉settings.py，46行，django.middleware.csrf.CsrfViewMiddleware',
#4.Django的app
# 4.1.1 新建项目 django-admin startproject projectName
# 4.1、新建app命令 python manage.py startapp [app名称]
# 4.2、引入app,在settings.py里面的INSTALLED_APPS新建app,如：app01.apps.App01Config
#5.ORM
# 5.1、在settings.py修改DATABASES
# 5.2、链接数据
# 'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'HOST': '192.168.118.171',
#        'PORT': 3603,
#        'NAME': 'Django',
#        'USER': 'dev',
#        'PASSWORD': '123456'
#    }
# 5.3、用pymysql包链接数据库
# 5.4、在项目的（不是应用）的__init__.py添加
#import pymysql
# 告诉Django用pymysql来代替默认的mysqldb
#pymysql.install_as_MySQLdb()
# 5.5、在app下models.py文件定义一个类，这个类不想基础models.Model
# 5.6、执行以下两个命令创建表
  # 5.6.1、python manage.py makemigrations   #检测model.py记录下来，保存到app01/makemigrations
  # 5.6.2、python manage.py migrate   #把改动翻译成sql语言到数据库执行
# 6、指定静态文件配置地址，在settings.py里面修改
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR,"static")
#]
  
# 模板语言
# 1、{{ name }} -->变量
# 2、for循环
#{% for i in book_list%}
#	{{ forloop.counter}}   计算
#   {{ forloop.last }}     当最后一个
#	{%i}
#{% endfor %}
# 3、if 判断
# {% if 10 > 5%}
# 。。。。 
# {% else %}
# 。。。
# {$ endif %}
# {% if name in name_list%}
# ......
# {% else %}
# {% if %}



# request
# 1、request.POST.get('下标',默认值) #获取post提交的值
# 2、request.get('下标',默认值) #获取get提交的值
# 3、request.method     #获取提交方式
# 4、request.path_info  #获取用户请求的路径，不包含ip和url参数

# response
# (一)from django.shortcuts import HttpResponse,render,redirect
# 1、HttpResponse        ---->返回字符串内容
# 2、render ---->返回内容
# 3、redirect --->返回重定向
# (二) from django.http import JsonResponse
# 返回json格式类型
# 1、 return JsonResponse(data)
# 2、 如果返回列表则加safe
#    return JsonResponse(data2,safe=False)

# Django连接现有mysql数据库
# 1、新建项目
# 2、新建应用
# 3、在settings.py导入应用
# 4、在__init__里面添加
# import pymysql
# pymysql.install_as_MySQLdb()
# 5、运行运行python mysite/manage.py inspectdb > mysite/myapp/models.py 目的是将旧的数据库写入到myapp的models里面













