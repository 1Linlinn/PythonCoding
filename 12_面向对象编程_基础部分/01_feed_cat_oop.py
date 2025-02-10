# 定义一个猫类，name，age，color是属性，或者称为成员变量

# 定义Cat类
class Cat:
    # 定义属性
    age = None
    name = None
    color = None

# 通过Cat类创建实例
cat1 = Cat()

# 进行赋值
cat1.age = 10
cat1.color = 'white'
cat1.name = 'mimi'

print(f'cat1的信息为:年龄{cat1.age},颜色{cat1.color},姓名{cat1.name}')
