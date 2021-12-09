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


char_dict = {'}': '{',  ']': '[', ')': '('}


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char in char_dict.values():
            stack.push(char)
        if char in char_dict.keys():
            if stack.peek() == char_dict[char]:
                stack.pop()
            else:
                return False
    return stack.size() == 0


print(is_balanced('())'))
print(is_balanced('()'))
print(is_balanced('{]{]'))
print(is_balanced('{[()]}'))
print(is_balanced('((([])))'))
