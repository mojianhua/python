l = [1,2,3,4]
iterator = l.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# Interable迭代器，含有__inter__都可迭代的
# [].__inter__() 迭代 --->__next__  #通过next可以从迭代器中一个一个的取值
# 只用__iner__就是可迭代的
# 可以被for循环的都是可迭代的 
# 可迭代的__iner__()的可以得到一个迭代器
# 内部有__next__和__iter__方法的就是迭代器
# print('__iter__' in dir([].__iter__()))

from collections import Iterable      # 是否迭代器
from collections import Iterator      # 是否可迭代
print(isinstance([],Iterable))
print(isinstance([],Iterator))