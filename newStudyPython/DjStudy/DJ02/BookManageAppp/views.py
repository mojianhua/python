from django.shortcuts import HttpResponse,render,redirect
from BookManageAppp import models
# Create your views here.
def publisher_list(request):
    publisher_list = models.Publisher.objects.all()
    return render(request,'publisher_list.html',{"publisher_list":publisher_list})

def publisher_add(request):
    msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name :
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        else:
            msg = '名字不能为空'
            return render(request, 'publisher_add.html',{"msg":msg})
    else:
        return render(request,'publisher_add.html')

def publisher_del(request):
    id = request.GET.get('id',None)
    # 根据id查数据
    obj = models.Publisher.objects.get(id=id)
    # 删除
    obj.delete()
    return redirect('/publisher_list/')

def publisher_update(request):
    id = request.GET.get('id', None)
    if request.method == 'POST':
        # 更新数据
        id = request.POST.get('id',None)
        # 先查询
        obj = models.Publisher.objects.get(id = id)
        # 跟新数据
        obj.name = request.POST.get('name')
        # 保存数据
        obj.save()
        return redirect('/publisher_list/')
    else:
        # 查询一条数据
        obj = models.Publisher.objects.get(id = id)
        return render(request,'publisher_edit.html',{"obj":obj})