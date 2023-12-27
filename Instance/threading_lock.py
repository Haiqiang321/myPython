# _*_ coding:utf-8 _*_
import datetime
import threading
import time

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

from threading import Thread, current_thread, Lock
from concurrent.futures import ThreadPoolExecutor
from random import choice
from multiprocessing import Process
import queue
import time

"""
daemon
"""
#
# def shopping():
#     while True:
#         print("Andy 进入了商场")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     thread1 = threading.Thread(target=shopping, daemon=True)
#     thread1.start()
#
#     print("Andy 买了西红柿")
#     time.sleep(0.5)
#     print("Andy 买了土豆")
#     time.sleep(0.5)
#     print("Andy 离开了商场")

"""
join()
"""
#
# def target():
#     if current_thread().name == "1":
#         print(f"主线程sleep 2秒")
#         time.sleep(5)
#     else:
#         print(f"非主线程sleep 4秒")
#         time.sleep(6)
#
#     print(f"线程{current_thread().name} 已退出")
#
#
# thread1 = Thread(target=target, daemon=True, name="1")
# thread2 = Thread(target=target, daemon=True, name="2")
#
# thread1.start()
# thread2.start()
#
# print("程序因线程1陷入阻塞")
# thread1.join(timeout=2)
# print("程序因线程2陷入阻塞")
# thread2.join(timeout=2)
# print("主线程已退出")

#############################################
"""
Lock
"""
# book_num = 100
# bookLock = Lock()
#
#
# def books_lease():
#     global book_num
#
#     while True:
#         bookLock.acquire()
#         book_num -= 1
#         print(f"借走1本书，现存图书为{book_num}")
#         bookLock.release()
#         time.sleep(1)
#
#
# def books_return():
#     global book_num
#
#     while True:
#         bookLock.acquire()
#         book_num += 1
#         print(f"归还1本书，现存图书为{book_num}")
#         bookLock.release()
#         time.sleep(2)
#
#
# if __name__ == '__main__':
#     thread_lease = Thread(target=books_lease)
#     thread_return = Thread(target=books_return)
#
#     thread_lease.start()
#     thread_return.start()

#########################################################
"""
queue
"""
# q = queue.Queue(maxsize=5)
# deallist = ["红烧猪蹄", "卤鸡爪", "酸菜鱼", "糖醋里脊", "九转大肠", "阳春面"]
#
#
# def cooking(chefname:str):
#     for i in range(4):
#         deal = choice(deallist)
#         q.put(deal, block=True)
#         print(f"厨师{chefname}带来了一道{deal}")
#
#
# def eating(custom: str):
#     for i in range(3):
#         deal = q.get(block=True)
#         print(f"顾客{custom} 吃掉了{deal}")
#         q.task_done()
#
#
# if __name__ == '__main__':
#     threadlist_chef = [Thread(target=cooking, args=chefname).start() for chefname in ["A", "B", "C"]]
#     threadlist_custom = [Thread(target=eating, args=str(custom)).start() for custom in range(4)]
#
#     q.join()
################################
"""
Flag: kill process
"""

# flag = True
# lock = Lock()
#
#
# def tar():
#     global flag, lock
#
#     while True:
#         lock.acquire()
#         """
#         线程逻辑
#         """
#         time.sleep(0.5)
#         print(time.time())
#         if flag is False:
#             print("时间到，线程已被杀死！")
#             break
#         lock.release()
#     lock.release()
#
#
# if __name__ == '__main__':
#     thread1 = Thread(target=tar)
#     thread1.start()
#
#     print("等待3秒，线程将被杀死！")
#     time.sleep(3)
#     flag = False

"""
# ThreadPoolExecutor
"""
# tasklist = ["task1", "task2", "task3", "task4"]
#
#
# def task(taskname: str):
#     time.sleep(5)
#     print(taskname + "已完成\n")
#     return taskname + "的执行结果"
#
#
# executor = ThreadPoolExecutor(max_workers=3)
# future_a = executor.submit(task, tasklist[0])
# future_b = executor.submit(task, tasklist[1])
# future_c = executor.submit(task, tasklist[2])
# future_d = executor.submit(task, tasklist[3])
# print(future_a.result(), future_b.result())

"""
multiprocessing
"""

#
# def task(proName: int):
#     print("This is Process{}".format(proName))
#
#
# if __name__ == '__main__':
#     proc1 = Process(target=task, args=(1,))
#     proc2 = Process(target=task, args=(2,))
#
#     proc1.start()
#     proc2.start()
#######################################
"""

"""
# num = 0
# lock = threading.Lock()
#
#
# def add():
#     with lock:
#         global num
#         for i in range(10000000):
#             num += 1
#         print("The status of lock is: ", lock.locked())
#
#
# def sub():
#     lock.acquire()
#     global num
#     for i in range(10000000):
#         num -= 1
#     lock.release()
#
#
# thread1 = Thread(target=add)
# thread2 = Thread(target=sub)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
#
# thread2.join()
#
# print("The num is:", num)
#######################################333

"""
conditionLock
"""
# currentRunThreadNum = 0
# maxThreadNum = 10
#
# conLock = threading.Condition()
#
#
# def task():
#     global currentRunThreadNum
#     thName = threading.current_thread().name
#
#     conLock.acquire()
#     print("start and wait run thread: %s" % thName)
#
#     conLock.wait()
#
#     currentRunThreadNum += 1
#     # print("The current thread num is: %s" % currentRunThreadNum)
#     print("carry on run thread: %s" % thName)
#     conLock.release()
#
#
# if __name__ == '__main__':
#     for i in range(maxThreadNum):
#         subThread = Thread(target=task)
#         subThread.start()
#
#     while currentRunThreadNum < maxThreadNum:
#         notifyNumer = int(input("please enter the number of threads that needs to be notified to run: "))
#
#         conLock.acquire()
#         time.sleep(5)
#         conLock.notify(notifyNumer)
#         conLock.release()
#
#     print("main thread ends!")

#################################################
"""
EventLock
"""
# maxTheadNum = 3
#
#
# def task():
#     thName = threading.current_thread().name
#
#     print("start and wait run thread %s" % thName)
#
#     eventLock.wait()
#
#     # main func, set()
#     print("green light, %s carry on run" % thName)
#
#
#     #main func, clear()
#     print("red light, %s stop run" % thName)
#     print("*"*20)
#
#     eventLock.wait()
#     #main func, set()
#     print("green light, %s carry on run" % thName)
#
#     print("sub thread %s run end" % thName)
#
#
# if __name__ == '__main__':
#
#     eventLock = threading.Event()
#
#     for i in range(maxTheadNum):
#         subthread = Thread(target=task)
#         subthread.start()
#
#     print("the now is: ", time.time())
#     eventLock.set()
#     print("green light, and wait 5 seconds")
#
#
#     time.sleep(5)
#     print("the now is: ", time.time())
#     eventLock.clear()
#     time.sleep(3)
#     eventLock.set()
################################

"""
semaphore
"""

# maxSubThreadNum = 6
#
#
# def task():
#     thName = threading.current_thread().name
#
#     semaLock.acquire()
#     print("run sub thread %s " % thName)
#     time.sleep(3)
#     semaLock.release()
#
#
# if __name__ == '__main__':
#     semaLock = threading.Semaphore(2)
#
#     for i in range(maxSubThreadNum):
#         subThread = threading.Thread(target=task)
#         subThread.start()

######################################

for func in threading.Condition.__dict__:
    print(func)



