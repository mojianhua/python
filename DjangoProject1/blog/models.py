from django.db import models

# Create your models here.

class Article(models.Model):
    # 文章id
    article_id =models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)

    #在Django Admin 显示title
    def __str__(self):
        return self.title