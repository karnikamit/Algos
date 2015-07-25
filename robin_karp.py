__author__ = 'karnikamit'


def robin_karp(text, pattern):
    if len(pattern) > len(text):
        return -1

    hash_text = Hash(text, len(pattern))
    hash_pattern = Hash(pattern, len(pattern))
    hash_pattern.update()
    for i in xrange(len(text) - len(pattern) + 1):
        if hash_text.hashed_value() == hash_pattern.hashed_value():
            if hash_text.text() == pattern:
                return i
        hash_text.update()
    return -1


class Hash:
    def __init__(self, text, size):
        self.str = text
        self.hash = 0

        for i in xrange(size):
            self.hash += ord(self.str[i])
        self.init = 0
        self.end = size

    def update(self):
        if self.end <= len(self.str)-1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def hashed_value(self):
        return self.hash

    def text(self):
        return self.str[self.init: self.end]

# print robin_karp('3141592421572', '1415')