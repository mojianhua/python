from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from alipay import AliPay,ISVAliPay
from django.conf import settings
import os
import random

'''
    支付宝接口
'''
class AliPayTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        '''
            1、1.3.0升级上来的先卸载，pycrypto
            pip uninstall pycrypto
            2、安装python-ali-sdk
            pip install python-alipay-sdk --upgrade
            3、生成私钥
            3.1、openssl
            genrsa -out app_private_key.pem 2048
            4、生成公钥
            rsa -in app_private_key.pem -pubout -out app_public_key.pem
            5、获取支付宝公钥保存到项目里面，以下例子支付宝公钥在，alipay_public_key.pem
            6、获取支付宝公钥保存到项目里面，以下例子电脑私钥是app_private_key.pem
            7、在支付宝那设置（RSA2(SHA256)密钥(推荐)）
            8、具体试用：https://github.com/fzlee/alipay/blob/master/README.zh-hans.md
        '''

        # 初始化
        alipay = AliPay(
            appid="2016082000301429",  # 应用id，由于我们是沙箱环境，所以直接拿沙箱应用下的APPID，实际开发环境根据自己实际应用ID填写
            app_notify_url=None,  # 支付宝默认回调函数，由于我们是本地项目，没有公网ip所以就算填写了，支付宝也访问不过来。
            app_private_key_path=os.path.join(settings.BASE_DIR, 'AliPayStudy/app_private_key.pem'),
            # alipay public key, do not use your own public key!
            alipay_public_key_path=os.path.join(settings.BASE_DIR, 'AliPayStudy/alipay_public_key.pem'),
            sign_type="RSA2",  # RSA or RSA2
            debug=True,  # 沙箱环境,所以需要设置为True
        )
        print(os.path.join(settings.BASE_DIR, 'AliPayStudy/alipay_public_key.pem'))
        print(os.path.join(settings.BASE_DIR, 'AliPayStudy/app_private_key.pem'))
        # 调用电脑支付接口
        # 电脑网站支付，需要跳转到: https://openapi.alipay.com/gateway.do? + order_string
        # 沙箱环境需要跳转地址为： https://openapi.alipaydev.com/gateway.do? + order_string
        total_amount = '2.02'  # Decimal类型，所以不能被序列化，所以需要转化未str
        order_string = alipay.api_alipay_trade_wap_pay(
            out_trade_no="000000004",  # 订单id
            total_amount=str(total_amount),  # 总结额：加运费
            subject='天天生鲜4',  # 标题
            return_url=None,
            notify_url=None
        )

        # 返回应答
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        print(pay_url)
        return JsonResponse({"res": 3, "pay_url": pay_url})

'''
    支付宝查看订单接口接口
'''
class AliPayCheckTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        # 初始化
        alipay = AliPay(
            appid="2016082000301429",  # 应用id，由于我们是沙箱环境，所以直接拿沙箱应用下的APPID，实际开发环境根据自己实际应用ID填写
            app_notify_url=None,  # 支付宝默认回调函数，由于我们是本地项目，没有公网ip所以就算填写了，支付宝也访问不过来。
            app_private_key_path=os.path.join(settings.BASE_DIR, 'AliPayStudy/app_private_key.pem'),
            # alipay public key, do not use your own public key!
            alipay_public_key_path=os.path.join(settings.BASE_DIR, 'AliPayStudy/alipay_public_key.pem'),
            sign_type="RSA2",  # RSA or RSA2
            debug=True,  # 沙箱环境,所以需要设置为True
        )
        # 调用支付宝查询接口
        # 订单支付查询接口                 商户订单号           支付宝交易号
        # 参数必传其一，由于是测试环境，我们就使用订单编号进行查询
        # api_alipay_trade_query(self, out_trade_no=None, trade_no=None)
        data = alipay.api_alipay_trade_query(out_trade_no="000000004")
        return JsonResponse({"res": 3, "data": data})