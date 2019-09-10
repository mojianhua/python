'''
orm 总结
在一个python文件里面加载Django项目
'''
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJ02.settings")
    import django
    django.setup()
    # # 第三多对多弄表方式
    # from app03 import models as App03Model
    # ret = App03Model.Author.objects.get(id = 1).bookManyToMany.all()
    # print(ret)
    # # 查询包含2书名的数据，区分大小姐
    # ret = App03Model.Book.objects.filter(title__contains="2")
    # print(ret)
    # # # 查询出版日期是2018的数据库
    # # ret = App03Model.Book.objects.filter(publish_date__year==2018)
    #
    # # 查询价格大于10的书
    # ret = App03Model.Book.objects.filter(price__gt=10)
    # print(ret)
    #
    # # 查询出版社是广州的数据
    # ret = App03Model.Publisher.objects.filter(addr="广州")
    # print(ret)
    #
    # # distinct
    # # 查所有书的关联的出版社
    # ret = App03Model.Book.objects.all().values_list("pid__name")
    # # 去重
    # print(ret.distinct())
    #
    # # 排序,desc排序
    # ret = App03Model.Book.objects.all().order_by("price")
    # print(ret)
    #
    # # 排序,asc排序
    # ret = App03Model.Book.objects.all().order_by("-price")
    # print(ret)
    #
    # # 查询书名是：书222,出版社地址
    # ret = App03Model.Book.objects.filter(title="书222").values("pid__addr")
    # print(ret)
    #
    # # 查询书名是：书222,作者的爱好，垮了2张表
    # ret = App03Model.Book.objects.filter(title="书222").values("author__detail__hobby")
    # print(ret)

    from app05 import models as App05Models
    ret = App05Models.Employee.objects.all().values("id","dept")
    print(ret)

    # 分组查询，以下例子是计算不同部门里面的平均工资
    from django.db.models import Avg
    ret = App05Models.Employee.objects.values("dept").annotate(avg=Avg("salary")).values("dept","avg")
    print(ret)

    # 链表查询分组查询，以下例子是计算不同部门里面的平均工资
    ret = App05Models.EmployeeNew.objects.values("dept__id").annotate(avg=Avg("salary")).values("dept__name","avg")
    print(ret)

    # 查询出所有员工和部门
    ret = App05Models.EmployeeNew.objects.values("name","dept__name")
    print(ret)

    # 查询出所有员工和部门，用于一对一和多对一比较好
    ret = App05Models.EmployeeNew.objects.select_related().values("name","dept__name")
    print(ret)

    # 查询出所有员工和部门还有所在地，prefetch_related用于一对多还有多对多比较好
    ret = App05Models.EmployeeNew2.objects.prefetch_related().values("name","city__city_cn","dept__name")
    print(ret)