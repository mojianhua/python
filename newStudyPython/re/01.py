import random
#大于等于1且小于5整数
print(random.randint(1,5))
#大于等于1且小于10的奇数
print(random.randrange(1,10,2))
#随机返回一个，传列表
print(random.choice([1,2,3,4,[4,2]]))
#在列表中返回指定的个数,一下返回2个
print(random.sample([1,2,3,4,5],2))
#打乱类别顺序
item = [2,1,4,5,67]
random.shuffle(item)
print(item)