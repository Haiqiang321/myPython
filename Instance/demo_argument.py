# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py
import argparse

parser = argparse.ArgumentParser(description='参数解析示例')

parser.add_argument('-gf', '--girlfriend', choices=['wuqian', 'zhanghuan'])
parser.add_argument('--house', type=int, default=0)
parser.add_argument('food')

args = parser.parse_args()
print('-----args---', args)
print('----gf----', args.girlfriend)
print('--------food---------', args.food)
print(dir(args))
print(dir(parser))