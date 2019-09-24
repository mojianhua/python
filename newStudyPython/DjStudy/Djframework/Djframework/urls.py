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
from django.conf.urls import url
from django.contrib import admin
from app01 import views as app01views
from api import views as apiViews

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
    url(r'^api/v1/user/$',apiViews.UserView.as_view())
]
