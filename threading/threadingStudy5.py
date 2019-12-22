import threading
import time
import random

'''
主要参数
    threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    group 默认为 None，为了日后扩展 ThreadGroup 类实现而保留。
    target 是用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
    name 是线程名称。默认情况下，由 "Thread-N" 格式构成一个唯一的名称，其中 N 是小的十进制数
    args 是用于调用目标函数的参数元组。默认是 ()
    kwargs 是用于调用目标函数的关键字参数字典。默认是 {}。
    daemon表示线程是不是守护线程。
    
Thread类常用方法与属性
    run(): 用以表示线程活动的方法。
    start():启动线程活动。 
    join(timeout=None): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
    name：线程对象名字
    setDaemon()：设置是否为守护线程
'''

# 事件同步
class Server(threading.Thread):
    '''
        向列表中生产随机整数
    '''
    def __init__(self,integers,event):
        super(Server,self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        '''
            实现Thread的run方法。在随机事件向列表中添加一个随机数
        '''
        while True:
            integer = random.randint(0,256)
            self.integers.append(integer)
            print('%d 添加到列表中 %s 线程' % (integer,self.name))
            # 设置事件
            self.event.set()
            print('%s 设置事件' % self.name)
            # 发送事件
            self.event.clear()
            print('%s 发送事件' % self.name)
            time.sleep(1)

class Consumer(threading.Thread):

    '''
        从列表中的消费整数
    '''

    def __init__(self,integers,event):
        super(Consumer,self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        '''
            实现Thread的run方法，从列表中消费整数
        '''
        while True:
            # 等待事件被触发
            self.event.wait()
            try:
                integer = self.integers.pop()
                print('%d 删除线程数据 %s' % (integer, self.name))
            except IndexError:
                # catch pop on empty list
                time.sleep(1)



if __name__ == '__main__':
    integers = []
    event = threading.Event()
    t1 = Server(integers, event)
    t2 = Consumer(integers, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()