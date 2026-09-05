name = input("Enter your name : ")
seat = input("Enter your seat number : ")

maths = int(input("Enter your marks of Mathematics : "))
phy = int(input("Enter your marks of Physics : "))
chem = int(input("Enter your marks of Chemistry : "))
de = int(input("Enter your marks of DE : "))
frm = int(input("Enter your marks of FRM : "))
ws = int(input("Enter your marks of Workshop : "))

total = maths + phy + chem + de + frm + ws
per = (total / 600) * 100


print()
print("-" * 8 + "RESULT OF FIRST YEAR ENGINEERING" + "-" * 8)
print()

print(f"Nameof student : {name}\nSeat number : {seat}")
print(f"Total marks = {total}/600 \nPercentage = {per:.2f}")

if per >= 75:
    print("Grade: Distinction")

elif per >= 60:
    print("Grade: First Class")

elif per >= 50:
    print("Grade: Second Class")

elif per >= 40:
    print("Grade: Third Class")

else:
    print("Grade: Fail")