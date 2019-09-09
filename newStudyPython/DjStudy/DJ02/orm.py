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

    # print("正向查询".center(80,'*'))
    # book_obj = models.Book.objects.all().first()
    # # 查询出版社名
    # ret = book_obj.pid.name
    # print(ret)
    # # 查询出版社名
    # ret = models.Book.objects.filter(id = 1).values("pid__name")
    # print(ret)
    #
    # print("反向查询".center(80, '*'))
    # publisher_obj = models.Publisher.objects.first()
    # ret = publisher_obj.back_book.all()
    # print(ret)
    #
    # ret = models.Publisher.objects.filter(id = 8).values("back_book__title")
    # print(ret)


    # 多对多
    # author_obj = models.Author.objects.first()
    # print(author_obj.name)
    # # 查询jim1写过的书
    # ret = author_obj.book.all()
    # print(ret)

    # 1.create，在jim1里面在添加一本书
    # 通过作者创建一本书，会自动保存
    # 做了两件事
    # 1.在book里创建一本新书，2、在作者和书的关系中新建一个关联记录
    # 注意对应book表里面的字段，title等于title字段，pid_id 等于 pid字段，不是跟model.py对应的
    # ret = author_obj.book.create(title="书本12",pid_id = 6)
    # print(ret)

    # add，在jim1里面在添加一本书
    # 先拿到id是12的书
    # book_obj = models.Book.objects.get(id = 10)
    # ret = author_obj.book.add(book_obj)
    # print(ret)

    # 添加多个
    # book_objs = models.Book.objects.filter(id__gt=2)
    # 要把列表打散再传进去
    # ret = author_obj.book.add(*book_objs)
    # print(ret)

    # 直接添加书本id是5的数据
    # ret = author_obj.book.add(5)
    # print(ret)

    # # remove
    # book_obj = models.Book.objects.get(id = 2)
    # ret = author_obj.book.remove(book_obj)
    # print(ret)
    #
    # # 将书ID 是 3 的从 属于 jim1的记录删除
    # author_obj.book.remove(3)
    #
    # # clear，清空，把jim2打入冰窖，意思说，将作者为jim2从所有书中删除，不留名
    # jim2 = models.Author.objects.get(id = 2)
    # jim2.book.clear()
    #
    # # 额外补充，外键的反向操作
    # # 找到id是1的出版社
    # publisher_obj = models.Publisher.objects.get(id = 1)
    # publisher_obj.back_book.clear()

    from django.db.models import Avg,Sum,Max,Min,Count
    # # 计算书本平均价格
    # ret = models.Book.objects.all().aggregate(price_avg = Avg('price'),price_sum = Sum('price'))
    # print(ret)
    #
    # # 分组查询
    # # 查询每一本书的作者个数
    # ret = models.Book.objects.all().annotate(author_num=Count("author"))
    # for book in ret:
    #     print("书名：{},作者数:{}".format(book.title,book.author_num))
    #
    # # 分组查询数量大于1的数据
    # ret = models.Book.objects.all().annotate(author_num=Count('author')).filter(author_num__gt=1)
    # for book in ret:
    #     print('书名：{}，数量：{}'.format(book.title,book.author_num))


    # 每个作者出书的总价
    # ret = models.Author.objects.all().annotate(price_sum=Sum("book__price"))
    # for i in ret:
    #     print("作者：{},总价：{}".format(i.name,i.price_sum))
    # print(ret.values_list("name","price_sum"))

    # F 和 Q
    from django.db.models import F
    # 取出库存数大于卖出数的数据,可用于字段间比较
    ret = models.Book.objects.filter(kuncun__gt=F("maichu"))
    print(ret)
    # 把没一本书的卖出数乘以3
    ret = models.Book.objects.update(maichu=F("maichu") * 3)

    # 给每一本数的书名后面加上第一版
    from django.db.models.functions import Concat
    from django.db.models import Value
    models.Book.objects.update(title=Concat(F("title"),Value("第一版")))

    # Q查询
    from django.db.models import Q
    # 卖出数大度100或价格小于10的数据
    ret = models.Book.objects.filter(Q(maichu__gt=100) | Q(price__lt=10))
    print(ret)
    # 卖出数大度100或价格小于10的数据,并且书名包含2的数据
    ret = models.Book.objects.filter(Q(maichu__gt=100) | Q(price__lt=10),title__contains='2')
    print(ret)
