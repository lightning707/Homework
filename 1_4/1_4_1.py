import random

lst = []

i = 0
while i < 10:
    lst.append(random.randrange(0, 100))
    i += 1

print(lst)

lst.sort(reverse=True)
print(lst[0])
