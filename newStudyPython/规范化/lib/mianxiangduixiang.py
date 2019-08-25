# 面向对象
def Persion(name,hp,ack,sex):
    persion = {
        'name': name,
        'hp': hp,
        'ack': ack,
        'sex': sex
    }
    # 人攻击
    def attck(dog):
        dog['hp'] = int(dog['hp']) - int(persion['ack'])
        print('%s 被打了，掉了%s的血' % (dog['name'], persion['ack']))
    persion['attck'] = attck
    return persion

def Dog(name,hp,ack,king):
    dog = {
        'name': name,
        'hp': hp,
        'ack': ack,
        'king': king,
    }
    # 狗咬人
    def bite(persion):
        persion['hp'] = int(persion['hp']) - int(dog['ack'])
        print('%s 被咬了，掉了%s的血' % (persion['name'], dog['ack']))
    dog['bite'] = bite
    return dog

def mianxiangduixiang():
    print('mianxiangduixiang')
    dog1 = Dog('Dog1', '12', '1', '2哈')
    # print(dog1)
    jim1 = Persion('Jim1','100','2','boy')
    dog1['bite'](jim1)
    jim2 = Persion('Jim2','200','2','man')
    jim2['attck'](dog1)