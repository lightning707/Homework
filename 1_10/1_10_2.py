a = input("Enter first number: ")
b = input("Enter second number")


try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Input is not numeric")
    exit(1)

try:
    print((a ^ 2) / b)
except ZeroDivisionError:
    print("Cannot divine by 0")
    exit(1)
