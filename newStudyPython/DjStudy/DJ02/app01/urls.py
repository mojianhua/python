from django.conf.urls import url
from app01 import views as app01views
urlpatterns = [
    url(r'login/', app01views.login),
    url(r'user_list/', app01views.user_list),
    url(r'user_add/', app01views.user_add),
    url(r'template_test/', app01views.template_test)
 ]