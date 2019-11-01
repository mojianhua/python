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
from rabbitmq import views as rabbitmqView
from api import views as apiViews

urlpatterns = [
    # 第一版发送数据
    url(r'^(?P<version>[v1|v2]+)/mqStudysend1/$',rabbitmqView.mqStudysend1.as_view()),
    # 第一版接收数据
    url(r'^(?P<version>[v1|v2]+)/mqStudyreceive1/$', rabbitmqView.mqreceive1.as_view()),
    # celery3
    url(r'^(?P<version>[v1|v2]+)/celeryStudy1/$', rabbitmqView.celeryStudy1.as_view()),
    # celery4
    url(r'^(?P<version>[v1|v2]+)/celery4Study1/$', rabbitmqView.celery4Study1.as_view()),
]
