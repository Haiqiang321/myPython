# _*_ coding:utf-8 _*_
import concurrent.futures
# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py


from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import os
import threading
import time

# maxWorks = 2
# threadPool = ThreadPoolExecutor(max_workers=maxWorks)
#
#
# def task(taskid, start_time):
#     time.sleep(1)
#     end_time = time.time()
#
#     print("任务id: %d\t线程名：%s\t完成时间： %d" % (taskid, threading.current_thread().name, end_time - start_time))
#     return taskid
#
#
# task_num = 4
# future_list = []
# start_time = time.time()
#
# for taskid in range(task_num):
#     future = threadPool.submit(task, taskid, start_time )
#     # future_list.append(future)
#     future_list.insert(0, future)

# for future in concurrent.futures.as_completed(future_list):
#     print("返回的任务名：%s" % future.result())
"""
Process
"""
#
# class ReuseProcess(multiprocessing.Process):
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#         self.daemon = True
#
#     def run(self):
#         while True:
#             func, args, kwargs = self.queue.get()
#             print("Hook1 进程名 %s" % os.getpid())
#             func(*args, **kwargs)
#             self.queue.task_done()
#
#     def add_new_task(self, func, *args, **kwargs):
#         print("Hook2 进程名 %s" % os.getpid())
#         self.queue.put((func, args, kwargs))
#
#     def join(self):
#         print("Hook3 进程名：%s" % os.getpid())
#         self.queue.join()
#
#
# def func(name):
#     print("Hook4 进程名 %s" % (os.getpid()))
#     time.sleep(1)
#     print(name)
#
#
# if __name__ == '__main__':
#     print("Hook5 进程名 %s" % (os.getpid()))
#     queue = multiprocessing.Manager().Queue()
#     process = ReuseProcess(queue)  # 新建可复用的进程
#     process.start()
#     process.add_new_task(func, "任务1")
#     process.add_new_task(func, "任务2")
#     process.join()
#     process.kill()

"""
multiProcess.Pool
"""

#
# def process_action(name, start_time):
#     end_time = time.time()
#     time.sleep(5)
#     print("任务名:%s\t进程ID:%d\t经历时间:%d" % (name, os.getpid(), end_time-start_time))
#
#
# if __name__ == '__main__':
#     ProcessPool = multiprocessing.Pool(processes=2)
#     start_time = time.time()
#     ProcessPool.apply_async(func=process_action, args=("任务1", start_time))
#     ProcessPool.apply_async(func=process_action, args=("任务2", start_time))
#     ProcessPool.apply_async(func=process_action, args=("任务3", start_time))
#     ProcessPool.apply_async(func=process_action, args=("任务4", start_time))
#     print("主进程结束")
#     ProcessPool.close()
#     ProcessPool.join()

""""
线程 和 进程并存
"""

thread_workers = 2
threadExecutor = ThreadPoolExecutor(max_workers=thread_workers)


def thread_action(task_id, start_time):
    time.sleep(1)
    end_time = time.time()
    print("进程ID：%d\t线程ID: %s\t任务ID: %s\t完成时间：%d" % (os.getpid(), threading.current_thread().name, task_id, end_time - start_time))


def process_action(task_id, start_time):
    time.sleep(0.1)
    threadExecutor.submit(thread_action, task_id, start_time)


if __name__ == '__main__':
    ProcessExecutor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    # print(ProcessExecutor.__dict__)
    start_time = time.time()
    for i in range(8):
        future = ProcessExecutor.submit(process_action, i, start_time)
        # print(future.result())

    ProcessExecutor.shutdown()





