
from django.urls import path, include
import blog.views

#应用路由
urlpatterns = [
    path('hello_world',blog.views.hello_world),
    path('index_index', blog.views.index_index),
    path('show/index',blog.views.showIndex),
    path('blog/add',blog.views.addSum),
    path('blog/add2/<int:a>/<int:b>/',blog.views.addSum2),
    path('blog/index',blog.views.get_index_page),
    path('blog/detail/<int:aid>/',blog.views.get_detail_page)
]