# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

#
# def func_yield():
#     print("first time")
#     yield "1"
#     print("second time")
#     yield "2"
#     print("third time")
#     yield "3"
#     print("forth time")
#     yield "4"
#
#
# res = func_yield()
# print(type(res))
# # for item in res:
# #     print(item)
# print(hasattr(res, "next"))
# print(hasattr(res, "__iter__"))
#
# print(res.__next__())
# print(res.__next__())
##################################################
#
# def run(b):
#     a = 0
#     while True:
#         try:
#             if a >= b:
#                 raise StopIteration("到尽头了,")
#             yield a
#         except StopIteration as msg:
#             print(f"{msg}结束")
#             return 1
#         finally:
#             a += 1
#
#
# res = run(3)
# print(res.__next__())


# for i in run(3):
#     print(i)
##########################################

# def generator_func():
#     value1 = yield 1
#     print("Value1 is: ", value1)
#
#     value2 = yield 0
#
#     print("Value2 is: ", value2)
#
#     value2 = yield 3
#     value2 = yield 4
#
#
# g = generator_func()
# print(g.__next__())
# g.send("shanghai")
# print(g.send("shanghai"))
# print(g.send("shenzhen"))
# g.send("shenzhen")
# print(g.__next__())

# g.close()
# print(g.__next__())


# print(g.send(2))

# res = range(2)
# print(type(res))
##############################

def func():
    try:
        yield "Hello, world!"
    except ValueError as msg:
        print("Someting is wrong!")
    finally:
        print("End!")


print(func().__next__())
print(func().throw(ValueError))