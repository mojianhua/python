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
# import xmltodict
from WxPay.common import Common

# Create your views here.
class WxPayTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def __init__(self):
        self.wxInfo ={
            'APPID':'123',
            'SECRET':'',
            'MCHID':'',
            'MCHKEY':''
        }
        self.openidUrl = 'http://wx.openidUrl.com'
        self.toOrderUrl = 'http://wx.toOrderUrl.com'

    def post(self, request, *args, **kwargs):
        # code = 123
        # # get方式请求接口，url请求地址，params传的参数，以json格式返回
        # # json格式返回结果
        # res = requests.get(
        #     url = self.openidUrl,
        #     params={
        #         'appid':self.wxInfo['APPID'],
        #         'secret': self.wxInfo['SECRET'],
        #         'js_code':code,
        #         'grant_type':'authorization_code'
        #     }
        # ).json()
        # # 获取openid，微信openi保存起来可以使用户免登陆
        # openid = res['openid']
        # print(openid)

        # 随机字符串
        nonce_str = ''.join(random.sample(string.ascii_letters + string.digits,32))


        # 订单号
        now_time = datetime.datetime.now()
        out_trade_no = str(now_time.year) + str(random.randrange(1000,9999))

        # 统一下单的参数
        params = {
            'appid': self.wxInfo['APPID'],
            'mch_id': self.wxInfo['MCHID'],
            'nonce_str':nonce_str,
            'body': '商品描述',
            'out_trade_no':out_trade_no,
            'total_fee':'1',
            'spbill_create_ip':'127.0.0.1',
            'notify_url':'http://notify_url.com',
            'trade_type':'JSAPI',
            'openid':'openid'
        }

        params['sign'] = Common.getSign(self,params)
        print(params)
        xmlmsg = Common.send_xml_request(self,self.params)
        print(xmlmsg)

        if xmlmsg['xml']['return_code'] == 'SUCCESS':
            print('支付')

        return HttpResponse('22222')
