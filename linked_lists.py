__author__ = 'karnikamit'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.length = 0

    @property
    def node_data(self):
        return self.data

    @node_data.setter
    def node_data(self, data):
        self.data = data

    @property
    def node_next(self):
        return self.next

    @node_next.setter
    def node_next(self, next):
        self.next = next

    def get_length(self):
        if self.data:
            for i in self.data:
                self.length += 1
            return self.length
        return self.length


def print_ll(node):
    while node:
        print node.node_data
        node = node.node_next
    print

if __name__ == '__main__':
    n1 = Node('Sharnappa')
    n2 = Node('Arpanna')
    n3 = Node('Amit')
    n4 = Node('Shantala')
    n1.node_next = n2
    n2.node_next = n3
    n3.node_next = n4
    print print_ll(n1)
