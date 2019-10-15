from django.db import models
# contenttype
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class UserInfo(models.Model):
    user_type_choices = (
        (1,'普通用户'),
        (2,'VIP'),
        (3,'SVIP'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo",on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

class Course(models.Model):
    '''
    普通课程
    '''
    title = models.CharField(max_length=32)
    #将课程跟表和价格表做关联
    price_policy_list = GenericRelation("PricePolicy")

class DergreeCourse(models.Model):
    '''
    学位课程
    '''
    title = models.CharField(max_length=32)
    # 将课程跟表和价格表做关联
    price_policy_list = GenericRelation("PricePolicy")


class PricePolicy(models.Model):
    '''
    价格策略
    '''
    pirce = models.IntegerField()
    period = models.IntegerField()

    content_type = models.ForeignKey(ContentType,verbose_name="关联表的名称")
    object_id = models.IntegerField(verbose_name="关联表的数据ID")
    # 帮助你快速实现content_type操作,上面的content_type表跟表里面的object_id对应
    content_object = GenericForeignKey('content_type','object_id')