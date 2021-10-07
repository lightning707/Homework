import random

inp = input("Enter a string: ")

result = []

for i in range(5):
    result_str = ''
    for i in range(len(inp)):
        result_str += random.choice(inp)
    result.append(result_str)

print(result)
