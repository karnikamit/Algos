__author__ = 'karnikamit'


class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.length = 0

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        if self.next is not None:
            return True
        return False

    def get_length(self):
        if self.data:
            for i in self.data:
                self.length += 1
            return self.length
        return self.length
