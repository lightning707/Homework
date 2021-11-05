def custom_range(start, end, step=1):
    idx = start
    while idx < end:
        yield idx
        idx += step


for i in range(5, 15, 2):
    print(i)

print("##############")

for i in custom_range(5, 15, 2):
    print(i)
