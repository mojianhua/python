import pika
import sys
import time

'''
    RabbitMq服务端
'''
class RabbitmqServer(object):

    def __init__(self,username,password,hosts,port):
        self.username = username
        self.password = password
        self.hosts = hosts
        self.port = port

    def connect(self):
        print(self.username)
        print(self.password)
        # 定义连接池
        credentials = pika.PlainCredentials(self.username,self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host= self.hosts,port=self.port, credentials=credentials))  # 创建连接
        # 生成管道
        self.channel = connection.channel()

    '''
        发送消息
        :param queuename key
        :param body 消息内容
    '''
    def Message(self,queuename,body):
        # 创建消息队列，表明我们向消息队列为hello的发送消息，类似redis的key
        self.channel.queue_declare(queue=queuename)
        # routing_key为刚刚的消息队列的名词，body为发送的字符串，类似向key里面塞值
        # 先把数据发给exchange交换器,exchage再发给相应队列
        self.channel.basic_publish(
            exchange='',
            routing_key=queuename,
            body=body
        )

        print("我阿吉发送了 Hello World")
        # return HttpResponse('我阿吉发送了 Hello World')

'''
    回调函数
    一条消息被一个消费者接收后，该消息就从队列删除
'''

def callback(ch, method, properties, body):
    print("-->ch", ch)
    print("-->method", method)
    print("-->properties", properties)
    print("[x] Received %r" % body)

if __name__ == '__main__':
    import json
    RabbitmqServer = RabbitmqServer("jim","jim","39.108.147.32","5672")
    RabbitmqServer.connect()
    # data = {"code":3}
    # RabbitmqServer.Message("hello",json.dumps(data))
    body = input('请输入内容')
    print(body)
    RabbitmqServer.Message("hello",body)