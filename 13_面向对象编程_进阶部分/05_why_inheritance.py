# 创建父类Student
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        __score = None
        gender = None

    def show_info(self):
        print(f"name = {self.name} age = {self.age} score = {self.__score}")

    def set_score(self, score):
        self.__score = score

# 创建小学生类
class Pupil(Student):

    def testing(self):
        print("--小学生在考小学数学--")

# 创建大学生类
class Graduate(Student):

    def testing(self):
        print("--大学生在考小学数学--")


# 测试
student1 = Pupil('apple', 10)
student1.testing()
student1.set_score(80)
student1.show_info()

print()
student1 = Graduate('banana', 20)
student1.testing()
student1.set_score(80)
student1.show_info()