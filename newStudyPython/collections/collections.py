from collections import namedtuple
# 可命名元祖，坐标的时候可以用
Point = namedtuple('point',['x','y'])
p = Point(1,2)
print(p)
print(p.x)
print(p.y)

Card = namedtuple('card',['suits','num'])
c1 = Card('红心',2)
print(c1)

# deque 双端队列

# 队列，先进先出，堆栈，先进后出
import queue
#创建队列
q = queue.Queue()
#往队列添加数据
q.put(10)
q.put(5)
q.put(6)
# 从队列里面获取数据，如果数据不够的话，会造成堵塞
print(q.get())
print(q.get())
print(q.get())
# 查看队列剩下大小
print(q.qsize())

# 双端队列
from collections import deque
# 重建队列
dq = deque([1,2])
dq.append('a') #从后面放数据
dq.appendleft('b') #从前面插入数据
dq.insert(2,3)     #（指定下标，要插入的数据）指定下标，指定数据后面插入数据
print(dq.pop())      # 从后面取数据
print(dq.popleft())  # 从前面取数据

# 字典排序
from collections import OrderedDict
from collections import defaultdict
od = OrderedDict([('c',3),('a',1),('b',2)])
print(od['b'])
# for i in od:
#     print(i)

# 如果字典的key的值不存在设置默认值，defaultdict
my_dict = defaultdict(list)
print(my_dict['k'])

# 如果要想设置默认字符串，则可以定义一个匿名函数
d = defaultdict(lambda : 5)
print(d['a'])

# 计算器,统计每个字节数
from collections import Counter
c = Counter('sfsaff123131sdfsfsgsg312')
print(c)