# 制作一个父类，如果子类方法不存在则直接调用父类里面的方法，目的是兼容错误
from abc import abstractclassmethod,ABCMeta
# 抽象类例子
class Payment(metaclass=ABCMeta):
    """
      @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
      @ property：方法伪装属性，方法返回值及属性值，被装饰方法不能有参数，必须实例化后调用，类不能调用
      @ classmethod：类方法，可以通过实例对象和类对象调用，被该函数修饰的方法第一个参数代表类本身常用cls，被修饰函数内可调用类属性，不能调用实例属性
      @staticmethod：静态方法，可以通过实例对象和类对象调用，被装饰函数可无参数，被装饰函数内部通过类名.属性引用类属性或类方法，不能引用实例属性
    """

    @abstractclassmethod
    def pay(self,money):
        # 如果没子类pay方法则直接执行改父类方法
        # 主动抛出一个错误
        # raise NotImplemented
        pass

class Alipay(Payment):
    def pay(self,money):
        print('已经使用支付宝支付了 %s 元' %money)

class Wechar(Payment):
    def pay(self,money):
        print('已经使用微信支付 %s 元' %money)

class ApplePay(Payment):
    # 因为收到父类的@abstractmethod 方法所以规定一定要有pay方法，不然报错
    def fuqian(self,money):
        print('已经使用applepay 支付了 %s 元' %money)

# 统一入口
class pay:
    def __init__(self,pay_obj,money):
        obj = pay_obj()
        obj.pay(money)


# 接口类

"""
  @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
  @ property：方法伪装属性，方法返回值及属性值，被装饰方法不能有参数，必须实例化后调用，类不能调用
  @ classmethod：类方法，可以通过实例对象和类对象调用，被该函数修饰的方法第一个参数代表类本身常用cls，被修饰函数内可调用类属性，不能调用实例属性
  @staticmethod：静态方法，可以通过实例对象和类对象调用，被装饰函数可无参数，被装饰函数内部通过类名.属性引用类属性或类方法，不能引用实例属性
"""

class Walk_Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def walk(self):
        print('walk')

class Fly_Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def fly(self):
        print('fly')

class Swim_Amimal(metaclass=ABCMeta):
    @abstractclassmethod
    def swim(self):
        print('swim')

# 因为继承了 Fly_Animal 和 Walk_Animal，所以类里面要有fly和walk类
class Eagle(Fly_Animal,Walk_Animal):
    __Eagle_name = 'Private_name'

    def __init__(self,age):
        # 私有属性,只能在内部使用
        self.__age = age
        print('Eagle')
        # 调用私有方法
        self.__private_get_age()
        # 调用私有的变量
        print(self.__Eagle_name)

    def fly(self):
        print(self.__age)
        print('eagle fly')

    def walk(self):
        print('eagle walk')

    # 设置私有方法
    def __private_get_age(self):
        print(self.__age)

e = Eagle(10)
e.fly()
# python没接口类
    # java没多基础，为了接口隔离原则，设计了接口这个概念，支持多继承
    # java本来就支持单继承，所以有了抽象类
    # python 中自带多继承，所以我们可以使用class实现接口类
# python 支持抽象类，一般情况下单继承不能实例化

# 多态-----pythont天生多态
# 鸭子类型---不依赖父类的情况下实现两个相似类中的同名方法

# 封装---私有的
# 再python只要名字有__名字，就开始私有化了

# 总结
    # 1、接口类是多继承，抽象类是单继承
    # 2、如果使用from abc import abstractclassmethod,ABCMeta就意味着你要定义一个规范
    # 2.1、      @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
    # 2.2、子类的方法只能多不能少，少了会报错
