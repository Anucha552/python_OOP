# เขียนโปรแกรมสร้าง class ชื่อ Cashier โดยมี attribute และ method ดังนี้
# attribute
# ㆍ products เป็น list ที่เก็บชื่อสินค้า
# method
# ㆍ recommend) ทำหน้าที่แนะนำสินค้า โดยเมื่อเมื่อเรียกใช้ โปรแกรมจะพิมพ์ We have <product>. ออกมา
# ตัวอย่าง
# Input
# cashier = Cashier(['apple', 'bana', 'orange'))
# cashier.recommend()
# Output
# We have apple banana orange.

class Cashier:
    def __init__(self, products):
        self.products = products

    def recommend(self):
        product_name = ''

        for value in  self.products:
            product_name += " " + value

        print("We have{}".format(product_name))

cashier = Cashier(['apple', 'bana', 'orange',])
cashier.recommend()



