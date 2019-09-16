import json
from django.shortcuts import render,HttpResponse

# Create your views here.
def JsonTest(request):
    s = '{"name":"Jim11","age":18}'
    # 字符串转数据类型
    ret = json.loads(s)
    print(ret,type(ret))
    # json变成字符串
    ret = json.dumps(ret)
    print(ret,type(ret))
    return HttpResponse('ok')

def JsonStudy(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print(username,pwd)
        return HttpResponse("ok")
    else:
        return render(request,'JsonStudyHtml/login.html')

from appJson import models
def JsonPersions(request):
    ret = models.Persions.objects.all()
    # person_list = []
    # for i in ret:
    #     person_list.append({"name":i.name,"age":i.age})
    # str = json.dumps(person_list)
    # print(str)
    # 序列化
    from django.core import serializers
    ret = serializers.serialize("json",ret)
    return HttpResponse(ret)

class Person(object):
    def __init__(self,name):
        self.name = name