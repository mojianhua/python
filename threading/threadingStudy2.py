import threading
import time

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

# 多线程
class MyThread(threading.Thread):

    def __init__(self,sec):
        super(MyThread,self).__init__()
        self.sec = sec

    def run(self):
        print('%s 线程开始' % threading.current_thread().name)
        time.sleep(self.sec)
        print('%s 线程结束' % threading.current_thread().name)

if __name__ == '__main__':
    print('主线程开始', threading.current_thread().name)
    s_time = time.time()
    # 创建thread对象，target传入线程执行的函数，args传参数
    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)
    # 使用start执行
    t1.start()
    t2.start()
    t3.start()
    # 使用join()完成线程同步
    t1.join()
    t2.join()
    t3.join()
    print('主线程执行结束时间', threading.current_thread().name)
    print('一共用时：', time.time() - s_time)