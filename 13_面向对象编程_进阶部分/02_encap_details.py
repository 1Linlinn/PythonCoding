# 创建一个职员（Clerk）类，属性有name，job，salary
# 1) 不能随便查看职位和工资等隐私属性
# 2) 提供公共方法，对职位和工资进行操作

class Clerk:

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name      # 公共属性
        self.__job = job      # 私有属性
        self.__salary = salary

    # 提供公共方法，对私有属性操作
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        print(self.__job)

    # 私有方法
    def __hi(self):
        print('hi()....')
    
    # 提供公共方法调用私有方法
    def f(self):
        self.__hi()

# 构造实例
clerk = Clerk("tiger", "工程师", 20000)

# 可以在类的外部直接访问公共属性
print(clerk.name) 

# 不可以在类的外部直接访问私有属性
clerk.get_job()
clerk.set_job('经理')
clerk.get_job()

# 间接调用私有方法
clerk.f()