# _*_ coding:utf-8 _*_
import time

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py


#
# class MyContextManager(object):
#     def __init__(self, filename, mode):
#         self.file = filename
#         self.mode = mode
#
#     def __enter__(self):
#         print("Entering the Manager.....")
#         self.open_file = open(self.file, self.mode)
#         return self.open_file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting the Manager .....")
#         self.open_file.close()
#         print("Type:", exc_type)
#         print("Value:", exc_val)
#         print("TraceBack:", exc_tb)
#
#         return True
#         # return False
#
#
# with MyContextManager("output.txt", mode="r") as fh:
#     print("In the Manager .....")
#     print(fh.write("Hello!"))

# from contextlib  import contextmanager
#
#
# @contextmanager
# def test():
#     print("this is __enter__")
#     yield "contextmanager demo"
#     print("this is __exit__")
#
#
# with test() as t:
#     print(f"result: {t}")


from contextlib import closing


class CloseDemo:
    def __init__(self):
        self.acquire()

    def acquire(self):
        print("lock data")

    def free(self):
        print("unlock data")

    def close(self):
        self.free()


with closing(CloseDemo()):
    print("use data")


