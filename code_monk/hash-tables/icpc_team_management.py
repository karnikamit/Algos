# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

'''
6 3
arjit
tijra
genius
chanda
ashish
arjit

13 1
vvguqow
xiaaivv
gahuvui
xvnlyhy
lddhbo
ekhtrk
dffuatb
zvdehjk
ofoqbyr
objhsy
yrebyw
qabtgrs
pcrpzkf
'''


def icpc_camps():
    n, k = map(int, raw_input().split(' '))
    participants = {}
    for _ in xrange(n):
        name = raw_input()
        participants.setdefault(len(name), []).append(name)
    teams = filter(lambda x: len(participants[x]) == k, participants)
    return 'Possible' if len(teams) == len(participants) else 'Not possible'

# TODO Correct it!
cases = int(raw_input())
for case in xrange(cases):
    print icpc_camps()
