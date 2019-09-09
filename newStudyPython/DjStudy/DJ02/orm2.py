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

    # 一对一查询
    author_obj = BookManageModel.Author.objects.get(id=2)
    # 查询作者表里面的作者详情
    obj = author_obj.detail
    print(obj.hobby,obj.addr)

    # 查询app02 里面查询ID 是2 的作者的书的标题
    from app02 import models as App02Model
    ret = App02Model.Author2Book.objects.filter(author_id = 2).values_list("book__id")
    print(ret)
    ret = [i[0] for i in ret]
    # 查书的表
    ret = App02Model.Book.objects.filter(id__in=ret)
    print(ret)

    # 第三多对多弄表方式
    from app03 import models as App03Model
    ret = App03Model.Author.objects.get(id = 1).bookManyToMany.all()
    print(ret)