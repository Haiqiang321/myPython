# _*_ coding:utf-8 _*_
import pickle

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

"""
zip()
    zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
    
       >>> list(zip('abcdefg', range(3), range(4)))
       [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    
    The zip object yields n-length tuples, where n is the number of iterables
    passed as positional arguments to zip().  The i-th element in every tuple
    comes from the i-th iterable argument to zip().  This continues until the
    shortest argument is exhausted.
    
    If strict is true and one of the arguments is exhausted before the others,
    raise a ValueError.
"""

# lst1 = ["a", "b", "c"]
# lst2 = [1, 2, 3]
#
# res = zip(lst1, lst2)
# print(res)
#
# for item in res:
#     print(item)

"""
map
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.

"""
# tpl = (1, 2, 3, 4, 5)
#
#
# def add_1(num):
#     return num+1
#
#
# res = map(add_1, tpl)
# print(res)
#
# for item in res:
#     print(item)
