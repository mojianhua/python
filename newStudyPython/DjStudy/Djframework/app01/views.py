import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect


# FBV方式
# @csrf_protect,该函数需要用csft验证
# 此方法免除csft验证
@csrf_exempt
def users(request):
    user_list = ['Jim','Jim1']
    return HttpResponse(json.dumps(user_list))

@csrf_exempt
def usersFbv(request):
    if request.method == 'GET':
        return HttpResponse('获取订单')
    elif request.method == 'POST':
        return HttpResponse('创建订单')
    elif request.method == 'PUT':
        return HttpResponse('修改订单')
    elif request.method == 'DELETE':
        return HttpResponse('删除订单')

# CBV方式
from django.views import View

# 需要在CBV中过滤其中一个方法不使用csft,需要导入的包
from django.utils.decorators import method_decorator
class MyBaseView(object):
    # 通过dispatch方法，可以做CBV方法的前置操作
    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('end')
        return ret

# 基础基类，调用公共方法
# # 需要在CBV中过滤其中一个方法不使用csft
@method_decorator(csrf_exempt,name="dispatch")
class Student(MyBaseView,View):

    # # 需要在CBV中过滤其中一个方法不使用csft
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Student,self).dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        print('Get方法')
        return HttpResponse('GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST')

@method_decorator(csrf_exempt,name="dispatch")
class StudentCbv(View):
    def get(self, request, *args, **kwargs):
        ret = {'code':10000,'msg':'ok'}
        return HttpResponse(json.dumps(ret),status=201)

    def post(self, request, *args, **kwargs):
        return HttpResponse('新增订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('修改订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')


from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
from rest_framework.request import Request

# Djang的 rest_framework自定义认证
class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        # 获取用户名密码，去数据库校验
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ("Jim",None)

    def authenticate_header(self,val):
        pass

class DogCbv(APIView):
    authentication_classes = [MyAuthentication,]
    def get(self, request, *args, **kwargs):
        ret = {'code': 10000, 'msg': 'ok'}
        print(request)
        print(request.user)
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        return HttpResponse('新增订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('修改订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')