# 对基础数据类型进行类型注解
n1 = 10
n2: int = 1
n3: float = 10.0


# 实例对象进行注解
class Cat:
    pass

# 标注cat类型是Cat
cat: Cat = Cat()


# 对容器类型进行注解
lst = [1, 2] # type: list[int]
lst1: list = [1, 1, 1, 1]

