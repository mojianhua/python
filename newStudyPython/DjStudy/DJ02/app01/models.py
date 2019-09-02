from django.db import models

# Create your models here.
class userInfo(models.Model):
    id = models.AutoField(primary_key=True)    #创建一个自增的主键字段
    name = models.CharField(null=False,max_length=255)        #创建一个varchar不能为空

    def __str__(self):
        return "<{}------{}>".format(self.id,self.name)