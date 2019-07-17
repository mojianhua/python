from django.urls import path,include
import blog2.views

urlpatterns = [
    path('index',blog2.views.index)
]