# -*- coding: utf-8 -*-
__author__ = "karnikamit"


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if not current:
            raise ValueError("%s is not in the list" % str(data))
        else:
            return 'Found the Node: %s' % current

    def delete(self, data):
        current = self.head
        found, deleted = False, False
        previous = None
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not current:
            raise ValueError('%s Not found in the list' % str(data))
        if previous:
            deleted = True
            previous.set_next(current.get_next)

        return 'deleted: %s' % deleted

    def display(self):
        current = self.head
        while current:
            print current.data,
            current = current.get_next()

if __name__ == '__main__':
    ll = LinkedList()
    for i in xrange(2):
        data = int(raw_input('data: '))
        ll.insert(data)
    ll.display()
    
