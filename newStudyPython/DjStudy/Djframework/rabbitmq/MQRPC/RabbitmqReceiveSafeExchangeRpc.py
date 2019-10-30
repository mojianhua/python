import pika
import time
import uuid

'''
    安全的RabbitMq接收到端,Rpc
'''
class RabbitmqReceive(object):
    def __init__(self,username,password,hosts,port):
        self.username = username
        self.password = password
        self.hosts = hosts
        self.port = port

        # 定义连接池
        credentials = pika.PlainCredentials(self.username,self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host= self.hosts,port=self.port, credentials=credentials,virtual_host='test1'))  # 创建连接
        # 生成管道
        self.channel = self.connection.channel()

        # 不指定que名，rabbit随机生成名字
        result = self.channel.queue_declare('',exclusive=True)
        self.queue_name = result.method.queue

        # 准备接收结果
        self.channel.basic_consume(queue=self.queue_name,
                                   # 如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。
                                   auto_ack=True,
                                   on_message_callback=self.on_response,
                                   )

    '''
        回调函数
    '''
    def on_response(self,ch,method,props,body):
        # props.correlation_id,服务器返回的id
        if self.corr_id == props.correlation_id:
            self.response = body

    '''
        发消息
        :param queuename key
        :param func 回调方法名
    '''
    def call(self, body):
        self.response = None
        # 唯一标识
        self.corr_id = str(uuid.uuid4())
        # 发送RPC请求内容到RPC请求队列`rpc_queue`，同时发送的还有`reply_to`和`correlation_id`
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=str(body),
            # 消息持久化
            properties=pika.BasicProperties(
                reply_to=self.queue_name,
                correlation_id=self.corr_id
            )
        )
        print('[*] Waiting for messages.To exit press CTRL+C')
        count = 0
        while self.response is None:
            # 检查队列里有没新消息,不会堵塞
            self.connection.process_data_events()
            count += 1
            print("count...",count)

        return int(self.response)

if __name__ == '__main__':
    import json
    RabbitmqServer = RabbitmqReceive("jim","jim","39.108.147.32","5672")
    response = RabbitmqServer.call(30)
    print("GO %r" % response)