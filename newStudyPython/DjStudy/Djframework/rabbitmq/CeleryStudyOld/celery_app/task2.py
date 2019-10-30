import time
from rabbitmq.CeleryStudyOld.celery_app import app

# 异步执行
@app.task
def multiply(x,y):
    time.sleep(15)
    return x * y