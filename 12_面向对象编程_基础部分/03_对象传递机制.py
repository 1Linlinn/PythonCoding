class Person:
    age = None
    name = None

p1 = Person()
p1.age = 10
p1.name = '小明'
p2 = p1 # 把p1赋给了p2
print(p2.age)
print(f"p1.name的地址:{id(p1.name)},p2.name的地址:{id(p2.name)}")
p2.age = 100
print(p1.age)
print(p2.age)
p2 = None
print(p2.age)