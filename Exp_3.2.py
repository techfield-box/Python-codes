#PRIME NUMBER ANALYSER
def prime(a):
    if a <= 1:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False

    return True


def gen_p(b):
    print(f"Prime numbers from 1 to {b} are:")
    for n in range(2, b + 1):
        if prime(n):
            print(n, end=" ")
    print()

while True:
    print("\n----- PRIME NUMBER ANALYSER -----")
    print("1. Check if a number is prime")
    print("2. Display prime numbers")
    print("3. Exit")

    c = int(input("Enter your choice: "))

    if c == 1:
        n = int(input("Enter a number to check: "))
        if prime(n):
            print(n, ": It is a PRIME number.")
        else:
            print(n, ": It is NOT a prime number.")

    elif c == 2:
        b = int(input("Enter the limit: "))
        gen_p(b)

    elif c == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")