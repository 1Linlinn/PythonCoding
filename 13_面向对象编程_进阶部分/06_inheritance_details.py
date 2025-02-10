class Base:
    # 公有属性
    n1 = 100
    # 私有属性
    __n2 = 200

    def __init__(self):
        print("Base的构造方法...")

    def hi(self):
        print('hi()的公共方法')

    def __hello(self):
        print('__hello()私有方法')


class Sub(Base):

    def __init__(self):
        print("Sub的构造方法...")

    # 访问非私有属性和方法
    def say_hi(self):
        print("say_ok()", self.n1)
        self.hi()


# 创建子类
sub = Sub()
sub.say_hi()
# sub.hello()









