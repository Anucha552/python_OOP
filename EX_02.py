# เขียนโปรแกรมสร้าง class ขื่อ people โดยมี Attrebute และ Method ดังนี้
# Attrebute
# name เป็นชื่อของทุกคน
# age เป็นอายุของทุกคน
# method
# Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ My name is <name>. I'm <age> year old

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print('My name is {}. I\'m {} year old'.format(self.name, self.age))

student = people('Anucha', 30)
student.Introduce()