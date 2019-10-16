from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# Create your views here.
class middleware1(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        print(1111)
        return HttpResponse('111')