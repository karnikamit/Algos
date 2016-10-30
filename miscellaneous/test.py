__author__ = 'karnikamit'
# Implement a simple BinaryTree


class BinaryTree(object):
    def __init__(self, root_id):
        self.left_child = None
        self.right_child = None
        self.root_id = root_id

    @property
    def right(self):
        return self.right_child

    @right.setter
    def right(self, node_value):
        self.right_child = node_value

    @property
    def left(self):
        return self.left_child

    @left.setter
    def left(self, node_value):
        self.left_child = node_value

    def insert_left_child(self, value):
        if self.left:
            temp = BinaryTree(self.left_child)
            temp.left = value
            self.left_child = temp
        else:
            self.left_child = value

    def insert_right_child(self, value):
        if self.right:
            temp = BinaryTree(self.right)
            temp.right = value
            self.right = temp
        else:
            self.right = value

    # def insert_left_child(self, value):
    #     if self.left_child is None:
    #         self.left_child = BinaryTree(value)
    #     else:
    #         tree = BinaryTree(value)
    #         tree.left, self.left =  self.left, tree
    #
    # def insert_right_child(self, value):
    #     if self.right_child is None:
    #         self.right_child = BinaryTree(value)
    #     else:
    #         tree = BinaryTree(value)
    #         tree.right, self.right_child = self.right_child, tree
###
cases = int(raw_input())
num = map(int, raw_input().split(' '))
assert len(num) == cases
for j in num:
    numbers = range(1, j+1)
    for i in numbers:
        if i % 5 == 0 and i % 3 == 0:
            print 'FizzBuzz'
        elif i % 5 == 0:
            print 'Buzz'
        elif i % 3 == 0:
            print 'Fizz'
        else:
            print i
