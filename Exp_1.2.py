#1.2 Bill Splitter Utility
# Bill Splitter Utility

b = float(input("Enter total bill amount:"))
t = float(input("Enter total tip percentage:"))
n = float(input("Enter total number of people:"))

a = (t / 100) * b
g = (18 / 100) * b
tamt = a + b + g
p = tamt / n

print("*" * 40)
print("*" * 9 + "Bill Splitter Utility" + "*" * 9)
print("*" * 40)
print()

print("Total Bill : Rs.", b)
print(f"Tip percentage : {t} %")
print(f"Tip amount : Rs. {a}")
print(f"GST(18%) : Rs. {g:.2f}")
print("*" * 40)
print("Final Bill : Rs.", tamt)
print("*" * 40)
print("No. of people :", n)
print("Amount per person :", p)