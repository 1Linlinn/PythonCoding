'''
编写Computer类,包含CPU,内存,硬盘等信息
1)get_details方法用于返回Computer的详细信息
2)编写PC子类,继承Copmuter类,添加特有属性[品牌brand]
3)编写NotePad类,继承Copmuter类,添加特有属性[颜色color]
4)完成测试,创建子类的实例对象,分别给特有属性赋值,以及从父类继承,使用方法输出信息
'''
class Computer:
    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def get_details(self):
        return f"CPU: {self.cpu}, 内存: {self.memory}GB, 硬盘: {self.disk}GB"

class PC(Computer):
    def __init__(self, cpu, memory, disk, brand):
        super().__init__(cpu, memory, disk)
        self.brand = brand

    def get_details(self):
        return f"{super().get_details()}, 品牌: {self.brand}"

class NotePad(Computer):
    def __init__(self, cpu, memory, disk, color):
        super().__init__(cpu, memory, disk)
        self.color = color

    def get_details(self):
        return f"{super().get_details()}, 颜色: {self.color}"

# 测试代码
pc = PC("Intel i7", 16, 512, "Dell")
notepad = NotePad("AMD Ryzen 5", 8, 256, "Silver")

print(pc.get_details())  # 输出: CPU: Intel i7, 内存: 16GB, 硬盘: 512GB, 品牌: Dell
print(notepad.get_details())  # 输出: CPU: AMD Ryzen 5, 内存: 8GB, 硬盘: 256GB, 颜色: Silver