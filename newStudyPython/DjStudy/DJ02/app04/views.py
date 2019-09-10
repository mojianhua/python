from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
#
def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if user == 'jim' and pwd == '123456':
            return redirect('http://www.baidu.com')
        else:
            return redirect('/v4login/')
    else:
        return render(request,'v4/login.html')

def transfer(request):
    if request.method == 'POST':
        froms = request.POST.get('from')
        to = request.POST.get('to')
        money = request.POST.get('money')
        return HttpResponse("转账成功")
    return render(request,'v4/ransfer.html')