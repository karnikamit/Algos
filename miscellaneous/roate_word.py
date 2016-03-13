# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
The function below will take a string(s) and rotate it a given amount(num).
i.e cheer rotated by 7(cheer,7) will return jolly, and (melon, -10) will return cubed.
'''


class Rotate:
    def __init__(self, word, num):
        self.word = word
        self.num = num
        self.new_word = ''

    @staticmethod
    def rotate_letter(letter, n):
        start = ord('a')
        c = ord(letter.lower()) - start
        i = (c+n) % 26 + start
        return chr(i)

    def get_new_word(self):
        for char in self.word:
            self.new_word += self.rotate_letter(char, self.num)
        return self.new_word

    def __str__(self):
        return self.get_new_word()

if __name__ == '__main__':
    print Rotate('cheer', 7)
    print Rotate('melon', -10)
