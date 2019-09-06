'''
orm 总结
在一个python文件里面加载Django项目
'''
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJ02.settings")
    import django
    django.setup()
    from BookManageAppp import models
    # print("查询一个表所有内容".center(80,'*'))
    # author = models.Author.objects.all()
    # print(author)
    # print("get查询，不存会报错".center(80,'*'))
    # author = models.Author.objects.get(name='jim1')
    # print(author)
    # print("filter查询，不存会报空")
    # author = models.Author.objects.filter(name='jim2')
    # print(author)
    # author = models.Author.objects.filter(id = 1)
    # print(author)
    # # 就算 查询只有一个，返回也是QuerySet,我们要用索引的方式取出第一个元素
    # author = models.Author.objects.filter(id = 1)[0]
    # print(author)
    # print("exclude,排除查询,例：排除id为1的数据".center(80,"*"))
    # author = models.Author.objects.exclude(id = 1)
    # print(author)
    # print('values 返回一个QuerySet 对象，里面都是字典，查询指定字段'.center(80,'*'))
    # author = models.Author.objects.values("name")
    # print(author)
    # print('values_list 返回一个QuerySet 对象，里面都是元祖，查询指定字段'.center(80,'*'))
    # author = models.Author.objects.values_list("name")
    # print(author)
    # print("order_by".center(80,'*'))
    # author = models.Author.objects.all().order_by("name","id")
    # print(author)
    # print("reverse将一个有序的QuerySet方向排序".center(80,'*'))
    # author = models.Author.objects.all().order_by("id").reverse()
    # print(author)
    # print("count，统计数据条数".center(80,'*'))
    # author = models.Author.objects.all().count()
    # print(author)
    # print("first，第一条数据".center(80,'*'))
    # author = models.Author.objects.first()
    # print(author)
    # print("last，最后一条数据".center(80,'*'))
    # author = models.Author.objects.last()
    # print(author)
    # print("查询id in (1,3,5)的结果".center(80,'*'))
    # ret = models.Author.objects.filter(id__in=[1,3,5])
    # print(ret)
    # print("查询 id not in(1,3,5)的结果".center(80,'*'))
    # ret = models.Author.objects.exclude(id__in=[1,3,5])
    # print(ret)
    # print("模糊搜索严格区分大小写".center(80, '*'))
    # ret = models.Author.objects.filter(name__contains="j")
    # print(ret)
    # print("模糊搜索不区分大小写".center(80, '*'))
    # ret = models.Author.objects.filter(name__icontains="j")
    # print(ret)
    # print("判断id值在那个区间的，sql中的 between 1 and 3".center(80, '*'))
    # ret = models.Author.objects.filter(id__range=[1,3])
    # print(ret)

    print("正向查询".center(80,'*'))
    book_obj = models.Book.objects.all().first()
    # 查询出版社名
    ret = book_obj.pid.name
    print(ret)
    # 查询出版社名
    ret = models.Book.objects.filter(id = 1).values("pid__name")
    print(ret)

    print("反向查询".center(80, '*'))
    publisher_obj = models.Publisher.objects.first()
    ret = publisher_obj.back_book.all()
    print(ret)

    ret = models.Publisher.objects.filter(id = 8).values("back_book__title")
    print(ret)