from django.conf.urls import url,include
from PayPalStudy import views as PayPalViews
urlpatterns = [
    # paypalv1版本
    url(r'^(?P<version>[v1|v2]+)/PayPalTest1/$',PayPalViews.PayPalTest1.as_view()),
    # paypalv2版本
    url(r'^(?P<version>[v1|v2]+)/PayPalTest2/$', PayPalViews.PayPalTest2.as_view()),
]