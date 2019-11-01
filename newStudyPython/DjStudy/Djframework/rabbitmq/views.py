from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
import pika

username = 'jim'
password = 'jim'
host = '39.108.147.32'

'''
    简单的发送消息
'''
class mqStudysend1(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self,request,*args,**kwargs):
        # 定义连接池
        credentials = pika.PlainCredentials(username,password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host,credentials=credentials,port=5672
        ))

        # 生成管道
        channel = connection.channel()
        # 创建消息队列，表明我们向消息队列为hello的发送消息，类似redis的key
        channel.queue_declare(queue='hello')
        # routing_key为刚刚的消息队列的名词，body为发送的字符串，类似向key里面塞值
        # 先把数据发给exchange交换器,exchage再发给相应队列
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body='Hello World'
        )

        print("我阿吉发送了 Hello World")
        return HttpResponse('我阿吉发送了 Hello World')

class mqreceive1(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        # 定义连接池
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, credentials=credentials, port=15672
        ))

        channel = connection.channel()
        # 接收端，也需要创建个队列
        # 无论我们先运行哪个程序，消息都不会抛弃
        channel.queue_declare(queue='hello')

        '''
            回调函数
            一条消息被一个消费者接收后，该消息就从队列删除
        '''
        def callback(ch,method,properties,body):
            print("-->ch", ch)
            print("-->method", method)
            print("-->properties", properties)
            print("[x] Received %r" % body)

        channel.basic_consume(queue='hello',
                              no_ack=True,          #no-ack ＝ False，如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。
                              on_message_callback=callback
                              )

        print('[*] Waiting for messages.To exit press CTRL+C')
        channel.start_consuming()
        return HttpResponse('我阿吉发送了 Hello World')

from rabbitmq.CeleryStudyDjango.task1 import CourseTask
'''
    celery3使用方式
'''
class celeryStudy1(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        print('start yibu111')
        # 执行异步
        CourseTask.delay()
        print('end yibu111')
        return HttpResponse(2222)

'''
    celery4使用方式
'''
from rabbitmq.CeleryStudyDjango.celery4Task.emailTask import emailTask
class celery4Study1(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        print('start yibu111')
        # 执行异步
        tid = '11'
        lang = 'zh-cn'
        sendData = 'sendData'
        r = emailTask.EmailTemplet.apply_async([tid, lang, sendData])
        # r = emailTask.EmailTemplet(self,tid, lang, sendData)
        print(r)
        print('end yibu111')
        return HttpResponse(2222)