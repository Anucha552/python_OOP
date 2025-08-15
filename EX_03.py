# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลังเพิ่มแล้ว

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def aging(self, year):
#         print('อายุปัจจุบัน = {}'.format(self.age))
#         self.age = self.age + year
#         print('อายุที่เพิ่มแล้ว = {}'.format(self.age))
#
# man = Human('Anucha', 30)
# man.aging(5)

import  time

rows = 40
for i in range(1, rows + 1):
    print(("1" * (rows - (i + rows)) + (" " * (i + (i - 1))) + ("1" * (rows - (i + rows)))))