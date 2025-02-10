class Monster:
    name = '狮子'
    age = 30

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print(f"hi() {self.name} {self.age}")

    @staticmethod
    def ok():
        print('ok().......')

# 通过Class对象引用属性
print(f"{Monster.name} {Monster.age}")

# 通过类名调用静态方法
Monster.ok()

# 通过类名调用非静态成员方法
Monster.hi(Monster)

print("*" * 50)

# 创建Monster类的实例
monster_instance = Monster("老虎", 5)
print(f"实例属性: {monster_instance.name} {monster_instance.age}")

# 调用实例方法
monster_instance.hi()
# 调用静态方法
monster_instance.ok()