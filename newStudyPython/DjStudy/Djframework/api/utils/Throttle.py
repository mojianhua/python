import time
from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
# 访问频率限制
VISIT_RECORD = {}
# class VisteThrottle(BaseThrottle):
#
#     def __init__(self):
#         self.history = None
#
#     # 60s内只能访问3次
#     def allow_request(self,request,view):
#         # 获取用户ip
#         remote_addr = request.META.get('REMOTE_ADDR')
#         ctime = time.time()
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [ctime,]
#             return True
#
#         # 通过ip作为下标访问查询时间
#         history = VISIT_RECORD.get(remote_addr)
#         self.history = history
#
#         # 当最旧的时间大于当前时间减60s,则从尾部删除最旧的一个时间
#         while history and history[-1] < ctime - 60:
#             history.pop()
#
#         # 当访问次数少于3，则从大字典里面记录访问时间
#         if len(history) < 3:
#             history.insert(0,ctime)
#             return True
#
#         # return Ture可以访问
#         # return False不可以访问
#
#     def wait(self):
#         # 还需要多少时间才能访问
#         ctime = time.time()
#         return 60 - (ctime - self.history[-1])


# 内置访问次数限制
class VisteThrottle(SimpleRateThrottle):
    # 跟setting.py里面的DEFAULT_THROTTLE_RATES
    scope = 'JimLimit'
    # 60s内只能访问3次
    def get_cache_key(self,request,view):
        # 返回唯一标识，以下是ip作为唯一标识
        return self.get_ident(request)


# 内置访问次数限制
class UserVisteThrottle(SimpleRateThrottle):
    scope = 'JimLimitUser'

    # 60s内只能访问3次
    def get_cache_key(self, request, view):
        return request.user.username