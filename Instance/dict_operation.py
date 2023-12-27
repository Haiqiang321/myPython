# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

dict_ = {
    "name": "Xiaomi",
    "age": 23
}
# print(dict_["name"])
# print(dict_.get("name"))

# print(dict_.pop("age"))
# print(dict_.keys())
# print(dict_.values())
# print(dict_.items())

# for key, value in dict_.items():
#     print(f"{key} -> {value}")

# for key in dict_.keys():
#     print(f"{key} - >{dict_[key]}")
#
# dict_1 = dict([["name", "xiaoming"]])
# print(dict_1)
# dict_2 = {"age": 23}
# print(dict_2)
# dict_1.update(dict_2)
# print(dict_1)

dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
print(dic.items())
dic_new = sorted(dic.items(), key=lambda x: x[0], reverse=False)
print(dic_new)

