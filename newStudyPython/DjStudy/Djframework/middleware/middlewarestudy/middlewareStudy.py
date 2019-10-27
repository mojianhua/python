from django.shortcuts import HttpResponse

'''
    中间件
'''
URL = ["uri1","uri2","/middle/v1/middleware1/"]
from django.utils.deprecation import MiddlewareMixin
class middlewareStudy(MiddlewareMixin):
    # 处理请求的中间件
    def process_request(self,request):
        print('这是第一个处理请求的中间件')

        # # 不能获取get后面的值
        # print(request.path_info)
        # # 获取get后面的只
        # print(request.get_full_path())

        # 白名单
        # if request.path_info in URL:
        #     # 直接响应，后面程序不执行
        #     return None
        # else:
        #     return HttpResponse('OUT')
        # # 直接响应，后面程序不执行
        # return HttpResponse('OUT')

        # # 如果不做任何操作直接return None
        # return None

    # 处理响应的中间件
    '''
        :param request: 浏览器发来的请求对象
        :param response: 视图函数返回的响应对象
    '''
    def process_response(self,request,resopnse):
        print('这是第一个响应中间件')
        return resopnse

    # 处理视图的中间件
    '''
        :param request:浏览器发来的请求对象
        :param view_func:将要执行的视图函数名称
        :param view_args:将要执行的视图函数位置参数:
        :param view_kwargs:将要执行的函数的关键词参数
    '''
    def process_view(self,request,view_func,view_args,view_kwargs):
        print('process_view的参数：view_func')
        print(view_func)
        print('process_view的参数：view_args')
        print(view_args)
        print('process_view的参数：view_kwargs')
        print(view_kwargs)
        return None


class middlewareStudy2(MiddlewareMixin):
    # 处理请求的中间件
    def process_request(self,request):
        print('这是第二个处理请求的中间件')
        return None

    # 处理响应的中间件
    def process_response(self,request,resopnse):
        print('这是第二个响应中间件')
        return HttpResponse('这是第二个响应中间件')