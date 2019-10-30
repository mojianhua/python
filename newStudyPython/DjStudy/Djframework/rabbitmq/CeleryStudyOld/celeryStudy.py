from rabbitmq.CeleryStudyOld.celery_app import task1
from rabbitmq.CeleryStudyOld.celery_app import task2

if __name__ == '__main__':
    print('start')
    result = task1.add.delay(2,8)
    result = task2.multiply.delay(2, 8)
    print('end')
    print(result)