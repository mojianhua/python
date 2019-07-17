import numpy as np
import matplotlib.pyplot as pt
#0至360的数,自增1
x = np.arange(0,720)
y = np.sin(2 * x * np.pi / 180.0)
z = np.cos(x * np.pi / 180.0)
#描绘(x坐标，y坐标，color = '颜色',lable ='说明')
pt.plot(x,y,color = 'blue',label="sin(2x)")
pt.plot(x,z,color = 'red',label="cos(x)")
#x轴限制长度
pt.xlim(0,720)
#y轴限制长度
pt.ylim(-1.2,1.2)
#y轴说明
pt.ylabel("Degreesssssss")
#x轴说明
pt.xlabel("Valuessss")
#图标标签
pt.title("sin function")
pt.legend()
pt.show()