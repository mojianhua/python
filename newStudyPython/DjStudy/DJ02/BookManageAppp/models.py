from django.db import models

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False,unique=True)

# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,null=False)
    # 一对多的
    pid = models.ForeignKey(to="Publisher",on_delete=models.CASCADE)
