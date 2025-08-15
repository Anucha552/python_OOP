# Super
# เมื่อต้องการเรียกใช้คุณสมบัติต่างๆ ในคลาสแม่
# เช่น Constructor, Method, Attribute
# คัวอย่าง
# super().__init__(name)

class Employee:
    # Class Variable
    minSalary = 2000
    maxSalary = 10000
    companyName = "บริษัท xy2 จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนักงาน = ' + self.__name)
        print('เงินเดือน =',format(self.__salary))
        print('แผนก = ' + self.__department)


class Accounting(Employee):
    __deparmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)
        super().showData()

class Programmer(Employee):
    __deparmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)
        super().showData()

class Sale(Employee):
    __deparmentName = 'แผนกโปรแกรมเมอร์'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)
        super().showData()

account = Accounting("A", 2000)
programmer = Programmer("B", 10000)
sale = Sale("C", 25000)
