from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from api import models
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication

# Create your views here.

# md5加密
def md5(username):
    import hashlib
    import time

    ctime = str(time.time())

    m = hashlib.md5(bytes(username,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

ORDER_DICT = {
    1:{
        "name":"order1",
        "age":18,
        "gender":"nv",
        "content":'123'
    },
    2:{
        "name":"order2",
        "age":19,
        "gender":"nan",
        "content":'1233333'
    }
}

class AuthView(APIView):
    """
    用户登录认证
    """

    # 因为不需要认证，所以定义一个空的认证
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        ret = {'code':10000,'msg':None}
        username = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username,password=pwd).first()
        try:
            if not obj:
                ret['code'] = 10001
                ret['msg'] = '用户名或密码错误'

            # 为用户保存token
            token = md5(username)
            # 存在就跟新，不存在新建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
            ret['msg'] = '登录成功'

        except Exception as e:
            ret['code'] = 10002
            ret['msg'] = '系统异常'


        return JsonResponse(ret)

class OrderView(APIView):
    """
    订单
    """
    # # 运行首要执行的类
    # authentication_classes = [FirstAuthotication,Authotication]

    def get(self,request,*args,**kwargs):

        # # 获取token，未登录
        # token = request._request.GET.get('token')
        # if not token:
        #     ret = {"code": 10001, "msg": "用户未登录", 'data': None}
        #     return JsonResponse(ret)

        # 这是上面Authotication方法中raise第一个值，即token_obj.user
        one = request.user
        print(one)
        # 这是上面Authotication方法中raise第二个值，即token_obj
        two = request.auth
        print(two)
        ret = {"code":10000,"msg":None,'data':None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


    def post(self,request,*args,**kwargs):
        ret = {'code':10000,'msg':None}
        username = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username,password=pwd).first()
        try:
            if not obj:
                ret['code'] = 10001
                ret['msg'] = '用户名或密码错误'

            # 为用户保存token
            token = md5(username)
            # 存在就跟新，不存在新建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
            ret['msg'] = '登录成功'

        except Exception as e:
            ret['code'] = 10002
            ret['msg'] = '系统异常'
        return JsonResponse(ret)


class UserView(APIView):
    """
    用户
    """
    def get(self,request,*args,**kwargs):
        print(request.user)
        # # 获取token，未登录
        # token = request._request.GET.get('token')
        # if not token:
        #     ret = {"code": 10001, "msg": "用户未登录", 'data': None}
        #     return JsonResponse(ret)

        # 这是上面Authotication方法中raise第一个值，即token_obj.user
        one = request.user
        print(one)
        # 这是上面Authotication方法中raise第二个值，即token_obj
        two = request.auth
        print(two)
        ret = {"code":10000,"msg":None,'data':None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


    def post(self,request,*args,**kwargs):
        ret = {'code':10000,'msg':None}
        username = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username,password=pwd).first()
        try:
            if not obj:
                ret['code'] = 10001
                ret['msg'] = '用户名或密码错误'

            # 为用户保存token
            token = md5(username)
            # 存在就跟新，不存在新建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
            ret['msg'] = '登录成功'

        except Exception as e:
            ret['code'] = 10002
            ret['msg'] = '系统异常'
        return JsonResponse(ret)