from django.conf.urls import url,include
from django.contrib import admin
from api02 import views
urlpatterns = [
    # 版本使用
    url(r'^(?P<version>[v1|v2]+)/users/$',views.UsersViews.as_view()),
    # 解析器
    url(r'^(?P<version>[v1|v2]+)/jiexiqiusers/$',views.UsersJieXiQiViews.as_view())
]