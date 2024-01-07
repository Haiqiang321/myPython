# _*_ coding:utf-8 _*_
import argparse
import sys


# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py


def parse_arg():
    parser = argparse.ArgumentParser(description="for func parameter")
    parser.add_argument("-n", "--name", metavar="", type=str, required=True, default="Xiaoming", help="the name of student")
    parser.add_argument("-a", "--age", metavar="", type=int, required=True, default=20, help="the age of student")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-b", "--brief", action="store_true", help="print brief description")
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose description")

    args = parser.parse_args()
    return args


def func(name, age):
    print(f"{name} is {age} years old")


if __name__ == '__main__':
    args = parse_arg()

    print(sys.argv)

    if args.brief:
        print("print result briefly")
    elif args.verbose:
        print("print result verbosely")
    else:
        func(args.name, args.age)



