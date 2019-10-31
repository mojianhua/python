import djcelery
from datetime import timedelta
djcelery.setup_loader()

# 设置队列
CELERY_QUEUES = {
    'beat_tasks':{
        'exchange':'beat_tasks',
        'exchange_type':'direct',
        'binding_key':'beat_tasks'
    },
    'work_queue':{
        'exchange':'work_tasks',
        'exchange_type':'direct',
        'binding_key':'work_tasks'
    },
}

# 默认队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# celery运行的包
CELERY_IMPORTS = (
    'rabbitmq.CeleryStudyDjango.task1'
)

# 有些情况能防止死锁
CELERY_FORCE_EXECV = True

# 设置并发的worker数
CELERY_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 没个worker最多执行100个被销毁
CELERY_MAX_TASKS_PER_CHILD = 100

# 最多运行时间以为S为单位
CELERY_TASK_TIME_LIMIT = 12 * 30

# # 定时任务
# CELERYBEAT_SCHEDULE = {
#     'task':'course-task',
#     # 5s执行一次
#     'schedule':timedelta(seconds = 5),
#     # #参数
#     # 'args':'44'
#     # 指定队列
#     'options':{
#         'queue':'beat_tasks'
#     }
# }

CELERYBEAT_SCHEDULE = {
        'update_info': {
            'task': 'course-task',
            "schedule": timedelta(seconds=1),
        },
        # # 指定队列
        # 'options':{
        #     'queue':'beat_tasks'
        # }
}