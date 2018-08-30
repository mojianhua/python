# encoding: utf-8
import pymysql.cursors
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup as bs
import re
# ssl._create_default_https_context = ssl._create_unverified_context
# resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
# soup = bs(resp,"html.parser")
# listUrls = soup.findAll("a",href=re.compile(r"/wiki/"))
# for url in listUrls:
#     if not re.search("\.(jpg|JPG)",url["href"]):
#         print(url.get_text(),"<--------->",url["href"])
#         conn = pymysql.connect(host='localhost',
#                                user='root',
#                                password='',
#                                db='python',
#                                charset='utf8')
#         try:
#             with conn.cursor() as cursor:
#                 sql = "insert into `wiki`(`title`,`url`) values (%s,%s)"
#                 cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))
#                 conn.commit()
#         finally:
#             conn.close()

#查询
# conn = pymysql.connect(host='localhost',
#                                user='root',
#                                password='',
#                                db='python',
#                                charset='utf8')
#
# try:
#     #会话指针
#     with conn.cursor() as cursor:
#         sql = "select * from wiki"
#         #执行sql
#         count = cursor.execute(sql)
#         #result = cursor.fetchall()
#         fetchmany = cursor.fetchmany(3)
#         print(fetchmany)
#         # print(result)
#         # print(count)
# finally:
#     conn.close()

# print(soup)