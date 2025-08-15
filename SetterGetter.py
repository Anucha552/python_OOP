# Getter / Setter method
# Setter เป็นการกำหนดค่าให้กับ Object
# Getter เป็นการดึงค่าจาก Object

# EX_Setter
    # def setName(self, newname):
    #     self.__name = newname
# EX_Getter
    # def getName(self):
    #     return self.__name

class Employee:
    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนักงาน = {}' + self.getName())
        print('เงินเดือน = {}' + self.getSalary())
        print('แผนก = {}' + self.getDepartment())

    # setter method
    def setName(self, newname):
        self.__name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdepartment):
        self.__department = newdepartment

    # getter method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

emp1 = Employee('นาย อนุชา', 150, 'ขอแม่')
# emp1.setName('อนุชา')
# emp1.setSalary(150)
# emp1.setDepartment('ขอแม่')
# emp1.showData()
# print('ข้อมูล : {}'.format(emp1.getName()))
emp1.showData()
