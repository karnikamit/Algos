# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


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

    def play(self):
        print 'input option as Ex: 1,1,X'
        print
        # self.matrix = self._build_matrix()
        while True:
            p1 = self._player_ip(1)
            while not self._mark_cell(p1):
                p1 = self._player_ip(1)
            p1_resp = self._rebuild_matrix(p1)
            self.display_matrix()
            if p1_resp:
                return p1_resp

            p2 = self._player_ip(2)
            while not self._mark_cell(p2):
                p2 = self._player_ip(2)
            p2_resp = self._rebuild_matrix(p2)
            self.display_matrix()
            if p2_resp:
                return p2_resp

            c = self._check()
            if c:
                return c

    def _player_ip(self, player):
        return raw_input('Mark it player %d: ' % player)

    def _mark_cell(self, option):
        i1, i2, mark = option.split(',')
        i1, i2 = map(int, [i1, i2])
        if not self.matrix[i1][i2] == '-':
            return True
        return False

    def _rebuild_matrix(self, option):
        i1, i2, mark = option.split(',')
        i1, i2 = map(int, [i1, i2])
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

    def display_matrix(self):
        for i in self.matrix:
            for k in i:
                print k,
            else:
                print
if __name__ == '__main__':
    t = TicTacToe()
    print t.play()
