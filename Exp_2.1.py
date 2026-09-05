# Logic Gate Stimulator

a = int(input("Enter your first input bit: "))
b = int(input("Enter your second input bit: "))

print("Operations that can be performed\n AND, OR, NOT, EXOR")
o = input("Operation to be performed : ").upper()

print()
print("-" * 8 + "LOGIC GATE OPERATION" + "-" * 8)
print(f"a = {a}")
print(f"b = {b}")
print(f"Operation = {o}")

if o == "AND":
    print(f"a AND b = {a} AND {b} = {a and b}")

elif o == "OR":
    print(f"a OR b = {a} OR {b} = {a or b}")

elif o == "NOT":
    print(f"NOT a = NOT {a} = {not a}")
    print(f"NOT b = NOT {b} = {not b}")

elif o == "EXOR":
    print(f"a EXOR b = {a} EXOR {b} = {a ^ b}")

else:
    print("INVALID INPUT") 