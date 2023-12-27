# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py
#
# with open(file="charging.log", mode="r", encoding="utf-8") as fh:
#     for line in fh:
#         print(line.strip())
#
#     # print(fh.tell())

"""
备份文件
"""
# import os
#
# file_name = input("请输入一个文件路径：")
# if os.path.isfile(file_name):
#     with open(file_name, mode="rb") as fh_old:
#         temp = os.path.splitext(file_name)
#         new_file = temp[0] + ".bak" + temp[1]
#
#         with open(new_file, mode="wb") as fh_new:
#             while True:
#                 content = fh_old.read(1024)
#                 fh_new.write(content)
#
#                 if not content:
#                     break
# else:
#     print("文件不存在，请确认！")
#
# """
# file path
# """
# file_path1 = r"D:\workshop\code\python\mypython\output.txt"
# file_path2 = "D:\\workshop\\code\\python\\mypython"
# file_path3 = "D:/workshop/code/python/mypython"
#
#
# print(file_path3)
# print(file_path2)
# print(file_path1)

# fh = open(file_path1, mode="r", encoding="utf-8")
# fh.seek(0, 2)
# res = fh.read(23)
# print(type(res))

"""
CSV 文件
"""

# import csv
#
# with open("file.csv", mode="w", encoding="utf-8", newline="") as fh:
#     writer = csv.writer(fh, delimiter=":")
#     # writer.writerow(["hi, python!"])
#     writer.writerows([["name", "age", "gender"], ["Andy", 23, "male"]])
#
# with open("file.csv", mode="r", encoding="utf-8") as fh_r:
#     reader = csv.reader(fh_r)
#     print(type(reader))
#     # print(reader.line_num)
#
#     for line in reader:
#         print(line)


"""
sys module
"""
import sys

# sin = sys.stdin
# while True:
#     content = sin.readline().rstrip("\n")
#     if content == "":
#         break
#     print(content)

# with open("output.txt", mode="w", encoding="utf-8") as fh_w:
#     sys.stdout = fh_w
#     print("hello, 2024")
#     print("加油！")

# with open("output.txt", mode="w", encoding="utf-8") as fh_w:
#     sys.stdout = fh_w
#     print([1, 2, 3])
