# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

import queue

"""
PriorityQueue
"""
#
# class dic:
#     def __init__(self, level, data):
#         self.level = level
#         self.data = data
#
#     def __lt__(self, other):
#         if self.level == other.level:
#             return len(self.data) < len(other.data)
#         return self.level < other.level
#
#
# queue_obj = queue.PriorityQueue()
# queue_obj.put(dic(5, {1:4, 2:5}))
# queue_obj.put(dic(3, {1:4}))
# queue_obj.put(dic(5, {1:2}))
#
# while not queue_obj.empty():
#     print(queue_obj.get().data)
#     print(queue_obj.qsize())
#     if queue_obj.empty():
#         print("空了！")

########################################

"""
Queue Expectation
"""
queue_obj = queue.Queue(3)

for item in range(3):
    try:
     queue_obj.put(item, block=False)
    except queue.Full as msg:
        print(msg)

for i in  range(4):
    queue_obj.get(timeout=5)