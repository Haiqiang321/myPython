# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

import subprocess

# # output = result.stdout
# with open(file="output.txt", mode="w", encoding="utf-8") as fp:
#     res = subprocess.getoutput(cmd="tasklist")
#     res1 = subprocess.g
#     print(type(res))
#     fp.write(res)

# with open(file="output.txt", mode="r", encoding="utf-8") as fr:
#         for line in fr.readlines():
#                 print(line.split("")[0])

obj = subprocess.Popen(args=["tasklist"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("print(1)")
print(obj.stdout.read())
# print(obj.poll())
# print(out)
