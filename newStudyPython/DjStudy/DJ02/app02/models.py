from django.db import models

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False,unique=True)
    # 指定默认值
    addr = models.CharField(max_length=255,default='广州市')

    def __str__(self):
        return "<models object:{}>".format(self.name)

# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,null=False)
    price = models.DecimalField(max_digits=5,decimal_places=2,default='99.99')
    # 库存
    kuncun = models.IntegerField(default=1000)
    # 卖出
    maichu = models.IntegerField(default=0)
    # 一对多的
    pid = models.ForeignKey(
        to="Publisher",
        on_delete=models.CASCADE,
        related_name="back_book",
        # 外键允许为空
        null=True
    )

    def __str__(self):
        return "<models object:{}>".format(self.title)

# 作者表
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    # 告诉ORM多对多，我这表和book是多对多关系
    book = models.ManyToManyField(to="Book")
    # 一对一，和AuthorDetial对应
    detail = models.OneToOneField("AuthorDetial",on_delete=models.CASCADE)

    def __str__(self):
        return "<Author object:{}>".format(self.name)

class AuthorDetial(models.Model):
    # 爱好
    hobby = models.CharField(max_length=32)
    # 地址
    addr = models.CharField(max_length=32)

# 自动动手创建作者和书的第三张表
# 此时在orm 层面就没多对多的关系
class Author2Book(models.Model):
    id = models.AutoField(primary_key=True)
    # 作者id
    author = models.ForeignKey(to="Author",on_delete=models.CASCADE)
    # 书的ID
    book = models.ForeignKey(to="Book",on_delete=models.CASCADE)