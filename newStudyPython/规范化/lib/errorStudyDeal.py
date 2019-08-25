# 异常处理
def errorStudyDeal():
    # # 指定处理异常类型
    # try:
    #     ret = int(input("请输入数字》》》》"))
    #     print(ret * ret)
    # except ValueError:
    #     # 如果错误显示的内容
    #     # 这个是错误输入类型错误
    #     print('输入内容有错，请输入一个数字')
    # except ImportError:
    #     print('超出列表长度')

    # 万能异常，处理所有的异常
    try:
        print(1)
        ret = int(input("请输入数字》》》》"))
        1/0
        name
        2+'3'
        ret = int(input("请输入数字》》》》"))
    # except ValueError:
    #     print('输入内容有错，请输入一个数字')
    except Exception as e:
        # as e 获取错误信息
       print(e)
    else:
        print('没报错正常！！！')
    finally:
        print('无论错误正常都执行。程序最后都要执行的，遇到return都会执行，除了exit')