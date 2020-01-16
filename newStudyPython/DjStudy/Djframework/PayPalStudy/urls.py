from django.conf.urls import url,include
from PayPalStudy import views as PayPalViews
urlpatterns = [
    # 发起支付
    url(r'^(?P<version>[v1|v2]+)/PayPalTest/$',PayPalViews.PayPalTest.as_view()),
    # # 查询支付结果支付
    # url(r'^(?P<version>[v1|v2]+)/AliPayCheckTest/$', AliPayViews.AliPayCheckTest.as_view()),
]