class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def _move_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, key):
        self.heap_list.append(key)
        self.heap_size += 1
        self._move_up(self.heap_size)

    def _search_max_child(self, i):
        if i * 2 + 1 > self.heap_size:
            return i * 2
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def _move_down(self, i):
        while i * 2 <= self.heap_size:
            mc_ind = self._search_max_child(i)
            if self.heap_list[i] < self.heap_list[mc_ind]:
                self.heap_list[i], self.heap_list[mc_ind] = self.heap_list[mc_ind], self.heap_list[i]
            else:
                break

            i = mc_ind

    def pop_max(self):
        max_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_list.pop()
        self.heap_size -= 1
        self._move_down(1)


bh = BinaryHeap()

bh.insert(5)
print(bh.heap_list)
bh.insert(51)
print(bh.heap_list)
bh.insert(13)
print(bh.heap_list)
bh.insert(25)
print(bh.heap_list)
bh.insert(100)
print(bh.heap_list)
