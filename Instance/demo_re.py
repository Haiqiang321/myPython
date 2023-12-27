# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py
import re

# re.math()
"""content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match("^Hello\\s\\d+\\s\\w{10}.*?Demo$", content)
print(result)
print(result.group())
print(result.span())"""

# re.search()
"""str = "手机号：123456789, 银行卡号：123456"
patten = "号：(.*?),"
res = re.search(patten, str)
print(res.group(0))
print(res.group(1))"""

# re.sub()
"""str = "https://python.org, https://epubit.com,"
patten1 = "http"
patten2 = "https"
res = re.sub(patten2, patten1, str)
print(res)"""

# re.split()
res = re.split(r'\W+', 'Books, books, books.')
print(res)