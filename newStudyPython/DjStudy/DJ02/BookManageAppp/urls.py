from django.conf.urls import url
from BookManageAppp import views as BookManageApppview
urlpatterns = [
    url(r'publisher_list/',BookManageApppview.publisher_list),
    url(r'publisher_add/',BookManageApppview.publisher_add),
    url(r'publisher_del/',BookManageApppview.publisher_del),
    url(r'publisher_update/',BookManageApppview.publisher_update),
    url(r'book_list/',BookManageApppview.book_list),
    url(r'book_add/',BookManageApppview.book_add),
    url(r'book_del/', BookManageApppview.book_del),
    url(r'book_update/', BookManageApppview.book_update),
    url(r'author_list/',BookManageApppview.author_list),
    url(r'author_add/',BookManageApppview.author_add),
    url(r'author_del/',BookManageApppview.author_del),
    # CBV版添加出版社
    url(r'publisher_add_cbv/',BookManageApppview.CbvAddPublisher.as_view()),
    url(r'json_test/',BookManageApppview.json_test),
    # 路由正则表达式
    url(r'json_re1/[0-9]{1,9}/$',BookManageApppview.json_test_re1),
    # 带括号分组的必须要在方法里面接收参数，一个括号一个参数
    url(r'json_re2/[0-9]{1,9}/([a-zA-Z]{3})/$', BookManageApppview.json_test_re2),
    # 分组命名方式
    url(r'json_re3/[0-9]{1,9}/(?P<year>[a-zA-Z]{3})/(?P<month>[a-zA-Z]{3})$', BookManageApppview.json_test_re3),
    # 删除出版社，使用正则路由
    url(r'publisher_re_del/([0-9]+)/$', BookManageApppview.publisher_del_re),
    # 分页设计
    url(r'json_page/$',BookManageApppview.json_page),
    url(r'json_page/(?P<page>[0-9]+)$',BookManageApppview.json_page),
]