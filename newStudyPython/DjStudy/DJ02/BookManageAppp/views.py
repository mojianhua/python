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
        # 上传文件
        # print(request.FILES)   # 查看所有上传文件
        # print(request.FILES['images'])  # 查看指定文件里面images是file里面的name
        # print(request.FILES['images'].name) # 查看上传文件名称
        filename = request.FILES['images'].name
        with open('./static/images/'+filename,"wb") as f:
            for i in request.FILES['images'].chunks():
                f.write(i)
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

def book_list(request):
    book_list = models.Book.objects.all()
    return render(request,'book_list.html',{"book_list":book_list})

def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title',None)
        pid = request.POST.get('pid',None)
        models.Book.objects.create(title=title,pid_id=pid)
        return redirect('/book_list/')
    else:
        publisher = models.Publisher.objects.all()
        return render(request,'book_add.html',{"publisher":publisher})

def book_del(request):
    id = request.GET.get('id',None)
    obj = models.Book.objects.get(id = id).delete()
    return redirect('/book_list/')

def book_update(request):
    id = request.GET.get('id')
    if request.method == 'POST':
        title = request.POST.get('title',None)
        pid = request.POST.get('pid',None)
        id = request.POST.get('id', None)
        book = models.Book.objects.get(id=id)
        book.pid_id = pid
        book.title = title
        book.save()
        return redirect('/book_list/')
    else:
        book = models.Book.objects.get(id=id)
        publisher = models.Publisher.objects.all()
        return render(request,'book_update.html',{"publisher":publisher,"book":book})

def author_list(request):
    author_list = models.Author.objects.all()
    # author_one = models.Author.objects.get(id = 1)
    # print(author_one.book.all())
    return render(request,'author_list.html',{"author_list":author_list})

def author_add(request):
    if request.method == 'POST':
        name = request.POST.get('name',None)
        # post的数据提交多个的时候,多选
        books = request.POST.getlist('books',None)
        # 创建作者对象
        newAuthorObj = models.Author.objects.create(name=name)
        # 更新作者和数据建立关系
        newAuthorObj.book.set(books)
        return redirect('/author_list/')
    else:
        book_list = models.Book.objects.all()
        return render(request,'author_add.html',{"book_list":book_list})

def author_del(request):
    id = request.GET.get('id',None)
    # 删除表并且删除对应关系
    models.Author.objects.get(id=id).delete()
    return redirect('/author_list/')

def author_update(request):
    id = request.GET.get('id',None)
    if request.method == 'POST':
        name = request.POST.get('name',None)
        books = request.POST.getlist('books',None)
        id = request.POST.get('id',None)
        obj = models.Author.objects.get(id = id)
        obj.name = name
        obj.book.set(books)
        return redirect('/author_list/')
    else:
        author = models.Author.objects.get(id=id)
        book_list = models.Book.objects.all()
        return render(request,'author_update.html',{"author":author,"book_list":book_list})
    
    
#CBV版添加出版社
from django.views import View
class CbvAddPublisher(View):
    def get(self,request):
        # 获取当前执行url路径，不带get参数不带域名
        print(request.path_info)
        return render(request,'publisher_add.html')

    def post(self,request):
        new_name = request.POST.get('name')
        # post 的数据是从body提取出来的
        print(request.body)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        else:
            msg = '名字不能为空'
            return render(request, 'publisher_add.html', {"msg": msg})

