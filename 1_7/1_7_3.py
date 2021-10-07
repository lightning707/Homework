import random

inp = input("Enter a string: ")

result = []

while (len(result) < 5) and (len(result) < len(inp) ** 2):  # anti-loop after 'and'
    result_str = ''
    for i in range(len(inp)):
        result_str += random.choice(inp)
    if result_str not in result:
        result.append(result_str)

print(result)
