# 食物类
class Food:
    name = None
    def __init__(self, name):
        self.name = name

class Fish(Food):
    pass

class Bone(Food):
    pass

# 动物类
class Animal:
    name = None
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 主人类
class Master:
    name = None
    def __init__(self, name):
        self.name = name

    # 喂猫猫鱼
    def feed_cat(self, cat: Cat, fish: Fish):
        print(f"主人{self.name} 给动物 {cat.name} 的食物是 {fish.name}")

        # 喂狗骨头
    def feed_dog(self, dog: Dog, bone: Bone):
        print(f"主人{self.name} 给动物 {dog.name} 的食物是 {bone.name}")


# 测试
master = Master('小米')
cat = Cat("小花猫")
fish = Fish("黄花鱼")
dog = Dog("小野狗")
bone = Bone("大骨头")

master.feed_cat(cat, fish)
master.feed_dog(dog, bone)

