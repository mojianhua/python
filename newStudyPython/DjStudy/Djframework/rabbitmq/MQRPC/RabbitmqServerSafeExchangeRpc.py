import pika
import sys
import time

'''
    安全的RabbitMq服务端,Rpc
'''
class RabbitmqServer(object):

    def __init__(self,username,password,hosts,port):
        self.username = username
        self.password = password
        self.hosts = hosts
        self.port = port

        # 定义连接池
        credentials = pika.PlainCredentials(self.username, self.password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.hosts, port=self.port, credentials=credentials,
                                      virtual_host='test1'))  # 创建连接
        # 生成管道
        self.channel = self.connection.channel()

        # 生成quene
        self.channel.queue_declare(queue='rpc_queue')

    # 数据处理方法
    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(self,n - 1) + self.fib(self.n - 2)

    # 处理任务
    def on_request(self,ch,method,props,body):
        n = int(body)
        print(" [.] fib(%s)" % n)

        # 调用数据处理方法
        response = self.fib(self,n)

        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=response
        )
        # 确认消息
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # 负载均衡，同一时刻发送给该服务器的请求不超过一个
        self.channel.basic_qos(prefetch_count=1)

        # 执行队列
        self.channel.basic_consume(queue='rpc_queue',on_message_callback=self.on_request)

        # 开始执行
        self.channel.start_consuming()

if __name__ == '__main__':
    import json
    RabbitmqServer = RabbitmqServer("jim","jim","39.108.147.32","5672")
    print("[X] Awaiting RPC requests")
    # body = input('请输入内容')
    # data = {"body":body}
    # # 广播发送
    # RabbitmqServer.Message(body)