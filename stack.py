__author__ = 'karnikamit'


class Stack:
    def __init__(self):
        self.stk = list()

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        return self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def extend(self, data):
        for i in data:
            self.push(i)

    def get_count(self):
        count = 0
        if self.stk:
            for i in self.stk:
                count += 1
            return count
        return count

    def is_empty(self):
        if self.get_count() > 0:
            return False
        return True

    def get_stack(self):
        return self.stk
