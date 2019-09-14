from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app05 import models
def Books(request):
    # # 添加
    # for i in range(1,50):
    #     models.Book.objects.create(title='book' + str(i))
    # return HttpResponse('OK')
    ## 从20条到第30条
    # = models.Book.objects.all()[20:30]
    # 从20条到第30条
    try:
        page_num = int(request.GET.get('page', 1))
    except Exception as e:
        page_num = 1
    # 总页数
    total_count = models.Book.objects.count()
    per_page = 10
    # 计算总页码
    count_page,m = divmod(total_count,per_page)
    if count_page == 0:
        page_num = 1
    else:
        if page_num <= 0:
            page_num = 1
        elif page_num > count_page:
            page_num = count_page
    # 开始页
    begin_num = (page_num - 1) * 10
    # 结束页
    end_num = page_num * 10

    # 页码显示总共多少页
    max_page = 11
    # 左右对称显示页数
    half_max_page = max_page // 2

    if count_page < half_max_page:
        page_start = 1
        page_end = count_page+1
    else:
        # 分页开始数
        if page_num <= half_max_page:
            page_start = 1
            page_end = page_num + half_max_page
        elif page_num + half_max_page  >= count_page:
            page_start = page_num - half_max_page
            page_end = count_page
        else:
            page_start = page_num - half_max_page
            page_end = page_num + half_max_page
    # # 分页结束数
    # page_end = page_num + half_max_page
    # 读取范围
    all_book = models.Book.objects.all()[begin_num:end_num]

    # 封装html
    page_html = []

    # 加上首页
    page_html.append('<li><a href="/v5Books?page=1">首页</a></li>')
    # 上一页
    if page_num > 1:
        page_html.append('<li><a href="/v5Books?page={}">上一页</a></li>'.format(page_num - 1))

    for num in range(page_start,page_end+1):
        tmp = '<li><a href="/v5Books?page={}">{}</a></li>'.format(num,num)
        page_html.append(tmp)

    # 下一页
    if page_num < count_page:
        page_html.append('<li><a href="/v5Books?page={}">下一页</a></li>'.format(page_num + 1))

    # 加上末页
    page_html.append('<li><a href="/v5Books?page={}">末页</a></li>'.format(count_page))
    page_html = "".join(page_html)
    return render(request,"v5/books.html",{
        "all_book":all_book,
        "count_page":count_page,
        "page_html":page_html
    })

from functools import wraps
# 装饰器登录校验
def check_login(func):
    # 装饰器修复技术
    @wraps(func)
    def inner(request,*args,**kwargs):
        ret = request.get_signed_cookie('zmkm', default=99, salt="abc")
        if ret == "1":
        # 已经登录过则执行
            return func(request,*args,**kwargs)
        else:
            # 获取当然url
            next_url = request.path_info
            print(next_url)
            return redirect('/v5login/')
    return inner

def v5login(request):
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'jim' and pwd == '123456':
            # 设置cookie
            rep = redirect('/v5home/')
            # rep.set_cookie('zmkm',"2")
            # 设置加密cookie,max_age 设置过期时间
            rep.set_signed_cookie('zmkm',"1",salt="abc",max_age=10)
            return rep
        else:
            return HttpResponse('error')
    else:
        return render(request,'v5/login.html')

def v5home(request):
    # 获取cookie
    # ret = request.COOKIES.get('zmkm',99)
    # 获取加密cookie
    ret = request.get_signed_cookie('zmkm',default=0,salt="abc")
    if ret == '1':
        return render(request,'v5/home.html')
    else:
        return redirect('/v5login/')

@check_login
def v5index(request):
    return render(request,'v5/index.html')