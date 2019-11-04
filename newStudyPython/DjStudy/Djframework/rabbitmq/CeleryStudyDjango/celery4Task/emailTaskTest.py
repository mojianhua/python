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

class emailTaskTest(object):
    @app.task(bind=True,ignore_result=True,name='rabbitmq.CeleryStudyDjango.celery4Task.emailTaskTest.EmailTemplet',default_retry_delay=3,queue='middle',max_retries=3,soft_time_limit = 20,base=BaseTask.BaseTask)
    def EmailTempletTest(self,tid, lang, sendData):
        try:
            print(tid)
            print(lang)
            print(sendData)
            data = {'email':'1657210793@qq.com','title':'Hi World Jim Title','content':'Hi World Jim Content'}
            return emailTaskTest.send_mail(self, data['email'], data['title'], data['content'])
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
        user = 'xxxx'
        host = 'smtp.qiye.163.com'
        port = 465
        password = 'xxxxx'
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
            emailTaskTest.send_mail_test(self, data['email'], data['title'], (str(e) + 'line：' + path))
            return (str(e))
        else:
            return 'SUCCESS'

