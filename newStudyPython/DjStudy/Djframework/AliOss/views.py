from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
import oss2

'''
    oss文件上传
'''
class AliOssTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
        auth = oss2.Auth('LTAIhHrPbeHwidYD', 'YCYEH66bS8KchPCl9suW40CHMeZlKl')
        # Endpoint以杭州为例，其它Region请按实际情况填写。
        bucket = oss2.Bucket(auth, 'https://pic.food2china.cn', 'f2c-pic')
        print(bucket)
        result = bucket.put_object_from_file('gaoda.jpg', 'file')
        if result.status == 200:
            url = '%s' % ('gaoda.jpg')
            print(url)

        return HttpResponse(111)