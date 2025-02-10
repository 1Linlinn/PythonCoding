# 定义Cat类
class Cat:
    # 定义属性
    age = 2
    name = 'mimi'
    color = 'white'

# 通过Cat类创建实例
cat1 = Cat()
print(f'cat1的信息为:年龄{cat1.age},颜色{cat1.color},姓名{cat1.name}')
print('-' * 50)
cat1.age = 10
print(f'cat1的信息为:年龄{cat1.age},颜色{cat1.color},姓名{cat1.name}')

