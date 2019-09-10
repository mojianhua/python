'''
orm 总结
在一个python文件里面加载Django项目
'''
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJ02.settings")
    import django
    django.setup()
    from BookManageAppp import models as BookManageModel

    # # 一对一查询
    # author_obj = BookManageModel.Author.objects.get(id=1)
    # # 查询作者表里面的作者详情
    # obj = author_obj.detail
    # print(obj.hobby,obj.addr)

    # # 查询作者id 是 1相关联的所有书
    # ret = BookManageModel.Author.objects.get(id = 1).book.all()
    # # 从作者表里面移除id是1的书
    # BookManageModel.Author.objects.get(id = 1).book.remove(1)

    # # 查询app02 里面查询ID 是2 的作者的书的标题
    # from app02 import models as App02Model
    # ret = App02Model.Author2Book.objects.filter(author_id = 1).values_list("book__id")
    # print(ret)
    # ret = [i[0] for i in ret]
    # # 查书的表
    # ret = App02Model.Book.objects.filter(id__in=ret)
    # print(ret)
    #
    # # 第三多对多弄表方式
    # from app03 import models as App03Model
    # ret = App03Model.Author.objects.get(id = 1).bookManyToMany.all()
    # print(ret)
    # # 从作者表关联的书里面移除id是1作者关联的书
    # # 没 Django ORM 封装自定义第三张表的删除方式
    # App03Model.Author2Book.objects.get(author_id=1,book_id=1).delete()