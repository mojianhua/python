import pika
import time

'''
    安全的RabbitMq接收到端,加入广播
'''
class RabbitmqReceive(object):
    def __init__(self,username,password,hosts,port):
        self.username = username
        self.password = password
        self.hosts = hosts
        self.port = port

    def connect(self):
        # 定义连接池
        credentials = pika.PlainCredentials(self.username,self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host= self.hosts,port=self.port, credentials=credentials,virtual_host='test1'))  # 创建连接
        # 生成管道
        self.channel = connection.channel()

    '''
        接收消息
        :param queuename key
        :param func 回调方法名
    '''
    def Receive(self, exchange, func):
        # 广播发送，exchange，指定
        self.channel.exchange_declare(exchange=exchange,exchange_type='fanout')
        # 不指定que名，rabbit随机生成名字
        result = self.channel.queue_declare('',exclusive=True)
        queue_name = result.method.queue
        # 绑定转发器
        self.channel.queue_bind(queue=queue_name,exchange=exchange)
        # 消费
        self.channel.basic_consume(queue=queue_name,
                                   # 如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。
                                   # auto_ack=True,
                                   on_message_callback=func,
                                   )
        print('[*] Waiting for messages.To exit press CTRL+C')
        # 消费队列，死循环
        self.channel.start_consuming()

'''
    回调函数
    一条消息被一个消费者接收后，该消息就从队列删除
'''

def callback(ch, method, properties, body):
    print("-->ch", ch)
    print("-->method", method)
    print("-->properties", properties)
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)#  接收到消息后会给rabbitmq发送一个确认

if __name__ == '__main__':
    import json
    RabbitmqServer = RabbitmqReceive("jim","jim","39.108.147.32","5672")
    RabbitmqServer.connect()
    RabbitmqServer.Receive("fanout",callback)