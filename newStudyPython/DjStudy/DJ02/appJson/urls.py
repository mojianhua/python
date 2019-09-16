from django.conf.urls import url
from appJson import views
urlpatterns = [
    url(r'JsonTest/$',views.JsonTest),
    url(r'JsonStudy/$',views.JsonStudy),
    url(r'JsonPersion/$',views.JsonPersions)
]