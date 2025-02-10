'''
1.定义员工类Employee,包含私有属性(姓名和月工资),以及计算年金额的方法get_annual()
2.普通员工(Worker)和经理(manager)继承员工类,经理类多了奖金bonus属性和管理manage方法,普通员工多了work方法
普通员工和经理根据需要重写get_annual方法
3.编写函数show_emp_annual(e: Employee), 实现获取员工对象的年工资
4.编写函数working(e: Employee),如果是普通员工,调用work方法,与果实经理调用manage方法
'''
class Employee:
    def __init__(self, name, monthly_salary):
        self.__name = name
        self.__monthly_salary = monthly_salary

    def get_annual(self):
        return self.__monthly_salary * 12

    def get_name(self):
        return self.__name

class Worker(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name, monthly_salary)

    def get_annual(self):
        return super().get_annual()

    def work(self):
        return f"{self.get_name()} 正在工作。"

class Manager(Employee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name, monthly_salary)
        self.__bonus = bonus

    def get_annual(self):
        return super().get_annual() + self.__bonus

    def manage(self):
        return f"{self.get_name()} 正在管理。"

def show_emp_annual(e: Employee):
    print(f"{e.get_name()} 的年工资是: {e.get_annual()}")

def working(e: Employee):
    if isinstance(e, Worker):
        print(e.work())
    elif isinstance(e, Manager):
        print(e.manage())

# 测试代码
worker = Worker("张三", 5000)
manager = Manager("李四", 10000, 20000)

show_emp_annual(worker)  # 输出: 张三 的年工资是: 60000
show_emp_annual(manager)  # 输出: 李四 的年工资是: 140000

working(worker)  # 输出: 张三 正在工作。
working(manager)  # 输出: 李四 正在管理。















