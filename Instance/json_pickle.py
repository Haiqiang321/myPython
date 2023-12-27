# _*_ coding:utf-8 _*_
import pickle

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

dict1 = {"name": "Andy", "age25": 23}

string_convert = pickle.dumps(dict1)
print(type(string_convert))

print(pickle.loads(string_convert))
# with open("output.txt", mode="wb") as fh:
#     fh.write(string_convert)


# with open("output.txt", mode="wb") as fh:
#     pickle.dump(dict1, fh)
#
# with open("output.txt", mode="rb") as fh_r:
#     res = pickle.load(fh_r)
#     print(type(res))
#     print(res)

