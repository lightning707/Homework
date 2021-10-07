import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operands = ['+', '-', '*', '**', '//', '%']
operand = random.choice(operands)

expression = str(num1) + ' ' + operand + ' ' + str(num2)

inp = input(f'{expression} = ')

is_number = False
if inp.isdecimal() or (inp[1:].isdecimal() and inp[0] == '-'):
    is_number = True

if is_number == False:
    print("Invalid number")
    exit(1)

if int(inp) == eval(expression):
    print("Correct!")
else:
    print("Incorrect.")
