

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return f'{self.key} -> {self.val}'

class HashTable:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size

    def hash_it(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum([])
        raise TypeError(f"Wrong {key} of type {type(key)}")

    def put(self, key, val):
        new_data = Node(key, val)
        ind = self.hash_it(key)
        self.items[ind] = new_data

    def get(self, key):
        ind = self.hash_it(key)
        if self.items[ind]:
            return self.items[ind].val
        raise IndexError(f"No data with such key: {key}")

    def __contains__(self, item):
        for node in self.items:
            if item == node.val:
                return True
        return False
        
    def __len__(self):
        count = 0
        for node in self.items:
            if node is not None:
                count += 1
        return count


ht = HashTable(11)
ht.put(45, 'abc')
ht.put('fg', 546)
print(ht.items)

print(ht.get(45))
