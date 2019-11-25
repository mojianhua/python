from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from modelsUpload.models import Article

'''
   model上传文件
'''
class upload(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        thumb = request.FILES.get('thumb')
        Article.objects.create(title=title,content=content,thumb=thumb)
        return HttpResponse(999999)