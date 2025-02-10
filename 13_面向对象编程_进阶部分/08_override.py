'''
1.编写一个Person类,包括属性(name, age),构造方法,say()方法(介绍person的信息,并打招呼)
2.编写一个Student类,继承Person类,增加属性(id,score),以及构造方法,重写say()方法(返回自己的自我介绍)
3.分别创建实例,调用say方法
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"大家好，我是{self.name}，今年{self.age}岁。"

class Student(Person):
    def __init__(self, name, age, student_id, score):
        super().__init__(name, age)
        self.student_id = student_id
        self.score = score

    def say(self):
        return f"大家好，我是{self.name}，今年{self.age}岁，我的学号是{self.student_id}，成绩是{self.score}分。"

# 测试代码
person = Person("张三", 30)
student = Student("李四", 20, "2025001", 95)

print(person.say())  # 输出: 大家好，我是张三，今年30岁。
print(student.say())  # 输出: 大家好，我是李四，今年20岁，我的学号是2025001，成绩是95分。