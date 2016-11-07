# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

N, M = map(int, raw_input().split(' '))
#  N: number of computers
#  M: no of cables in the network
connection = {}
computer_table = {}
for _ in xrange(M):

    a, b, l = map(int, raw_input().split(' '))  # a, b: computers; l: latency of connection b/w them
    connection.setdefault((a, b), []).append(l)

cables_avail = int(raw_input())
latencies = map(int, raw_input().split(' '))
