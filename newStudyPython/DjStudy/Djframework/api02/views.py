from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
# from rest_framework.versioning import BaseVersioning,QueryParameterVersioning,URLPathVersioning

# 获取版本类
class ParamVersion(object):
    def determine_version(self,request,*args,**kwargs):
        version = request.query_params.get('version')
        return version

# Create your views here.
class UsersViews(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    # # 通过自定义版本类，获取版本号
    # versioning_class = ParamVersion

    # 内置版本控制，结合setting.py使用
    # versioning_class = QueryParameterVersioning

    # 内置版本控制，结合路urls.py使用
    # versioning_class = URLPathVersioning
    def get(self,request,*args,**kwargs):
        # # 获取版本，通过GET
        # version = request.query_params.get('version')
        # print(version)
        print(request.version)
        return HttpResponse('ok5555')
