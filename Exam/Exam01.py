
# เขียนโปรแกรมสร้าง class ชื่อ Drive โดยมี attribute และ method ดังนี้
# attribute
# ㆍHP เป็นพลังชีวิต
# ㆍgenerated_money เป็นเงินที่ทำหาได้
# method
#   drive() ทำหน้าที่แสดงค่าพลังชีวิต และเงินที่หามาได้ หลังจากขับแท็กซี่ โดยจะลด HP 10 หน่วย แต่จะ
#   เพิ่ม generated_money 10 หน่วย
#   care() ทำหน้าที่แสดงค่าพลังชีวิต และเงินที่หามาได้ หลังจากพักผ่อน โดยจะเพิ่ม HP 10 หน่วย แต่จะ
# ลด generated_money 10 หน่วย
# ตัวอย่าง
# Input
# driver_A = Driver(100, 100)
# driver_A.drive()
# driver_A.report()
# driver_A.care()
# driver_A.report()
# Output
# HP = 90, Generated Money = 110
# HP = 100, Generated Money = 100

class Driver:
    def __init__(self, HP, generated_money):
        self.HP = HP
        self.generated_money = generated_money

    def drive(self):
        self.HP -= 10
        self.generated_money += 10

    def care(self):
        self.HP += 10
        self.generated_money -= 10

    def report(self):
        print('hp = {}, Generated Money = {}'.format(self.HP, self.generated_money))

driver_A = Driver(100, 100)
driver_A.drive()
driver_A.report()
driver_A.care()
driver_A.report()