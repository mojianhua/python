"""Djframework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views as app01views
from api import views as apiViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # FBV方式，以function为单位
    url(r'^users/$', app01views.users),
    url(r'^usersFbv/$', app01views.usersFbv),
    # CBV方式，以class为单位
    url(r'^students/',app01views.Student.as_view()),
    url(r'^studentsCbv/',app01views.StudentCbv.as_view()),
    # framework
    url(r'^dogCbv/',app01views.DogCbv.as_view()),
    # api
    url(r'^api/v1/auth/$',apiViews.AuthView.as_view()),
    url(r'^api/v1/order/$',apiViews.OrderView.as_view()),
    url(r'^api/v1/user/$',apiViews.UserView.as_view()),
    # contenttype
    url(r'^api/v1/contenttype/$',apiViews.contenttypeView.as_view()),
    # api02路由
    url(r'^api2/',include('api02.urls')),
    # 中间件路由
    url(r'^middle/',include('middleware.urls')),
    # rabbitmq路由
    url(r'^mq/', include('rabbitmq.urls')),
    # AliOss路由
    url(r'^Alioss/', include('AliOss.urls')),
    # AliPay路由
    url(r'^AliPay/', include('AliPayStudy.urls')),
    # model文件上传路由
    url(r'^modelsUpload/', include('modelsUpload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    其中：+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    目的是能直接访问media文件夹里面的文件，访问地址为：http://127.0.0.1:8000/media/1.jpg
'''
