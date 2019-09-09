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

    # 一对一查询
    author_obj = models.Author.objects.get(id=1)
    # 查询作者表里面的作者详情
    obj = author_obj.detail
    print(obj.hobby,obj.addr)