# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

def num_sun(*args):
    result = 0
    for num in args:
        result += num
    return result


tup1 = (1, 3, 5, 7, 9)
print(num_sun(*tup1))


def std_info(**kargs):
    print(f"you name: {kargs.get("name")}")
    print(f"you age: {kargs.get("age")}")


std1 = {"name": "Andy", "age": 25}

std_info(**std1)