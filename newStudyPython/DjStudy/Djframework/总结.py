# FBV、CBV
# CBV是基于反射实现根据方式不同，执行不同的方法
# 原理
# url->view方法->dispatch方法（反射执行其他方法）
# 小知识
# 面试题，csrf token
  # 1、Django中间件最多可以写5个方法
  #  process_request
  #  process_view
  #  process_response
  #  process_exception
  #  process_render_template
  # 2、中间件做个什么
  # - 权限
  # - 用户登录
  # - csft怎么实现的，是基于
  # 使用通过process_view实现的，检查视图是否被@csrf_exempt,去请求体或cookie获取token，加入csrf_exempt不用csft验证

# 谈谈自己对restful api规范的认识
# Django声明周期，FBV：wsgi，中间件，视图。CBV走：dispatch反射，在通过中间件，在走视图，
# 包含restframework,前面没变，只是dispatch反射改变了

#安装，pip install djangorestframework

# 认证流程
# 1、先走dispatch，先对request封装，在走get_authenticators里面的authentication_classes进行验证（获取认证类，局部或者全局，通过列表生成对象）
# 2、再走get_authenticators里面的initial，走perform_authticate实现验证，request.user
# 3、到user里面的_authenticate(),最后走自定义认证类Authotication


# 认证ps
# 可以局部使用

# 内置认证
# 认证类必须继承：from rest_framework.authentication import BasicAuthentication
# 其他认证类：BasicAuthentication


# 用户认证使用流程
# 1、认证类必须继承：from rest_framework.authentication import BasicAuthentication，必须包含authenticate方法，里面写认证逻辑
# 2、返回值有3种返回值，None表示下一个认证来执行，
# 2.1、如果raise则抛出exceptions.AuthenticationFailed('用户认证失败')异常，需要导入from rest_framework import exceptions
# 2.2、正确执行（元素1，元素2），赋值给request.user,元素2返回request.auth
# 3、可以全局使用或局部使用
# 3.1、在类里面写静态字段
'''
 # # 运行首要执行的类
    # authentication_classes = [FirstAuthotication,Authotication]
    '''
#3.2可以是全局使用，在setting里面设置REST_FRAMEWORK




# -------------------------------------------------权限-----------------------------------------------------------------
# 基本使用
'''
1、使用，必须继承：BasePermission，必须实现，has_permission方法
   from rest_framework.permissions import BasePermission
   返回：True,有权访问
   返回：False,无权访问
    class SVIPPermisson(BasePermission):
        # 提示信息
        message = "必须是SVIP才能访问"
        def has_permission(self,request,view):
            if request.user.user_type == 3:
                return True
            return False
    
    局部调用：
        # # # 局部设置权限，如果写了以当前为准
    # permission_classes = [OtherPermisson,]
    全局调用：
        "DEFAULT_PERMISSION_CLASSES":['api.utils.Permission.SVIPPermisson']
'''


# --------------------------------------访问频率限制--------------------------------------------------------------------
'''
    1、基本使用，from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
        - 类，继承BaseThrottle，必须包含allow_request和wait方法
        - 类，继承SimpleRateThrottle，要有get_cache_key、里面要用scope = "JimLimit",配置setting里面的key
    使用
        - 局部： throttle_classes = [VisteThrottle,]
        - 全局：在setting.py里面配置
            # 设置全局使用访问次数
            "DEFAULT_THROTTLE_CLASSES": ['api.utils.Throttle.UserVisteThrottle'],
            # 全局使用内置访问次数限制
            "DEFAULT_THROTTLE_RATES":{
                # 一分钟访问3次，JimLimit记录的key，对应访问限制类里面的scope
                "JimLimit": '3/m',
                "JimLimitUser": '10/m'
            }
'''



#----------------版本-----------------------
'''
    总结
        使用
            配置文件
            REST_FRAMEWORK = {
                # 默认版本号
                "DEFAULT_VERSION":'v1',
                # 允许通过的版本
                "ALLOWED_VERSIONS":['v1','v2'],
                # 版本key
                "VERSION_PARAM":'version',
                # 根据urls.py控制版本
                "DEFAULT_VERSIONING_CLASS":"rest_framework.versioning.URLPathVersioning"
            }
        路由系统：
          url(r'^api2/',include('api02.urls'))
            urlpatterns = [
                url(r'^(?P<version>[v1|v2]+)/users/$',views.UsersViews.as_view())
            ]
        视图使用方式：
'''

#-----------------------------------------解析器------------------------------------------------------------------------
'''
    使用：
        全局使用："DEFAULT_PARSER_CLASS":["rest_framework.parsers.JSONParser","rest_framework.parsers.FormParser","rest_framework.parsers.MultiPartParser","rest_framework.parsers.FileUploadParser"]
        局部使用：parser_classes = [JSONParser,FormParser]
    调用
         # 获取请求请求头，获取用户请求体，根据用户的请求头和parser_classes的请求进行比较
        print(request.data)
'''


# ---------------------------------------------------序列化-------------------------------------------------------------
'''
    from rest_framework import serializers
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
        
        # 获取表里面的所有字段
        class UserInfoModelSerializer(serializers.ModelSerializer):
            # # 获取model里面的可执行的值
            user_type = serializers.CharField(source="get_user_type_display")
            # 自定义显示
            rls = serializers.SerializerMethodField()
            group = serializers.CharField(source="group.title")
            class Meta:
                model = models.UserInfo
                fields = ['id','username','password','user_type','rls','group']
        
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
'''

'''
    中间件5个固定方法
    process_request   处理请求，正序请求
    process_view      处理视图
    process_response  处理响应，倒序响应
    process_exception 处理异常
    process_template_response  处理页码
'''


#-----------------------------------------------------Django中反向生成models.py------------------------------------------------------------------#
'''
	python manage.py inspectdb > common/model/models.py
'''

