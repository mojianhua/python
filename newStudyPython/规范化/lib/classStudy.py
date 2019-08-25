class Persion:
    # 静态属性
    country = 'China'
    # 构造函数
    def __init__(self,*args):
        # 获取class的传的默认参数
        print(args)
        # 更新class的默认参数
        self.name = args[0]
        self.hp = args[1]
        self.ack = args[2]
        self.sex = args[3]
        # self 字典，可以存储很多属性的大字典
        print(self.__dict__)

    # 一般情况下必须有self,后面才跟其他参数
    def walk(self,age):
        print('%s走路,年级%s' %(self.name,age))

class Persion2:
    def __init__(self,*args):
        self.name = args[0]
        self.hp = args[1]
        self.ack = args[2]
        self.sex = args[3]

    def attack(self,dog):
        dog.hp = int(dog.hp) - int(self.ack)
        print('%s 被 %s 攻击, 伤了 %s 点血,还剩下 %s' % (dog.name,self.name,self.ack,dog.hp))
        if (int(self.hp) == 0):
            print('%s被 %s 击败了' % (dog.name,self.name))

class Dog():
    def __init__(self,*args):
        self.name = args[0]
        self.hp = args[1]
        self.ack = args[2]
        self.kind = args[3]

    def bite(self,persion):
        persion.hp = int(persion.hp) - int(self.ack)
        print('%s 被 % s 攻击, 伤了 %s , 还剩下 %s' % (persion.name,self.name,self.ack,persion.hp))
        if (int(self.hp) == 0):
            print('%s 被 %s 击败了' % (persion.name,self.name))