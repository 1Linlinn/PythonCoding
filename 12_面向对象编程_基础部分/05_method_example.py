
class Person:
    # 属性（成员变量）
    name = None
    age = None

    # 添加成员方法
    # 打招呼
    def hi(self):
        print("hi, python")

    # 计算1+2+...1000
    def cal01(self):
        result = 0
        for i in range(1, 1001):
            result += i
        print('result=',result)
    
    # 接受一个数n，计算1+...n
    def cal02(self, n):
        result = 0
        for i in range(1, n+1):
            result += i
        print('result=',result)
    
    # 计算两数之和
    def get_sum(self, a, b):
        return a + b

# 测试
p = Person()
p.hi()
p.cal01()
p.cal02(2)
print(p.get_sum(1,2))