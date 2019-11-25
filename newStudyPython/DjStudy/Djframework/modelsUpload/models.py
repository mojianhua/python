from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # thumb = models.FileField(upload_to='files')          # 长传到指定文件夹，不需要手动创建
    thumb = models.FileField(upload_to='%Y/%m/%d')         # 自动保存到media文件夹(配合setting.py配合，media文件夹要手动创建)
