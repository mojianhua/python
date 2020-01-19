from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from django.conf import settings
import os
import sys
import paypalrestsdk

from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest


'''
    paypay支付接口(V1)
'''
class PayPalTest1(APIView):
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
    paypay支付接口(V2)
'''
class PayPalTest2(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        '''
            1、安装步骤
            https://github.com/paypal/Checkout-Python-SDK
            2、安装扩展
            pip install paypal-checkout-serversdk
        '''

        # 支付配置,或客户端ID和密钥
        client_id = "ATEQmbELmKGz1SSEqdsLiDKT7hJFUEMa6bVDkeCeDTA-Clk1zkXAyRyAdg79QmiYzprlEx9l-H1AZDT5"
        client_secret = "EJ41EU53uhly-niPE7Cb0b7WhXIk2wfzgs5A6jr0cGBtUOwf5xTmm7pj1GqmeVdaztW_yO_icjFi_Kiz"
        # Creating an environment
        environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        client = PayPalHttpClient(environment)

        # 创建订单
        request = OrdersCreateRequest()
        request.prefer('return=representation')
        request.request_body(
            {
                "intent": "CAPTURE",
                "application_context": {
                    "return_url": "https://www.example.com/success",
                    "cancel_url": "https://www.example.com/cancel",
                    "brand_name": "EXAMPLE INC",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": "220.00",
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "shipping_discount": {
                                    "currency_code": "USD",
                                    "value": "10"
                                }
                            }
                        },
                        "items": [
                            {
                                "name": "T-Shirt",
                                "description": "Green XL",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "90.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "quantity": "1",
                                "category": "PHYSICAL_GOODS"
                            },
                            {
                                "name": "Shoes",
                                "description": "Running, Size 10.5",
                                "sku": "sku02",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "45.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "5.00"
                                },
                                "quantity": "2",
                                "category": "PHYSICAL_GOODS"
                            }
                        ],
                        "shipping": {
                            "method": "United States Postal Service",
                            "name": {
                                "full_name": "John Doe"
                            },
                            "address": {
                                "address_line_1": "123 Townsend St",
                                "address_line_2": "Floor 6",
                                "admin_area_2": "San Francisco",
                                "admin_area_1": "CA",
                                "postal_code": "94107",
                                "country_code": "US"
                            }
                        }
                    }
                ]
            }
        )

        # try:
        #     # Call API with your client and get a response for your call
        #     response = client.execute(request)
        #     print('Order With Complete Payload:')
        #     print('Status Code:', response.status_code)
        #     print('Status:', response.result.status)
        #     print('Order ID:', response.result.id)
        #     print('Intent:', response.result.intent)
        #     print('Links:')
        #     for link in response.result.links:
        #         print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        #         print('Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,response.result.purchase_units[0].amount.value))
        #         order = response.result
        #         print(order)
        # except IOError as ioe:
        #     print(ioe)
        #     if isinstance(ioe, HttpError):
        #         # Something went wrong server-side
        #         print(ioe.status_code)
        #
        #
        # # 执行支付，翻来例子（https://www.example.com/success?token=0GY18103X3714024Y&PayerID=CNJZ7XSZ642R2），传token作为订单id,执行支付
        # request = OrdersCaptureRequest("0GY18103X3714024Y")
        # try:
        #     response = client.execute(request)
        #     order = response.result.id
        #     print(order)
        # except IOError as ioe:
        #     if isinstance(ioe, HttpError):
        #         # Something went wrong server-side
        #         print(ioe.status_code)
        #         print(ioe.headers)
        #         print(ioe)
        #     else:
        #         # Something went wrong client side
        #         print(ioe)

        return JsonResponse({"res": 3, "pay_url": 123})