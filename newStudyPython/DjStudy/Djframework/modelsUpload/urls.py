from django.conf.urls import url,include
from modelsUpload import views as modelsUpload

urlpatterns = [
    # 第一版通过model上传文件
    url(r'^(?P<version>[v1|v2]+)/modelsUploadTest/$',modelsUpload.upload.as_view()),
]