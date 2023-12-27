# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


def sort_key(company):
    return company[2]


companies.sort(key=lambda company: company[2], reverse=True)
print(companies)