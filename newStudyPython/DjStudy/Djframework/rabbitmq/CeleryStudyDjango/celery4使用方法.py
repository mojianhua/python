'''
   1、安装celery和djcelery模块,pip install django-celery
   2、讲djcelery添加到settings的INSTALLED_APPS
   3、添加配置文件
   4、编写配置文件，如下我是在./rabbitmq/CeleryStudyDjango/Celery4config.py
   4、启动celery命令
    解释：celery -A [celery配置文件] worker -l info
    celery -A celery_tasks.main worker -l info
    4.1、启动指定管道，其中以下的middle是管道名称，配置结合，rabbitmq.CeleryStudyDjango.Celery4config worker配置文件中的CELERY_QUEUES参数使用
    celery -A rabbitmq.CeleryStudyDjango.Celery4config worker -Q middle

   5、celery建议
   https://blog.csdn.net/qq_37049050/article/details/82352509
   6、celery实践
   https://blog.csdn.net/orangleliu/article/details/37967433
'''