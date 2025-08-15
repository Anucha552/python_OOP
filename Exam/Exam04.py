# เขียนโปรแกรมสร้าง class ชื่อ Dog โดยมี attribute และ method ดังนี้
# attribute
# breed
# ㆍ breed เป็น พันธุ์สุนัข
# ㆍ color เป็นสีของสุนัข
# ㆍ height เป็นส่วนสูง (หน่วยเปียเซนดิเมตร)
# ㆍ weight เป็นน้ำหนัก (หน่วยเป็นกิโลกรัม)
# method
# growth) ทำหน้าที่แสดงความสูงและน้ำหนักที่เพิ่มขึ้นของสุนัขอย่างละ 10%
# ตัวอย่าง
# Input
# dog_A = Dog("Jack russell Terrier", "White", 30,7)
# dog_A.growth()
# print(height =', dog_A.height)
# print(weight =', dog_A.weight)
# Output
# height = 33.0
# weight = 7.70000000000001

class Dog:
    def __init__(self, breed, color, height, weight):
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight

    def growth(self):
        self.height = self.height * (10 / 100 + 1)
        self.weight = self.weight * (10 / 100 + 1)


dog_A = Dog("Jack russell Terrier", "White", 30,7)
dog_A.growth()
print(dog_A.height)
print(dog_A.weight)
