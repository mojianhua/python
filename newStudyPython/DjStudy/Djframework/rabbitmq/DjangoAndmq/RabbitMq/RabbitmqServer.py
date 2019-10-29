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
        # 定义连接池
        credentials = pika.PlainCredentials(self.username,self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host= self.hosts,port=self.port, credentials=credentials,virtual_host='test1'))  # 创建连接
        # 生成管道
        self.channel = self.connection.channel()


    def sms(self,name,age):
        i = 4
        j = 55
        sum = i + j
        return str(sum)

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
            body=body,
            # 消息持久化
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        # 关闭连接
        self.connection.close()
        return True


# if __name__ == '__main__':
#     import json
#     RabbitmqServer = RabbitmqServer("jim","jim","39.108.147.32","5672")
#     RabbitmqServer.connect()
#     # body = input('请输入内容')
#     # data = {"body":body}
#     # RabbitmqServer.Message("safehello1",json.dumps(data))
#     body = RabbitmqServer.test('jim123','99')
#     RabbitmqServer.Message("safehello1", body)