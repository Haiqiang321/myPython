# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py


# class Func(object):
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("create a new instance")
#     #     if not hasattr(cls, "_ins"):
#     #         cls._ins = super(__class_, cls).__new__(cls, *args, **kwargs)
#     #         setattr(cls, "_ins", )
#     #     return cls._ins
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#         # self.file = open(file="../output.txt", mode="w")
#
#     def __call__(self, *args, **kwargs):
#         print("The __call__ magic method, my name is: %s" % self.name)
#
#     def __str__(self):
#         # return "The __str__ magic method, my name: {}".format(self.name)
#         # return f"Object of {type(self).__name__} at {hex(id(self))}"
#         if self.gender == "male":
#             return f"Mr.{self.name}"
#         elif self.gender == "female":
#             return f"Ms.{self.name}"
#         else:
#             return f"{self.name}"
#
#     def __repr__(self):
#         return f"The __repr__ magic method, my name:{self.name}"
#
#     def __len__(self):
#
#         return len(self.name)
#
#
# ins1 = Func("Andy", "male")
# # ins2 = Func("Angel", "female")
# print(ins1)
# # print(ins2)
# print(len(ins1))


"""
__getitem__
"""


# class Test:
#     def __init__(self, data):
#         self.data = data

    # def __getitem__(self, index):
    #     try:
    #         return self.data[index]
    #     except IndexError as msg:
    #         print(msg)

        # for i, item in enumerate(self.data):
        #     if i == index:
        #         return item
        # raise IndexError("Index out of range")

    # def __setitem__(self, index, value):
    #     for i, item in enumerate(self.data):
    #         if i == index:
    #             self.data[index] = value
    #             return
    #     raise IndexError("Index out of range.")
    #
    # def __delitem__(self, key):
    #     del self.data[key]
    #
    # def __getattr__(self, item):
    #     # return f"{item} attribute is not there"
    #
    #     if item == "name":
    #         return "Andy"
    #     else:
    #         raise AttributeError(f"{self.__class__.__name__} object has no attribute '{item}'")

    # def __setattr__(self, key, value):
        # if key == "name":
        #     raise AttributeError(f"'{key}' attribute is there, you could not modify!")
        # else:
        #     self.__dict__[key] = value
        #
    # def __setattr__(self, name, value):
    #     print(f"setting attribute: {name} = {value}")
    #     self.__dict__[name] = value

#     def __call__(self, *args, **kwargs):
#         # print(f"The data is {self.data}")
#         return self.data + list(args)
#
#
# if __name__ == '__main__':
#     test = Test([1, 2, 3, 4, 5])
#     result = test([6, 7, 8])
#     print(result)

###########################################################

# class Decorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Before calling function")
#         res = self.func(*args, **kwargs)
#         print("After calling function")
#         # print(type(res))
#         return res
#
#
# @Decorator
# def my_function():
#     print("Inside my_function")
#
#
# my_function()
############################################################

"""
__iter__, __next__
"""

#
# class MyIterable:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         return MyIterator(self.data)
#
#
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
#
# my_iterable = MyIterable([1, 2, 3, 4, 5])
#
# # print(next(my_iterable))
# for num in my_iterable:
#     print(num)

######################################################
"""
__name__
"""

#
# def func():
#     pass
#
#
# print(func.__name__)
#
#
# class Nation:
#     pass
#
#
# print(Nation.__name__)
############################################

import num_convert

class A:
    pass


class B(A):
    pass


class C:
    pass


obj = B()
# print(obj.__class__.__bases__)
# obj.__class__ = C
# print

print(obj.__module__)
print(B.__name__)
# print(num_convert.__name__)

