# _*_ coding:utf-8 _*_
import time


# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

from collections.abc import  Iterator, Iterable
class Fibonacci:
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        ret = self.a

        if self.count < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return ret
        else:
            raise StopIteration


my_Fibonacii = Fibonacci(5)

for item in my_Fibonacii:
    print(item)
    time.sleep(2)

