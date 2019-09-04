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
from django.conf.urls import url
from django.contrib import admin

# 视图
from .views import login,savelogin
# app里面的视图
from app01 import views
from BookManageAppp import views as BookManageApppview
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^savelogin/', savelogin),
    url(r'^app01login/', views.login),
    url(r'user_list/',views.user_list),
    url(r'user_add/',views.user_add),
    url(r'publisher_list/',BookManageApppview.publisher_list),
    url(r'publisher_add/',BookManageApppview.publisher_add),
    url(r'publisher_del/',BookManageApppview.publisher_del),
    url(r'publisher_update/',BookManageApppview.publisher_update),
    url(r'book_list/',BookManageApppview.book_list),
    url(r'book_add/',BookManageApppview.book_add),
    url(r'book_del/', BookManageApppview.book_del),
    url(r'book_update/', BookManageApppview.book_update),
    url(r'author_list/',BookManageApppview.author_list),
    url(r'author_add/',BookManageApppview.author_add),
    url(r'author_del/',BookManageApppview.author_del),
    url(r'template_test/',views.template_test),
    # CBV版添加出版社
    url(r'publisher_add_cbv/',BookManageApppview.CbvAddPublisher.as_view()),
]
