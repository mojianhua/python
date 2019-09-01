class A:   # 父类，基类，超类
    pass
    # def func(self):
    #     print('AAAA')

class B:    # 父类，基类，超类
    def func(self):
        print('bbbbb')
class AB_son(A,B):pass    # 子类，派生类
class A_son(A):pass          # 子类，派生类

# 查看，某个类继承哪些类
print(A_son.__bases__)
print(AB_son.__bases__)


class Animal:
    def __init__(self,name,ack,hp):
        self.name = name
        self.ack = ack
        self.hp = hp
    def attck(self):
        return self.name + 'attck'
# 人类继承动物
class Person(Animal):
    # 继承父类的__init__
    # 类似php的parent::construct()
    def __init__(self,name,ack,hp,sex):
        # 派生属性
        self.sex = sex
        # 继承父类属性
        super().__init__(name,ack,hp)
        # 查看是否能获取到父类的属性
        print(self.name)

    def attck(self):
        return 'son_' + self.name + '_attck'

jim = Person('Jim',123,1111,'boy')
# 直接调用人类继承的属性
print(jim.ack)
print(jim.sex)
# 调用子类里面的方法
print(jim.attck())


# 多继承
class C:
    pass
    # def func(self):
    #     print('CCCC')

class D(A,B,C):
    def func(self):
        print('dddd')

d = D()
# 找的顺序是A,B,C,D来找
d.func()

# 新式类，就是广度优先，继承顺序是从左往右
