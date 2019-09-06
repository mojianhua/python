from django.shortcuts import render,HttpResponse,redirect
from F2c import models
from django.db.models import Q
# Create your views here.
def test(request):
    ret = models.F2CAssociatorContacts.objects.filter(Q(name__contains="生") | Q(name__contains="王"))
    print(ret)
    for i in ret:
        print("name:{},grade:{}".format(i.name,i.grade))
    return HttpResponse('test')