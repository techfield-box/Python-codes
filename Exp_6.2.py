class Item:
    def __init__(self,itemId,title,price,seller):
        self.itemId = itemId
        self.title = title
        self.price = float(price)
        self.seller = seller
        self.isAvailable = True
        
    def displayDetails(self):
        status = "Available" if self.isAvailable else "Sold"
        print(f"---Item Details---")
        print(f"ID : {self.itemId}| Title : {self.title}")
        print(f"Seller : {self.seller}| Price : Rs.{self.price:.2f}| Status : {status}")

class UsedItem(Item):
    def __init__(self,itemId,title,originalprice,seller,condition,years):
        super().__init__(itemId,title,originalprice,seller)
        
        if condition == "Like New":
            factor=0.9
        elif condition == "Good":
            factor=0.75
        elif condition == "Fair":
            factor=0.6
        else:
            factor=0.45
            
        self.price = float(originalprice) * factor
        self.condition = condition
        self.years = years
        
    def displayDetails(self):
        super().displayDetails()
        print(f"Condition : {self.condition}| Years Used: {self.years}")

print("Select Item Type: 1 for Used & 2 for Unused")
choice = input("Choice:")

id_in = input("Enter ID:")
title_in = input("Enter Title:")
price_in = float(input("Enter Original Price of Product:"))
seller_in = input("Enter Seller:")

if choice == "1":
    cond_in = input("Enter Condition of Product(Like New,Good,Fair,Poor):")
    years_in = int(input("Enter Years of Usage: "))
    product = UsedItem(id_in,title_in,price_in,seller_in,cond_in,years_in)
else:
    product = Item(id_in,title_in,price_in,seller_in)

product.displayDetails()