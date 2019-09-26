from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# fest_framwwork序列化
from rest_framework import serializers
from rest_framework.request import Request
# from rest_framework.versioning import BaseVersioning,QueryParameterVersioning,URLPathVersioning
import json
from api02 import models

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


# ---------------------------------------------------序列化-------------------------------------------------------------
# 需要序列化的字段
class RolesSerializers(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField()


class RolesViews(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        #
        # # 基础django
        # roles = models.Role.objects.all().values('id','title')
        # roles = list(roles)
        # ret = json.dumps(roles)
        # # 中文不转行
        # # ret = json.dumps(roles,ensure_ascii=False)

        #rest_framework 里面的对[obj,obj,obj]解决序列化
        roles = models.Role.objects.all()
        # 如果多条数据就要加many=True,单条加False
        ser = RolesSerializers(instance=roles,many=True)
        # 序列化后结果,ser.data,是一个字典
        print(ser.data)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(ret)

class UserInfoSerializers(serializers.Serializer):
    # sourc代表源的意思，对应数据库的字段，abc代表别名
    abc = serializers.IntegerField(source='user_type')
    # # 获取model里面的可执行的值
    # cba = serializers.CharField(source="get_user_type_display")
    username = serializers.CharField()
    password = serializers.CharField()
    # 通过外键链表查询，一对一的查询
    gp = serializers.CharField(source="group.title")
    # 多对多的，链表查询,自定显示
    # rls = serializers.CharField(source="role.all")
    # 自定义显示
    rls = serializers.SerializerMethodField()

    # 多对多链表查询跟上面rls对应
    def get_rls(self,row):
        role_obj = row.role.all()
        ret = []
        for item in role_obj:
            ret.append({'id':item.id,'title':item.title})
        return ret

class UserInfoView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        user = models.UserInfo.objects.all()
        ser = UserInfoSerializers(instance=user,many=True)
        ret = json.dumps(ser.data,ensure_ascii=True)
        return HttpResponse(ret)

# 自定义myFiwld
class MyField(serializers.CharField):
    def to_representation(self, value):
        print(value)
        return "5555"

# 获取表里面的所有字段
class UserInfoModelSerializer(serializers.ModelSerializer):
    # # # 获取model里面的可执行的值
    # user_type = serializers.CharField(source="get_user_type_display")
    # # 自定义显示
    # rls = serializers.SerializerMethodField()
    # group = serializers.CharField(source="group.title")
    # MyField = MyField(source="username")
    class Meta:
        model = models.UserInfo
        fields = ['id','username','password','user_type','group','role']
        # fields = '__all__'
        # 自动序列化链表操作，深度层数
        depth = 0

    def get_rls(self,row):
        role_obj = row.role.all()
        ret = []
        for item in role_obj:
            ret.append({'id':item.id,'title':item.title})
        return ret

class UserInfoModelView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        user = models.UserInfo.objects.all()
        ser = UserInfoModelSerializer(instance=user,many=True)
        ret = json.dumps(ser.data,ensure_ascii=True)
        return HttpResponse(ret)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup
        field = '__all__'

class GroupView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        obj = models.UserGroup.objects.filter(pk=pk).first()
        ser = GroupSerializer(instance=obj,many=False)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(ret)


# ----------------------------------------------------验证--------------------------------------------------------------
# 自定义认证规则
class Textvalidators(object):
    def __init__(self,base):
        self.base = base

    def __call__(self, value):
        if not value.startswith(self.base):
            msssage = "标题必须以 %s 开头" % self.base
            raise serializers.ValidationError(msssage)

class UserGroupViewSerializer(serializers.Serializer):
    # error_messages错误信息，validators自定义认证规则
    title = serializers.CharField(error_messages={"required":"标题不能为空"},validators=[Textvalidators('Test')])

class UserGroupView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self,request,*args,**kwargs):
        ser = UserGroupViewSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)
        print(request.data)
        return HttpResponse('ok')