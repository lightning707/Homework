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
        return max_val


class ValuePriority:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __int__(self):
        return self.priority

    def __lt__(self, y):
        return self.priority < y

    def __gt__(self, y):
        return self.priority > y


class PriorityQueue(BinaryHeap):
    def __init__(self):
        super().__init__()

    def enqueue(self, value, priority):
        vp = ValuePriority(value, priority)
        self.insert(vp)

    def dequeue(self):
        vp = self.pop_max()
        return vp.value


q = PriorityQueue()

q.enqueue(5, 1)
q.enqueue(6, 1)
q.enqueue(1, 2)
q.enqueue(2, 2)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
