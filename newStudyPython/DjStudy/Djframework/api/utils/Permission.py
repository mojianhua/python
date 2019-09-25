from rest_framework.permissions import BasePermission
# 权限设置
class SVIPPermisson(BasePermission):
    # 提示信息
    message = "必须是SVIP才能访问"
    def has_permission(self,request,view):
        if request.user.user_type == 3:
            return True
        return False

class OtherPermisson(BasePermission):
    def has_permission(self,request,view):
        if request.user.user_type != 3:
            return True
        return False