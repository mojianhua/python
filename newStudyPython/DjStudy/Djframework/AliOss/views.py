from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
import oss2
import uuid

'''
    oss文件上传
'''
class AliOssTest(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):

        # auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
        # # Endpoint以杭州为例，其它Region请按实际情况填写。
        # bucket = oss2.Bucket(auth, '<EndPoint（地域节点）>', '<yourBucketName>')

        # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
        auth = oss2.Auth('xxxxx', 'xxxxxxx')
        # Endpoint以杭州为例，其它Region请按实际情况填写。
        bucket = oss2.Bucket(auth, 'https://oss-cn-shenzhen.aliyuncs.com', 'f2c-pic')
        print(bucket)

        # 单文件上传
        file_obj = request.FILES.get('image', None)
        # 上传网络流
        # bucket.put_object('<oss路径>', file_obj)
        result = bucket.put_object('abc/98.jpg', file_obj)
        if result.status == 200:
            # print('http url: {0}'.format(filename))  # 上传文件生成的url，可以用它进行下载或查看
            print('http status: {0}'.format(result.status))  # HTTP返回码，成功返回200
            print('request_id: {0}'.format(result.request_id))  # 请求ID，强烈建议把它作为程序日志的一部分
            print('ETag: {0}'.format(result.etag))  # etag则是put_object返回值特有的属性
            print('date: {0}'.format(result.headers['date']))  # HTTP响应头部

        print(file_obj.name)
        print(file_obj.size)
        with open('./static/images/' + file_obj.name ,'wb') as f:
            # 分块写入文件
            for line in file_obj.chunks():
                print(line)
                # bucket.put_object('<oss路径>', file_obj)

                # 2）指定方式上传put_object，支持上传
                #       1）字符串，2）bytes：直接上传，3）unicode：会自动转换为UTF-8编码的bytes进行上传，
                #       4）上传本地文件以文件对象方式：必须以二进制的方式打开文件，因为内部实现需要知道文件包含的字节数
                # bucket.put_object('remote.txt', 'content of object')
                # bucket.put_object('remote.txt', b'content of object')
                # bucket.put_object('remote.txt', u'content of object')
                ret = bucket.put_object('abc/97.jpg', line)
                print(ret)
                f.write(line)
        f.close()

        # 本地文件上传到oss
        ret = bucket.put_object_from_file('abc/96.jpg', './static/images/96.jpg')
        print(ret)
        # # 删除oss文件
        # bucket.delete_object('abc/96.jpg')

        # 多文件上传
        file_objs = request.FILES.getlist('images', None)
        for file_obj in file_objs:
            print(file_obj.name)
            print(file_obj.size)

        return HttpResponse(111)