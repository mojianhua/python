import smtplib
from email.mime.text import MIMEText
# 邮箱配置
from config import conf
from email.mime.multipart import MIMEMultipart
from email.header import Header
from rabbitmq.DjangoAndmq.RabbitMq import RabbitmqServer
import json
import time

# 发送邮件
class SendEmail(object):
    def __init__(self):
        return None

    '''
        :param 获取邮件模板
        :param tid:模板id
        :param lang:语言
        :param data:数据
        :return
        '''
    def EmailTemplet(self,tid,lang,data):
        if lang == 'zh-cn':
            emailLang = 'cn'
        else:
            emailLang = 'en'

        # 读取模板文件
        f = open(conf.__EMAIL_TEMPLATE_FILE__, mode='r', encoding='utf-8')
        content = f.read()
        f.close()
        content = json.loads(content)
        emailContent = content[str(tid)]['email_content_' + emailLang]
        for key,val in data.items():
            emailContent = emailContent.replace('%'+ key,str(val))
        content[str(tid)]['email_content_' + emailLang] = emailContent
        # return SendEmail.send_mail(self,data['email'],content[str(tid)]['email_title_' + emailLang],emailContent)

        # 放入队列
        Server = RabbitmqServer.RabbitmqServer("jim", "jim", "39.108.147.32", "5672");
        Server.connect()
        sendData = {'email':data['email'],'title':content[str(tid)]['email_title_' + emailLang],'content':emailContent}
        add = Server.Message("safehello1", json.dumps(sendData))
        print(add)
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
    def send_mail(self,recv,title,content):
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(content,'html','utf-8'))
        msg['Subject'] = Header(title,'utf-8')
        msg['From'] = Header(conf.EMAIL_USER,'utf-8')
        msg['To'] = Header(recv,'utf-8')
        try:
            smtp = smtplib.SMTP_SSL(conf.EMAIL_HOST,port=conf.EMAIL_PORT)
            smtp.login(conf.EMAIL_USER,conf.EMAIL_PASSWORD)
            smtp.sendmail(conf.EMAIL_USER,[recv],msg.as_string())
        except Exception as e:
            return (str(e))
        else:
            return 'SUCCESS'

