# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

import re
# names = ["name1", "_name", "2name"]
# pattern = r"[a-zA-Z_][\w]*"
# for name in names:
#     ret = re.match(pattern, name)
#     if ret:
#         print("变量名%s符合规范" % name)
#     else:
#         print(f"非法变量名{name}")

"""
匹配0-100的数字
"""
# ret = re.match(pattern=r"[1-9]?\d$|100", string='100')
# print(ret.group())

"""
匹配163邮箱
"""
# email_lst = ["xiaomi@163.com", "shanghai@163.comhi", "haiqiang0321@126.com"]
# pattern = r"[\w]{4,20}@(163|126|qq)\.com$"
# for email in email_lst:
#     if re.match(pattern, email):
#         print(f"{email}符合邮件地址规则")
#     else:
#         print("{0}不符合要求".format(email))

"""
匹配电话号码
"""
# tels_num = ["13100001234", "18912344321", "10086", "18800007777"]
# pattern = re.compile(r'1\d{9}[0-35-68-9]')
# print(type(pattern))
# for num in tels_num:
#     if pattern.match(num):
#         print(f'{num} 理想手机号')
#     else:
#         print("%s 不是想要的手机号" % num)

"""
提取区号和电话号码
"""
# tels = "0378-8639025"
# pattern = r"([0-9]{4})-(\d{7})"
#
# ret = re.match(pattern, tels)
# print(ret.group(1))
# print(ret.group(2))

"""
\num # 分组的引用
"""
# labels = ["<html><h1></h2>www.baidu.com</h1></html>", "<html><h1>www.itcast.cn</h2></html>" ]
# pattern = r"<(\w*)><(\w*)>.*</\2></\1>"
#
# for label in labels:
#     ret = re.match(pattern, label)
#     if ret:
#         print(f"{label}是符合要求的标签")
#     else:
#         print("%s 不符合要求" % label)


"""
(?P<name>) # 用于标记一个分组
(?P=name) #用于在同一个表达式中复用
"""
# labels = ["<html><h1></h2>www.baidu.com</h1></html>", "<html><h1>www.itcast.cn</h2></html>" ]
#
# pattern = re.compile(r'<(?P<web1>\w*)><(?P<web2>\w*)>.*</(?P=web2)></(?P=web1)>')
# for label in labels:
#     ret = pattern.match(label)
#     if ret:
#         print(f"{label} -> okay")
#     else:
#         print(f"{label} -> wrong!")


"""
匹配身份证
"""
# id_num = "410221198903025678"
#
# a = re.match(r'(?P<province>[0-9]{3})(?P<city>[0-9]{3})(?P<birthday>[0-9]{4})', id_num)
# print(a.groupdict())


"""
findall()
"""
# pattern = re.compile(r"\d+")
# # pattern = r"\d+"
# str1 = "python = 9999, c = 7890, c++ = 12345"
#
# # ret = re.findall(pattern, str1)
# ret = pattern.findall(str1)
# print(type(ret))
# print(ret)

"""
finditer()
"""
# pattern = re.compile(r"\d+")
# # pattern = r"\d+"
# str1 = "python = 9999, c = 7890, c++ = 12345"
#
# # ret = re.findall(pattern, str1)
# ret = pattern.finditer(str1)
# print(type(ret))
# # print(ret)
#
# for match in ret:
#     print(match.group())

"""
re.sub()
"""

#
# def add(temp):
#     strnum = temp.group()  # int（）参数必须是字符串，类似字节的对象或数字，而不是“re.Match”. 这里temp是re.Match 对象
#     num = int(strnum) + 1
#     return str(num)
#
#
# pattern = r"\d+"
# ret = re.sub(pattern, add, "python = 99")
# print(ret)

"""
subn
"""

# pattern = re.compile(r"(\w+) (\w+)")
# string1 = "i say, hello world!"
#
# ret = re.subn(pattern, r'\2 \1', string1)
# print(type(ret))
# print(ret)
#
#
# def func(m):
#     return m.group(1).title() + " " + m.group(2).title()
#
#
# print(re.subn(pattern, func, string1))

"""
r" "
"""
# mm = "c:\\a\\b\\c"
# print(mm)
# pattern = r"c:\\"
# ret = re.match(pattern, mm)
# print(ret.group())

"""
\b
"""
# pattern = r"e\b"
# str1 = "apepl"
#
# ret = re.search(pattern, str1)
# print(ret.group())

"""
非贪婪匹配
"""
# pattern = ".+?b"
# string1 = "abcabcabc"
#
# res = re.findall(pattern, string1)
# print(res)

