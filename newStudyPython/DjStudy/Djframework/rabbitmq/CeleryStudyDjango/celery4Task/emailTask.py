import smtplib
from email.mime.text import MIMEText
# 邮箱配置
# from config import conf
from email.mime.multipart import MIMEMultipart
from email.header import Header
from rabbitmq.CeleryStudyDjango.Celery4config import app
import json
import time

class emailTask(object):
    @app.task(bind=True,ignore_result=True)
    def EmailTemplet(self,tid, lang, sendData):
        print(tid)
        print(lang)
        print(sendData)
        data = {'email':'1657210793@qq.com','title':'Hi World Jim Title','content':'Hi World Jim Content'}
        return emailTask.send_mail(self, data['email'], data['title'], data['content'])

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

