from rabbitmq.CeleryStudyDjango.Celery4config import app
# 具体的可以看看Task类中的方法
class BaseTask(app.Task):
    abstract = True

    def on_retry(self, exc, task_id, args, kwargs):
        ret = {'exc':exc,'task_id':task_id,'kwargs':kwargs,'args':args}
        print(ret)

    def on_failure(self, exc, task_id, args, kwargs):
        ret = {'exc':exc,'task_id':task_id,'kwargs':kwargs,'args':args}
        print(ret)

    def on_success(self, exc, task_id, args, kwargs):
        ret = {'exc': exc, 'task_id': task_id, 'kwargs': kwargs, 'args': args}
        print(ret)
