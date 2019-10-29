import pika
import sys
import time

'''
    安全的RabbitMq服务端,加入组播
'''


class RabbitmqServer(object):

    def __init__(self, username, password, hosts, port):
        self.username = username
        self.password = password
        self.hosts = hosts
        self.port = port

    def connect(self):
        # 定义连接池
        credentials = pika.PlainCredentials(self.username, self.password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.hosts, port=self.port, credentials=credentials,
                                      virtual_host='test1'))  # 创建连接
        # 生成管道
        self.channel = self.connection.channel()

    '''
        发送消息
        :param queuename key
        :param body 消息内容
    '''
    def Message(self, exchange, routing_key, body):
        # 创建消息队列，表明我们向消息队列为hello的发送消息，类似redis的key,type类型，fanout,全民广播，direct,组播，topic,根据特征发送
        self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
        # routing_key为刚刚的消息队列的名词，body为发送的字符串，类似向key里面塞值
        # 先把数据发给exchange交换器,exchage再发给相应队列
        self.channel.basic_publish(
            exchange='direct',
            routing_key=routing_key,
            body=body,
            # 消息持久化
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        # 关闭连接
        # self.connection.close()


if __name__ == '__main__':
    import json

    RabbitmqServer = RabbitmqServer("jim", "jim", "39.108.147.32", "5672")
    RabbitmqServer.connect()
    while True:
        body = input('请输入内容')
        data = {"body": body}
        # 广播发送
        RabbitmqServer.Message("direct", 'direct_routing_key_2', json.dumps(data))