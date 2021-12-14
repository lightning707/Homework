from pythonds.basic import Stack
from pythonds.basic import Queue


class BinaryTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        new_node = self.__class__(value)
        new_node.left_child = self.left_child
        self.left_child = new_node
        return new_node

    def insert_right(self, value):
        new_node = self.__class__(value)
        new_node.right_child = self.right_child
        self.right_child = new_node
        return new_node

    def get_root_value(self):
        return self.value

    def set_root_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def bfs(self):
        q = Queue()
        q.enqueue(self)

        while not q.isEmpty():

            curr_node = q.dequeue()
            print(curr_node.value, end=' ')

            if curr_node.left_child:
                q.enqueue(curr_node.left_child)
            if curr_node.right_child:
                q.enqueue(curr_node.right_child)


def convert_expr_to_list(expr):
    # Convert expression string to list:
    expr_li = []
    current_number = ''
    for char in expr:
        if char.isdigit():
            current_number += char
        if char in ['*', '/', '+', '-', ')', '(']:
            if len(current_number) > 0:
                expr_li.append(current_number)
                current_number = ''
            expr_li.append(char)
    if len(current_number) > 0:
        expr_li.append(current_number)

    return expr_li


def build_parse_tree(expr_li, tree=None):
    # Initialize tree
    # if tree is None:
    #     tree = BinaryTreeNode()
    #     tree.left_child = expr_li[0]
    #     return build_parse_tree(expr_li[1:], tree)

    result_tree = BinaryTreeNode()
    i = 0
    while i < len(expr_li):

        if expr_li[i] == '(':
            end_id = len(expr_li) - 1
            while expr_li[end_id] != ')':
                end_id -= 1
            expr_li[i] = build_parse_tree(expr_li[i+1:end_id])
            expr_li = expr_li[:i+1] + expr_li[end_id+1:]

        elif type(expr_li[i]) == BinaryTreeNode:
            if result_tree.left_child is None:
                result_tree.left_child = expr_li[i]
            else:
                result_tree.right_child = expr_li[i]
            i += 1

        elif expr_li[i].isdigit():
            if result_tree.left_child is None:
                result_tree.left_child = BinaryTreeNode(expr_li[i])
            else:
                result_tree.right_child = BinaryTreeNode(expr_li[i])
            i += 1

        elif expr_li[i] in ['+', '-']:
            if result_tree.value is None:
                result_tree.value = expr_li[i]
            else:
                new_tree = BinaryTreeNode(expr_li[i])
                new_tree.left_child = result_tree
                result_tree = new_tree
            i += 1

        elif expr_li[i] in ['*', '/']:
            if result_tree.value is None:
                result_tree.value = expr_li[i]
                i += 1
            else:
                new_tree = BinaryTreeNode(expr_li[i])
                new_tree.left_child = result_tree.right_child
                new_tree.right_child = BinaryTreeNode(expr_li[i+1])
                result_tree.right_child = new_tree
                i += 2

    return result_tree


a = convert_expr_to_list('25+(13/2+55*3)')
result_tree = build_parse_tree(a)
print(result_tree.right_child.left_child)
result_tree.bfs()

