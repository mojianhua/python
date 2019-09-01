# 安装指定Dj版本
# pip install django==1.11.17
# Django命令
  # python3 manage.py runserver ip:端口—->指定的ip和端口运行
  # python3 manage.py runserver 端口—>指定运行端口
  # python3 manage.py runserver —>默认在本机的8000端口运行

2.配置相关，项目名settings.py文件，
  1、Templates,指定Django在哪里找到模板文件
  2、静态文件
     STATIC_URL = ‘/static/’
  3、所有静态文件（css/js/图片）都放在以下配置文件夹中
     STATICFILE_DIRS = [
     	 os.path.join(BASE_DIR,”staticv”)
     ]