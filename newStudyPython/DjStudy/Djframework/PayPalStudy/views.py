from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from django.conf import settings
import os
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
import paypalrestsdk
import logging

'''
    paypay支付接口
'''
class PayPalTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        '''
            1、安装步骤
            https://github.com/paypal/PayPal-Python-SDK
            2、对应中文说明
            https://www.kutu66.com//GitHub/article_102910
        '''

        # 支付配置
        paypalrestsdk.configure({
            "mode": "sandbox",  # sandbox or live
            "client_id": "ATEQmbELmKGz1SSEqdsLiDKT7hJFUEMa6bVDkeCeDTA-Clk1zkXAyRyAdg79QmiYzprlEx9l-H1AZDT5",
            "client_secret": "EJ41EU53uhly-niPE7Cb0b7WhXIk2wfzgs5A6jr0cGBtUOwf5xTmm7pj1GqmeVdaztW_yO_icjFi_Kiz"})

        # 创建付款
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:3000/payment/execute",
                "cancel_url": "http://localhost:3000/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "test1",
                        "sku": "test1",
                        "price": "99.99",
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": "99.99",
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            print("Payment created successfully")
        else:
            print(payment.error)

        # 授权付款
        for link in payment.links:
            if link.rel == "approval_url":
                # Convert to str to avoid Google App Engine Unicode issue
                # https://github.com/paypal/rest-api-sdk-python/pull/58
                approval_url = str(link.href)
                print("Redirect for approval: %s" % (approval_url))

        # 执行付款
        payment = paypalrestsdk.Payment.find("PAYID-LYR3MOY0CW8768545121633R")

        if payment.execute({"payer_id": "CNJZ7XSZ642R2"}):
            print("Payment execute successfully")
        else:
            print(payment.error)

        #取付款支付信息
        payment = paypalrestsdk.Payment.find("PAYID-LYR3MOY0CW8768545121633R")
        print(payment)

        return JsonResponse({"res": 3, "pay_url": 123})

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