# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใคร ๆ
# ก็สามารถเข้าถึงและเรียกใช้งานได้
# ตัวอย่าง
# self.name = name

# Protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูก
# ที่สืบทอดคุณสมบัติไปใช้เท่านั้น
# ตัวอย่าง
# self._name = name

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้
# ตัวอย่าง
# self.__name = name

class Employee:
    def __init__(self, name, salary, department):
        self.name = name # Public
        self._salary = salary # Protected
        self.__department = department # Private

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self._salary))
        print('แผนก = {}'.format(self.__department))

emp1 = Employee('นาย A', 50000, 'วิชาการ')
emp1.__salary = 71000
emp1.showData()
