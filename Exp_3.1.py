# Menu Driven Program using Recursive Functions

def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)


def fib(b):
    if b == 0:
        return 0
    elif b == 1:
        return 1
    else:
        return fib(b - 1) + fib(b - 2)


def sum_digit(c):
    if c == 0:
        return 0
    else:
        return (c % 10) + sum_digit(c // 10)

while True:
    print()
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Sum of Digits")
    print("4. Exit")

    c = int(input("Enter your choice: "))

    if c == 1:
        num = int(input("Enter a number: "))
        print(f"Factorial {num}! =", fact(num))

    elif c == 2:
        num = int(input("Enter number of terms: "))
        print("Fibonacci Series:")
        for i in range(num):
            print(fib(i), end=" ")

    elif c == 3:
        num = int(input("Enter a number: "))
        print("Sum of digits =", sum_digit(num))

    elif c == 4:
        break

    else:
        print("Invalid choice! Please try again.")