'''
用ZooKeeper作分布式锁
'''

from multiprocessing import Pool
import os
import arrow
import redis
from kazoo.client import KazooClient

HOT_KEY = 'count'
conn = redis.Redis(host='192.168.118.123',port='6379',password='1qa2ws#ED',db=1)

def seckilling():
    # 进程号
    name = os.getpid()
    v = conn.get(HOT_KEY)
    if int(v) > 0:
        print(name,'decr redis.')
        conn.decr(HOT_KEY)
    else:
        print(name,' can not set redis.',v)

def run_with_lock(name):
    # 连接zookeeper
    zk = KazooClient(hosts='39.108.147.32:2182')
    # 启动连接
    zk.start()
    # 创建锁
    lock = zk.Lock("/lockpath", "my-identifier")
    while True:
        # 获取当前秒数，当秒数为5时同时访问秒杀函数
        if arrow.now().second % 5 == 0:
            with lock:
                seckilling()
                return

if __name__ == '__main__':
    # 创建进程数，以下是16个进程
    p = Pool(16)
    conn.set(HOT_KEY, 1)
    for i in range(16):
        # 该函数用于传递不定参数，非阻塞的且支持结果返回后进行回调
        # 第一个参数传方法名，第二个参数传值
        p.apply_async(run_with_lock,args=(i,))
    print('现在16个进程将被锁定！')
    # 关闭进程池（pool），使其不在接受新的任务。
    p.close()
    # 主进程堵塞等待子进程的退出，join方法要在close或terminate之后使用
    p.join()
    print('全部执行完')