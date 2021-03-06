# 导入包
from __future__ import absolute_import,unicode_literals
import os
from celery import Celery,platforms
from datetime import timedelta
import djcelery
from kombu import *

# 启动配置
djcelery.setup_loader()

# 加载配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Djframework.settings")

# 实例化
app = Celery('celeryTest1',
             backend='amqp://jim:jim@39.108.147.32:5672/test1',
             broker='amqp://jim:jim@39.108.147.32:5672/test1',
             )

# root 可以启动celery
platforms.C_FORCE_ROOT = True

# 任务队列
app.autodiscover_tasks([
    'rabbitmq.CeleryStudyDjango.celery4Task.emailTask',
    'rabbitmq.CeleryStudyDjango.celery4Task.emailTaskTest'
])

# celery配置

'''
    CELERY_QUEUES说明
    django代理中设置
    Queue:管道名称
    Exchange-----
        name:基本跟Queue名称一样
        type:类型
'''

app.conf.update(
    CELERY_ACKS_LATE=True,#允许重试
    CELERY_ACCEPT_CONTENT=['pickle', 'json'],
    CELERYD_FORCE_EXECV=True,  #有些情况可以防止死锁
    CELERYD_CONCURRENCY=4,    #设置并发worker数量
    CELERYD_MAX_TASKS_PER_CHILD=500,#每个worker最多执行500个任务被销毁，可以防止内存泄漏
    BROKER_HEARTBEAT=0,#心跳
    CELERYD_TASK_TIME_LIMIT=12*30,#超时时间
    CELERY_QUEUES = (
            Queue('low', Exchange(name='low', type='direct')),
            Queue('middle', Exchange(name='middle', type='direct')),
            Queue('high', Exchange(name='high', type='direct')),
        ),
    # # 设置默认不存结果
    # CELERY_IGNORE_RESULT = True
     )