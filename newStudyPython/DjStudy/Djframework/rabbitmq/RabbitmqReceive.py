from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
import pika

username = 'jim'
password = 'jim'
host = '39.108.147.32'

'''
    RabbitMq接收到端
'''
class RabbitmqReceive(APIView):
    def Receive(self):
        # 定义连接池
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, credentials=credentials, port=5672
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