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
# 1、先走dispatch，先对request封装，在走get_authenticators里面的authentication_classes进行验证
# 2、再走get_authenticators里面的initial，走perform_authticate实现验证
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