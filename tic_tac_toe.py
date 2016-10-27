# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

'''
initial matrix
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

example input:
    'player 1(path, option): 1,1,X

    re built matrix
    [[0, 0, 0],
     [0, 'X', 0],
     [0, 0, 0]]

    so on ...

'''


class TicTacToe:

    def __init__(self):
        self.matrix = self._build_matrix('-')
        self.display_matrix()

    def _build_matrix(self, initial=None):
        matrix = []
        for i in xrange(3):
            temp = []
            for k in xrange(3):
                temp.append(initial)
            matrix.append(temp)
        return matrix

    def _play(self):
        print 'input option as Ex: 1,1,X'
        print
        print self.matrix
        print
        self.matrix = self._build_matrix()
        while True:
            p1 = self._rebuild_matrix(self._player1_ip())
            print self.matrix
            if p1:
                return p1
            p2 = self._rebuild_matrix(self._player2_ip())
            print self.matrix
            if p2:
                return p2

            c = self._check()
            if c:
                return c

    def _player1_ip(self):
        return raw_input('player 1(path, option): ')

    def _player2_ip(self):
        return raw_input('player 2(path, option): ')

    def _rebuild_matrix(self, option):
        i1, i2 = int(option[0]), int(option[2])
        mark = option[4]
        if not self.matrix[i1][i2]:
            self.matrix[i1][i2] = mark

        if len(filter(lambda x: x == mark, self.matrix[i1])) == 3:      # horizontal check
            return 'player with %s mark has won the game' % mark
        if len([i for i in xrange(3) if self.matrix[i][i2] == mark]) == 3:    # vertical check
            return 'player with %s mark has won the game' % mark
        #  Diagonal check \
        if len([mark for i in xrange(len(self.matrix)) if self.matrix[i][i] == mark]) == 3:
            return 'player with %s mark has won the game' % mark
        #  Diagonal check /
        i, j, result = 2, 0, []
        while i > -1:
            if self.matrix[i][j] != mark:
                break
            else:
                result.append(mark)
            i -= 1
            j += 1
        if len(result) == 3:
            return 'player with %s mark has won the game' % mark

    def _check(self):
        f = 0
        for i in self.matrix:
            if all(i):
                f += 1
        else:
            if f == 3:
                return 'Board full'

if __name__ == '__main__':
    t = TicTacToe()
    print t._play()