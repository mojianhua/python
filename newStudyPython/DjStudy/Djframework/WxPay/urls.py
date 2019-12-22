from django.conf.urls import url,include
from WxPay import views as WxPayViews
urlpatterns = [
    # 发起支付
    url(r'^(?P<version>[v1|v2]+)/WxPayTest/$',WxPayViews.WxPayTest.as_view()),
]