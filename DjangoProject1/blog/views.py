#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

#分页类
from django.core.paginator import Paginator
# Create your views here.

def index_index(request):
    return HttpResponse("Hello World index")

def hello_world(request):
    return HttpResponse("Hello World 啊啊")

def showIndex(request):
    return HttpResponse("Hello showIndex")

def addSum(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def addSum2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page is ',page)
    all_article = Article.objects.all()

    #把数据生成分页,Paginator(数据，每页显示数量)
    paginator = Paginator(all_article,2)
    #打印分页数量
    print('page num :',paginator.num_pages)
    page_num = paginator.num_pages
    #每页分页的列表
    page_article_list = paginator.page(page)

    #如果有下一页
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page

    #如果有上一页
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    #最新的2篇文章,order_by()带减号是倒序，不带减号默认是正序
    newarticle = Article.objects.order_by('-publish_date')[:2]
    return render(request,'blog/index.html',{
        'article_list':page_article_list,
        #分页数量
        'page_num':range(1,page_num + 1),
        #当前页面
        'curr_page':page,
        #下一页
        'next_page':next_page,
        #上一页
        'previous_page':previous_page,
        #最新的2篇文章
        'newarticle':newarticle
    })

def get_detail_page(request,aid):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    for index,article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            next_index = index
            previous_index = index - 1
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == aid:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break


    section_list = curr_article.content.split('\n')
    return render(request,'blog/detail.html',{
        'curr_article':curr_article,
        'section_list':section_list,
        'previous_article':previous_article,
        'next_article':next_article
    })