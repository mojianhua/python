from django.conf.urls import url,include
from django.contrib import admin
from api02 import views
urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/users/$',views.UsersViews.as_view())
]