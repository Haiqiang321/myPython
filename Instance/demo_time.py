# _*_ coding:utf-8 _*_
import threading
# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

import threading
import os, time, random
from concurrent.futures import ThreadPoolExecutor

"""
def fun_thread(sec, tname):
    '''
    线程函数，用于修改线程的名称
    :param sec:
    :param tname:
    :return:
    '''
    print('启动线程', current_thread().name, ":", current_thread().is_alive())
    print('Setname 修改线程名字')
    current_thread().name = tname
    sleep(sec)
    print("{}线程结束".format(current_thread().name))


if __name__ == '__main__':
    threads = []  # 维护线程
    for i in range(3):
        t = threading.Thread(target=fun_thread, name='thread-%d'%i, args=(3, "My"+str(i)+'Thread'))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
"""
"""
loops = (4, 2)
# print(type(loops))


class MyThread(threading.Thread):
    def __init__(self, target, args):
        super().__init__()
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)


def loop(nloop, nsec):
    print(ctime(), 'start loop', nloop)
    sleep(nsec)
    print(ctime(), 'end loop', nloop)


def main():
    threads = []
    nloops = range(len(loops))
    print(nloops)
    for i in nloops:
        t = MyThread(loop, (i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()


if __name__ == '__main__':
    main()
"""


def task(n):
    print(f"子线程：{os.getpid()}正在执行")
    time.sleep(random.randint(1, 3))
    return n**2


if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=4)
    futures = []
    for i in range(1, 10):
        future = thread_pool.submit(task, i)
        futures.append(future)

    thread_pool.shutdown(True)

    # print(futures)
    for future in futures:
        print(future.result())

