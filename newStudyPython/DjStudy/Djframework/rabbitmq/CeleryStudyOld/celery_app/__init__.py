import time
from celery import Celery

# broker消息中间件
app = Celery('demo')

# 通过实例加载配置模块
app.config_from_object('celery_app.config')