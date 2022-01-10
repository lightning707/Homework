class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList:
    def __init__(self, lst = []):
        self.head = None
        while len(lst) > 0:
            temp = self.head
            self.head = Node(lst[-1])
            self.head.next = temp
            lst.pop()

    def __len__(self):
        current_node = self.head
        lst_len = 0
        while current_node:
            current_node = current_node.next
            lst_len += 1
        return lst_len

    def is_empty(self):
        return self.head is None

    def add_head(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def append(self, value):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)

    def __str__(self):
        lst = []
        current_node = self.head
        while current_node:
            lst.append(current_node.value)
            current_node = current_node.next
        return str(lst)

    def index(self, value):
        current_node = self.head
        idx = 0
        while current_node:
            if current_node.value == value:
                return idx
            idx += 1
            current_node = current_node.next
        return None

    def pop(self, pop_idx=-1):
        prev_node = self.head
        current_node = self.head.next
        pop_idx = pop_idx % len(self)
        idx = 1

        if pop_idx == 0:
            pop_value = self.head.value
            self.head = self.head.next
        else:
            while idx < pop_idx:
                idx += 1
                prev_node = current_node
                current_node = current_node.next

            pop_value = current_node.value
            prev_node.next = current_node.next
        return pop_value

    def insert(self, insert_idx, value):
        prev_node = self.head
        current_node = self.head.next
        insert_idx = insert_idx % len(self)
        idx = 1
        insert_node = Node(value)

        if insert_idx == 0:
            insert_node.next = self.head
            self.head = insert_node
        else:
            while idx <= insert_idx:
                idx += 1
                prev_node = current_node
                current_node = current_node.next

            prev_node.next = insert_node
            insert_node.next = current_node

    def slice(self, start_idx, stop_idx):
        slice_lst = UnorderedList()
        current_node = self.head
        idx = 0
        while idx < start_idx:
            idx += 1
            current_node = current_node.next

        slice_lst.head = Node(current_node.value)
        current_node_slice = slice_lst.head
        while idx < stop_idx - 1:
            current_node_slice.next = Node(current_node.next.value)
            idx += 1
            current_node_slice = current_node_slice.next
            current_node = current_node.next

        return slice_lst


class Queue:
    def __init__(self, lst):
        self.lst = UnorderedList(lst)

    def __len__(self):
        return len(self.lst)

    def is_empty(self):
        return len(self.lst) == 0

    def peek(self):
        return self.lst.head.value

    def dequeue(self):
        return self.lst.pop(0)

    def enqueue(self, value):
        self.lst.insert(-1, value)


q = Queue([5, 6, 7, 2, 3])
print(q.peek())
print(q.lst)
print(q.dequeue())
print(q.lst)
print(q.enqueue(23))
print(q.lst)
