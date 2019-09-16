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

'''
cookie 参数
key, 键
value='', 值
max_age=None, 超时时间
expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
path='/', Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
domain=None, Cookie生效的域名
secure=False, https传输
httponly=False 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
'''

from functools import wraps
# 装饰器登录校验
def check_login(func):
    # 装饰器修复技术
    @wraps(func)
    def inner(request,*args,**kwargs):
        ret = request.get_signed_cookie('is_login', default=99, salt="abc")
        if ret == "1":
        # 已经登录过则执行
            return func(request,*args,**kwargs)
        else:
            # 获取当然url
            next_url = request.path_info
            print(next_url)
            return redirect('/v5login/?next_url={}'.format(next_url))
    return inner

def v5login(request):
    # 当前访问的全路径
    print(request.get_full_path())
    # 当前请求的路径
    print(request.path_info)
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        # 从url获取数据
        next_url = request.GET.get('next_url')
        if user == 'jim' and pwd == '123456':
            # 设置cookie
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect('/v5home/')
            # rep.set_cookie('zmkm',"2")
            # 设置加密cookie,max_age 设置过期时间
            rep.set_signed_cookie('is_login',"1",salt="abc",max_age=10)
            return rep
        else:
            return HttpResponse('error')
    else:
        return render(request,'v5/login.html')

def v5home(request):
    # 获取cookie
    # ret = request.COOKIES.get('zmkm',99)
    # 获取加密cookie
    ret = request.get_signed_cookie('is_login',default=0,salt="abc")
    if ret == '1':
        return render(request,'v5/home.html')
    else:
        return redirect('/v5login/')

@check_login
def v5index(request):
    return render(request,'v5/index.html')

# 登出
def v5loginout(request):
    rep = redirect('/v5login/')
    # 删除cookie
    rep.delete_cookie("is_login")
    return rep


'''
session相关方法
# 获取、设置、删除Session中数据
request.session['k1']
request.session.get('k1',None)
request.session['k1'] = 123
request.session.setdefault('k1',123) # 存在则不设置
del request.session['k1']


# 所有 键、值、键值对
request.session.keys()
request.session.values()
request.session.items()
request.session.iterkeys()
request.session.itervalues()
request.session.iteritems()

# 会话session的key
request.session.session_key

# 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()

# 检查会话session的key在数据库中是否存在
request.session.exists("session_key")

# 删除当前会话的所有Session数据
request.session.delete()
　　
# 删除当前的会话数据并删除会话的Cookie。
request.session.flush() 
    这用于确保前面的会话数据不可以再次被用户的浏览器访问
    例如，django.contrib.auth.logout() 函数中就会调用它。

# 设置会话Session和Cookie的超时时间
request.session.set_expiry(value)
    * 如果value是个整数，session会在些秒数后失效。
    * 如果value是个datatime或timedelta，session就会在这个时间后失效。
    * 如果value是0,用户关闭浏览器session就会失效。
    * 如果value是None,session会依赖全局session失效策略。

'''
# 装饰器登录校验
def check_login_session(func):
    # 装饰器修复技术
    @wraps(func)
    def inner(request,*args,**kwargs):
        # 获取session
        ret = request.session.get('is_login')
        if ret == 1:
        # 已经登录过则执行
            return func(request,*args,**kwargs)
        else:
            # 获取当然url
            next_url = request.path_info
            print(next_url)
            return redirect('/v5loginSession/?next_url={}'.format(next_url))
    return inner

def v5loginSession(request):
    # 当前访问的全路径
    print(request.get_full_path())
    # 当前请求的路径
    print(request.path_info)
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        # 从url获取数据
        next_url = request.GET.get('next_url')
        if user == 'jim' and pwd == '123456':
            # 设置cookie
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect('/Session/v5home/')
                # 设置session
                request.session["is_login"] = 1
            return rep
        else:
            return HttpResponse('error')
    else:
        return render(request,'v5/Session/login.html')

def v5homeSession(request):
    # 获取session
    ret = request.session.get('is_login')
    if ret == 1:
        return render(request,'v5/Session/home.html')
    else:
        return redirect('/Session/v5login/')

@check_login_session
def v5indexSession(request):
    return render(request,'v5/Session/index.html')

# 登出
def v5loginoutSession(request):
    # 删除SESSION和cookie
    ret = request.session.flush()
    return redirect('/Session/v5login/')