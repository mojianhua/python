# Create your views here.
# 路由测试
from django.shortcuts import HttpResponse,render,redirect
from app01 import models
# 登录方法
def login(request):
    error_msg = ''
    # 返回响应httpResponse 对象
    # return HttpResponse('hihihihi')
    if request.method == "GET":       #request.method请问方式
        # 指定使用模板
        return render(request,"login.html")
    elif request.method == 'POST':
        # 获取用户提交的数据
        email = request.POST.get('email', None)  # post提交，如果key写错则返回默认值
        pwd = request.POST.get('pwd', None)
        if (email == '1657210793@qq.com' and pwd == '123456'):
            # 跳转
            return redirect('http://www.baidu.com')
            #return HttpResponse('登录成功')
        else:
            error_msg = '邮箱或密码错误'
            # {"error_msg":error_msg} 赋值传参
            return render(request,"login.html",{"error_msg":error_msg})
    else:
        return  HttpResponse('报错')

def user_list(request):
    user_list = models.userInfo.objects.all()
    # print(user_list[1].name) 通过下标获取一条数据
    return render(request,'user_list.html',{"user_list":user_list})

def user_add(request):
    if request.method == 'POST':
        name = request.POST.get('name',None)
        models.userInfo.objects.create(name=name)
        return redirect('/user_list/')
    else:
        return render(request,'user_add.html')

# 模板测试类
class Persion(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dream(self):
        return 'aaaaadddddddweeeee'

    def __str__(self):
        return "<Persion Object:{}>".format(self.name)


# 模板语言
def template_test(request):
    name = 'jim'
    name_list = ["a",'a1','a2']
    name_dict = {"key1":"val1","key2":"val2"}
    p1 = Persion('jim',2)
    p2 = Persion('jim2',5)
    file_size = 3354445656
    from datetime import datetime
    now = datetime.now()
    a_html = "<a href='http://www.baidu.com'>百度</a>"
    return render(request,'template_test.html',
                  {"name":name,
                   "name_list":name_list,
                   "name_dict":name_dict,
                   "p1":p1,
                   "p2": p2,
                   "file_size":file_size,
                   "now":now,
                   "a_html":a_html
                   }
                  )