class Person:
    # 构造方法
    def __init__(self, name, age):
        print(f"__init__执行了| {name} | {age}")
        # 把接受的值赋给属性
        self.name = name
        self.age = age

p1 = Person('kobe',20)
