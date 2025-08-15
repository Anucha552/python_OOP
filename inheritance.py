# การสืบทอดคุณสมบัติ (inheritance)

# หลักการของ inheritance คือ ทำการสร้างสิ่งใหม่ขึ้นด้วยสืบทอดหรือรับเอา (inheritance)
# คุณสมบัติบางอย่างมาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย

# ข้อดีของการ inheritance คือ จากการที่สามารถนำสิ่งที่เคยสร้างขึ้นแล้วนำกลับมาใช้ใหม่ (re-use) ได้
# ทำให้ช่วยประหยัดเวลาการทำงานลง เนื่องจากไม่ต้องเสียเวลาพัฒนาใหม่หมด

# Class -> ยกเว้น Private Attribute & Private Method

# การสืบทอดคุณสมบัติ
# คลาสแม่
# class Employee:

# คลาสลูก
# class Programmer(Employee)

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
        print('ชื่อพนักงาน = {}' + self.__name)
        print('เงินเดือน = {}' + self.__salary)
        print('แผนก = {}' + self.__department)


class Accounting(Employee):
    __deparmentName = 'แผนกบัญชี'
    def __init__(self):
        pass

class Programmer(Employee):
    __deparmentName = 'แผนกพัฒนาระบบ'
    def __init__(self):
        pass

class Sale(Employee):
    __deparmentName = 'แผนกโปรแกรมเมอร์'
    def __init__(self):
        pass

account = Accounting()
print(account.companyName)
programmer = Programmer()
print(programmer.minSalary)
sale = Sale()
print(sale.maxSalary)
