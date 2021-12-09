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
            res = self.stack[0]
            self.stack = self.stack[1:]
            return res
        else:
            raise ValueError("Cannot remove elements from empty stack")

    def size(self):
        return len(self.stack)


def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)
    result = ''
    while stack.size() > 0:
        result += stack.pop()
    return result


print(reverse_string('abcdef'))
