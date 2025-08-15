# ObjectToString
# แปลง Object เป็น String
# ตัวอย่าง
# def __str__(self)
#   return "ชุดข้อความ"

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

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก {} , เงินเดือน {} , รายได้ต่อปี {}".
                format(self.__name, self.__department, self.__salary,
                       self._getIncome()))


class Accounting(Employee):
    __deparmentName = 'บัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)

class Programmer(Employee):
    __deparmentName = 'พัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)

class Sale(Employee):
    __deparmentName = 'โปรแกรมเมอร์'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deparmentName)

account = Accounting("A", 2000)
programmer = Programmer("B", 10000)
sale = Sale("C", 25000)
print(account.__str__())
print(programmer.__str__())
print(sale.__str__())