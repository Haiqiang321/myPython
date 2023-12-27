# _*_ coding:utf-8 _*_
import time


# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

# def addition(func):
#     def inner(a, b):
#         print("number are", a, "and", b)
#         return func(a, b)
#     return inner
#
#
# @addition
# def add(a, b):
#     print("The sum is: ", end="")
#     return a + b
#
#
# print(add(2, 3))

# def outer(num):
#     print(f"The base num is {num}")
#
#     def inner(num1):
#         print(f"The sum is: {num + num1}")
#
#     return inner
#
#
# func = outer(100)
# # func(10)
# func(20)

"""
案例需求：
原函数： comment()  一个评论功能
新的需求：在评论之前，检查是否登录
"""


# def login_check(fn):
#     def inner():
#         print("登陆验证中。。。。。")
#         fn()
#
#     return inner
#
#
# @login_check
# def comment():
#     print("进行评论。。。。。。")
#
#
# comment()

"""

func()
需求：统计函数执行所消耗的时间（新）
1.执行函数前记录当前时间
2.执行函数
3.函数执行结束之后，再次记录当前时间（新）
两次的时间差就是就是函数执行的时间
"""

#
# def calc_time(func):
#     def inner():
#         start = time.time()
#         print(f"开始时间为：{start}")
#         func()
#         end = time.time()
#         print(f"结束时间为：{end}")
#         print(f"函数耗时为：{end - start}秒")
#
#     return inner
#
#
# @calc_time
# def func():
#     for i in range(10):
#         print(i, " ", end="")
#         time.sleep(0.5)
#     print("函数执行完毕")
#
#
# # if __name__ == '__main__':
#
# func()

"""
实现统计函数执行的次数功能
"""


# def func_count():
#     num = 0
#
#     def inner():
#         nonlocal num
#         num += 1
#         print("Hello, world!")
#         print(f"共执行次数{num}")
#     return inner
#
#
# f = func_count()
# f()
# f()
# f()

"""
一个函数，返回一个字符串，使用装饰器实现对这个字符串添加后缀.txt
"""


def add_extension(func):

    def inner(info):
        res = func(info)
        return res + ".txt"

    return inner


@add_extension
def comment(info):
    return info


print(comment("hello"))