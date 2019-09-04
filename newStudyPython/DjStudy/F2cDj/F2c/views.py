from django.shortcuts import render,HttpResponse,redirect
from F2c import models
# Create your views here.
def test(request):
    ret = models.F2CProductCn.objects.all()
    print(ret)
    return HttpResponse('test')