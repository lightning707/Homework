class SkipList:
    """Skips every second element of the list"""

    def __init__(self, iterable: list):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 2
            return result
        raise StopIteration

    def __getitem__(self, index):
        skip_list = []
        i = 0
        while i < len(self.iterable):
            skip_list.append(self.iterable[i])
            i += 2
        return skip_list[index]


lst = SkipList(['A', "B", "C", "D", "E", "F"])
print(next(lst))
print(next(lst))
print(next(lst))

print("##########")
print(lst[:])
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[-1])
