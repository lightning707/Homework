def custom_enum(iterable, start=0):
    yield [(start + idx, iterable[idx]) for idx in range(len(iterable))]


for num in custom_enum([1, 3, 5, 10, 15]):
    print(num)
