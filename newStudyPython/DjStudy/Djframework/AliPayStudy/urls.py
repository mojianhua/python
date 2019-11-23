from django.conf.urls import url,include
from AliPayStudy import views as AliPayViews
urlpatterns = [
    # 发起支付
    url(r'^(?P<version>[v1|v2]+)/AliPayTest/$',AliPayViews.AliPayTest.as_view()),
    # 查询支付结果支付
    url(r'^(?P<version>[v1|v2]+)/AliPayCheckTest/$', AliPayViews.AliPayCheckTest.as_view()),
]