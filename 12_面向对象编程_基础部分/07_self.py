class Dog:
    name = '猫'
    age = 2

    def info(self, name):
        print(f'name信息:{name}')
        # 访问属性name
        print(f"成员变量name：{self.name}")

    # 静态方法,把普通方法转化为静态方法
    @staticmethod
    def ok():
        print('ok()....')
    
    def eat(self):
        print(f"{self.name} is hungry.")

    def cry(self, name):
        print(f"{name} is crying.")
        print(f"{self.name} is crying.")
        self.eat()

    
dog = Dog()
dog.info('加菲猫')

# 调用静态方法
# 1.使用对象调用
dog.ok()
# 2.使用类名调用
Dog.ok()

dog.cry("小狗")


