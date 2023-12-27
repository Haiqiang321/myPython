# _*_ coding:utf-8 _*_
import time

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

from assertpy import assert_that

# dic = dict(a=4, b=5)
dic = {i :i*2 for i in [1, 2, 3]}

assert isinstance(dic, dict), f"{dic} is not a list"

assert_that(1+2, "expected 3 here").is_zero()


print(dic)