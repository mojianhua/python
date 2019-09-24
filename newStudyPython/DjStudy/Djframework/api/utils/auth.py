from api import models
from rest_framework import exceptions
# 内置认证类
from rest_framework.authentication import BasicAuthentication

class FirstAuthotication(BasicAuthentication):
    def authenticate(self,request):
       pass

    def authenticate_header(self,request):
        pass

class Authotication(BasicAuthentication):

    # 认证类
    def authenticate(self,request):
        token = request._request.GET.get('token')
        print(token)
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest framework,将这两个字段赋值给request以供后续使用
        return (token_obj.user,token_obj)

    # 浏览器返回的响应头
    def authenticate_header(self,request):
        return 'Basic realm="api"'