# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def user_info(self):
        print(f"name: {self.name}, age: {self.age}")


class Child1(Parent):
    def __init__(self, school):
        # super().__init__(name, age)
        self.school = school

    def student_info(self):
        print(f"school: {self.school}")


class Child2(Parent):
    def __init__(self, school, name, age):
        super().__init__(name, age)
        self.school = school

    def student_info(self):
        print(f"school: {self.school}")


if __name__ == '__main__':
    parent = Parent("dgw", 26)
    parent.user_info()

    child1 = Child1("清华")
    child1.student_info()
    # child1.user_info()

    child2 = Child2("whq", 25, "北大")
    child2.student_info()
    child2.user_info()
