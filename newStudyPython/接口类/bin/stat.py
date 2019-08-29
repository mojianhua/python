import time
import sys
import os
from core import core
from core import InterfaceStudy
# 获取当前路径
# print(os.getcwd())
# # 要包含当前目录上一级目录
# print(os.path.dirname(os.getcwd()))
# # 然后把整个路面导入到sys.path里面就能全局调用
sys.path.append(os.path.dirname(os.getcwd()))
# 异常处理
if __name__ == '__main__':
    # alipay = InterfaceStudy.pay(InterfaceStudy.Alipay,300)
    # wc = InterfaceStudy.pay(InterfaceStudy.Wechar,900)
    applePay = InterfaceStudy.pay(InterfaceStudy.ApplePay,255)
    # print(applePay.money)