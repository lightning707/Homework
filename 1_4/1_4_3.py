lst = []

i = 1
while i <= 100:
    lst.append(i)
    i += 1

result_lst = []
for num in lst:
    if (num % 7 == 0) and (num % 5 != 0):
        result_lst.append(num)

print(result_lst)
