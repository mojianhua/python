import time
import sys
import os
from core import core
# 获取当前路径
# print(os.getcwd())
# # 要包含当前目录上一级目录
# print(os.path.dirname(os.getcwd()))
# # 然后把整个路面导入到sys.path里面就能全局调用
sys.path.append(os.path.dirname(os.getcwd()))
# 异常处理
from lib import errorStudyDeal
from lib import mianxiangduixiang
from lib import classStudy
if __name__ == '__main__':
    # # 初始化框架
    # # core.main()
    # # 异常处理学习
    # # errorStudyDeal.errorStudyDeal()
    # # 面向对象
    # # mianxiangduixiang.mianxiangduixiang()
    # # 实例化类，调用加括号往类里面传值
    # 对象 = 类(参数是init方法)
    # retClass = classStudy.Persion('Jim',100,10,'boy')
    # print(retClass)
    # # 获取class里面的默认值
    # print(retClass.name)
    # retClass.walk(13)
    # # 调用类里面的静态方法,可以不用实例化的
    # print(classStudy.Persion.country)
    # # 类里面重现赋默认值
    # retClass.name = 'jim2'
    # print(retClass.name)
    retDog = classStudy.Dog('斯莱曼',100,13,'2哈')
    retPersion = classStudy.Persion2('真传奇',200,29,'boy')
    # 狗咬人
    #retDog.bite(retPersion)
    #print(retPersion.hp)
    # 人打狗
    #retPersion.attack(retDog)
    #print(retDog.hp)
    # while retDog.hp:
    #     retPersion.attack(retDog)
    #     # print(retPersion.name , retDog.hp)
    #     time.sleep(1)
    #     retDog.bite(retPersion)
    #     # print(retDog.name, retPersion.hp)
    #     time.sleep(1)

    # 计算圆
    # cirecle = classStudy.Circle(6)
    # ret = cirecle.area()
    # # 面积
    # print(ret)
    # ret = cirecle.perimeter()
    # print(ret)

    # 圆环计算
    # ring = classStudy.Ring(10,9)
    # print(ring.area())
    # print(ring.perimeter())

    # 生日
    # b = classStudy.Birthday(2011,1,16)
    # egg = classStudy.Teacher('sb1',0,'boy',b)
    # # 获取类里面的年纪
    # print(egg.birthday.year)
    # # 获取老师课程
    # print(egg.course.lesson)