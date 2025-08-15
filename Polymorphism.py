# Polymorphism
# การพ้องรูป
# เกิดจาก poly หลากหลาย morphology รูปแบบ
# ในทางโปรแกรมคือการที่ method ชื่อเดียวกัน
# สามารถรับอาร์กิวเมนต์ที่แตกต่างกันได้หลายรูปแบบ
# โดย method นี้จะถูกเรียกว่า overload method

#Overloading
class Employee:
    # Class Variable
    __minSalary = 2000
    maxSalary = 10000
    companyName = "บริษัท xy2 จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self._department = department

    def showData(self):
        print('ชื่อพนักงาน = ' + self.__name)
        print('เงินเดือน =',format(self.__salary))
        print('แผนก = ' + self._department)

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก {} , เงินเดือน {} , รายได้ต่อปี {}".
                format(self.__name, self.__department, self.__salary,
                       self._getIncome()))


class Accounting(Employee):
    __deparmentName = 'บัญชี'
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__deparmentName)
        self.age = age

    def showData(self):
        super().showData()
        print('อายุ = {} '.format(self.age))

class Programmer(Employee):
    __deparmentName = 'พัฒนาระบบ'
    def __init__(self, name, salary, experies, skill):
        super().__init__(name, salary, self.__deparmentName)
        self.experies = experies
        self.skill = skill

    def showData(self):
        super().showData()
        print('ประสบการณ์ = {}'.format(self.experies))
        print('Skill = {} '.format(self.skill))

class Sale(Employee):
    __deparmentName = 'โปรแกรมเมอร์'
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__deparmentName)
        self.area = area

    def showData(self):
        super().showData()
        print('พื้นที่รับผิดชอบ = {}'.format(self.area))

account = Accounting("A", 2000, 35)
programmer = Programmer("B", 10000, 2, 'พัฒนาเกม')
sale = Sale("C", 25000, 'เชียงคาน')
account.showData()
print()
programmer.showData()
print()
sale.showData()

