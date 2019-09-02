# 封装
class Room:
    def __init__(self,name,length,width):
        self.__name = name
        # 私有
        self.__length = length
        self.__width = width

    # 获取私有属性的name
    def get_name(self):
        return self.__name

    # 更新私有属性里面的name
    def set_name(self,newName):
        if type(newName) is str and newName.isdigit() == False:
            self.__name = newName

    def area(self):
        return self.__length * self.__width