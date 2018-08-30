# -*- coding:utf-8 -*-
import pymysql.cursors
from urllib import parse
from urllib.request import Request
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup as bs
import re

#携带头
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
req = Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
req.add_header("Origin","http://www.thsrc.com.tw")

#post提交
postData = parse.urlencode([
    ("StartStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation","a7a04c89-900b-4798-95a3-c01c455622f4"),
    ("SearchDate","2018/08/29"),
    ("SearchTime","09:30"),
    ("SearchWay","DepartureInMandarin"),
])

resp = urlopen(req,data=postData.encode('utf-8'))
print(resp.read().decode("utf-8"))