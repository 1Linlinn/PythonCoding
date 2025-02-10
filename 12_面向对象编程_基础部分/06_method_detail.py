# hi
def hi():
    print("hi!")



class Person:
    name = None
    age = None



# 创建实例p1和p2
p1 = Person()
p2 = Person()

"""
    使用动态方法给p1添加方法，只给p1对象添加方法！
    新增加的方法名称自己取
"""
p1.m1 = hi
p1.m1()
# 测试p2
try:
    p2.m1()
except:
    print("p2没有这个方法")
    