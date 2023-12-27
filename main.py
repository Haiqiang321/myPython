# _*_coding:utf-8_*_

list1 = list()
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (i != k):
                # print(i, j, k)
                num = 100*i + 10*j + k
                # print(num)
                list1.append(num)


print(list1)
length_list = len(list1)
print(length_list)
