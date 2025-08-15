# เขียนโปรแกรมสร้าง class ชื่อ Car โดยมี attribute และ method ดังนี้
# attribute
# ㆍ brand เป็นยี่ห้อของรถ
# ㆍ model เป็นรุ่นของรถ
# ㆍ year เป็นปีของรถ
# ㆍ color เป็นสีของรถ
# method
# new_color) รับพารามิเตอร์ 1 ตัว ชื่อว่า color ทำหน้าที่แสดงสีใหม่ของรถที่ต้องการเปลี่ยน
# ตัวอย่าง
# Input
# car_A = Car("Honda", "Civic", "2019", "Black")
# car_A.new_color('Red')
# print('color =', car_A.color)
# Output
# color = Red

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def new_color(self, color):
        self.color = color

car_A = Car("Honda", "Civic", "2019", "Black")
# car_A.new_color('Red')
print('color =',car_A.color)