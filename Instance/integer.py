# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/11/24 11:43
# @FileName :integer.py

for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
            n = (i-j)/2
            x = n*n - 100
            print(x)
