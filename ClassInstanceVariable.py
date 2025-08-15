# ClassInstanceVariable
from math import expm1


# Class Variable คือตัวแปรที่ทำงานภายใน Class
# ส่วนอื่นสามารถเข้าถึงข้อมูลในส่วนนี้ได้เลย (Static attribute)
# โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

# Instance Variable คือ ตัวแปรที่อยู่ภายใน Object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา


class Employee:
    # Class Variable
    __min = 5
    __max = 200
    __companyName = "บริษัท xy2 จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนักงาน = {}' + self.__name)
        print('เงินเดือน = {}' + self.__salary)
        print('แผนก = {}' + self.__department)



emp1 = Employee('นาย อนุชา', 150, 'ขอแม่')
# print("ค่า = " + str(emp1._max))
print(Employee._companyName)