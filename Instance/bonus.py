# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/11/21 22:17
# @FileName :profit.py

def bonus(profit):
    array1 = [1000000, 600000, 400000, 200000, 100000, 0]
    rate = [0.01, 0.015,  0.03,    0.05,  0.075,  0.1]
    r = 0

    for i in range(6):
        if profit > array1[i]:  # for example 25w, i = 2
            r += (profit - array1[i])*rate[i]
            profit = array1[i]

    return r


result = bonus(120000)
print(result)

