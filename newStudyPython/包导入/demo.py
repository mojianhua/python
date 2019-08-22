# 可以约束这个包里面的方法和变量，可要配合 from demo import * 使用
__all__ = ['demo1','test_momny']
print('这是01.py')
test_momny = 1003
def demo1():
    print('这是demo里面的demo1')

def demo2():
    print('这是demo2222')

if __name__ == '__main__':
    demo2()