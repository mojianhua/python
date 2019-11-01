'''
   1、安装celery和djcelery模块
   2、讲djcelery添加到settings的INSTALLED_APPS
   3、添加配置文件
   4、编写配置文件，如下我是在./rabbitmq/CeleryStudyDjango/Celery4config.py
   4、启动celery命令
    解释：celery -A [celery配置文件] worker -l info
    celery -A celery_tasks.main worker -l info
'''