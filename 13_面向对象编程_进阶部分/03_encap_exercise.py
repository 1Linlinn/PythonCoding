'''
定义Account类
1) 姓名(长度为2-4位),余额(必须大于20),密码(必须是6位)
如果不满足,则给出提示信息,并给默认值,密码与余额为私有属性
2)通过set_xxx方法给属性赋值
3)编写方法query_info()接受姓名和密码,如果正确,返回该账号信息
'''
class Account:
    def __init__(self, name, balance, password):
        self.set_name(name)
        self.set_balance(balance)
        self.set_password(password)

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self._name = name
        else:
            print("姓名长度必须为2-4位,已设置为默认值'未知'")
            self._name = "未知"

    def set_balance(self, balance):
        if balance > 20:
            self.__balance = balance
        else:
            print("余额必须大于20,已设置为默认值21")
            self.__balance = 21

    def set_password(self, password):
        if len(password) == 6:
            self.__password = password
        else:
            print("密码必须是6位,已设置为默认值'000000'")
            self.__password = "000000"

    def query_info(self, name, password):
        if self._name == name and self.__password == password:
            return f"姓名: {self._name}, 余额: {self.__balance}"
        else:
            return "姓名或密码错误"

# 示例用法
account = Account("张三", 50, "123456")
print(account.query_info("张三", "123456"))  # 输出: 姓名: 张三, 余额: 50
print(account.query_info("李四", "123456"))  # 输出: 姓名或密码错误

