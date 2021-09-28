import random

def create_random_list(length=10, range=[1, 11]):
    lst = []
    i = 0
    while i < length:
        lst.append(random.randrange(range[0], range[1]))
        i += 1
    return lst

lst1 = create_random_list()
lst2 = create_random_list()

print(lst1)
print(lst2)
print()

result_lst = []
for num1 in lst1:
    for num2 in lst2:
        if (num1 == num2) and (num1 not in result_lst):
            result_lst.append(num1)

print(result_lst)
