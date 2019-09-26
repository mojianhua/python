from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from api import models
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from rest_framework.throttling import BaseThrottle
# 引入权限文件
from api.utils.Permission import SVIPPermisson
from api.utils.Permission import OtherPermisson
# 引入自定义访问限制
from api.utils.Throttle import VisteThrottle
import time
# Create your views here.

# md5加密
'''
update(arg)传入arg对象来更新hash的对象。必须注意的是，该方法只接受byte类型，否则会报错。这就是要在参数前添加b来转换类型的原因。
同时要注意，重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖。也就是说，m.update(a); m.update(b) 等价于m.update(a+b)。
hexdigest()在英语中hex有十六进制的意思，因此该方法是将hash中的数据转换成数据，其中只包含十六进制的数字。
'''
def md5(username):
    import hashlib
    import time
    ctime = str(time.time())
    #中文进行加密,要转码
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
    # 权限认证，因为不需要，所以定义为空
    permission_classes = []
    # 局部调用，自定义限制访问次数类
    throttle_classes = [VisteThrottle,]

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
    # # # 局部设置权限，如果写了以当前为准
    # permission_classes = [OtherPermisson,]

    def get(self,request,*args,**kwargs):
        # 权限的判断，因为在验证类那边已经保存
        print(request.user.user_type)
        print(request.user.username)
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