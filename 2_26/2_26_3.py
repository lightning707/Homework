class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[0]
        else:
            return None

    def push(self, element):
        self.stack = [element] + self.stack

    def pop(self):
        if len(self.stack) != 0:
            self.stack = self.stack[1:]
        else:
            raise ValueError("Cannot remove elements from empty stack")

    def size(self):
        return len(self.stack)

    def get_from_stack(self, item):
        copy = self.stack
        for index in range(self.size()):
            if self.stack[index] == item:
                self.stack = self.stack[:index] + self.stack[index+1:]
                return item
        raise ValueError("Element not found")


s = Stack()
s.push(5)
s.push(51)
s.push(52)
s.push(53)
s.push(54)
print(s.stack)
s.get_from_stack(51)
print(s.stack)
