from django.conf.urls import url,include
from AliOss import views as AliOss
urlpatterns = [
    # 第一版发送数据
    url(r'^(?P<version>[v1|v2]+)/AliOssTest/$',AliOss.AliOssTest.as_view()),
]