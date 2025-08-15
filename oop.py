# ชื่อ ,เงินเดือน
class Employee:  # การสร้าง class
    # สร้าง method
    def detail(self, name, salary,department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนังงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))


# Attribute เป็นกลไกที่กำหนดคุณสมบัติให้กับ class
# การสร้าง Attribute
# self.name = ชื่อพนังงาน
# self .salary = เงินเดือน
# self .age = อายุของพนังงาน

# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
# def getName(self):
# การเรียกใช้งาน
# ชื่อวัตถุ.getName()


# คีย์เวิร์ด SELF
# การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
# ให้บอกตัวตนของวัตถนุั้น ๆ เช่น กการกำหนดคุณสมบัติต่างๆ ในวัตถ

# Constructor
# เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง Constructor
# ded __init__(self):

# การสร้างวัตถุ

emp1 = Employee()
emp1.detail('พีระยุทธ', 50000,'วิชาการ')
emp1. showData()

emp2 = Employee()
emp2.detail('ขำตรี', 25000,'กิจการ')
emp2. showData()

emp3 = Employee()
emp3.detail('alther', 150000,'อาคาร')
emp3. showData()