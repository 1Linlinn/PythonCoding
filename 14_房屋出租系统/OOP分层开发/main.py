class House:
    def __init__(self, id, owner, phone, address, rent, status):
        self.id = id
        self.owner = owner
        self.phone = phone
        self.address = address
        self.rent = rent
        self.status = status

    def __str__(self):
        return f"{self.id}\t{self.owner}\t{self.phone}\t{self.address}\t{self.rent}\t{self.status}"


class HouseRentalSystem:
    def __init__(self):
        self.houses = []
        self.next_id = 1

    def add_house(self):
        owner = input("姓名：")
        phone = input("电话：")
        address = input("地址：")
        rent = input("租金：")
        status = input("状态：")
        house = House(self.next_id, owner, phone, address, rent, status)
        self.houses.append(house)
        self.next_id += 1
        print("======= 添加房屋成功 =======")

    def find_house(self):
        id = int(input("请输入要查找的id："))
        for house in self.houses:
            if house.id == id:
                print("======= 查找房屋信息 =======")
                print("|编号|房主|电话|地址|月租|状态|")
                print("|---|---|---|---|---|---|")
                print(f"|{house.id}|{house.owner}|{house.phone}|{house.address}|{house.rent}|{house.status}|")
                return
        print(f"======= 查找房屋信息id {id}不存在 =======")

    def delete_house(self):
        id = int(input("请输入待删除的编号(-1退出)："))
        if id == -1:
            return
        for house in self.houses:
            if house.id == id:
                confirm = input("请输入你的选择(Y/N),请确认选择：")
                if confirm.lower() == 'y':
                    self.houses.remove(house)
                    print("======= 删除房屋信息成功 =======")
                return
        print("====== 删除房屋信息失败，房屋编号不存在 =======")

    def modify_house(self):
        id = int(input("请输入待修改的编号(-1退出)："))
        if id == -1:
            return
        for house in self.houses:
            if house.id == id:
                house.owner = input("姓名：")
                house.phone = input("电话：")
                house.address = input("地址：")
                house.rent = input("租金：")
                house.status = input("状态：")
                print("======= 修改房屋信息成功 =======")
                return
        print("====== 修改房屋信息失败，房屋编号不存在 =======")

    def list_houses(self):
        print("======= 房屋列表 =======")
        print("|编号|房主|电话|地址|月租|状态|")
        print("|---|---|---|---|---|---|")
        for house in self.houses:
            print(f"|{house.id}|{house.owner}|{house.phone}|{house.address}|{house.rent}|{house.status}|")

    def main_menu(self):
        while True:
            print("======= 房屋出租系统菜单 =======")
            print("1.新增房源")
            print("2.查找房屋")
            print("3.删除房屋信息")
            print("4.修改房屋信息")
            print("5.房屋列表")
            print("6.退出")
            choice = input("请输入你的选择(1 - 6)：")
            if choice == '1':
                self.add_house()
            elif choice == '2':
                self.find_house()
            elif choice == '3':
                self.delete_house()
            elif choice == '4':
                self.modify_house()
            elif choice == '5':
                self.list_houses()
            elif choice == '6':
                confirm = input("请输入你的选择(Y/N),请确认选择：")
                if confirm.lower() == 'y':
                    print("你退出了程序，欢迎下次使用")
                    break
            else:
                print("选择错误，请重新输入。")


if __name__ == "__main__":
    system = HouseRentalSystem()
    system.main_menu()