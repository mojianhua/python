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
        # # 内置获取版本，通过GET
        print(request.version)
        return HttpResponse('ok5555')



# -------------------------------解释器----------------------------------------
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser,FileUploadParser
class UsersJieXiQiViews(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    '''
    JSONParser:只能接收json发送来数据
    FormParser:能处理x-www-form-urlencoded提交的数据
    MultiPartParser:form提交的
    FileUploadParser:上传文件的
    '''
    # # 局部解析器调用方法
    # parser_classes = [JSONParser,FormParser]
    def post(self,request,*args,**kwargs):
        # 获取请求请求头，获取用户请求体，根据用户的请求头和parser_classes的请求进行比较
        print(request.data)
        return HttpResponse('ok5555')