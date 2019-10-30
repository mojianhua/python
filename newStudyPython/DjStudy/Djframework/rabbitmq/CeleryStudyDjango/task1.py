from celery.task import Task
import time

class CourseTask(Task):

    # 任务名称
    name = 'Course-Task'

    def run(self,*args,**kwargs):
        print('start.....')
        time.sleep(10)
        print('runting.........')
        print('end.........')