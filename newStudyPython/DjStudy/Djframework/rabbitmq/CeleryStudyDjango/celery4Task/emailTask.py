import smtplib
from email.mime.text import MIMEText
# 邮箱配置
# from config import conf
from email.mime.multipart import MIMEMultipart
from email.header import Header
from rabbitmq.CeleryStudyDjango.Celery4config import app
import json
import time
import Djframework.settings
import os
# 导入基本Task
from rabbitmq.CeleryStudyDjango.celery4Task import BaseTask

class emailTask(object):
    '''
        异步发送邮件
        bind = True 固定的
        ignore_result 不需要返回数据
        name = 任务名称，使用模块名称作为命名空间，这样的话如果有一个同名任务函数定义在其他模块也不会产生冲突。
        max_retries = 失败重试次数
        soft_time_limit = 最大执行时间
        default_retry_delay 重试时间间隔
        exchange：Exchange是消息队列中一个核心的概念，一条消息进行消息队列后首先会进入Exchange。
        queue：Queue是Worker等待处理的任务队列。
        routing_key：routing_key决定了Exchange中的消息是如何发生给Queue的。即其决定了哪些消息插入哪个队列。
        场景：工程A利用tornado接收微信转发过来的用户信息，但信息的处理是在使用Django的工程B中。也就是说，由工程A做消息的生产者，工程B作为消息的消费者。若工程A，B的broker都是一样的，那么只需要在工程A设置一个同名的异步任务并指定exchange, routing_key即可。若broker不一致, 则先指定broker，指定exchange, 指定routing_key。原理就是，amqp协议中，只要指定了exchange和routing_key，就可以将任务分发到绑定的队列当中了。celery库做了封装，会更具queue来指定exchange和routing_key。
    '''
    @app.task(bind=True,ignore_result=True,name='rabbitmq.CeleryStudyDjango.celery4Task.emailTask.EmailTemplet',default_retry_delay=3,queue='middle',max_retries=3,soft_time_limit = 20,base=BaseTask.BaseTask)
    def EmailTemplet(self,tid, lang, sendData):
        try:
            print(tid)
            print(lang)
            print(sendData)
            data = {'email':'1657210793@qq.com','title':'Hi World Jim Title','content':'Hi World Jim Content'}
            return emailTask.send_mail(self, data['email'], data['title'], data['content'])
        except Exception as e:
            print(str(e))
        else:
            return 'SUCCESS'


    '''
        :param 发送邮件
        :param recv:邮件接收人地址，多个账号以逗号隔开
        :param title:邮件标题
        :param content:邮件内容
        :param mail_host:邮件服务器
        :param port:端口号
        :return
    '''
    def send_mail_test(self, recv, title, content):
        user = 'alert@corp.food2china.com'
        host = 'smtp.qiye.163.com'
        port = 465
        password = 'F2c_2302'
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = Header(user, 'utf-8')
        msg['To'] = Header(recv, 'utf-8')
        try:
            smtp = smtplib.SMTP_SSL(host, port=port)
            smtp.login(user, password)
            smtp.sendmail(user, [recv], msg.as_string())
        except Exception as e:
            return (str(e))
        else:
            return 'SUCCESS'

    '''
        :param 发送邮件
        :param recv:邮件接收人地址，多个账号以逗号隔开
        :param title:邮件标题
        :param content:邮件内容
        :param mail_host:邮件服务器
        :param port:端口号
        :return
    '''
    def send_mail(self, recv, title, content):
        user = 'xxxx'
        host = 'smtp.qiye.163.com'
        port = 465
        password = 'xxxxxxx'
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = Header(user, 'utf-8')
        msg['To'] = Header(recv, 'utf-8')
        try:
            smtp = smtplib.SMTP_SSL(host, port=port)
            smtp.login(user, password)
            smtp.sendmail(user, [recv], msg.as_string())
        except Exception as e:
            # 报错邮件
            data = {'email': '1657210793@qq.com', 'title': 'Hi World Jim Title', 'content': 'Hi World Jim Content'}
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            emailTask.send_mail_test(self, data['email'], data['title'], (str(e) + 'line：' + path))
            return (str(e))
        else:
            return 'SUCCESS'

