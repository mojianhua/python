from rest_framework.views import APIView
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import requests
import hashlib
import time
import datetime
import random
import string
import xmltodict

class Common(object):

    # 生成签名方法
    def getSign(self,params):
        # 签名
        stringA = ''
        ks = sorted(params.keys())
        # 参数排序
        for k in ks:
            stringA += (k + '=' + params[k] + '&')

        # 拼接商户KEY
        stringSignTemp = stringA + "key=" + self.wxInfo['MCHKEY']
        # md5 加密
        hash_md5 = hashlib.md5(stringSignTemp.encode('utf-8'))
        return hash_md5.hexdigest().upper()

    # 发送xml请求
    def send_xml_request(self,url,params):
        params = {'xml':params}
        # xml转成字典
        xml = xmltodict.unparse(params)
        # post请求，data，数据，headers 请求头
        response = requests.post(url = url,data=xml.encode('UTF8'),headers={
            'Content-Type':'chareset=utf-8'
        })
        msg = response.text
        return xmltodict.parse(msg)
