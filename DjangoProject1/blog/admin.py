from django.contrib import admin

# Register your models here.

#注册模型到admin
from .models import Article

admin.site.register(Article)