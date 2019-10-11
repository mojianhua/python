from django.conf.urls import url,include
from django.contrib import admin
from api02 import views
from api import views as apiViews
urlpatterns = [
    # 版本使用
    url(r'^(?P<version>[v1|v2]+)/users/$',views.UsersViews.as_view()),
    # 解析器
    url(r'^(?P<version>[v1|v2]+)/jiexiqiusers/$',views.UsersJieXiQiViews.as_view()),
    # 序列化
    url(r'^(?P<version>[v1|v2]+)/roles/$',views.RolesViews.as_view()),
    url(r'^(?P<version>[v1|v2]+)/UserInfoView/$',views.UserInfoView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/UserInfoModelView/$',views.UserInfoModelView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/group/(?P<pk>\d+)$',views.GroupView.as_view(),name='gp'),
    # 验证
    url(r'^(?P<version>[v1|v2]+)/UserGroupView/$',views.UserGroupView.as_view()),
    # 分页
    url(r'^(?P<version>[v1|v2]+)/UserGroupPageView/$', apiViews.UserGroupPageView.as_view()),
    # 视图
    url(r'^(?P<version>[v1|v2]+)/NewUserGroupPageView/$', apiViews.NewUserGroupPageView.as_view()),
    # get请求和方法中的list对应
    url(r'^(?P<version>[v1|v2]+)/NewUserGroupPageView2/$', apiViews.NewUserGroupPageView2.as_view({'get':'list','post':'create'})),

]