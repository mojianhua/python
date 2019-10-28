import pika

username = 'jim'
password = 'jim'
host = '39.108.147.32'

'''
    RabbitMq接收到端
'''
class RabbitmqReceive(object):
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
        接收消息
        :param queuename key
        :param func 回调方法名
    '''
    def Receive(self, queuename, func):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(on_message_callback=func,
                                   queue=queuename,
                                   # no-ack ＝ False，如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。
                                   # no_ack=True,
                                   )
        print('[*] Waiting for messages.To exit press CTRL+C')
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


if __name__ == '__main__':
    import json
    RabbitmqServer = RabbitmqReceive("jim","jim","39.108.147.32","5672")
    RabbitmqServer.connect()
    RabbitmqServer.Receive("hello",callback)