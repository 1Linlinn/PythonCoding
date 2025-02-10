# 抽象类更多在于设定规范
from abc import ABC, abstractmethod

# 抽象类
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# 具体类
class Dog(Animal):
    def sound(self):
        return "汪汪"

    def move(self):
        return "跑"

class Bird(Animal):
    def sound(self):
        return "啾啾"

    def move(self):
        return "飞"

# 测试代码
dog = Dog()
bird = Bird()

print(f"狗的叫声: {dog.sound()}")  # 输出: 狗的叫声: 汪汪
print(f"狗的移动方式: {dog.move()}")  # 输出: 狗的移动方式: 跑
print()
print(f"鸟的叫声: {bird.sound()}")  # 输出: 鸟的叫声: 啾啾
print(f"鸟的移动方式: {bird.move()}")  # 输出: 鸟的移动方式: 飞