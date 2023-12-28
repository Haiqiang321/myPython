# _*_ coding:utf-8 _*_
import concurrent.futures
import os
# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py


from concurrent.futures import ThreadPoolExecutor
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

import inspect

for item in inspect.getmembers(os, inspect.isbuiltin):
    print(item[0])

print(help(os.replace))
print()


