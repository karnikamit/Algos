# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


class TicTacToe:

    def __init__(self):
        self.matrix = []

    def _build_matrix(self, initial='-'):
        matrix = []
        for i in xrange(3):
            temp = []
            for k in xrange(3):
                temp.append(initial)
            matrix.append(temp)
        return matrix

    def _play(self):
        self.matrix = self._build_matrix()
        while True:
            p1 = self._player1_ip()

        
    def _player1_ip(self):
        return raw_input('player 1: ')

    def _player2_ip(self):
        return raw_input('player 2: ')

    def _rebuild_matrix(self, option):
