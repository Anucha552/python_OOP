# FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

# isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
# dir => แสดง attribute และ method
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self,  name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}\nเงินเดือน = {}\nแผนก = {}'.format(self.name, self.salary, self.department))
        # print('เงินเดือน = {}'.format(self.salary))
        # print('แผนก = {}'.format(self.department))

emp1 = Employee('อนุชา', 0, 'นักศึกษา')
emp2 = Employee('นาย ข', 25000, 'กิจการ')
emp3 = Employee('นาย จ', 10000, 'อาคาร')
emp4 = Employee('plim', 20000, 'HR')

print(isinstance(emp1, Employee)) # ตรวจสอบว่า Obj ถูกสร้างจาก Class ที่ตรวจสอบไหม
print(dir(emp1)) # ตรวจสอบว่า method และ Attribute ของ Obj นั้นมอะไรบ้าง
print(emp1.__class__) # ตรวจสอบว่า Obj นั้นสร้างจาก class ชื่อว่าอะไร