# # backend 队列
BROKER_URL = 'amqp://jim:jim@39.108.147.32:5672/test1'
# backend 队列结果
CELERY_RESULT_BACKEND = 'amqp://jim:jim@39.108.147.32:5672/test1'
# 时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# 导入任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)