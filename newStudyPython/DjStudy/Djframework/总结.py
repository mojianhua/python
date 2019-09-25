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
