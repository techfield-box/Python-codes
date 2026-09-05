# Degree F to Degree C

print("+" + "-"*5 + "TEMPERATURE UNIT CONVERTER" + "-"*5 + "+")
print("")

f = float(input("Enter Temperature (in degree F): "))
c = (f - 32) * 5 / 9
print(f"{f} degree F = {c:.3f} degree C")

c = float(input("Enter Temperature (in degree C): "))
f = 32 + (9/5 * c)
print(f"{c} degree C = {f:.3f} degree F")