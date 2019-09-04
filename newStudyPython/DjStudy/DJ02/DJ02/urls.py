"""DJ02 URL Configuration

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
# 视图
from .views import login,savelogin
# app里面的视图
from app01 import views as app01views
from app01 import urls as app01urls
from BookManageAppp import views as BookManageApppview
from BookManageAppp import urls as BookManageApppurl
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^savelogin/', savelogin),
    # 导入应用BookManageApppview 的路由
    # 里面的访问方式变成/BookManageApppview/+应用路由
    #url(r'BookManageApppview',include(BookManageApppurl)),
    # 导入app01应用路由
    url(r'app01', include(app01urls)),
    # url(r'^login/', app01views.login),
    # url(r'^user_list/', app01views.user_list),
    # url(r'^user_add/', app01views.user_add),
    # url(r'^template_test/', app01views.template_test)
]
