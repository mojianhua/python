class Request(object):
    def __init__(self,obj):
        self.obj = obj

    @property
    def user(self):
        return self.obj.authticate()

class Auth(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def authticate(self):
        return self.name


class APIView(object):
    def dispatch(self):
        self.f2()

    def f2(self):
        a = Auth('JIM',12)
        req = Request(a)
        print(req.obj)
        print(req.user)

obj = APIView
obj.dispatch()